---
title: Compute Shader
layout: post
category: study
tags: [directx, computer graphics, cpp, shader]
published: false
---

## Motivation

Unreal 또는 Unity 를 다루다 보면, 어떤거는 Vertex Shader / Pixel Shader / Geometry Shader 를 Pipeline Stage 를 태워서 사용해야하는지, 어떤거는 Graphics Pipeline 에 속하지 않은 GPGPU 를 아이디어를 사용한 Compute Shader 를 사용해야할지 모를수가 있다. 한참 Radar Simulation 을 구현하다가.. 한참 Pixel Shader 로 Unity 로 작성되어있길래 Unreal 에서도 Pixel Shader 로 하면 되겠구나...? 이러다가 2 개월이 지난 지금 엄청나게 후회하고 있고, 정확하게 Usage 도 모르게 사용했다 라는것에 현타가 오고, Compute Shader 에 대해서 정확하게 정리 된 글이 없어서 작성을 하기로 하였다. (개인적으로 Unity 는 뭔가 다 알아서 해주는 느낌인데, Unreal 은 뭔가 이거 아니면 안된다 라는 느낌이 강하다.)

## Prerequisites
* HLSL Code
* Multithread in C++

## Vertex / Geometry / Pixel Shader vs Compute Shader
//TODO

## Compute Shader

- `UnorderedAccessView` 는 Input 도 되고 출력도 된다.
- ** `Dispatch` **: Argument 로 `ThreadGroupCountX`, `ThreadGroupCountY`, `ThreadGroupCountZ` 로 나누어져 있음. (ex: 만약 Argument 로 `UINT(ceil(screenWidth / 256)), screenHeight, 1)`. 이런식으로 되어있고, `ScreenWidth` 가 1280 이라고 한다면, 5 개를 세로로 나눠서 계산 하고 `ScreenHeight` 로는 전부 계산하고, 마지막 인자 1 은 2 차원 배열이기 때문에, z 값이 1이다는 소리이다, 즉 가로 방향으로는 5 개를 Group 을 나눠서 계산하고, 세로 방향으로는 전체 height 만큼 계산한다는 이야기이다.) 

```c++
RWTexture2D<float4> gOutput : register(u0) // Readable & Writable Texture 2D, pixel format => float4

[numthreads(256, 1, 1)] // Thread group 안에서 1 개의 Thread Group 안에서, thread 의 개수 
void main(int3 gID: SV_GroupID, uint3 : SV_DispatchThreadID)
```
## Warp 개념

아래의 그림을 CPU 랑 비교했을때의 GPU 의 Processing 의 역활이다. GPU 는 CPU 와는 달리, 각각의 여러개의 Core 들이 Control 하나와 L1 Cache 가 붙어있다. 즉 Control 이라는 관리자에서 "야 우리팀은 이 일만 공장처럼 찍어낼꺼야" 라는 뜻이 내포되어있다고 생각하면 된다. 즉, 단순 작업의 양이 많을때, Block(Group) 단위로 관리를 하며, Processing 을 한다고 생각하면된다.

![!\[Alt text\](image.png)
](../../../assets/img/photo/10-12-2024/gpu.png)

일단 GPU 의 구조상으로는 [CUDA](https://nyu-cds.github.io/python-gpu/02-cuda/) SIMT(Single Instruction, Multiple Thread) 를 가지고 있다. 그리고 `a scalable array of multithreaded Streaming Multiprocessors (SMs)` 이런말이 있는데 결국에는 thread 가 여러개인 array 인 형태를 띄고 있으며, Streaming 방식으로 쭉쭉 Processing 이 이뤄진다라는걸 볼수 있다. 그리고 Core 개수가 여러개로 나눠져있으니, 이것들의 Core 들을 Scheduling 을 해주며, 관리해서 Multiprocessor 이런식으로 표현한것 같다.

본질적으로 **Warp** 라는 개념은 `Group of 32 parallel threads` 이다. 즉 Hardware 의 하나의 묶음, 동시에 일을 하는 묶음 이라고 생각하면 될것 같다. 그리고 `A warp executes one commmon instruction at a time, so full efficiency is realized when all 32 threads of a warp agree on their execution path` 라고 문서에 나와있는데, 이 말은 즉슨 Warp 라는 하나의 Group, 32 개의 동시에 일하는 thread 가 execution path 가 동일하다이며, 최대한의 효율적으로 하기 위해서 32 개를 사용한다. 우리가 위에서 봤을때 처럼, `dispatch` 할때, Group 개수와, 그 한 그룹에 Thread 개수를 지정을 해서 사용하며 어떠한 Block 형태로 실행을 시켰었다. 마찬가지로, SMs 의 개수에 따라서 Block 이 어떻게 Parallel 하게 Processing 하는지를 아래의 그림으로 확인을 할 수 있다.

![Automatic Scalability](../../../assets/img/photo/10-12-2024/block.png)

GPGPU Programming 에서 기본적으로 Grid 의 형태를 아래의 그림처럼 띄고 있다 즉 여러개의 Thread Block(Group) Grid 형태로 띄고 있다는걸 할수 있다. 기본적으로 Processor 은 일을 따로 따로 하기 때문에 Processor 라고 칭하는데, Processor 와 다른 Processor 끼리는 명령을 내릴수 없고 Memory 도 Share 하기가 어렵다. 하지만 Block 안에서 Thread 끼리는 동기화를 할수 있으며, 메모리를 공유한다. **즉 Thread 끼리는 의사 소통을 할수 있다.**
일단 여기까지 개념이야기를 맞추며, 그다음으로 부터는 실제 구현을 알아보겠다. 

![!\[Alt text\](image.png)](../../../assets/img/photo/10-12-2024/grid.png)

### Gaussian Blur (Separable)

- 다시말하자면, Compute Shader 안에서는 Unordered Acess View 를 사용한다는 점, 그리고 RWStructureBuffer 사용한거
- PSO 가 있다 (GraphicsPSO)
- `UnorderedAccessView` 는 Input(입력) 도 되고 Output(출력)도 된다.

- **** `Dispatch` ****: Argument 로 `ThreadGroupCountX`, `ThreadGroupCountY`, `ThreadGroupCountZ` 로 나누어져 있음. (ex: 만약 Argument 로 `UINT(ceil(screenWidth / 256)), screenHeight, 1)`. 이런식으로 되어있고, `ScreenWidth` 가 1280 이라고 한다면, 5 개를 세로로 나눠서 계산 하고 `ScreenHeight` 로는 전부 계산하고, 마지막 인자 1 은 2 차원 배열이기 때문에, z 값이 1이다는 소리이다, 즉 가로 방향으로는 5 개를 Group 을 나눠서 계산하고, 세로 방향으로는 전체 height 만큼 계산한다는 이야기이다.) 


```


// hlsl
RWTexture2D<float4> gOutput : register(u0) // Readable & Writable Texture 2D, pixel format => float4

[numthreads(256, 1, 1)] // Thread group 안에서 1 개의 Thread Group 안에서, thread 의 개수 
void main(int3 gID: SV_GroupID, uint3 : SV_DispatchThreadID) // SV_DispatchThreadID -> Thread ID 여기서는 Pixel 의 Index | SV_GroupID => ThreadGroup ID.
{

}
```

### GPU 시간 계산

### Structured Buffer

### Consume / Append Buffers

### Density Field

### Indirect Arguments
- 최적화할떄는 필요하다. DrawInstanced Method vs Draw 와 비교

- 하나당 Vertex 가 몇개다
- Instance 가 몇개다
- Offset (StartVertexLocation, StartInstanceLocation),

미리 GPU 에다가 할당, 다시 CPU 에서 간접적으로 알려주는 Pointer 역활정도

```c++
struct IndirectArgs
{
    UINT VertexCountPerInstance;
    UINT InstanceCount;
    UINT StartVertexLocation;
    UINT StartInstanceLocation;
}
...
vector<IndirectArgs> m_argsCPU = {{32, 1, 0, 0}, {64, 1, 0, 0}, {256, 1, 0, 0}}; // 32 개의 Vertex 가 1 개의 Instance 안에 정해져 있음
ComPtr<ID3D11Buffer> m_argsGPU;
...

 D3D11Utils::CreateIndirectArgsBuffer(m_device, UINT(m_argsCPU.size()),
                                      sizeof(IndirectArgs), m_argsCPU.data(),
                                      m_argsGPU);

const UINT offset = sizeof(IndirectArgs) * 0;
m_context->DrawInstancedIndirect(m_argsGPU.Get(), offset)
```

### Bitonic Sort
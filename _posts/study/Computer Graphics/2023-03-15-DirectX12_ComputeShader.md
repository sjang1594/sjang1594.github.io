---
title: Compute Shader & Particle System & Instancing
layout: post
category: study
tags: [directx, computer graphics]
---

### Compute Shader & Particle System

잠깐 언급이 됬듯이 CPU 와 GPU 의 차이점은 바로 연산을 담당하는 Core 의 개수이다. CPU 같은 경우는 "Optimized for Serial Tasks" 라는 점과 GPU 같은 경우는 "Optimized for many parallel tasks" 라는 점이다.

[TODO: Compute Shader Image 추가]

일단 Shader 파일에 사용되는 곳에 `RWTexture2D<float4> g_rwtex_0 : register(u0):` 이런 Register 를 사용하는걸로 보인다. `u0` 는 Computer Shader 전용으로 사용되는 친구이다. 여기서 궁금할수 있는게 RW 즉 Read Write 할수있는 Texture2D 이다. 

예를 들어서, Microsoft 공식 문서에 가보면 `ID3D12GraphicsCommandList::Dispatch` 봐보면, 3 차원 처럼 ThreadGroupCount 가 X, Y, Z 로 나누어져있는걸로 보인다. 그래서 
```
[numthreads(1024, 1, 1)]
void CS_Main(int3 threadIndex : SV_DispatchTrheadID)
{
    if (threadindex.y % 2 == 0)
        g_rwtex_0[threadIndex.xy] = float4(1.f, 0.f, 0.f, 1.f);
    else
        g_rwtex_0[threadIndex.xy] = float4(0.f, 1.f, 0.f, 1.f); 
}
```

### Particle System

Particle System 이란 것은 결국 어떤 물체의 Effect 효과 중에 Particle 이 튀는것처럼 보이는게 Particle System 이라고 한다. 그런데, 생각을 해보면 이 Particle System 작업은, 메인 작업에 비해 생각보다 중요도가 낮다. 그래서 만약에 Particle System 이 메인이되서 Rendering 을 하게 된다면, 프로그램의 부하가 일어날것이다. 그래서 이걸 해결할수 있는게 바로 Instancing 으로 해결하면 된다. Instancing 에서 `SV_InstanceID` 를 사용하게 되면, 각 Particle 에 ID 가 번호가 매겨지게 된다. 그리고 Particle 의 이러한 특징으로 인해서 CPU 에서 계산하는게 아니라, GPU 에서 계산하게끔 넘겨주는 역활만 하면 된다. 그래서 VRAN 에게 Particle 에 대한 정보를 가지고 있고, GPU 에서 매번의 Tick 마다 Particle 이 죽었는지 살았는지 이런식으로 넘기면 된다.

### Instancing

keyword : drawcall / instancing 이 필요한 상황 -> 많은 부하. 

vertex buffer 를 여러개(1 - 15) 사용 가능. 예: 첫번째 Buffer 에서는 물체의 정점 정보를 나타내고, 두번째 buffer 는 각 물체의 Position 정보 등. 

버퍼의 종류 (Structure Buffer, Constant Buffer, Instancing Buffer) 

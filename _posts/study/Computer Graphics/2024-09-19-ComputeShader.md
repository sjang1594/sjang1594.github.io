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

## Vertex / Geometry / Pixel Shader vs Compute Shader

## Compute Shader

- `UnorderedAccessView` 는 Input(입력) 도 되고 Output(출력)도 된다.

- **** `Dispatch` ****: Argument 로 `ThreadGroupCountX`, `ThreadGroupCountY`, `ThreadGroupCountZ` 로 나누어져 있음. (ex: 만약 Argument 로 `UINT(ceil(screenWidth / 256)), screenHeight, 1)`. 이런식으로 되어있고, `ScreenWidth` 가 1280 이라고 한다면, 5 개를 세로로 나눠서 계산 하고 `ScreenHeight` 로는 전부 계산하고, 마지막 인자 1 은 2 차원 배열이기 때문에, z 값이 1이다는 소리이다, 즉 가로 방향으로는 5 개를 Group 을 나눠서 계산하고, 세로 방향으로는 전체 height 만큼 계산한다는 이야기이다.) 


```
// Dispatch


// hlsl
RWTexture2D<float4> gOutput : register(u0) // Readable & Writable Texture 2D, pixel format => float4

[numthreads(256, 1, 1)] // Thread group 안에서 1 개의 Thread Group 안에서, thread 의 개수 
void main(int3 gID: SV_GroupID, uint3 : SV_DispatchThreadID) // SV_DispatchThreadID -> Thread ID 여기서는 Pixel 의 Index | SV_GroupID => ThreadGroup ID.
{

}
```

- 여러개의 Pixel 들을 어떻게 나눠서 사용하는지 관건


---
title: HLSL Introduction
layout: post
category: study
tags: [directx, computer graphics, shader]
published: true
---

## Shader Programming

Programming 언어에서도 여러가지 종류가 달라지듯이, Pipeline 안에서 각각의 Stage 마다, 안보이는 Shader Programming 을 해줘야 하고, 언어도 다른 종류가 있다.

아래의 그림을 참고해서 그림을 보자면, IA Stage 에서 Memory Resource (Buffer, Texture, Constant Buffer) 에서, IA 로 들어간 이후에 아래쪽으로 쉐이더를 통과해서 진행한다. 참고로, 이때 Memory Resource 에서 IA 로 들어가는 데이터의 배치상태(layout) 이라고한다.

DirectX 에서는, HLSL(High Level Shader Language) 를 사용한다. [HLSL](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl) 에 들어가보면, 이런 구문이 보인다. `HLSL is the C-like high-level shader language that you use with programmable shaders in DirectX.` C Language 하고 비슷하다. 그리고 HLSL 로 Compute Shader 할때는 Direct Machine Learning 을 사용하라고 한다.

즉 일단 Shader Programming 이란, 결국에 GPU 에서 작동하는 Programming 이라고 생각하면 편할것 같다.

일단 기본적으로 아래와 같이 Shader Programming 을 할수 있다. C 나 C++ 처럼, 제일 처음에 시작되는 부분이 바로 main 부분이다. Shader 에도 main 이 따로 있다. 일단 Shader 의 종류가 여러가지가 있다. 예를들어서 Vertex Shader 가 있고, Pixel Shader 등등 있는데, 서로 연관성은 없으며, 하나의 독립적인 Module 이라고 생각하면 편하다, 독립적인 Module 이기 때문에, Compile 도 따로한다. 하지만 data 는 Share 할수 있다.

예를 들어서 아래의 HLSL Programming 을 봐보자.

```hlsl
struct VertexShaderInput
{
    float3 pos : POSITION;
    float3 color : COLOR0;
}

struct PixelShaderInput
{
    float4 pos : SV_POSITION;
    float3 color : COLOR;
}

PixelShaderInput main(VertexShaderInput input)
{
    PixelShaderInput output;
    float4 pos = float4(input.pos, 1.0f);
    pos = mul(pos, model);
    pos = mul(pos, view);
    pos = mul(pos, projection);

    output.pos = pos;
    output.color = input.color;

    return output;
}

// pixel shader
float4 main(PixelShaderInput input) : SV_TARGET
{
    return float4(input.color, 1.0);
}
```

위의 코드 같은 경우 `float3 pos : POSITION` 이라고 나와있는데 colon(:) 다음에 나오는건 Sematics 인데, 어떤 Parameter 종류다라는것을 명시한다. 자세한건 [Shader Semantics](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-semantics) 참고하자.

그렇다면 Vertex Shade.r 와 Pixel Shader 를 조금 더 알아보자. 위의 코드에서 `__ShaderInput` 이라는 구조체가 보인다. 그렇다면 Pipeline 에서 Output 도 존재할수 있는데, 여기서 Vertex Shader 의 Output 이 Interpolation 을 거쳐서 Pixel Shader 의 Input 이 되기때문에 따로 명시하진 않았다.

그리고 위의 PixelShaderInput 구조체에서 Vertex Shader 와 비슷하게 생겼지만 `SV` (System-value semantics)라는게 들어가 있는데, 이 이유는 Shader의 Input 으로 들어온다 라는걸 표시한다.

Pixel Shader 에서는 Graphics Pipeline 안에서 제일 마지막에 위치해있기때문에 Semantics 가 SV_TARGET 즉 Render 를 할 Target 이라는 semantics 를 넣어주어야한다.

Shader 에서 Constant Buffer 도 거쳐서 계산하게끔 도와줘야한다. 그러기 때문에 이것에 필요한 문법도 따로 명시해줘야한다. 아래와 같이 표현 할수 있는데 여기서 register 안에 b0 이라는 인자가 들어간게 보인다. 이건 Register Type 인데 b 일 경우는 Constant Buffer, t 일때는 Texture buffer, c 일 경우 Buffer offset 등 여러가지 타입이 존재한다.

```hlsl
cbuffer ModelViewProjectionConstantBuffer : register(b0)
{
    matrix model;
    matrix view;
    matrix projection;
}
```

## Resource
- [Graphics Pipeline](https://learn.microsoft.com/en-us/windows/win32/direct3d11/overviews-direct3d-11-graphics-pipeline)
- [High-level Shalder Language](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl)
- [Shader Semantics](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-semantics)
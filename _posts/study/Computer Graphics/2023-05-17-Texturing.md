---
title: DirectX11 - Texturing
layout: post
category: study
tags: [directx, computer graphics, shader]
published: true
---

### DirectX11 - Texturing

일단, Texturing 을 하기 위해서, Shader Programming 해야된다. 일단 Texturing 을 하려면 Vertex Shader 에서 해야되는지, Pixel Shader 에서 해야되는지가 고민이 되는데, 일단 Microsoft 공식문서에서는 Pixel Shader 에서 하라고 명시가 되어있다.

그러면 PixelShader 의 Program 을 잠깐 봐보자. 일단 GPU 에서 Texture Image 를 `Texture2D` 로 받아 올수 있다. 그리고 앞에서 잠깐 언급했듯이, Texture Image 안에서 색깔 값을 가져오는 걸 Sampling 이라고 했었다. 그래서 `SamplerState` 도 사용해야한다. 여기서 register 일때의 `t0` 과 `s0` 이 있다. `t0` 같은 경우, Texture 일때, 그리고 index 는 0, 그리고 sampler 일때는 s 그리고 index 는 0. 자세한건, 이 [Resource](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-variable-register) 를 활용하자.

{% raw %}
```hlsl
Texture2D g_texture0 : register(t0);
SamplerState g_sampler : register(s0);

cbuffer PixelShaderConstantBuffer : register(b0) {}

struct PixelShaderInput
{
    float4 pos : SV_POSITION;
    float3 color : COLOR;
    float2 texcoord : TEXCOORD;
}

float4 main(PixelShaderInput input) : SV_TARGET
{
    return g_texture0.Sample(g_sampler, input.textcoord);
}
```

hlsl 에서 이렇게 작성을 했다고 한다면, CPU 에서 보내주는 Member 도 만들어줘야한다. 여기서 ShaderResourceView 같은 경우, Texture 의 Resource 로 사용하는데, 왜 구지? View 가 필요하지라고 생각할수 있다. 사실 View 라는건 Texture 자체를 RenderTarget 로 사용할수 있기 때문이다. 같은 Memory 를 사용하더라도, RenderTarget 으로 설정이 가능하며, 이 Shader 를 가지고, 다른 쉐이더로 Input 으로 넣어줄때 ResourceView 로 넘겨줄수있다.

```c++
ComPtr<ID3D11Texture2D> m_texture;
ComPtr<ID3D11ShaderResourceView> m_textureResourceView;
ComPtr<ID3D11SamplerState> m_samplerState;
```

주의해야될점은 한 Texture 를 한 Shader 안에서 동시에 Resource 와 RenderTarget 으로 사용할수 없다. 그래서 Texture 가 두개가 있다고, 가정하면, Res1 -> Shader -> RT2 = Res2 -> Shader -> RT1 이렇게 사용이 가능하다.

## Resource
- [Create Textures](https://opengameart.org/content/3-crate-textures-w-bump-normal)
- [Texutre in OpenGL](https://learnopengl.com/Getting-started/Textures)
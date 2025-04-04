---
title: Render Target View
layout: post
category: study
tags: [directx, computer graphics]
published: true
---

### Render Target View

Render Target

* Forward Shader

Rendering Pipeline
물체의 Index 와 Vertex 정보(Topology) 정보를 input assembler 에게 넘겨준다. 그런다음에 이 정점들을 가지고 어떤일을 해야되는지 기술한 다음에
Vertex Shader 와 Pixel Shader 를 통해서 처리를 했다. Output merger 에서 Render Target View 에서 결과를 받아서 뿌려졌었다.

그래서 RTV 를 처리하기 위해서 Command Queue 에서, 어떤 Buffer 에다가 render 를 할지 결정을 했었다.
```c++
D3D12_CPU_DESCRIPTOR_HANDLE backBufferView = _swapChain->GetBackRTV();
_cmdList->ClearRenderTargetView(backBufferView, Colors::Black, 0, nullptr);

D3D12_CPU_DESCRIPTOR_HANDLE depthStencilView = GEngine->GetDepthStencilBuffer()->GetDSVCCpuHandle();
_cmdList->OMSetRenderTargets(1, &backBufferView, FALSE, &depthStencilView);
// --> 즉 여기서 OMSetRenderTarget 이 어디에다가 뿌려줄것인가 였다.

_cmdList->ClearDepthStencilView(depthStencilView, D3D12_CLEAR_FLAG_DEPTH, 1.0f, 0, 0, nullptr);
```

그래서 실질적으로 그려지는 부분은 Shader 쪽에서 위에서 작성된 코드와 맞물려서 실행된다.

```c
float4 PS_MAIN(VS_OUT input) : SV_Target
{
    float4 color = float4(1.f, 1.f, 1.f, 1.f);
    if(g_text_on_0)
	color = g_text_0.Sample(g_same_0, input.uv);
    float3 viewNormal = input.viewNormal;
    if(g_text_on_1)
    
    LightColor totalColor = (LightColor)0.f;
    
    for (int i = 0; i < g_lightCount; ++i)
    
    color.xyz = (totalColor.diffuse.xyz * color.xyz) + totalColor.ambient.xyz * color.xyz + totalColor.specular.xyz;

    return color;
}
```

이 방식에서 아쉬운 (중요한) 점은, 우리가 열심히 중간 부품을 만들어서 사용하는데, 그게 다 날라간다는것이다. 즉 빛 연산이나, Normal 값들을 사용하지 않은채, Color 로만 return 을 하니까 중간들 계산값들이 날아가게(손실) 된다는것이다.
---
title: Mipmap & LOD
layout: post
category: study
tags: [directx, computer graphics, cpp]
published: false
---

## MipMap Introduction

Mipmap 이라는건 Main Texture 를 downsized 를 시킨 여러개의 사진이라고 생각하면 된다. 즉 여러개의 해상도를 조정하며 만든 여러개의 Image 라고 생각 하면 된다.

Computer Vision 에서는 Image Pyramid 

어디에서 사용하는지? -> LOD Detail 을 표현을 할때, None-Minmap 과 Minmap 차이 보여주기 (Aliasing)

Point Sampler / Linear Interpolation Sampler

// TODO: 언리얼 Mipmap 보여주기 

// Mag Filter (To interpolate a value from neihboring texel) -> magnifying 할 때 사용 (Point Filter or Linear Filter), Texture 의 Texel 들이 작게 하나로 들어가는거.

Subresoruce -> Texture 의 배열로 각각 다른 Texture 에 대해서, 각각의 Mipmap 들을 생성한는것이 바로 Array Slice 이다. 같은 LDO 끼리를 묶는걸 MIP Slice. A Single Subresoruce(Texture) 즉 하나의 Resource 안에서, Subresource 를 선택해서 골라갈수 있다.

Staging Texture 임시로 데이터를 놓는다. 만들수 있는 최대 mipmap 을 만든다.

```c++
D3D11_TEXTURE2D_DESC txtDesc;
txtDesc.Width = width;
txtDesc.Height = height;
txtDesc.MipLevels = 0; // Max MipMap
txtDesc.Usage = D3D11_USAGE_DEFAULT; // Staging Texture Copy
txtDesc.BindFlags = D3D11_BIND_SHADER_RESOURCE | D3D11_BIND_RENDER_TARGET;
txtDesc.MiscFlags = D3D11_RESOURCE_MISC_GENERATE_MIPS;
txtDesc.CPUAccessFlags = 0;

// Copy the highest resolution from the staging texture
context->CopySubresourceRegion(texture.Get(), 0, 0, 0, 0, stagingTexture.Get(), 0, nullptr);

// Creating Resource View
device->CreateShaderResourceView(texture.Get(), 0, textureResourceView.GetAddressOf());

// Generate Mipmap reducing the resolution
context->GenerateMips(textureResourceView.Get()); 
```

결국에는 Mipmap 을 사용해줘야하므로, HLSL 에서는 그냥 `Sample()` 아니라 `SampleLevel()` 을 해줘야한다.


## Resources
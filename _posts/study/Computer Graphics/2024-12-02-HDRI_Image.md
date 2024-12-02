---
title: HDRI Images
layout: post
category: study
tags: [directx, computer graphics, cpp, shader]
published: false
---

## Introduction

Image 기반 Lighting 을 사용할때 환경 Map 일것이다. 

- SDR (Standard Dynamic Range) or LDR(Low Dynamic Range) 지금까지 사용해온것처럼 0.0 ~ 1.0 범위로 색을 표현하는 방식

- HDR (High Dynamic Range Rendering): HDRR 또는 High Dynamic Range Lighting 은 HDR 에서 Lighting 을 계산하는것이다. 결국 더 넓은 범위에 대한 조명에 대해서 REndering 을 할수 있다는 말... 넓은 범위라는건, 사용하는 숫자의 대한 범위가 넓다. LDR 이나 SDR 에서 하나 Pixel 에 대한 색깔을 표현할때에, `R8G8B8A8_UNORM` 기본 적으로 32 bits(8 x 4) 를 사용했고, 0 - 255 까지의 unsigned integer 의 값을 사용했으며, 그 범위를 Normalize 해서 사용했었다. 

즉 만약 환경의 Light 들이 많아서, Pixel Shader 에서 값을 처리 Color 값을 Return 할때 1 보다 큰값들을 처리를 못했었다. 즉 내부적으로는 output.pixelColor = clamp (..., 0.0, 1.0) 이런식으로 처리가 된다고 보면 된다. 

그래서 HDR 을 사용할때는 DXGI_FORMAT_R16G16B16_FLOAT 이러한 형태로 사용되기 때문에, 숫자의 범위가 굉장히 넓다고 보면 된다.

float 은 기본적으로 32 bits wide 인데, 최근 들어서는 16 bit 로도 충분하기 때문에 Half precision floating point 도 있다. GPU 는 최종적으로 half precision floating point 에 최적화가 잘되어있다고 한다. 그래서 대부분은 아래와 같은 방식으로 f16 library 를 사용하면 된다

```c++
vector<float> f32(image.size() / 2);
uint16_t *f16 = (uint16_t *)image.data();
for(int i =0 ; i < image.size() / 2; i++){
    f32[i] = fp16_ieee_to_fp32_value(f16[i]);
}

f16 = (uint16_t *)image.data();
for (int i = 0; i < image.size(); i++)
{
    f16[i] = fp16_ieee_from_fp32_value(f32[i] * 2.0f);
}
```

Tone Mapping: HDR 는 32 bit 를 16 bit 로 사용하는 숫자의 넓이를 크게... 근데 뭉뜽그려지는 빛이 있다. //TODO: image upload
 이러한 색부분을 조정을 해줘야한다. 이미지를 우리 모니터가 표현할수 있는 작은 범위로 바꿔주는걸 Tone Mapping 이라고 한다.

Expose: 카메라의 어떤 현상, 렌즈를 오래 열어 놓으면, 빛을 더 많이 받아들이는 현상 (즉 multiplication)

// TODO Expose 를 낮춰서, 강렬한 태양까지를 포함, 대신 16 bit 는 포함 하지 않는다. (그냥 전체가 어두어짐 Expose 를 낮췄을때)

Gamma Correction : 어떤 영역에 색을 더 넓게 보여줄지를 의미
OPENGL Gamma correction:

CRT 값은 2.2 낮춰지는 곡선이였는데, 1/2.2 를 곱하게 되면 직선으로 표혆라수 있다.
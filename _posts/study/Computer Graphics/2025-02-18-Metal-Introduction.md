---
title: Hello Triangle (Introduction to Metal) through IPAD App
layout: post
category: study
tags: [metal, computer graphics, shader]
published: false
--- 

## Introduction to Metal

DirectX 와 마찬가지로, GPU 를 사용할수 있게 만든 API 라고 할수 있다. 이 API 같은 경우 Parallel Processing 또는 Rendering 을 담당한다고 볼수 있다. 

## Draw Triangle on APP
일단 개발 Base 는 SwiftUI 로 하고, UIkit 은 사용하지 않는다. 

일단 중요한 Metal 에 뿐만 아니라 Graphics API (DirectX, Vulkan) 를 사용할때, 여러개의 Keyword 가 존재한다. 그리고 이거 Mapping 되는 Metal 의 API 를 보겠다.

```
* Device: 물리적인 하드웨어를 관리하는 객체 => MTLDevice 
* Command Queue: 커맨드를 저장하는 큐 => MTLCommandQueue 
* Command Buffer: 커맨드를 저장하는 버퍼 => MTLCommandBuffer 
* Render Command Encoder: 렌더링 커맨드를 인코딩하는 객체 => MTLRenderCommandEncoder 
* Render Pipeline: 렌더링 파이프라인 => MTLRenderPipeline
* Vertex Buffer: 정점 버퍼
* Index Buffer: 인덱스 버퍼
* Render Pipeline State: 렌더링 파이프라인 상태
* Descriptor: Rendering Pipeline 에 어떻게 Rendering 할지 정의하는 블루프린트
* Fence (Can be occluded)
```

TODO: 코드 추가

## Reference

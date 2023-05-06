---
title: Projection
layout: post
category: study
tags: [directx, computer graphics]
---

### DirectX Projection

Orthographic Projection (직교 투영)

Graphic (Rendering) Pipeline
Local -> World -> View -> Projection -> Screen

만약에 직교투영이 필요한 케이스는 바로 2D UI 를 작업할때 필요한데, 이때 Layer 라는게 필요하다.
그래서 한카메라는 UI 를 제외한 것을 보고, UI 의 카메라가 따로 있는거다.
Unity 같은 경우 32 Layer 이 있다.


Perspective Projection (원근 투영)
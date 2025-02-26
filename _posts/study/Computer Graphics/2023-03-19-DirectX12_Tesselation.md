---
title: Tesselation & Terrain & Picking
layout: post
category: study
tags: [directx, computer graphics]
published: false
---

### Tessellation
// TODO: Graphics Pipeline 추가

DirectX12 의 기준으로, Vertex Shader Stage 를 지난다음, `Hull Shader Stage`, `Tesellator Stage`, `Domain Shader Stage` 가 `Tessellation Stages 이다. Tesellation Stage 도 Geometric Shader Stage 처럼, 정점을 추가하는 Stage 이다. 

Dynamic LOD(Level Of Detail) 에 사용, 거리에 따로 Mesh 안에 Polygon 의 숫자가 달라진다. 

구성요소
Patch 안에(Control Point Group), Vertex 같은 Point 를 Control Point 라고 불림

Domain Shader 에서 모든 정점정보를 들고 오는데, 그때 정점과의 비율을 나타내는 `location` 정보를 가지고 있음.. 이거의 예시 필요

### Terrain
X, Y 축을 건들지 않고, Z 축만 사용해서 Terrain 이 표현 가능. 높이맵이 필요. (Terrain Surface & High Texture)

### Picking
Ray Casting 기술, 카메라위치에서 Ray 를 쏴서 물체가 Hit 했는지 안했는지
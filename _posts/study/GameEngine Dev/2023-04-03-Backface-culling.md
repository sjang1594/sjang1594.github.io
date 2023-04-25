---
title: Backface Culling
layout: post
category: study
tags: [Computer Graphics]
---

### Backface Culling (Ray Tracing / Rasterization)

Culling 이라는 단어는 "select from a large quantity; obtain from a variety of sources." 이렇게 정의가 된다. 여기서는 Backface culling 은 마치 Backside 를 골라서 없앤다라고 더 이해하면 될것같다. 즉 우리눈에 보이지 않는걸 구지 그릴 필요라는 의미에서 생긴다. 그렇다면 그 다음 질문은 왜? 그리지 않을까? 당연히 Rendering 을 할때, 구지 뒷면을 할 필요가 없다.

즉 우리 눈에 보이는 위치에서 물체를 뒷면을 고려하지 않고 그리는거다. 일단, 그렇다면 여기서 중요한거는 바로 수학이다. 어떻게 뒷면이고 앞면인지를 알수 있을까? 일단 Screen 좌표계가 있다고 가정하면, 세점의 vertex 의 normal 의 방향을 계산 하는 cross product 를 하는 방식에 따라서 앞면과 뒷면으로 나누어진다. 

TODO: Explain the coordinate system in virtual / screen 
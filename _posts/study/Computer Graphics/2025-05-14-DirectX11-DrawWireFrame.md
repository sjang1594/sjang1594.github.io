---
title: DirectX11 - Drawing WireFrame
layout: post
category: study
tags: [directx, computer graphics, shader]
published: true
---

### DirectX11 - Drawing Wire Frame

가끔씩은 우리가 어떤 Mesh 를 사용하고, 삼각형의 개수가 몇개인지를 알아야 할 필요가 있다. 그 이유에 대해서는 예를들어서, Mesh 들의 형태에 따라서, Performance 가 나올수도 있고, 더 Detail 한 Terrain 이나, Statue 에 따라서 내가 Runtime 에서 이 모델을 쓸수 있는지 없는지도 판단이 가능하다. 특히나 Unreal Engine 의 Nanite System 같은경우 Vertex 의 개수를 수많이 부풀려서, 더 그럴듯한 Model 을 만들기도 한다. 이거는 어느정도 Art 적인 면들도 충분히 있다. 


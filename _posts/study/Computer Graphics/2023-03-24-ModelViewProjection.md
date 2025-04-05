---
title: Model View Projection
layout: post
category: study
tags: [computer graphics, DirectX11]
published: true
---

### Model, View, Projection

생각보다, Virtual Environment, 즉 사람이 모니터를 봤을때, 물체의 움직임을 어떻게 정의하고, CPU 에서는 충분히 가능한 이야기일수 있다. 하지만 Game Engine 은 어떠한 물체를 그리기 위해서는, GPU 를 통해서 그려야만한다. 그때 그릴때, Vertex 의 정보 (Position, Index, Primitive:triangle...) 등을 정의할수 있다. 그리고 Pixel 정보에서 그림을 그릴때, Vertex 의 정보를 가지고 그리기를 시작한다. 
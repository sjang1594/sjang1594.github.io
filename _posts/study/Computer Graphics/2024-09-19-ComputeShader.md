---
title: Compute Shader
layout: post
category: study
tags: [directx, computer graphics, cpp, shader]
published: false
---

## Motivation

Unreal 또는 Unity 를 다루다 보면, 어떤거는 Vertex Shader / Pixel Shader / Geometry Shader 를 Pipeline Stage 를 태워서 사용해야하는지, 어떤거는 Graphics Pipeline 에 속하지 않은 GPGPU 를 아이디어를 사용한 Compute Shader 를 사용해야할지 모를수가 있다. 한참 Radar Simulation 을 구현하다가.. 한참 Pixel Shader 로 Unity 로 작성되어있길래 Unreal 에서도 Pixel Shader 로 하면 되겠구나...? 이러다가 2 개월이 지난 지금 엄청나게 후회하고 있고, 정확하게 Usage 도 모르게 사용했다 라는것에 현타가 오고, Compute Shader 에 대해서 정확하게 정리 된 글이 없어서 작성을 하기로 하였다. (개인적으로 Unity 는 뭔가 다 알아서 해주는 느낌인데, Unreal 은 뭔가 이거 아니면 안된다 라는 느낌이 강하다.)

## Prerequisites

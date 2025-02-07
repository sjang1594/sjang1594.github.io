---
title: Height Map
layout: post
category: study
tags: [directx, computer graphics, cpp, shader]
published: false
---

## Introduction

이제 점점 PBR 에 가까워지기 위해서는 Texture 들의 표현 방식들과 어떻게 shader 에서 이걸 처리 하느냐가 이제 Game Engine 에 따라서 굉장히 Realistic 한지를 판가름이 난다. 그중에 하나의 기술인 Height Map 을 보려고 한다.

## Height Map (Displacement Mapping)

Height Map 의 기본적인 요소는 grey scale image 라고 생각하면 된다.
자연의 불규칙적인것들을 표현 하기 위해서... 

// TODO: Image 

## AO (Ambient Occlusion)

구석자리는 옆에 있는 물체는 빛이 잘들어가지 않기 때문에, 자연스럽다. (Rasterization State 일때는, Ambient occlusion map)
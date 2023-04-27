---
title: Shadow Mapping
layout: post
category: study
tags: [directx, computer graphics]
---

### Shadow Mapping

결국 한마디로 그림자를 어떻게 만들지? 의 문제이다. 현실에서 그림자가 생기는 이유는, 어떠한 빛(Directional Light) 에 의해서 물체에 비추게 되어있을때, 그 물체가 만약에 빛이 통과되지 않는 물체라고 가정하에, 그 뒤에 배경이 빛을 못받아서 그림자가 생기는 이유이다.

Pixel Shader 에서 물체의 색상을 고려할때, 앞에 물체가 있는지 없는지만 판단?

Directional Light 에 카메라를 두고, `WorldViewProjMatirx` -> `ClipPos` -> W 로 나누기 -> `ProjPos(투영)` -> `Depth = Proj.Pos.z` Depth 를 RenderTarget 에 저장. 

그럼 우리가 화면에서 보여지는거는, 우리가 현재 보고 있는 카메라를 기준으로 `ViewPos` -> `ViewInverseMatrix` -> `WorldPos` 으로 간다음에, Directional Light 에 있는 카메라로 가서 ViewPojMatrix 를 보고 있는 화면 카메라의 `WorldPos` 에 곱해주면 -> `ClipPos` 로 넘어오고 -> w 로 나누면 -> `ProjPos(투영)` 좌표계로 넘어오면 [-1, 1] -> [0 ~ 1], [1 ~ -1] -> [0 ~ 1] -> 이 결과는 UV 좌표계로 넘어오면 Depth 정보를 받아서 비교 후에 그림자 적용을 할수 있다.  
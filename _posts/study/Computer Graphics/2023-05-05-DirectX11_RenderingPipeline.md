---
title: Rendering PipeLine in DirectX11
layout: post
category: study
tags: [directx, computer graphics]
---

### COMPTR

DirectX 의 공부에 앞서서, c++ 에서 자주 사용하는 shared_ptr 이있는데, Microsoft 에서 제공하는 `Microsoft::WRL::ComPtr is a c++ template smart-pointer for COM(Component Object Model) objects that is used extensively in Winodws Runtime (WinRT) C++ Programming.` 이라고 한다.

일단 사용할때 아래와 같이 정의할수 있다.
```c++
Microsoft::WRL::ComPtr<ID3D11Device> device; // COM Interface
Microsoft::WRL::ComPtr<ID3D11DeviceContext> context;
```

### Implement Initialization in Direct3D
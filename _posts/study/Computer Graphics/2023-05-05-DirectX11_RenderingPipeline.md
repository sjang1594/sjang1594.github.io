---
title: Rendering PipeLine in DirectX11
layout: post
category: study
tags: [directx, computer graphics]
---

## COMPTR - Window Programming & DirectX11 Initialization

DirectX 의 공부에 앞서서, c++ 에서 자주 사용하는 shared_ptr 이있는데, Microsoft 에서 제공하는 `Microsoft::WRL::ComPtr is a c++ template smart-pointer for COM(Component Object Model) objects that is used extensively in Winodws Runtime (WinRT) C++ Programming.` 이라고 한다.

일단 사용할때 아래와 같이 정의할수 있다.

```c++
Microsoft::WRL::ComPtr<ID3D11Device> device; // COM Interface
Microsoft::WRL::ComPtr<ID3D11DeviceContext> context;
```

만약 이러한 `ComObject` 와 관련된걸, brute-force 하게, C++ 로 만든다면, 이렇게 표현을 할것이다. `std::shared_ptr<ID3D11Device> device = make_shared<ID3D11Device>(...);1D3D11Device *device = nullptr;`. 그리고 `make_shared` or `new` 를 하는게 아니라, 용도에 맞게, 지정되어있는 함수로 만들어야한다.

Adapter 가 만들어졌다고 하는 가정하에, DirectX11 의 Device 와 Device Context 를 만들어줘야한다. DirectX 11 의 Device 란 Object 이며, 이 device 는 Desired Adaptor 에서, DirectX11 Render 가 사용할 object 를 생성하는 역활을 하고, 대부분 initialize 를 할때 개체가 생성되고, 소멸된다. `context` 는 사실 `device context` 인데, 이 역활은 어떤 Commands 를 submit 해주고, adaptor 가 실행을 시켜준다. 예를 들어서 Render Command 나, 어떠한 Transfer 할 Data 를 update 하는데 사용된다 (주로 Rendering Process 중일때...) 즉 둘다 Interface 라고 생각하면된다. 그래서 생성될때, `ID3D11Device` 와 `ID3D11DeviceContext` interface 를 통해서 생성된다.

일단 `Device` 에 관련되서 생성을 하려면 아래와 같이 해야한다. 그리고 필요한건 `context` 이다.

```c++
Microsoft::WRL::ComPtr<ID3D11Device> device; // COM Interface
Microsoft::WRL::ComPtr<ID3D11DeviceContext> context;

const D3D_FEATURE_LEVEL featureLevels[2] = {
        D3D_FEATURE_LEVEL_11_0,
        D3D_FEATURE_LEVEL_9_3};

D3D_FEATURE_LEVEL featureLevel;

HRESULT hr = D3D11CreateDevice(
    nullptr,
    D3D_DRIVER_TYPE_HARDWARE,
    0,
    creationFlags,
    featureLevels,
    ARRAYSIZE(featureLevels),
    D3D11_SDK_VERSION,
    &device,
    &m_d3dFeatureLevel,
    &context);
```

Device 가 생성된다고 해서, Render 를 한다는 말은 아니다. DirectX11 에서는 swapchain DXGI 를 통해서 만들어줘야한다.
 `SwapChain` 이란 `backbuffer` 의 개수를 관리하고, 한 buffer 마다 access 를 가능하다, 즉 이때 모니터에 갈거 따로 하나 backbuffer 에 그릴거 하나 이렇게 cover 를 한다. 그래서 아래의 그림처럼 SwapChain 안에 Buffer 를 끌어다가 Texture 를 설정해주고, 실제 Render 할 TargetView 만들어준다음에 기다리면서 switching 을 할수 있게 한다.

<figure>
  <img src = "../../../assets/img/photo/7-31-2023/architecture.png">
</figure>

```c++

```

## Introduction to Rendering Pipeline in D11

일단 어떤 기하의 정보를 정의한 이후로 Vertex Buffer 를 만들어줘야된다. 여기에서 Buffer 같은 경우는 GPU Memory 를 준비한다. 그래서 `Vertex` 의 정보(정점별 위치 및 Textrue Data) 를 담는 `VertexBuffer` 가 있고, 그 Vertex 가 어떤 순서로 이루어져야 하는지는 `IndexBuffer`(Rendering 할 모형의 Index 를 제공, 동일한 정점을 재사용) 에다가 넣어준다. 또 `Constant Buffer` 는 `MVP (Model, View, Projection)` 으로 정의 되어있다. `Constant Buffer` 의 의미상으로는 어떤 static data 를 가지고 있는데, 이게 pixel shader 호출에 필요한 정적데이터를 또는 모든 버텍스 및 Pixel 를 가르친다. 즉 Buffer 들을 CPU 가 정의했다가, GPU 에 넘기는 용도로 사용된다.

일단 구현을 봐보자면,

```c++

```

## Resources

- [Vulkan Pipeline Basics](https://vulkan-tutorial.com/Drawing_a_triangle/Graphics_pipeline_basics/Introduction)
- [Device and Device Context](https://www.milty.nl/grad_guide/basic_implementation/d3d11/device.html)
- [DirectX Tutorial](http://www.directxtutorial.com/Lesson.aspx?lessonid=111-4-1)
- [Projective Projection](https://en.wikipedia.org/wiki/Transformation_matrix#Perspective_projection)

### Implement Initialization in Direct3D
```c++
const D3D_DRIVER_TYPE driverType = D3D_DRIVER_TYPE_HARDWARE;

```

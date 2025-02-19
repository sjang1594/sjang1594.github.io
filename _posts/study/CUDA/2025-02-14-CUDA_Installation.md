---
title: CUDA Installation
layout: post
category: study
tags: [CUDA, c++, c]
---

## Prerequiste for CUDA

* CUDA 를 설치하기 위해서 해야하는것을 간단히 소개 하겠다. CUDA 를, 즉 개발 환경을 설정하려면 아래의 목록 대로 설치 할 필요가 있다.
    * Visual Studio 2019/2022
    * Nvida Graphic App
    * CUDA Toolkit (*******)
    * Nsight Visual Studio Editon Extension in Visual Studio
    * Nsight System
    * Nsight Compute 
    * vcpkg (C++ Library, like pip)

* vcpkg 에 필요한 라이브러리는 설명하지는 않겠다. 단 몇가지를 설치할 필요가 있다.

```
./vcpkg install vulkan:x64-windows, stb:x64-windows, glfw3:x64-windows, glm:x64-windows
./vcpkg install vulkan:x64-windows stb:x64-windows glfw3:x64-windows glm:x64-windows
./vcpkg install vulkan:x64-windows
./vcpkg install stb:x64-windows
./vcpkg install glfw3:x64-windows
./vcpkg install glm:x64-windows
```

## CUDA: Hello World
위의 내용을 설치하지 않아도, `cuda tool kit` 이 설치가 완료 되었다고 한다고 하면, 굳이 할 필요 없다. Visual Studio 만으로도 충분히 사용할 수 있다. 일단 C 에 Program Files 안에 CUDA Toolkit 안에 있는 예제 `.exe` 파일을 돌려보거나, 설치가 되어있다고 하면, Project 를  생성할때 아래와 같이 사용할수 있다.

![Alt text](../../../assets/img/photo/02-14-2025/image.png)

```c++

```


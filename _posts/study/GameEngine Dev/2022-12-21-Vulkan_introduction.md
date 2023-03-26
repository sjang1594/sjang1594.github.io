---
title: Vulkan Introduction
layout: post
category: study
tags: [Vulkan, Computer Graphics]
---

### Vulkan Introduction

The Vulkan is the graphical API made by `Khronos` providing the better abstraction on newer graphic cards. This API outperform? the Direct3D and OpenGL by explaining what it perform. The idea of the Vulkan is similar to the Direct3D12 and Metal, but Vulkan is cross-platform, and it can be used and developed in Linux or Window Environment.

However, the drawback of this could be is there will be many detailed procedure while using the Vulkan API, such as creating the buffer frame, managing the memory for buffer and texture image objects. That means we would have to set up properly on application. I realized that the Vulkan is not for everyone, it is only for people who's passionate on Computer Graphics Area. The current trends for computer graphics in Game Dev, they are switching the DirectX or OpenGL to Vulkan : [Lists of Game made by Vulkan](https://www.vulkan.org/made-with-vulkan). One of the easier approach could be is to learn and play the computer graphics inside of Unreal Engine and Unity.

By designing from scratch for the latest graphics architecture, Vulkan can benefit from improved performance by eliminating bottlenecks with multi-threading support from CPUs and providing programmers with more control for GPUs. Reducing driver overhead by allowing programmers to clearly specify intentions using more detailed APIs, and allow multiple threads to create and submit commands in parallel and Reducing shader compilation inconsistencies by switching to a standardized byte code format with a single compiler. Finally, it integrates graphics and computing into a single API to recognize the general-purpose processing capabilities of the latest graphics cards.

There are three preconditions to follow
* Vulkan (NVIDA, AMD, Intel) compatible graphic cards and drivers
* Expereince in C++ ( RAII, initializer_list, Modern C++11)
* Compiler above C++17 (Visual Studio 2017, GCC 7+, Clang 5+)
* 3D computer Graphics Experience
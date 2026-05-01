---
layout: page
title: Luna Engine
category: [Computer Graphics]
type: image
thumbnail: /assets/img/photo/1_latest/lunaEngine-thumbnail.png
year: 2024
---

## Luna Engine

Backend-agnostic real-time rendering engine supporting **Vulkan** and **DirectX 12** backends, built from scratch with a HAL (Hardware Abstraction Layer) design for portability and extensibility.

## Features

| Component | Description |
|-----------|-------------|
| Render Backend | Vulkan / DirectX 12 (swappable via HAL) |
| GPU Profiler | Frame timing and pipeline-stage attribution |
| Resource Management | Explicit memory, barriers, descriptor heaps |
| Isaac Sim Interop | Streaming simulation state into the renderer |
| Build System | Premake5 |
| Debug UI | ImGui integration |

## Architecture

- **HAL Design Pattern** — graphics API calls abstracted behind a unified interface, enabling backend swap without touching render logic
- **Render Graph** — explicit dependency tracking between passes for automatic resource barrier insertion
- **Explicit Memory Management** — manual heap allocation, resource upload, and lifetime control on both DX12 and Vulkan

## Motivation

Built as an open-source alternative to proprietary sim environments (Isaac SIM, etc.) for sensor simulation research, and as a portfolio demonstration of low-level GPU systems engineering.

## Source

- [GitHub — sjang1594/luna-engine](https://github.com/sjang1594/luna-engine)

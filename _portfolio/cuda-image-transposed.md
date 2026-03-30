---
title: CUDA Image Transposed
category: [CUDA, Parallel Computing]
type: video
year: 2025
---

## CUDA Image Transposed

| File | Kernel | Memory pattern |
|------|--------|----------------|
| `naive_transpose.cu` | Row-major read, column-stride write | Write NOT coalesced |
| `tiled_transpose.cu` | Shared memory tile, bank-conflict-free | Coalesced read AND write |

## Jargon
- Bank conflict: Shared Memory is divded into banks. If multiple threads access the same bank, accesses are serialized, leading to performance degradation. (This is important because it gives a good understanding of gpu architecture and how to optimize memory access patterns.)
- Stride: The step size between consecutive memory accesses. For example, in a row-major order, the stride for column access is equal to the number of columns, which can lead to non-coalesced accesses.
- Coalesced access: When threads in a warp access memory addresses that are contiguous or follow a specific pattern, allowing the GPU to combine these accesses into a single transaction, improving performance.

## Profiling
CPU Kernel Profiling via NVIDIA Nsight Systems (nsys) and NVIDIA Nsight Compute (ncu) reveals the following performance metrics for the three kernels:

| Kernel                    | Avg (ms) | Med (ms) | Instances |
| ------------------------- | -------- | -------- | --------- |
| copyKernel (peak ref)     | 0.351    | 0.345    | 100       |
| naiveTranspose            | 1.131    | 1.084    | 101       |
| tiledTransposeNoPad (V1)  | 0.618    | 0.609    | 100       |
| tiledTranspose +1Pad (V2) | 0.392    | 0.381    | 101       |

**67.1MB read + 67.1MB write = 134.2MB**
| Kernel         | ms    | GB/s     | vs Copy             |
| -------------- | ----- | -------- | ------------------- |
| Copy (peak)    | 0.345 | 389 GB/s | baseline            |
| Naive          | 1.084 | 124 GB/s | 32% (strided write) |
| Tiled NoPad V1 | 0.609 | 220 GB/s | 57% (bank conflict) |
| Tiled +1Pad V2 | 0.381 | 352 GB/s | 90%                 |


### Analysis
Naive (32%)
- Strided writes continuously evict data from the L2 cache
- Each element results in a separate DRAM write

Tiled NoPad V1 (57%)
- Shared memory 32-way bank conflict
- Phase 2 (Shared→Global) Serialized

Tiled +1Pad V2 (90%)
- bank conflict = 0
- Bi-directional coalesced (read + write)
- Copy bandwidth의 90%

### Resource
- [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html)
- [Source Code](https://github.com/sjang1594/self-study/tree/master/CUDA%20Programming%20and%20Pytorch/cuda/5.%20ImagTranspose)
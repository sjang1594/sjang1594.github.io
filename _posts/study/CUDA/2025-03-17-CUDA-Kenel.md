---
title: Vector Addition 
layout: post
category: study
tags: [c++, cuda]
published: true
---

# CUDA Kernel

## Kernel Function (Vector Addition)

일반적으로 c 에서는 두가지의 Vector(Array) 를 더한다고 가정을 했을때, 아래의 방식대로 더한다.

```c
int main(void) {
    // host side
    const int SIZE = 6;
    const int a[SIZE] = {1, 2, 3, 4, 5, 6 };
    const int b[SIZE] = {10, 20, 30, 40, 50, 60 };
    int c[SIZE] = {0};

    for (register int i = 0; i < SIZE; ++i) {
        c[i] = a[i] + b[i];
    }
    return 0;
}
```add.cu

위의 For-Loop 안에 있는 Body 가 있다, 이때를 `Kernel Function` 이라고도 한다. (with proper value). 실제 예시로는 아래와 같다. 왜 굳이 idx 를 넘기느냐는 병렬 처리를 위해서 `Kernel Function` 을 Define 하는것과 같다. 하지만 여기도 아직은 CPU 에서 처리를 하는거다. (CallStack 에는 CPU[0] executes add_kernel(0 ...)) 이런식으로 수행이 SIZE - 1 만큼 될거다. 즉 이건 sequential execution 이라고 생각한다.

```c
void add_kernel(int idx, const int* a, const int* b, int*c) {
    int i = idx;
    c[i] = a[i] + b[i];
}

for (register int i = 0; i < SIZE; ++i) {
    add_kernel(i, a, b, c);
}
```

만약 multi-core CPU's 또는 Parallel Execution 을 한다고 가정을 하면 어떨까? 즉 코어가 2개라면, 짝수개씩 병렬로 처리가 가능하다.

```
at time 0: CPU = core#0 = executes add_kernel(0, ...) 
at time 0: CPU = core#1 = executes add_kernel(1, ...)
at time 1: CPU = core#0 = executes add_kernel(2, ...) 
at time 1: CPU = core#1 = executes add_kernel(3, ...)
...
at time (n-1)/2: CPU = core#1 = executes add_kernel(SIZE - 1, ...)
```

그렇다면 GPU 는 어떻게 될까? GPU 는 엄청 많은 Core 들을 가지고 있기 때문에, 엄청난 Parallelism 을 가지고 갈수 있다. 아래와 같이 Time 0: 에 ForLoop 을 처리를 병렬 처리로 할수 있다는거다.

```
at time 0: CPU = core#0 = executes add_kernel(0, ...) 
at time 0: CPU = core#1 = executes add_kernel(1, ...)
at time 0: CPU = core#2 = executes add_kernel(2, ...) 
at time 0: CPU = core#3 = executes add_kernel(3, ...)
...
at time 0: CPU = core(#n-1) = executes add_kernel(SIZE - 1, ...)
```

위의 내용을 정리 하자면 아래와 같다. 즉 시간 순서별로 처리를 하는쪽은 CPU, 코어별로 처리를 하는건 GPU 라고 볼수 있다.

| CPU Kernels                              | GPU Kernels            |
| :--------------------------------------: | :-----------------:    |
| with a single CPU Core, For loop         | a set of GPU Cores     |
| sequential execution                     | parallel execution     |
| for-loop                                 | kernel lanuch          |
| CPU[0] for time 0                        | GPU[0] for core #0     |
| CPU[1] for time 1                        | GPU[1] for core #1     |
| CPU[n-1] for time n-1                    | GPU[n-1] for core #n-1 |

CUDA vector addition 같은 경우 여러가지 Step 이 있다고 한다.
1. host-side
   1. make A, B with source data
   2. prepare C for the result
2. data copy host -> device
   1. cudaMemcpy from host to device
3. addition in CUDA
   1. kernel launch for CUDA device
   2. result will be stored in device (VRAM)
4. data copy device -> host
   1. cudaMemcpy from device to host
5. host-side
   1. cout

### CUDA Programming Model

### CUDA Implementation

### CUDA Kernel Launch
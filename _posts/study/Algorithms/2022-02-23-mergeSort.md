---
title: Merge Sort
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Merge Sort 
* Reviewing what I studied, how this work will be explained as well. 
---

This sorting algorithm is based on the `devide and conquer` strategy. The steps in simple array are as follows:

1. Divide the input array into two halves. (Divide)
2. Sort each half. (Conquer)
3. Merge the two halves. (Combine)

Basically, we're breaking the problem of sorting the array into two smaller problems. (sub-problems), then we merge the two halves, which are sorted.

The problem state: Give some array, and sort it in increasing order. There are two solution can exist: bottom up (for loop), and top down (recursive). Let's explore what are the code looks like, and the logic behind.

1. If the size of the array or the vector is 0 or 1, it is already sorted. The sort doesn't happen when it's divided, it happens when it's merged.

```c++

int main() 
{
    std::vector<int> vec = {3, 5, 8, 9, 6, 2};
    mergeSort(vect, )
}
```

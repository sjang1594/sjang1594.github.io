---
title: Quick Sort
layout: post
category: study
tags: [c++, algorithm]
published: false
---

## Quick Sort

* Reviewing what I studied, how this work will be explained as well. 
---

This sorting algorithm is based on the `divide and conquer` strategy. This is the quick sort's strategy, but as compared to merge sort, the list is divided into unbalanced partitions. Let's review the divide and conquer strategy in quick sort.

* Divide: Since you have a pivot value, you can divide the list into two partitions. Each partition can have an unequal number of elements.
* Conquer: You can sort each partition recursively.
* Combine: Since the partitions are sorted, you don't need to do anything.

Let's actually see how this works. 

First Pass:
* Initial State: {5, 3, 8, 4, 9, 1, 6, 2, 7}
1. Pick a pivot value: 5 (it can be any value, but for now, let's pick 5)
2. pick a pointer from the left: 3
3. pick a pointer from the right: 7
4. compare the left pointer and the right pointer. 
5. if the left pointer is less than the pivot value, move the left pointer to the right. else swap the right pointer and the left pointer.
6. if the right pointer is greater than the pivot value, move the right pointer to the left else swap the left pointer and the right pointer.
7. repeat the process until the left pointer and the right pointer cross each other.
8. swap the pivot value with the right pointer value.

Second Pass:
1. Divide into two partitions: {3, 4, 1, 2} and {9, 8, 6, 7}
2. Pick a pivot value: 3
3. pick a pointer from the left: 4
4. pick a pointer from the right: 2
5. compare the left pointer and the right pointer. 
6. if the left pointer is less than the pivot value, move the left pointer to the right. else swap the right pointer and the left pointer.
7. repeat the process until the left pointer and the right pointer cross each other.
8. swap the pivot value with the right pointer value.

Third Pass:
1. Divide into two partitions: {1, 2} and {4, 3}
2. Pick a pivot value: 1
3. pick a pointer from the left: 2
4. pick a pointer from the right: 2

and so on.

This can be done recursively. Let's look at the code.

```cpp

```

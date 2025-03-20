---
title: Quick Selection Sort
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Quick Selection Sort

* Reviewing what I studied, how this work will be explained as well. 
---

### Quick Selection Sort
Quick Selection, also known as Quickselect or Hoare's Selection Algorithm, is an efficient algorithm designed to find the kth smallest element in an unordered list. Developed by Tony Hoare (the same computer scientist who created Quicksort), this algorithm shares the same partitioning strategy as Quicksort but with a crucial difference in its recursive approach.

### Algorithm Overview
Quickselect uses a divide-and-conquer approach similar to Quicksort:

1. Choose a Pivot: Select an element from the array as the pivot
2. Partition: Rearrange the array so elements less than the pivot are on the left, and elements greater are on the right
3. Selective Recursion: Unlike Quicksort which recurses on both partitions, Quickselect only recurses on the partition that contains the kth element we're looking for

This selective recursion is what gives Quickselect its efficiency advantage over a full sorting algorithm when we only need to find a specific element.

### Implementation

```c++
int partition(int data[], int lo, int hi) {
    int pivot = data[hi];

    int i = lo -1;
    for(int j = lo; j < hi; j++) {
        if (data[j] <= pivot)
            swap(data[++i], data[j];)
    }
    swap(data[++j], data[hi]);
    return i;
}

void quickSelectRec(int data[], int lo, in hi, int k) 
{
    if (lo == hi) return;

    int pivotIndex = partition(data, lo, hi);

    if (k == pivotIndex)
        return;
    else if (k < pivotIndex) 
        quickSelectRec(data, lo, pivotIndex - 1, k);
    else
        quickSelectRec(data, pivotIndex + 1, hi, k);
}


void quickSelect(int data[], int n, int k) {
    quickSelectRec(data, 0, n - 1, k);
}

```

### Time Complexity
The time complexity of Quickselect varies depending on the scenario:

1. Best Case: O(n) - This occurs when each partition divides the array into roughly equal halves.
2. Average Case: O(n) - Even with random pivot selection, the algorithm performs linearly on average.
3. Worst Case: O(n²) - This happens when the partitioning is maximally unbalanced (e.g., when the array is already sorted and we choose the first or last element as pivot).

The linear average-case time complexity makes Quickselect significantly more efficient than sorting algorithms (which require at least O(n log n) time) when we only need to find a specific element.
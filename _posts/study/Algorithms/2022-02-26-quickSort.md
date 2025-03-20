---
title: Quick Sort
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Partition & Quick Sort

* Reviewing what I studied, how this work will be explained as well. 
---

Quick Sort is an efficient, comparison-based sorting algorithm that employs the divide and conquer strategy. Unlike Merge Sort which divides arrays into equal halves, Quick Sort creates unbalanced partitions based on a pivot element. This characteristic gives Quick Sort its name - it's particularly "quick" for many real-world scenarios.

### The Divide and Conquer Strategy in Quick Sort
1. Divide: Select a pivot element and partition the array into two sub-arrays - elements less than the pivot and elements greater than the pivot.
2. Conquer: Recursively sort the sub-arrays.
3. Combine: Since the partitions are already sorted in place, no explicit combination step is needed.
Let's actually see how this works. 

### Partitioning
Partitioning is a crucial step in the Quick Sort algorithm where elements are rearranged around a pivot value. There are two main partitioning schemes: Lomuto and Hoare.

**Lomuto Partition Scheme**
The Lomuto partition scheme typically selects the last element as the pivot. It uses a one-directional scanning technique that maintains three distinct partitions: elements less than the pivot, elements greater than the pivot, and the unknown section.

```c++
pair<int, int> lomutoPartition(int data[], int lo, int hi) {
    int pivot = data[hi]; // alternatively you can select the pivot in the middle of the array.

    int i = lo - 1; // int i = 0
    for (int j = lo; j < hi; j++) {
        if(data[j] <= pivot)
            swap(data[++i], data[j]);  // data[i++]
    }

    swap(data[++i], data[hi]);   // data[i]
    return make_pair(i - 1, i + 1);
}
```

**Hoare Partition Scheme**
The Hoare partition scheme, developed by Sir Charles Antony Richard Hoare (the creator of Quick Sort), typically selects the first element as the pivot. It uses a two-directional scanning technique with two pointers moving in opposite directions.

```c++
pair<int, int> hoarePartition(int data[], int lo, int hi) {
    int pivot = data[(lo + hi) / 2];
    int i = lo - 1;
    int j = hi + 1;

    while(true){
        do i++; while(data[i] < pivot);
        do j--; while(data[j] > pivot);

        if (i < j)
            swap(data[i], data[j])
        else 
            break;
    }

    return make_pair(j, j+1);
}
```

version 2:
```c++
pair<int, int> hoarePartition2(int data[], int lo, int hi) {
    int pivot = data[(lo + hi) / 2];

    int i = lo;
    int j = hi;
    while( i <= j ){
        while(data[i] < pivot)
            i++;
        while(data[j] > pivot)
            j--;

        if (i < j)
            swap(data[i++], data[j--];
        else
            i++;
    }
    return make_pair(j, j+1);
}
```

version 3: when pivot was selected in the first element
```c++
pair<int, int> hoarePartition3(int data[], int lo, int hi) {
    int pivot = data[lo];

    int i = lo;
    int j = hi+1;
    while(true) {
        do i++; while( i <= hi && data[i] < pivot);
        do j--; while( j > lo && data[i] > pivot);

        if(i < j)
            swap(data[i], data[j]);
        else
            break;
    }
    swap(data[lo], data[hi]);
    return make_pair(j -1, j+1);
}
```

### 3-way Partitioning
This is very specific cases, where there are multiple or repetitive numbers:

Then we use `3-way partitioning`. There are two 3-way partitioning; **hoare partition** and **Bentley-Macllroy.**

```c++
pair<int, int> partition3wayHoare(int data[], int lo, int hi) {
    int pivot = data[(lo + hi)/2];

    int lt = lo;
    int gt = hi;
    for (int i = lo; i <= gt;) {
        if(data[i] < pivot)
            swap(data[lt++], data[i++])
        else if (data[i] > pivot)
            swap(data[i], data[gt--])
        else
            i++;
    }
    return make_pair(lt - 1, gt + 1);
}

pair<int, int> partitionBently3way(int data[], int lo, int hi) {
    int pivot = data[(lo + hi) /2];
    int i = lo - 1, j = hi + 1;
    int p = lo - 1, q = hi + 1;

    while(true) {
        while(data[++i] < pivot);
        while(data[--j] > pivot);
    

        if (i < j) {
            swap(data[i], data[j]);
            if (data[i] == pivot)
                swap(data[++p], data[i]);
            if (data[j] == pivot)
                swap(data[--q], data[j]);
        } else {
            if (i == j)
                swap(data[++p], data[i]);
            break;
        }
    }

    i = j +1;
    for (int k = lo; k <= p; k++)
        swap(data[k], data[j--]);
    for (int k = hi; k >= q; k--)
        swap(data[k], data[i++]);
    return make_pair(j, i);
}
```

So using one of those partition mechanism, we can use one of those above.

### How to select right pivot value?
1. first or last: 
2. random: `int pivot = data[rand() % (hi - lo + 1) + lo];`
3. middle
4. MED3 (Median of Median)

Standard C++ Library: Select Pivot
```c++
int choosePivot(int data[], int lo, int hi)
{
    int n = hi - lo + 1;
    int mid = (lo + hi) / 2;
    if (n > 7) {
        if (n > 40) {
            lo = MED3(data, lo, lo + d, lo + 2*d);
            mid = MED3(data, mid - d, mid, mid + d);
            hi = MED3(data, hi - 2*d, hi - d, hi);
        }
        mid = MED3(data, lo, mid, hi);
    }
    return mid;
}

int pivot = data[choosePivot(data, lo, hi)];
```

### Algorithm Walkthrough
Let's trace through the Quick Sort algorithm with a concrete example:

`Initial Array: {5, 3, 8, 4, 9, 1, 6, 2, 7}`

First Partition:
1. Select pivot: Let's choose the first element, 5
2. Initialize pointers:
   - Left pointer starts at index 1 (value 3)
   - Right pointer starts at the last index (value 7)
3. Partitioning process:
   - Move left pointer rightward until finding an element ≥ pivot
   - Move right pointer leftward until finding an element ≤ pivot
   - Swap these elements if pointers haven't crossed
   - Continue until pointers cross

4. Final swap: Place pivot at its correct position by swapping with the right pointer
5. Result: {2, 3, 1, 4, 5, 9, 6, 8, 7}

Now we have two sub-arrays: {2, 3, 1, 4} (elements < 5) and {9, 6, 8, 7} (elements > 5).

Second Partition (Left Sub-array):
1. Select pivot: 2
2. Partitioning process: Similar to above
3. Result: {1, 2, 3, 4} with sub-arrays {1} and {3, 4}

Third Partition (Right Sub-array):
1. Select pivot: 9
2. Partitioning process: Similar to above
3. Result: {7, 6, 8, 9} with sub-arrays {7, 6, 8} and {}

The process continues recursively until all sub-arrays are sorted.

This can be done recursively. Let's look at the code.

```cpp

void quickSortRect(int data[], int lo, int hi) {
    if (lo >= hi) return;

    int leftLast, rightFirst;
    auto [leftLast, rightFirst] = partition(data, lo, hi);

    quickSortRec(data, lo, leftLast);
    quickSortRec(data, rightFirst, hi);
}

void quickSort(int data[], int n) {
    quickSortRec(data, 0, n -1)
}
```

### Time Complexity
The time complexity is based on the pivot value, because this will make array to be unbalanced. The worst case would be O(n^2), but the best case would be O(nlogn)
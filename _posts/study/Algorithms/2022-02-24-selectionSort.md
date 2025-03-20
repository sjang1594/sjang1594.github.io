---
title: Selection Sort
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Selection Sort

* Reviewing what I studied, how this work will be explained as well. 
---

Selection Sort is a simple and intuitive comparison-based sorting algorithm. The core idea behind this algorithm is to divide the array into a sorted portion and an unsorted portion, then repeatedly find the smallest (or largest) element from the unsorted portion and place it at the end of the sorted portion.

### Algorithm Steps
Selection Sort operates through the following steps:

1. Initialization: Conceptually divide the array into a sorted portion (initially empty) and an unsorted portion (initially the entire array).
2. Find Minimum: Find the smallest element in the unsorted portion.
3. Swap: Exchange the found minimum with the first element of the unsorted portion.
4. Boundary Shift: Move the boundary between sorted and unsorted portions one position to the right.
5. Repeat: Continue this process until the entire array is sorted.

You may find this algorithm to be too easy!

### Implementation

```c++
void SelectionSort(vector<int>& arr) {
    int n = arr.size();

    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;

        for (int j = i + 1; j <= n; j++) {
            if (arr[j] < arr[minIdx])
                minIdx = j;
        }

        swap(arr[i], arr[minIdx]);
    }
}

void printArray(vector<int>& arr) {
    for (int& val : arr) {
        cout << val << " ";
    }
    cout << endl;
}


int main()
{
    vector<int> arr = { 64, 25, 12, 22, 11 };
    cout << "Original array: ";
    printArray(arr);

    SelectionSort(arr);

    cout << "Sorted array: ";
    printArray(arr);
}
```

The time complexity would be in for-loop (inner loop and outer loop) => O(n²) for all cases.

### Kth Selection Sort

**Problem Statement:**
The selection problem is defined as: Given an array of n elements and an integer k (1 ≤ k ≤ n), find the kth smallest (or largest) element in the array.

### Implementation
```c++

void SelectionSort(vector<int> vec, int lo, int hi)
{
    int minIdx = lo;
    for (int i = lo + 1; i <= hi; i++)
    {
        if(vec[i] < vec[minIdx])
            minIdx = j;
    }
    swap(vec[lo], vec[minIdx]);
}

void PartialSelectionSort(vector<int> vec, int k) 
{
    for (int i = 0; i < k; i++) 
    {
        SelectionSort(vec, i, k)
    }
}

int main() {
    vector<int> vec = { 7, 10, 4, 3, 7, 20, 15 };
    int k = 4;
    PartialSelectionSort(vec, k);
}
```

The time complexity for this O(kn), but if k is smaller value, it can be interpreted as O(n), but if k is large enough, it is considered to be O(n²)
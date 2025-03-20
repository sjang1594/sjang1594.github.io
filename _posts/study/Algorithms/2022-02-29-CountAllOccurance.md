---
title: Count All Occurence
layout: post
category: study
tags: [c++, algorithm]
published: true
---

### Count All Occurence 

* Reviewing what I studied, how this work will be explained as well. 
---

### Problem Statement
정렬되어 있는 배열 안에 어떤 값이 몇번 들어있는지를 세는 알고리즘을 작성하시요

>> Input: 
>> Array: 1, 2, 3, 3, 3, 5, 6, 6, 7, 16
>> Target: 3
>> Output: 3

### Linear Search
```c++
int CountAllOccurence(int arr[], int n, int x) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) count++;
    }
    return count;
}
```

Time complexity would be O(N).

### Two Pointer
```c++
int countSpecficElement(const std::vector<int>& vec, int target) {
    if (vec.empty()) { return 0; }

    int n = vec.size();
    int i = 0;

    while(i < n && vec[i] <= target) {
        if (vec[i] == target) {
            int j = i;

            while(j < n && vec[j] == target) {
                j++;
            }

            return j - i;
        }

        i++;
    }
    return 0;
}
```

Time Complexity would be O(N).

### Binary Search

```c++
int BinarySearch(const vector<int>& vec, int lo, int hi, int x){
    while(lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (vec[mid] < x) lo = mid+1;
        else if (vec[mid] > x) hi = mid-1;
        else return mid;
    } 
    return -1;
}
```

The Time complexity would be O(logN + count)

### Two Binary Search (Range Method)
I called this as range is because we find the first occurence(location within the range) from left to right, and second occurence from right to left, then we return the total count from that range.

```c++
int Count(const vector<int>& vec, int x) {
    const int n = vec.size();
    int i = BinarySearch(vec, 0, n-1, x);
    if (i == -1) return;

    // we find the first one
    int count = 1;
    int left = i - 1;
    while (left >= 0 && arr[left] == x) {
        count++;
        left--;
    }

    int right = i + 1;
    while(right < n; && arr[right] == x) {
        count++;
        right++;
    }
    return count;
}
```

This guarentees the time complexity to be O(logN)
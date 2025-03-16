---
title: Sequence and Queries 1. [Lv0]
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Programmers: Lv.0 Sequency and Queries 1.
Given an integer array arr and a 2D integer array queries, where each element of queries represents a query in the form of [s, e], perform the following operation for each query:
For each query, increment arr[i] by 1 for all i such that s ≤ i ≤ e.
Return the array arr after processing all queries according to the above rule.

### Constraints:
The length of arr is between 1 and 1,000 (inclusive).
Each element of arr is between 0 and 1,000,000 (inclusive).
The length of queries is between 1 and 1,000 (inclusive).
For each query [s, e], s and e are between 0 and the length of arr minus 1 (inclusive).

### Implementation
```cpp
vector<int> solution(vector<int> arr, vector<vector<int>> queries) {
    for (int i = 0; i < queries.size(); i++) {
        int start = queries[i][0];
        int end = queries[i][1];
        for (int j = start; j <= end; j++) {
            arr[j]++;
        }
    }
    return arr;
}
```

instead of creating the output answer, we can just reduce the space, by writing into arr directly.
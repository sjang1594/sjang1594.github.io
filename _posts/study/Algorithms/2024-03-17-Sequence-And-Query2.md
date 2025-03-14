---
title: Sequence and Queries 2. [Lv0]
layout: post
category: study
tags: [C/C++, Algorithm]
published: true
---
## Programmers: Lv.0 Sequency and Queries 2.
Given an integer array arr and a 2D integer array queries, where each element of queries represents a query in the form of [s, e, k], perform the following operation for each query: For each query, find the smallest element in arr[i] that is greater than k for all i such that s ≤ i ≤ e. Return an array containing the answers for each query in the order they were processed. If no such element exists for a query, store -1 for that query.

### Constraints:
The length of arr is between 1 and 1,000 (inclusive).
Each element of arr is between 0 and 1,000,000 (inclusive).
The length of queries is between 1 and 1,000 (inclusive).
For each query [s, e, k], s and e are between 0 and the length of arr minus 1 (inclusive).

### Implementation
```cpp
vector<int> solution(vector<int> arr, vector<vector<int>> queries) {
    int INF = std::numeric_limits<int>::max();
    vector<int> answer(queries.size(), INF);
    for(int i = 0; i < queries.size(); i++) {
        int start = queries[i][0];
        int end = queries[i][1];
        int compare = queries[i][2];
        
        for (int j = start; j <= end; j++) {
            if (arr[j] > compare) {
                answer[i] = min(answer[i], arr[j]);
            }
        }
        
        if (answer[i] == INF) answer[i] = -1;
    }
    return answer;
}
```

Since, we're looping through the queries n, which is O(n), but there is inner loop which is start time to end time. In the worst case, it can be O(n^2).
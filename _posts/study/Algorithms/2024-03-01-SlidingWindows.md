---
title: Sliding Windows Problem LeetCode - Diet Plan Performance
layout: post
category: study
tags: [C/C++, Algorithm]
published: true
---

## LeetCode - Diet Plan Performance [Sliding Windows - Easy] - 1176

* [LeetCode - Diet Plan Performance](https://leetcode.com/problems/diet-plan-performance/)

## How to Solve

```cpp
int dietPlanPerformance(vector<int>& calories, int k, int lower, int upper) {
    int points = 0;
    int current_sum = 0;

    for (int i = 0; i < calories.size(); i++) {
        current_sum += calories[i]; // 일단 현재의 Current Sum 을 구한다.

        if (i - k >= 0) {                           // 만약 윈도우 사이즈를 넘어가면, 왼쪽 원소를 빼준다. 즉 이말은 즉슨, k = 1 이면 전에 있던 0 을 빼줘, 1 만 보게끔 하는것이다. 
            current_sum -= calories[i - k]; 
        }

        if (i - k + 1 >= 0) {                      // 윈도우의 시작점 Index 다. k = 2 라고 하면, i - k + 1 = 0 이, 0 부터 만들어진다는 뜻이다. 
            if (current_sum < lower) {
                points--;
            } else if (current_sum > upper) {
                points++;
            }
        }
    }
}
```

## Review
하... Easy 라고 했는데 오랜만에 하니까, Sliding Window 문제가 생각이 안나서 좀 헤맸다. Sliding Windows 라는건 Array[i] 가 있다고 하면, w size 만큼 윈도우를 옮겨가면서 처리하는 문제를 말한다. 

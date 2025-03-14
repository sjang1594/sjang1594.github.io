---
title: Climbing Stairs [Easy]
layout: post
category: study
tags: [C/C++, Algorithm]
published: true
---

## LeetCode 70: Climbing Stairs [Easy]
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### Approach
This is typically done in recursive fashion. But think of this. if i have steps 1, 2, 3, ... i - 2, i - 1, i. Then, we need to use a step for i - 1 or i - 2 to get to i. This means I have several different steps to get to i. (this satisfies the optimal substructure). we can make a simple S(1) = 1, S(2) = 2, S(n) = S(n - 1) + S(n - 2).

### First Implementation:
When I tested this on recursive way and submit, it exceed Time Limit!... Oh no...
```cpp
class Solution {
public:
    int climbStairs(int n) {
        if (n < 1 || n > 46) return 0;
        if (n == 1) return 1;
        if (n == 2) return 2;
        return climbStairs(n - 1) + climbStairs(n - 2);
    }
};
```

### Second Implementation:
Now, I need to use dynamic programming, for top-down approach, it exceed Memory Limit, which possibly because of recursive way of saving into cache won't work very well.

```cpp
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 0) return 0;
        else if (n == 1) return 1;
        else if (n == 2) return 2;
        vector<int> dp(n+1, 0);
        
        if (dp[n]) return dp[n];
        int result = climbStairs(n - 1) + climbStairs(n - 2);
        return dp[n] = result;
    }
};
```

### Third Attempts:
Now I choose the bottom up approach, and it worked very well! 
```cpp
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 0) return 0;
        else if (n == 1) return 1;
        else if (n == 2) return 2;
        vector<int> dp(n+1, 0);
        dp[1] = 1;
        dp[2] = 2;
        
        for(int i = 3; i <= n; i++) {
            dp[i] = dp[i -1] + dp[i -2];
        }
        return dp[n];
    }
};
```
---
title: Programmers - Target Number & LeetCode - Target Sum
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Programmers: Target Number

### Description
Given an array of non-negative integers numbers, and a target number target, write a function solution that returns the number of ways to add or subtract these numbers without changing their order to reach the target number.

For example, using the numbers ``, you can make the target number 3 in the following five ways:

>> -1+1+1+1+1 = 3
>> +1-1+1+1+1 = 3
>> +1+1-1+1+1 = 3
>> +1+1+1-1+1 = 3
>> +1+1+1+1-1 = 3

### Thinking Process

Intially, when I try to solve this problem, I was thinking that this is typcial dp problem in such that if you select one number in the array, then you can choose either - number or positive number. Then, I was thinking you don't really have to approach this problem with dp, just simple bfs or dfs can be possible
- If we want to solve this by the recursive way, we need a constraint, constraint would be the vector's size. Let's say that we've started the +1 by adding the first number in the vector, then index has been already incremented by 1. So, by having the index, we can track what index we've used to get the target value.

### Implementation
DFS
```c++
#include <string>
#include <vector>

using namespace std;
void searchTargetNumber(vector<int>& vec, int tar, int index, int sum, int& answer) {
    if (index == vec.size()) {
        if (sum == tar) {
            answer++;
        }
        return;
    }
    
    searchTargetNumber(vec, tar, index+1, sum + vec[index], answer);
    searchTargetNumber(vec, tar, index+1, sum - vec[index], answer);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    searchTargetNumber(numbers, target, 0, 0, answer);
    return answer;
}
```

BFS
This actually worked on several test cases, except if there are a lot of nums in vector, it exceeds time limits because this is 2^n
```c++
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int answer = 0;

        deque<pair<int, int>> dq;
        dq.push_back({nums[0], 0});
        dq.push_back({-nums[0], 0});
        
        while(!dq.empty()) {
            int value = dq.front().first;
            int index = dq.front().second;
            index += 1;
            dq.pop_front();

            if (index < nums.size()) {
                dq.push_back({value + nums[index], index});
                dq.push_back({value - nums[index], index});
            } 
            else {
                if (value == target)
                    answer++;
            }
        }
        return answer;
    }
};
```

### Dynamic Programming
Top-down Approach: This it pretty special one, one thing we need to notice is the way to save the totalsum with current sum. This is efficient way to store all possible sum. For example, if the total sum is 5, then `-5 + 5 = 0` which is index at 0, `-4 + 5 = 1(index)`, `-3 + 5 = 2(index)`, and so on. This ensures the O(n * totalSum);
```c++
class Solution {
public:
    int memoization(vector<int>& nums, int currentIndex, int currentSum, int target, vector<vector<int>>& memo) {
        if (currentIndex == nums.size()) {
            if (currentSum == target) {
                return 1;
            } else {
                return 0;
            }
        } else {
            // done
            if (memo[currentIndex][currentSum + totalSum] != numeric_limits<int>::min()) {
                return memo[currentIndex][currentSum + totalSum];
            }
            int add = memoization(nums, currentIndex + 1, currentSum + nums[currentIndex], target, memo);
            int subtract = memoization(nums, currentIndex + 1, currentSum - nums[currentIndex], target, memo);
            memo[currentIndex][currentSum + totalSum] = add + subtract;
            return memo[currentIndex][currentSum + totalSum];
        }
    }

    int findTargetSumWays(vector<int>& nums, int target) {
        totalSum = accumulate(nums.begin(), nums.end(), 0);
        vector<vector<int>> memo(nums.size(), vector<int>(2 * totalSum + 1, numeric_limits<int>::min()));
        return memoization(nums, 0, 0, target, memo);
    }

public:
    int totalSum;
};
```
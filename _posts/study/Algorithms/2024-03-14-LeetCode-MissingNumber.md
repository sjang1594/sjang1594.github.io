---
title: Missing Number [Easy]
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## LeetCode 268: Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

### Approach
* the fact that we're looking for the sum, we just need to subtract the value in the `nums`, from the summation untill N.

```c++
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int N = nums.size();
        int sum = 0;
        int compareSum = 0;
        for (int i = 0; i < N; i++){
            sum += nums[i];
        }
        
        for (int i = 0; i <= N; i++){
            compareSum += i;
        }

        return compareSum - sum;
    }
};

But this is O(N).
```

### Can we make it better ?

Let's think about this way, we are going to all the power to the sort(), which means the time complexity depends on sort algorithm. Then we can divide three cases: 
1. If the first digit is missing, which is mostly likely 0 if the vector is sorted
2. If the last digit is missing, which is mostly likely the max Value of the vector.
3. If the any middle index are missing, starting from 0 to N-1, find the missing number and return the index.

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        if (nums[0] != 0) return 0; // 0 is missing

        if (nums[n-1] != n) return n; // if the last character is missing

        for(int i = 1; i < nums.size(); i++){
            if (nums[i] != i) {
                return i;
            }
        }
        return 0;
    }
};
```
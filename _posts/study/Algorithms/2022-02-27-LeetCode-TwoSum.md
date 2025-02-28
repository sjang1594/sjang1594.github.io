---
title: Leet Code - Two Sum
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## LeetCode - Two Sum [Easy] - 1

* [LeetCode - Two Sum](https://leetcode.com/problems/two-sum/)

The Brute force way is to traverse array for, i and j. and if `nums[i] + nums[j] == target`, then return the index of two.

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        for(int i = 0; i < n-1; i++){
            for(int j = i+1; j < n; j++){
                if(nums[i] + nums[j] == target){
                    return {i, j};
                }
            }
        }

        return {};
    }
};
```

The time complexity for this case is O(N^2), the space complexity is O(1) is because we're traversing vector twice with the size of N. The vector itself doesn't take any space, so its O(1). Normally, in this case. We can make it by O(n) for time complexity and space complexity is O(n) by using hash map.

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
        int n = nums.size();
        for(int i = 0; i < n; i++){
            int x = target - nums[i];
            if(hash.find(x) != hash.end()){
                return {hash[x], i}; // order doesn't matter
            }
            hash[nums[i]] = i;
        }
        return {};
    }
};
```

if we switch some logic, which is `int x = target - nums[i];` to `int x = nums[i] - target;`, then we can get the index of the two numbers that add up to the target. By using the dictionary, we can get the index of the two numbers that add up to the target. If we find the number, we can return the index of the two numbers. If we don't find the number, we can add the number to the dictionary.

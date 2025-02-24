---
title: Count Duplicates
layout: post
category: study
tags: [c++, algorithm]
published: false
---

### Problem Statement

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

```
Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.
Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

If we sort this, the duplicates must be adjacent each other. The built-in function for `sort()` in c++ is based on `Quick Sort()` the average time complexity is n*log(n). The worst case for quick sort can be n^2 which is the brute force way.

```c++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 1; i < nums.size(); i++){
            if(nums[i] == nums[i - 1])
                return true;
        }

        return false;
    }
};
```

Can we make it better ? We can use HashSet because to insert, and look up takes O(1). The process are following: we push the data to the set. if we have seen the data for incoming element, return true, otherwise keep inserting. Time Complexity in this case would be O(N), space would be O(N) as well, but worst case would be all unique elements

```c++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> set;
        for (int num : nums){
            if(set.count(num) > 0){
                return true;
            }
            set.insert(num);
        }

        return false;
    }
};
```


---
title: Find All Numbers Disappeared in an Array [Easy]
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## LeetCode 448: Find All Numbers Disappeared in an Array
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

## Approach
I thought if you put all the numbers in Set, then it will make my life easier, so I created set, then if loop counter is not in, then append to outputs like below

```cpp
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> output;
        set<int> mySet(nums.begin(), nums.end());
        cout << nums.size() << endl;
        for (int i = 1; i <= nums.size(); i++)
        {
            if (!mySet.contains(i))
                output.push_back(i);
        }
        return output;
    }
};
```

Then I checked, and the time complexity was indeed O(n), but it took about 83 ms, which wasn't what I wanted. One thing I was missing was considering the space complexity by switching to a set. However, as I looked at the hint, I realized that using the index itself was the key to improving performance.

One interesting aspect of the implementation below is that the elements at the corresponding index are marked as -1, indicating that the number exists somewhere, but the indices with positive values are the ones where the numbers do not correspond to their indices.

```cpp
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();
        vector<int> output;
        for(int i = 0; i < n; i++){
            int index = abs(nums[i]) - 1;
            if (nums[index] > 0){
                nums[index] = -nums[index];
            }
        }

        vector<int> result;
        for(int i = 0; i < n; i++) {
            if (nums[i] > 0)
                result.push_back(i + 1);
        }
        return result;
    }
};
```

Of course, unordered_map can be also good and fast, but space complexity can be O(n) in that case.

```cpp
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        unordered_set<int> arr(nums.begin(), nums.end());
        int n = nums.size();
        vector<int> ans;
        for(int i = 1; i <= n; i++) {
            if(arr.find(i) == arr.end()) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};
```

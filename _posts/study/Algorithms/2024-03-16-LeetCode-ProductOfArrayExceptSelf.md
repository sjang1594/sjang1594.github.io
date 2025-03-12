---
title: Product of Array Except Self [Medium]
layout: post
category: study
tags: [C/C++, Algorithm]
published: true
---

## LeetCode 238: Product of Array Except Self [Medium]
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

The major constraint is to calculate the product of array except itself. If you implement in brute force way, you will get O(n^2). However, this is the constraints! 
We need to solve this problem for O(n) time complexity with no extra space complexity.

### Approach

This 2D structure represents the products of all numbers except the one at each index. The second and third lines show how we can calculate the left and right parts separately.
```cpp
24, 2, 3, 4
1, 12, 3, 4
1,  2, 8, 4
1,  2, 3, 6
```

For the input array , the output array represents the prefix products, which are the products of all numbers to the left of each index. This prefix product is calculated by accumulating the numbers to the left at each iteration.

For instance, in the first iteration, there are no numbers to the left, so it's just 1. In the second iteration, you have 1 to the left, so the output is 1 * 1 = 1. In the third iteration, you have 1 and 2 to the left, so the output becomes `1 * 2 = 2``, and so on.

This process continues until you have the prefix products for all indices. After calculating the prefix products, you can calculate the suffix products and multiply them with the prefix products to get the final result.

Then you do the right, which are going to be the product of suffix. You can do the same thing from right to left.


### Implementation
```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();

        std::vector<int> output(n, 1);

        // left
        for(int i = 1; i < n; i++) {
            output[i] = output[i - 1] * nums[i - 1];
        }
        
        // right
        int right = 1;
        for (int i = n - 1; i >= 0; i--){
            output[i] *= right;
            right *= nums[i];
        }
        
        return output;
    }
};
```
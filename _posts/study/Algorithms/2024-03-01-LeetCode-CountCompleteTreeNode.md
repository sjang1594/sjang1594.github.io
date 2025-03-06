---
title: Count Duplicates [Easy]
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## LeetCode 222. Count Complete Tree Nodes [Easy]

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

### You can use the priority queue to solve this problem or use the property of the complete binary tree.

```cpp
class Solution {
public:
    int getHeight(TreeNode* node) {
        int height = 0;
        TreeNode* curr = node;
        while (curr) {
            height++;
            curr = curr->left;
        }
        return height;
    }

    bool exist(TreeNode* root, int index){
        int h = 0;
        for (int i = index; i > 1; i >>= 1)
            h++;
        
        TreeNode* curr = root;
        while(curr) {
            if (h == 0)
                return true;
            if (index & (1 << --h))
                curr = curr->right;
            else 
                curr = curr->left;
        }
        return false;
    }

    int countNodes(TreeNode* root) {
        if (root == nullptr) return 0;

        int h = getHeight(root);
        int lo = 1 << (h - 1); // 8
        int hi = (1 << h) - 1;
        while(lo <= hi){
            int mid = lo + (hi - lo)/2;
            if (!exist(root, mid))
                hi = mid -1;
            else
                lo = mid + 1;
        }
        return hi;
    }
};
```

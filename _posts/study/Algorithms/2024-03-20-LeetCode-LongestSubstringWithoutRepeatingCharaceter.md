---
title: Longest Substring Without Repeating Character [Medium]
layout: post
category: study
tags: [c++, algorithm]
published: false
---

## LeetCode 3: Longest Substring Without Repeaing Character [Medium]
Given a string s, find the length of the longest substring without duplicate characters.

### Implementation
What we want to do is to find the longest substring 

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLength = 0;
        unordered_set<char> charSet;
        int l = 0;
        for (int r = 0; r < s.size(); r++){
            while(charSet.find(s[r]) != charSet.end()) {
                charSet.erase(s[l]);
                l++;
            }
            charSet.insert(s[r]);
            maxLength = max(maxLength, r - l + 1);
        }
        return maxLength;
    }
};
```

### Resource 
[Longest Substring Without Repeating Character](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)
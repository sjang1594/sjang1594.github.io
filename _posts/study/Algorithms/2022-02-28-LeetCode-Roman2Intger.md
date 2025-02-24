---
title: Leet Code - Roman to Integer
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Romans to Integer

Let's look at the problem statement below

```
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
```

Now what we want is basically convert Romans to Integer. How can we solve it. If we have all those unique values stored in some dictionary, then we can check whether we could use those integer and sum it up. The special case would be two letter associated for example IV which is 4. (V - I). With this logic, we can solve it by two approaches.

If we have all those unique values stored in dictionary, then we need to handle the single one, then the two letter one. The time complexity would be the string size (N).
```c++
class Solution {
public:
    int romanToInt(string s) {
        std::map<string, int> roman = {
            {"I", 1}, {"V", 5}, {"X", 10}, {"L", 50}, {"C", 100}, {"D", 500}, {"M", 1000}, 
            {"IV", 4}, {"IX", 9}, {"XL", 40}, {"XC", 90}, {"CD", 400}, {"CM", 900}};
        
        if (s.length() <= 0 && s.length() > 16)
            return 0;
    

        int i = 0;
        int sum = 0;
        while (i < s.length())
        {
            // Two String Handle
            if (i < s.length() - 1){
                string doubleStr = s.substr(i, 2);
                
                if (roman.count(doubleStr)){
                    sum += roman[doubleStr];
                    i+=2;
                    continue;
                }
            }

            // OneString
            string singleStr = s.substr(i, 1);
            sum += roman[singleStr];
            i+=1;
        }

        return sum;
    }
};
```

Okay, let's think further more. For example, if we have `DXCI`, then we can calculate D + (C - X) + I or CMXCIV = (M - c) + (c - x) + (v - i), which is very useful in the logic. Also, let's not use all those special cases which are the two letters combination.

```c++
class Solution {
public:
    int romanToInt(string s) {
        std::map<char, int> roman = {
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
        
        if (s.length() <= 0 && s.length() > 16)
            return 0;

        int sum = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            if(roman[s[i]] < roman[s[i+1]])
                sum -= roman[s[i]];
            else
                sum += roman[s[i]];
        }

        return sum + roman[s[s.length()-1]];
    }
};
```

If we have `MCMXCIV`, when we think about this problem, we can see that M + (M - C) + (C - X) + (V - I). This case, the constraint is if [i+1] > [i], then we subtract [i], else we add. Then, we can simply get the code above.
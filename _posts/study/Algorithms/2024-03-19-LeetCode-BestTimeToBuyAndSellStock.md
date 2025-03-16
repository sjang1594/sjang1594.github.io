---
title: Best Time to Buy and Sell Stock [Easy]
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## LeetCode 121: Best Time to Buy and Sell Stock [Easy]
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.1

### Implementation
* This is typical greey probelm, you select one, and compare it to get the maximum or the best output for goal once. 
This case, you want to maximize the profit, which in this case, you select one prices, and loop through to get the meximum prices.

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int buy = prices[0];
        for (int i = 1; i < prices.size(); i++) {
            int sell = prices[i];
            if (buy < sell) {
                profit = max(profit, sell - buy);
            } else {
                buy = sell;
            }
        }

        return profit;
    }
};
```

### Resource
[Best Time to Sell Stocks](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
---
title: Rod Cutting Problem
layout: post
category: study
tags: [C/C++, Algorithm]
published: true
---

## Rod Cutting Problem
* Reviewing what I studied, how this work will be explained as well. 
---

Rod Cutting Problem is a problem that we have a rod of length `n` and we want to cut the rod into `n` pieces, and we want to maximize the profit.
For example, let's look at the table below. If I have a rod of length 4, then we have 4 ways to cut the rod. Then we calculate the profit for each case

1. Cut the rod into 1, 1, 1, 1     => max profit = 1 + 1 + 1 + 1 = 4
2. Cut the rod into 2, 2           => max profit = 5 + 5 = 10
3. Cut the rod into 3, 1 or 1, 3   => max profit = 8 + 1 = 9
4. Length 4 rod itself             => max profit = 9

the maximum profit we can get is 10.

```
Length:                     0  1  2  3  4   5   6   7   8   9  10
vector<int> price_table = { 0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30 };
```

So, let solve this in naive recursive way

```c++
int RecurCutRod(const vector<int>& prices, int length)
{
	if (length == 0)
		return 0; // return length* prices[0];

	int max_price = numeric_limits<int>::min();
	for (int i = 1; i <= length; i++)
	{
		max_price = std::max(max_price, prices[i] + RecurCutRod(prices, length - i));
	}

	return max_price;
}
```

Then, let's do top-down, top-down basically needs a cache, so that repetitive calculation must be excluded, and used the data retrieved from memo.

```c++
// initialize 
vector<int> memo(length + 1);
memo[0] = 0;

// function
int MemoizedCutRodHelper(const vector<int>& prices, int length, vector<int>& memo)
{
	if (memo[length] >= 0)
		return memo[length];

    int max_prices;
    if (length == 0){
        max_price = 0
    }
    else {
        max_price = std::max(max_price, MemoizedCutRodHelper(prices, length - i, memo))    
    }
	
    for (auto& t : memo) cout << setw(3) << t; cout << endl;
	return memo[length];
}
```

Then, let's do bottom-up, Bottom-up Apprach is called tabulation, so we need kinda like table. I would say bottom up approch can be more familier if you are good at for-loop! (jk)

```c++
int BottomUpCutRod(const vector<int>& prices, int length)
{
	vector<int> table(length + 1, -1); -1로 초기화
	table[0] = 0; // length* prices[0];

	for (int j = 1; j <= length; j++)
	{
		int max_price = numeric_limits<int>::min();
		for (int i = 1; i <= j; i++) {
			max_price = std::max(max_price, prices[i] + table[j - 1]);
		}
		for (auto& t : table) cout << setw(3) << t; cout << endl;
		table[j] = max_price;
	}

	return table[length];
}
```

But when we think about the time complexity. it would be depending on the O (length). Of course, we do have space complexity which is about O(length + 1).
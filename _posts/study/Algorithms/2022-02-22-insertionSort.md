---
title: Insertion Sort
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Insertion Sort

* Reviewing what I studied, how this work will be explained as well. 
---

Given this array / vector that has `{2, 8, 5, 3, 9, 4}`. We want to sort this increasing order.

1. Work left to right
2. Examine each item and compare it to items on its left. 
3. Insert the item in the corect position in the array.

We sure that first element is sorted out, that's why we loop from 1 to vector size. Since we partition the first group (element), then we compare the next value and the far right of the partioned group. (ex: if i index = 2, then j = 2, compare `8` and `5`, `5` is smaller than 8, so we swap them.) Also, another case would be if i index = 3, we compare `8`, and `3`, then swap. Then we compare `3` and `5`, and swap. Basically we're inserting every time if next value and the partioned array's of last index by comparing. Basically, that's what inserting happend!

```c++
#include <iostream>
#include <vector>

void Print(const std::vector<int>& vec)
{
	for (auto& v : vec) {
		std::cout << v << " ";
	}
	std::cout << std::endl;
}

int main()
{
	std::vector<int> vec = { 2, 8, 5, 3, 9, 4 };
	Print(vec);

	// Logic:
	// first element is always sorted.
	for (int i = 1; i < vec.size(); i++)
		for (int j = i; j > 0 && vec[j-1] > vec[j]; j--)
			std::swap(vec[j - 1], vec[j]);
	
	Print(vec);
}
```

But we can also simplify, and a bit optimize version by not using `std::swap`

```c++
for (int i = 1; i < vec.size(); i++)
{
	int key = a[i];
	int j = i;
	for(; j >0 && a[j -1] > key; j--)
		a[j] = a[j-1];
	a[j] = key
}
```

### Time Complexity && Worst Case

We know that two for loop, which means it will compare the new value and the partitioned elements. So, it will be `O(n^2)`. Best Case is `O(n)` when the array is already sorted. But Worst Case is `O(n^2)` when the array is sorted in decreasing order.

## Resource
* [Insertion Sort](https://www.geeksforgeeks.org/selection-sort-algorithm-2/)
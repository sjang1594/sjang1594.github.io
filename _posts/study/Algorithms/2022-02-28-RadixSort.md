---
title: Radix Sort
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Radix Sort
* Reviewing what I studied, how this work will be explained as well. 
---

Radix Sort is similar to Counting Sort, but it handles different types of inputs. Consider the array `vector<int> arr = { 170, 45, 75, 90, 802, 24, 2, 66 };`. If we were to sort this array using comparison-based sorts like Merge Sort or Quick Sort, we would achieve a time complexity of O(N log N). However, as we know from Counting Sort, we can achieve a linear time complexity of O(N) under certain conditions.

### How it works 

Radix Sort leverages a similar approach to achieve efficient sorting. The key idea is to sort numbers digit by digit, starting from the least significant digit (ones place) to the most significant digit. To do this, we need a placeholder for each digit (0 through 9). We iterate through each digit position (ones, tens, hundreds, etc.) and sort the numbers based on that digit.

Let's implement Radix Sort similarly to Counting Sort. The crucial part is indexing each digit. The expression `count[a / exp % 10]` returns the index for each digit. We then increment this count. After counting, we accumulate these counts to determine the positions where each number should be placed, just like in Counting Sort.

Finally, we iterate through the array from right to left (last index to first). For each number, `count[temp[i] / exp % 10] - 1` gives us the index where the number should be assigned in the sorted array. We subtract 1 because array indices start at 0.assigned.

```cpp
void CountingSort(vector<int>& arr, int k, int exp)
{
	vector<int> temp = arr; // copy
	
	vector<int> count(k + 1, 0);
	for (auto a : arr)
		count[a / exp % 10] += 1;

	for (int i = 1; i < count.size(); i++)
		count[i] += count[i - 1];

	Print(count);

	for (int i = arr.size() - 1; i >= 0; i--)
	{
		arr[count[temp[i] / exp % 10] - 1] = temp[i];
		count[temp[i] / exp % 10]--;
	}
}

void RadixSort(vector<int>& arr)
{
	int k = 9; // from 0 to 9
	int m = *max_element(arr.begin(), arr.end());

	for (int exp = 1; m / exp > 0; exp *= 10)
	{
		CountingSort(arr, k, exp);
		Print(arr);
	}
}


vector<int> arr = { 170, 45, 75, 90, 802, 24, 2, 66 };
RadixSort(arr);
```
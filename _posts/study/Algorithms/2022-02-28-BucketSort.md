---
title: Bucket Sort
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Bucket Sort
Bucket Sort is a sorting algorithm that is similar in concept to Radix Sort and Counting Sort, but it is designed to handle floating-point numbers. Like these other algorithms, Bucket Sort uses placeholders to sort elements efficiently. However, unlike Radix Sort, which sorts integers digit by digit, Bucket Sort distributes floating-point numbers into buckets and then sorts each bucket individually.

## Time Complexity
The time complexity of Bucket Sort can vary depending on the distribution of the input data. In the best case, where the numbers are uniformly distributed, the time complexity can be O(N + K), where N is the number of elements and K is the number of buckets. However, if the numbers are not well-distributed and most elements end up in a single bucket, the time complexity can degrade to O(N^2) due to the sorting algorithm used within each bucket.

## Steps to Implement Bucket Sort
1. Divide Data into Buckets: If there are N data points, divide them into K buckets. Ideally, K should be close to N for optimal performance.
2. Distribute Elements into Buckets: Place each element into its corresponding bucket based on its value.
3. Sort Each Bucket: Use a sorting algorithm like Insertion Sort to sort the elements within each bucket.
4. Merge Sorted Buckets: Combine the sorted elements from all buckets to produce the final sorted array.

## Implementation
Here's an example implementation of Bucket Sort for floating-point numbers. We'll consider a simple case with 10 buckets and the input array `{ 0.78f, 0.17f, 0.39f, 0.26f, 0.72f, 0.94f, 0.21f, 0.12f, 0.23f, 0.67f }`.

```cpp
// Insertion Sort
void InsertionSort(vector<float>& bucket)
{
	for (int i = 1; i < bucket.size(); ++i) {
		float key = bucket[i];
		int j = i - 1;
		while (j >= 0 && bucket[j] > key) {
			bucket[j + 1] = bucket[j];
			j--;
		}
		bucket[j + 1] = key;
	}
}

void BucketSort(vector<float>& arr, int num_buckets)
{
	vector<vector<float>> buckets(num_buckets);

	// Put Bucket
	for(auto& a : arr)
	{
		int index = int(a * num_buckets);
		buckets[index].push_back(a);
	}

	for (int i = 0; i < buckets.size(); i++) {
		InsertionSort(buckets[i]);
    }

    // update arr from sorted bucket
	int index = 0;
	for (int i = 0; i < buckets.size(); i++)
	{
		for (int j = 0; j < buckets[i].size(); j++)
		{
			arr[index++] = buckets[i][j];
		}
	}
}
```
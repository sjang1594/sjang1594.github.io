---
title: Counting Sort
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Counting Sort
* Reviewing what I studied, how this work will be explained as well. 
---

Counting Sort is a sorting algorithm that works by counting the number of objects that have each distinct key value, and using arithmetic to determine the positions of each key value in the output sequence. It's like creating a histogram of the data by counting the number of occurences of each key value.

### How it works
1. Create a count array to store the count of each unique number (the size would be the highest integer + 1)
2. Count the occurences of each element in the input array and store it in the count array.
3. Add the previous count to the current count to get the position of the element in the output array.
4. Create the ouptut array to store the sorted elements.
5. In Reverse order of output array, place the input array's element in the `output[count[input[i]] - 1]` index, and update the count of the element in the count array. (which is subtracting 1 from the count)

```c++
void Print(vector<int>& arr)
{
	for (auto a : arr)
		if (a == -1)
			cout << "X ";
		else
			cout << a << " ";
	cout << endl;
}

vector<int> CountingSort(const vector<int>& arr, int k)
{
	vector<int> count(k + 1, 0); 

	for (int i = 0; i < arr.size(); i++) {
		count[arr[i]] += 1;
	}

	// update the count 
	for (int i = 1; i < k + 1; i++) {
		count[i] += count[i - 1];
	}

	cout << "Count: ";
	Print(count);

	vector<int> output(arr.size(), -1);

    // reverse order
	for (int i = output.size() - 1; i >= 0; i--)
	{
	
		output[count[arr[i]] - 1] = arr[i];
		count[arr[i]] --;
		cout << "Count: ";
		Print(count);
	
		cout << "Output: ";
		Print(output);
	}

	return output;
}
```

Input is `{ 2, 5, 3, 0, 2, 3, 0, 3 }` and the output would be `{ 0, 0, 2, 2, 3, 3, 3, 5 }`.

### Time Complexity

The time complexity of Counting Sort is O(n + k) where n is the number of elements in the input array and k is the range of the input.

### Space Complexity

The space complexity of Counting Sort is O(n + k) where n is the number of elements in the input array and k is the range of the input.

### Stability

Counting Sort is a stable sorting algorithm unlike quick sort.

---
title: Merge Sort
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Merge Sort

* Reviewing what I studied, how this work will be explained as well. 
---

This sorting algorithm is based on the `devide and conquer` strategy. The steps in simple array are as follows:

1. Divide the input array into two halves. (Divide)
2. Sort each half. (Conquer)
3. Merge the two halves. (Combine)

Basically, we're breaking the problem of sorting the array into two smaller problems. (sub-problems), then we merge the two halves, which are sorted.

The problem state: Given some array, and sort it in increasing order. There are two solution can exist: bottom up (for loop), and top down (recursive). Let's explore what are the code looks like, and the logic behind.
If the size of the array or the vector is 0 or 1, it is already sorted. The sort doesn't happen when it's divided, it happens when it's combining(merging).

Let's look at the recursive way to solve this first (top-down merge sort)

```c++
void Merge(vector<int>& a, int lo, int mid, int hi)
{
    aux.resize(a.size())
    int i = lo; j = mid + 1;
    for (int k = lo; k <= hi, k++)
    {
        aux[k] = a[k];
    }

    // you can do while in the similar way, which can be way easier than this
    for (int k = lo; k <= hi; k++)
    {
        if (i > mid) a[k] = aux[j++];                // left array is already sorted, now look at right array
        else if (j > hi) a[k] = aux[i++];            // right array is already sorted, now look at left array
        else if (aux[i] < aux[j]) a[k] = aux[i];     // compare the value, get the min value
        else a[k] = aux[i++];                        // just copy the value
    }
}

void SortHelper(vector<int>& a, int lo, int hi)
{
    if(hi <= lo) return;
    int mid = lo + (hi - lo) / 2;
    SortHelper(a, lo, mid);
    SortHelper(a, mid+1, hi);
    Merge(a, lo, mid, hi);
}

int main() 
{
    std::vector<int> vec = {3, 5, 8, 9, 6, 2};
    SortHelper(vec, 0, vec.size() - 1);
}
```

Let's look at the bottom-up approach 

```c++

void Sort(vector<int>& a)
{
	aux.resize(a.size());

	int N = a.size();

	for (int sz = 1; sz < N; sz = sz + sz) {
		for (int lo = 0; lo < N - sz; lo += sz + sz)
			Merge(a, lo, lo + sz - 1, std::min(lo + sz + sz - 1, N - 1));
	}
}

void Merge(vector<int>& a, int lo, int mid, int hi)
{
	int i = lo, j = mid + 1;
	if (a[mid] <= a[j]) return;
	for (int k = lo; k <= hi; k++)
		aux[k] = a[k];
	for (int k = lo; k <= hi; k++)
	{
		if (i > mid) a[k] = aux[j++];
		else if (j > hi) a[k] = aux[i++];
		else if (aux[j] < aux[i]) a[k] = aux[j++];
		else a[k] = aux[i++];
	}
}


int main() 
{
    std::vector<int> vec = {3, 5, 8, 9, 6, 2};
    Sort(vec, 0, vec.size() - 1);
}
```

### Time Complexity & Accuracy
* this is definitive way to sort array or vector. If we have a n problem, we divided into n/2 and so on, then level is created is log(N), so this becomes O(n * log n)
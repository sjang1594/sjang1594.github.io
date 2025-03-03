---
title: Binary Heap
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Binary Heap  
* Reviewing what I studied, how this work will be explained as well. 
---

Binary Heap is a **complete binary tree** that satisfies the heap property. 

### Heap Property
* **Max-Heap** : Parent node is greater than or equal to child node. 
* **Min-Heap** : Parent node is less than or equal to child node.

### Heap Constraints
1. Access the max element instantaneously (that's why the max element in in the root) -> Max Heap | Min Heap
2. which extends to the idea that, the parent node should be bigger than the children node.
3. Swap (If we are to insert the last element into last tree level, then we need to compare the value, and update the tree)

### Heap Operations

* Search (O(N))
* Deletion (Log N)
* Peek (O(1))
* Insertion (Log N) -> Worst Case / But Best Case is O(1)
* Heapify (O(N))

### Heapify
If you take a look at the heapify function, it is a function that takes an array, and makes it a heap. So this approximation can be done as follows.

In the logic, we don't calculate the leaf nodes, we only did siftDown from the first non-leaf node (which is second last node). Maximum number of nodes in each level is `floor(n_total / 2^h+1)`. (h is the height of the tree). Then we can calculate this...  1 * n/4 + 2 * n/8 + 3 * n/16 + ... + h * n/2^(h+1).. then n/4 {1 + 2/4 + 3/8 + 4/16 + ... + h/2^(h-1)}.. then n/4 {1 + 1/2 + 1/4 + 1/8 + ... + 1/2^(h-1)}.. then n/4 {1 / (1 - 1/2)^2} = n. (1/(1-x)^2) = sigma(n *x^(n-1)). This is why it is O(N).

### Heap Implementation

```cpp
struct MaxHeap {
    vector<int> heap;

    MaxHeap() {
        heap.resize(1); // heap 은 무조건 1 부터 시작, 안보이는 0 이 존재
    }

    // ---- priority queue
    void push(int x) {
        int index = int(heap.size());
        heap.push_back(x);
        siftUp(index);
    }

    void siftUp(int index) {
        for (int i = index; i > 1 && heap[i / 2] < heap[i]; i /= 2)  // O(logN)
            swap(heap[i / 2], heap[i]);
    }

    int top() const {
        return heap[1];    
    }

    bool pop() {
        int N = int(heap.size());
        if (N <= 1)
            return false;
        swap(heap[1], heap[N - 1]);
        heap.pop_back();
        siftDown(1);
        return true;
    }

    void siftDown(int index) {
        int N = int(heap.size());
        cout << N << endl;
        for (int i = index, j = index * 2; j < N; i = j, j *= 2) {
            if (j + 1 < N && heap[j] < heap[j + 1])
                j++;
            if (heap[i] >= heap[j])
                break;
            swap(heap[i], heap[j]);
        }
    }

    void heapify(const int arr[], int size) {
        heap.resize(1);
        heap.insert(heap.end(), arr, arr + size);
        
        for (int i = size / 2; i >= 1; i--)
            siftDown(i);
    }
};
```

### The interesting fact about this heap. 

Let's mark that the parent heap is denoted as i, then child on left is i * 2, and right is i * 2 + 1. If you actually draw the tree, parent node is 0001, then left child is 0010, and right child is 0011. then parent node is 0100, left child is 0101, and right child is 0110. then parent node is 0111, left child is 1000, and right child is 1001. then parent node is 1010, left child is 1011, and right child is 1100. 

This is interesting! Why? from the parent node, the resulting of left child is shifting left by 1, and right child is shifting left by 1 and adding 1. Then we can back track how many parent nodes are from the child node. For example, if node 9 is 1001, remove MSB, 001. We can see that 0(left)->0(left)->1(right) in that direction, so we have three parent nodes from child node 9. 

In the next post, I will show you the leet code problem that uses this heap property.

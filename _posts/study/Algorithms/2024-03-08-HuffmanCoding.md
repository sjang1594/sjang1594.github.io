---
title: Huffman Coding
layout: post
category: study
tags: [c++, algorithm]
published: false
---

## Huffman Coding

* Reviewing what I studied, how this work will be explained as well. 
---

Huffman coding is a lossless data compression technique, primarily used for compressing text data. This algorithm generates variable-length prefix codes to compress data. Huffman coding was developed by David A. Huffman and published in 1952.

###  Key Concepts of Huffman Coding
* Variable-Length Code: Huffman coding adjusts the length of codes based on the **frequency of characters**. Frequently occurring characters **are assigned shorter codes**, while less frequent characters receive longer codes.

* **Prefix Property**: Huffman codes are prefix-free codes, meaning no code can be a prefix of another code. This ensures that codes can be uniquely interpreted.

### Prefix Code
* A prefix code is a coding system that satisfies the **prefix property**. This means no code can be a prefix of another code. Prefix code can be variable-length codes, with Huffman coding being a notable example. Prefix codes ensures that dat can be uniquely interpreted and prevent code collisions.

### Example of Prefix Property
Consider the following Huffman codes for character A, B, C, and D:
* A: 0
* B: 10
* C: 110
* D: 111

In this code, no code is a prefix of another: 
* The code for A(0) is not a prefix of any other code
* The code for B(10) is not a prefix of C(110) or D(111) because it does not match the starting bits of those codes.

This property allows for efficient decoding, as each code can be uniquely identified without ambiguity.

### Huffman Tree
A Huffman tree is a binary tree used in Huffman coding. Each node represents a character and its frequency, with leaf nodes representing actual characters. The Huffman tree is constructed through the following process:

1. Initialization: Create leaf nodes for each character and store their frequencies.
2. Tree Construction: Select the two nodes with the smallest frequencies and create a new internal node. The frequency of this node is the sum of its child nodes' frequencies.
3. Iteration: Repeat the process until only one root node remains.

### Implementation
```cpp
struct Node
{
    string data;
    int freq;
    Node* left = nullptr;
    Node* right = nullptr;
};

struct Compare
{
    bool operator()(Node* l, Node* r) { return (l->freq > r->freq); }
}

void HuffmanCoding(vector<char> data, vector<int> freq) {
    priority_queue<Node*, vector<Node*>, Compare> heap;

    for(int i = 0; i < data.size(); i++)
        heap.push(new Node{ string(1, data[i]), freq[i] });

    while (heap.size() != 1) {
        Node* left = heap.top();
        heap.pop();
        Node* right = heap.top();
        heap.pop();

        Node* top = new Node();
        top->data = left->data + right->data;
        top->freq = left->freq + right->freq;
        top->left = left;
        top->right = right;

        heap.push(top);
    }
}
```

### Resource
* [How computers compress text: Huffman Coding and Huffman tree](https://www.youtube.com/watch?v=JsTptu56GM8&ab_channel=TomScott)
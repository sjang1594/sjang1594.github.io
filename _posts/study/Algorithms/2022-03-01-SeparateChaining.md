---
title: Separate Chaining
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Separate Chaining

* Reviewing what I studied, how this work will be explained as well. 
---

### Separate Chaining: A Collision Resolution Technique in Hashing
Separate chaining is indeed one of the most common collision resolution techniques used in hash tables. As a technical engineer who has implemented this in several projects, I can confirm it's both elegant and efficient when properly configured. This algorithm can be seen as an extension of bucket sort.

**Let's break down how it works:**
Hash Function: We use a hash function to determine which slot a key should go into. For example, if we have a value 0.84, we might use a floor operation as our hash function, resulting in slot 8.
Collision Handling: However, hashing can lead to collisions. For instance, values like 0.32, 0.39, and 0.31 would all hash to slot 3 using our floor operation. This is where collision resolution comes in.

### Separate Chaining vs Open Addressing:
In Open Addressing, when a collision occurs, we would need to find open spots for each value, often by probing linearly through the table.
Separate Chaining takes a different approach. Instead of linear probing, it allows multiple keys to be stored in the same slot using a linked list.
This is why it's called "separate chaining" - each slot in the hash table can chain together multiple values in a separate linked list. This approach efficiently handles collisions by allowing multiple elements to exist at the same index of the hash table. There are also different chaining technique like cuckoo hashing (which results O(1) if implemented properly)

The key advantage of separate chaining is that it degrades gracefully under a high load factor and doesn't require the frequent resizing that open addressing might. However, it does require additional memory for the linked list pointers.

### How Separate Chaining Works
In separate chaining, each slot of the hash table points to a linked list that stores all elements hashing to the same location. When a collision occurs (multiple keys map to the same index), we simply add the new element to the linked list at that particular index

### Implementation

```cpp
#include <iostream>
#include <iomanip>
#include <string>

using namespace std;
struct Node
{
    string key;
    int val;
    Node* next;
};

class HashTable 
{
public:
    HashTable(int _size) : size(_size)
    {
        hash_table = new Node * [size];
        for (int i = 0; i < size; i++) {
            hash_table[i] = nullptr;
        }
    }

    ~HashTable() 
    {
        for (int i = 0; i < size; i++)
        {
            Node* p = hash_table[i];
            if (p != nullptr) {
                Node* chain = p->next;
                while (chain != nullptr) {
                    Node* target = chain;
                    chain = chain->next;
                    delete target;
                }

                delete p;
                hash_table[i] = nullptr;
            }
        }

    }

    Node* insert(string key, int val)
    {
        Node* new_node = new Node();
        new_node->key = key;
        new_node->val = val;

        int idx = hash(key, size);
        new_node->next = hash_table[idx];
        hash_table[idx] = new_node;
        return new_node;
    }

    bool remove(string key) 
    {
        int idx = hash(key, size);

        if (hash_table[idx]->key.compare(key) == 0)
        {
            Node* target = hash_table[idx];
            hash_table[idx] = hash_table[idx]->next;
            delete target;
            return true;
        }

        for (Node* p = hash_table[idx]; p->next != nullptr; p = p->next)
        {
            if (p->next->key.compare(key) == 0)
            {
                Node* target = p->next;
                p->next = p->next->next;
                delete target;
                return true;
            }
        }
        return false;
    }

    Node* get(string key) 
    {
        int idx = hash(key, size);
        for (Node* p = hash_table[idx]; p != nullptr; p = p->next) {
            if (p->key.compare(key) == 0)
                return p;
        }
        return nullptr;
    }

    void display(std::string msg)
    {
        cout << msg << endl;

        // Traverse the entire hash table
        for (int i = 0; i < size; ++i) {
            cout << "  +--------+--------+" << endl;
            cout << i << " |";
            Node* p = hash_table[i];
            if (p == NULL) {
                // NULL record, print empty
                cout << " " << setw(6) << "" << " | " << setw(6) << "" << " |";

            }
            else {
                // Print the record from the table
                cout << " " << setw(6) << left << p->key << " | " << setw(6) << right << p->val << " |";

                // Traverse and print the chain
                for (p = p->next; p != NULL; p = p->next) {
                    cout << " --> " << "[ " << p->key << " | " << p->val << " ]";
                }
            }
            cout << endl;
        }
        cout << "  +--------+--------+" << endl << endl;
    }

private:
    int hash(string key, int size)
    {
        int hash = 0;
        for (int i = 0; i < key.size(); i++) {
            hash += key[i];
        }
        return hash % size;
    }

    Node** hash_table;
    int size;
};

int main()
{
    HashTable customers(8);

    // Insert key-value pairs
    customers.insert("Alice", 101);
    customers.insert("Bell", 102);
    customers.insert("Max", 103);
    customers.insert("Evin", 104);
    customers.insert("Ana", 105);
    customers.insert("Dave", 106);
    customers.insert("Leo", 107);
    customers.display("HASH TABLE after insertion of customers 'Alice', 'Bell', 'Max', 'Evin', 'Ana', 'Dave', and 'Leo'.");

    // Delete key-value pairs
    customers.remove("Dave");
    customers.remove("Ana");
    customers.remove("Max");
    customers.display("HASH TABLE after deletion of customers 'Dave', 'Ana', and 'Max'.");
}
```

### Time Complexity
**Average Case**
* Search: O(1 + α) where α is the load factor (number of elements divided by table size)
* Insertion: O(1 + α)
* Deletion: O(1 + α)

For a successful search, approximately 1 + (α/2) links need to be traversed on average.

**Worst Case**
* Search: O(n) when all keys hash to the same bucket
* Insertion: O(n) in the pathological case where all elements end up in one chain
* Deletion: O(n) since deletion requires searching first

### Resource
[Youtube](https://www.youtube.com/watch?v=_xA8UvfOGgU&ab_channel=GeeksforGeeks)
[Youtube](https://www.youtube.com/watch?v=T9gct6Dx-jo&t=368s&ab_channel=WilliamFiset)
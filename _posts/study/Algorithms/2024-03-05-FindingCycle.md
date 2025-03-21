---
title: Finding whether it's cylic graph or acyclic graph.
layout: post
category: study
tags: [c++, algorithm]
published: true
---

### Directed Cycle Detection

Cycle detection in a directed graph is a fundamental problem in graph theory with applications in deadlock detection, dependency resolution, and circuit analysis. The algorithm I've implemented uses a depth-first search (DFS) approach with a recursive traversal strategy to identify cycles in directed graphs.

### Key Concepts
**The algorithm relies on three key data structures:**
1. A visited flag for each vertex to track which vertices have been explored
2. An on_stack array to track vertices currently in the DFS recursion stack
3. An edge_to array to maintain the DFS tree structure for cycle reconstruction

### Implementation
```c++
struct Vertex 
{
    Vertex(int v) { index = v; }

    int index = -1;
    bool visited = false;
    vector<Vertex*> out_neighboors;
}

class Graph
{
public:
    Graph(int num_vertices)
    {
        vertices.resize(num_vertices);
        for (int i = 0; i < num_vertices; i++)
            vertices[i] = new Vertex(i);
    }

    ~Graph() 
    {
        for (auto* v : vertices)
            delete v;
    }

    void addEdge(int v, int w)
    {
        verticies[v]->out_neighboors.push_back(vertices[w]);
    }

    void DetectCycle()
    {
        on_stack.resize(vertices.size(), false);
        cycle.clear();
        edge_to.resize(vertices.size(), nullptr);

        for (auto* v : vertices)
            v->visited = false;

        for (auto* v : vertices)
        {
            DetectCycleRecurr(v)
            if (!cycle.empty()) {
                cout << "cycle Detected" << endl;
            }
        }
    }

    void DetectCycleRecurr(Vertex* v)
    {
        v->visited = true;
        on_stack[v->index] = true;

        for(auto* w : v->out_neighboors)
        {
            if (!cycle.empty())
                return;
            else if (!w->visited) 
            {
                edge_to[w->index] = v;
                DetectCycleRecurr(w);
            }
            else if (on_stack[w->index])
            {
                Vertex* x = v;
                cycle.push_back(x);

                while(x->index != w->index) 
                {
                    cycle.push_back(x);
                    x = edge_to[x->index]
                }

                reverse(cycle.begin(), cycle.end())
                return;
            }
        }
    }

private:
    vector<Vertex*> vertices;
    vector<Vertex*> cycle;
    vector<bool> stack;
    vector<Vertex*> edge_to;
}

int main() 
{
    Graph g(3);
    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
}
```

### Time Complexity
Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges. Each vertex and edge is processed exactly once in the worst case

The cycle reconstruction takes at most O(V) time

### Space Complexity: O(V)
on_stack, edge_to, and recursion stack each require O(V) space. The cycle array stores at most V vertices
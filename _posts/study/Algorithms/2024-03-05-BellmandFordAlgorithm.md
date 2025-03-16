---
title: Bellman Ford Algorithm
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Bellman Ford Algorithm
* Reviewing what I studied, how this work will be explained as well. 
---

The Bellman Ford Algorithm is a graph search algorithm that finds the shortest path from a source vertex to all other vertices in a weighted graph. It is similar to Dijkstra's Algorithm but can handle graphs with negative weight edges. However, it can detect negative cycles, which are cycles whose total weight is negative.

## Key Differences from Dijkstra's Algorithm
1. Negative Weight Edges: Bellman Ford can handle negative weight edges, whereas Dijkstra's Algorithm assumes all edges have non-negative weights.
2. Negative Cycles: Bellman Ford can detect negative cycles, which is not possible with Dijkstra's Algorithm.

## Algorithm Overview
1. Initialization: Initialize the distance to the source vertex as 0 and all other vertices as infinity.
2. Relaxation: Relax the edges repeatedly. For each edge, if the distance to the destination vertex can be reduced by going through the current vertex, update the distance.
3. Negative Cycle Detection: After relaxing all edges V-1 times, check for negative cycles by attempting one more relaxation. If any distance can still be reduced, a negative cycle exists.

## Time Complexity
The time complexity of the Bellman Ford Algorithm is O(V*E), where V is the number of vertices and E is the number of edges. This is because in the worst case, we relax all edges V-1 times.

## Implementation
Here's a corrected and complete implementation of the Bellman Ford Algorithm:

```c++
void Print(vector<double>& dist)
{
	for (int i = 0; i < dist.size(); i++)
		cout << setw(6) << dist[i];
	cout << endl;
}

struct Edge
{
	int v, w;
	double weight;
};

constexpr double kInf = numeric_limits<double>::infinity();
vector<double> dist(V, kInf);
for (int v = 1; v < V; v++)
{
	for (auto e : edges)
	{
		if (dist[e.w] > dist[e.v] + e.weight) {
			dist[e.w] = dist[e.v] + e.weight;
			prev[e.w] = e.v;
		}
	}
	Print(dist);
}
```

Then how do you think about getting the negative edges!? It's basically same logic! if the distance the next edge is greater than the current(whole) distance, then we can conclude that there will be negative edge. Normally, the dist arrays two indices where negative values are very likely that it's negative cycle.
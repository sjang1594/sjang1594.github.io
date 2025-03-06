---
title: Bellman Ford Algorithm
layout: post
category: study
tags: [C/C++, Algorithm]
published: true
---

## Bellman Ford Algorithm

* The main goal is to find the optimal solutions (Finding the shortest path). It's smiliar to Dijkstra Algorithm. But there is difference, which is the edge weight can be negative.

* The funny thing about this algorithm is that it loops through Vertex (V-1) times and E edges. So the maximum iteration time would be O(V-1 * E). But if the order is correct in some sense, it's faster.

### Negative Cycle 

* Since the negative cycles are allowed in this algorithm, it is possible that negative sum (edge.weight + vertex_index) becomes negative. then we should stop the algorithm because the negative weight will make the sum to be more negative.

Let's look at the algorithm!

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
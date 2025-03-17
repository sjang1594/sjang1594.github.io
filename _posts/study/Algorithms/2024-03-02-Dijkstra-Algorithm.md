---
title: Dijkstra Algorithm
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Dijkstra Algorithm
* Reviewing what I studied, how this work will be explained as well. 
---

Dijkstra Algorithm is a shortest path algorithm that finds the shortest path from a starting node to all other nodes in a graph. Instead of using BFS, it uses priority queue to find the shortest path.

Constraints:

* No negative weight edges
* No negative cycles

This is not dependent on the how many nodes we are passing through, but the weight of the edges. (distance in this case.)

Let's see the steps of the algorithm.

1. Initialize the distance of the starting node to 0, and the rest of the nodes to infinity.
2. Push the starting node to the priority queue & Pop the starting node from the priority queue.
3. Update the distance of the adjacent nodes (setting infinity to the edge weight), then push them to the priority queue.
4. Then select the node with the smallest distance from the priority queue and repeat the process.

Code is as follows.
```cpp
#include <iostream>
#include <list>
#include <vector>
#include <limits>
#include <queue>
#include <iomanip>

using namespace std;

// Sedgewick p. 642
class DirectedEdge
{
public:
	int v;         // edge tail
	int w;         // edge head
	double weight; // edge weight

	DirectedEdge(int v, int w, double weight)
	{
		this->v = v;
		this->w = w;
		this->weight = weight;
	}

	double Weight() { return weight; }
	int From() { return v; }
	int To() { return w; }
};

class EdgeWeightedDigraph
{
public:
	int num_vertices;
	int num_edges;
	vector<vector<DirectedEdge>> adj;

	EdgeWeightedDigraph(int num_vertices)
	{
		this->num_vertices = num_vertices;
		this->num_edges = 0;
		adj.resize(this->num_vertices);
	}

	void AddEdge(DirectedEdge e)
	{
		adj[e.From()].push_back(e);
		num_edges += 1;
	}

	vector<DirectedEdge>& Adj(int v) { return adj[v]; }
};

class DijkstraShortestPaths
{
public:
	DijkstraShortestPaths(EdgeWeightedDigraph& g, int s)
		:
		prev(g.num_vertices, -1),
		dist(g.num_vertices, numeric_limits<double>::infinity()),
		visited(g.num_vertices, false)
	{
		dist[s] = 0.0; // distance for self is 0

		pq.push(pair<double, int>{ 0.0, s });

		PrintIndex(dist);
		PrintDist(dist);

		while (!pq.empty())
		{
			int v = pq.top().second;
			pq.pop();

			if (visited[v]) continue;
			visited[v] = true;

			Relax(g, v);
		}

		PrintPaths();
	}

	void Relax(EdgeWeightedDigraph& g, int v)
	{
		// Get the edge of the v
		for (DirectedEdge& e : g.Adj(v)) {
			int w = e.To();
			
			if (visited[w]) continue;

			// update
			double new_dist = dist[v] + e.Weight();
			if (dist[w] > new_dist) {
				dist[w] = new_dist;

				prev[w] = e.From();
				pq.push({ dist[w], w});
			}
		}
		PrintDist(dist);
	}

	void PrintIndex(vector<double>& dist)
	{
		cout << "Vertex: ";
		for (int i = 0; i < dist.size(); i++)
			cout << setw(6) << i;
		cout << endl;
	}

	void PrintDist(vector<double>& dist)
	{
		cout << "Dist  : ";
		for (int i = 0; i < dist.size(); i++)
			cout << setw(6) << dist[i];
		cout << endl;
	}

	void PrintPaths()
	{
		for (int i = 0; i < prev.size(); i++) {
			deque<int> path;
			path.push_front(i);
			int v = prev[i];
			while (v != -1) {
				path.push_front(v);
				v = prev[v];
			}

			for (auto v : path) {
				cout << v;
				if (v != path.back())
					cout << "->";
			}
			cout << endl;
		}
	}

private:
	vector<int> prev;     
	vector<double> dist;
	vector<bool> visited;

	priority_queue<pair<double, int>, vector<pair<double, int>>, greater<pair<double, int>>> pq;
};
```

The update function is shown below, as new_distance is smaller than the current distance, we update the distance and push the node to the priority queue.

```cpp
double new_dist = dist[v] + e.Weight();
	if (dist[w] > new_dist) {
		dist[w] = new_dist;

		prev[w] = e.From();
		pq.push({ dist[w], w});
}
```

### Time Complexity
* If we use just a simple array, you can get O(V^2), but if you use priority queue, you can get (V+E) * LogV because priority queue insertion / deletion (Log V), then this happens for each Vertex => V * Log V. Edge Iteration => O(E) Then for relaxation, we update the distance to add that edge would be E * LogV. So we can conclude that it is (V+E) LogV in average. So, sum all it up (O(ELogV + E + VLogV)) => O(V+E logV).
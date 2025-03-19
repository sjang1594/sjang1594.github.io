---
title: Kruskal MST
layout: post
category: study
tags: [c++, algorithm]
published: true
---

### Kruskal Minimum Spanning Tree

* Reviewing what I studied, how this work will be explained as well. 
---

자, Kruskal Algorithm 은 [Union-Find](https://sjang1594.github.io/study/UnionFind.html) 을 사용해서, 알고르즘을 Process 하며, 결국에는 어떻게 최소의 weight 으로 모든 Vertex 를 연결 할지를 찾기 때문에, greedy choice 를 가져간다. Prim's 와는 다르게, 전역 Edge 에 대해서 weight 별로 정렬을 한다. 그리고 `Union(a, b)` or `Union(b,a)` 를 진행하면서 disjoint-set 들을 만들어간다. 즉 Prim's 와는 다르게 어떠한 Random 한곳에서 시작하는곳이 아니라 Weight 이 제일 작은 것부터 시작해서, 모든 Edge 별로 disjoint-set 을 만들어가며, Minimum spanning Tree 를 만든다.

생각보다 Union Code 를 활용해서, Path Compression 및 Union-by Rank 를 사용하면, 코드는 간단해진다. 물론 코드가 간단해지지만 Union-Find 가 있다라는 가정하에 이 모든 알고리즘이 쉬워진다고 볼수 있다.

```c++
int main()
{
	vector<Edge> edges =
	{
		{ 0, 1, 4.0 },
		{ 0, 7, 9.0 },
		{ 1, 2, 8.0 },
		{ 1, 7, 11.0 },
		{ 2, 3, 7.0 },
		{ 2, 5, 4.0 },
		{ 2, 8, 2.0 },
		{ 3, 4, 9.0 },
		{ 3, 5, 14.0 },
		{ 4, 5, 10.0 },
		{ 5, 6, 2.0 },
		{ 6, 7, 1.0 },
		{ 6, 8, 6.0 },
		{ 7, 8, 7.0 },
	};

	std::sort(edges.begin(), edges.end());
    double mst_wt = 0.0;

    UnionFind uf(9);

    for (auto& e : edges)
    {
	
	    if (uf.Find(e.u) != uf.Find(e.v)) {
		    uf.Union(e.u, e.v);
		    mst_wt += e.weight;
	    }
	    cout << e.u << " - " << e.v << " : " << e.weight << endl;
    }

    cout << mst_wt << endl;
}
```


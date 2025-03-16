---
title: Kruskal MST
layout: post
category: study
tags: [c++, algorithm]
published: false
---

### Kruskal Minimum Spanning Tree

* Reviewing what I studied, how this work will be explained as well. 
---

자, Kruskal Algorithm 은 [Union-Find](https://sjang1594.github.io/study/UnionFind.html) 을 사용해서, 알고르즘을 Process 하며, 결국에는 어떻게 최소의 weight 으로 모든 Vertex 를 연결 할지를 찾기 때문에, greedy choice 를 가져간다. Prim's 와는 다르게, 전역 Edge 에 대해서 weight 별로 정렬을 한다. 그리고 `Union(a, b)` or `Union(b,a)` 를 진행한다. 
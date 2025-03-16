---
title: Course Schedule [Medium]
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## LeetCode 207: Course Schedule [Medium]

### Description
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

### Implementation
1. This problem resembles a typical graph problem, where detecting cycles is crucial. While DFS can be used with states like visited, not visited, and visiting, we'll employ topological sorting via Khan's algorithm instead. This choice is suitable for our needs because it efficiently orders nodes in a directed acyclic graph (DAG), which is relevant if we assume the graph doesn't contain cycles.

2. Topological sorting relies on the indegree of nodes. Nodes with an indegree of 0, meaning they have no incoming edges, are always placed at the front of the queue. This is because they have no dependencies and can be processed immediately.

3. edges are pointed to 0 -> 1 (in order to take 0, we need to take 1)

what we need to prepare is the result vector, and the inDegree vector adjacent link list (link list can be just vector).

```cpp
vector<int> result;
vector<int> inDegree(numCourses, 0);
vector <int> adj[numCourses];
```

Then, we would have to everything we need. From prerequsites vector, we would need to push the course we need to take, then directed to prerequsite node(class). Then we increment inDegree vector. why are we increasing the inDegree vector, because we need to tell that there is edge points to 1 (in above example)
```cpp
for (auto x : prerequisites) {
    adj[x[0]].push_back(x[1]);
    inDegree[x[1]]++;
}
```

Then, we need to prepare for the queue, and check if the indegree is 0, which means it's gonna be first to check. Then, we're gonna check the outgoing edge from each node, and we are going to get rid of that edge (-=). Then, there is no incoming edge, then we push to the queue. Then we just have to check whether the size is equal or not to number of courses.
```cpp
queue<int> q;
for(int i = 0; i < numCourse; i++) {
    if (inDegree[i] == 0) q.push(i)
} 

while(!q.empty()) {
    int val = q.front();
    q.pop();
    result.push_back(val);

    for(auto edge : adj[val]) {
        inDegree[edge] -= 1;
        if (inDegree[edge] == 0) q.push(edge);
    }
}

return result.size() == numCourse;
```

### Resource 
[Course Schedule](https://leetcode.com/problems/course-schedule/)
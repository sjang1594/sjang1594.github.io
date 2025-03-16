---
title: Course Schedule 2 [Medium]
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## LeetCode 207: Course Schedule 2 [Medium]
```c++
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        int n = prerequisites.size(); // same as numCourses
        vector<int> inDegree(numCourses, 0);
        vector<int> result;

        unordered_map<int, vector<int>> adj;
        for (int i = 0; i < n; i++) {
            adj[prerequisites[i][0]].push_back(prerequisites[i][1]);
        }

        // fill inDegree
        for (auto it : adj) {
            for (int node : adj[it.first])
                inDegree[node]++;
        }

        queue<int> q;
        for (int i = 0; i < numCourses; i++){
            if (inDegree[i] == 0)
                q.push(i);
        }


        while(!q.empty()) {
            int node = q.front();
            q.pop();

            result.push_back(node);
            for (int e : adj[node]) {
                inDegree[e]--;
                if (inDegree[e] == 0)
                    q.push(e);
            }
        }

        reverse(result.begin(), result.end());
        if (result.size() == numCourses){
            return result;
        }
        return {};
    }
};
```
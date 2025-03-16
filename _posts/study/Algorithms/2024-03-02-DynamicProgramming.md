---
title: Dynamic Programming
layout: post
category: study
tags: [c++, algorithm]
published: true
---

## Dynamic Programming
* Reviewing what I studied, how this work will be explained as well. 
---

Dynamic Programming is a method for solving a complex problem by breaking it down into simpler sub-problems. It's one of a method for solving optimization problems. There are two components of Dynamic Programming:

1. Optimal Substructure
2. Overlapping Subproblems

### Optimal Substructure

Optimal Substructure means that the optimal solution to a problem can be constructed from optimal solutions to its sub-problems. Basically, if you break it down to smaller array from big array, and you have an optimal solution to smaller array, you can use it to solve the big array. But when you think about this Optimal Substructure, it's similar to Divide and Conquer. However there are differences. For example, in Divide and Conquer, we divide the big array into smaller array (divide), calculate, combine, and merge. But we try to find the set of sub-problems that have optimal solutions, and use it to solve the big problem. Also, we can compared this with Greedy Algorithm. Within all the solution that we get from optimal substructure (which is the set of sub-problems), we choose the best solution is the greedy algorithm.

This is normally done by using recursion.

### Overlapping Subproblems

When we solve the problem using recursion, we solve the same sub-problem multiple times. This is called Overlapping Subproblems. For example, in the Fibonacci sequence, we can conclude in the following way:

```
             [ 1 ] n = 1
fib =        [ 1 ] n = 2 
             [ fib(n-1) + fib(n-1) ], n = 3, 4, 5, ...
```

Then, we can simply draw the tree of the sub-problems (draw yourself!). Then we can see that, fib(4) = fib(3) + fib(2) is calculated twice. This is called Overlapping Subproblems. Then, we can use the same sub-problem as cache to solve the problem.

### Two types of Dynamic Programming

* Top-Down (Memoization)
* Bottom-Up (Tabulation)

### Top-Down (Memoization)

* Solve the sub-problem using recursing
* Memoize the overlapping sub-problems
* Reuse the memoized sub-problems to solve the big problem

### Bottom-Up (Tabulation)

* Solve the sub-problem using iteration
* Using the tabulation, we can store the result of the sub-problem in a table

### When to use Dynamic Programming?

* State Transition
* Simple Condition -> Fibonacci, Tiling, Digit DP(if digit condition is met, count the number of cases)
* Array -> Kadane's algorithm (sub-array sum), Kapsack Problem, Matrix(DAG, #of Path, Path Cost),  String(LIS, LCS, Edit Distance), Max Profit (Buy and Sell Stock), Rod Cutting, Matrix Chain Multiplication
* Tree -> DAG, DAG Shortest Path, DAG Longest Path, DAG Topological Sort, # of BST.
* Optimization Problem -> Convex Hull, Matrix Multiplication Order
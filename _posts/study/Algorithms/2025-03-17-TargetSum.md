---
title: Programmers - Target Number
layout: post
category: study
tags: [c++, algorithm]
published: false
---

## Programmers: Target sum

### Description
Given an array of non-negative integers numbers, and a target number target, write a function solution that returns the number of ways to add or subtract these numbers without changing their order to reach the target number.

For example, using the numbers ``, you can make the target number 3 in the following five ways:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

### Thinking Process

Intially, when I try to solve this problem, I was thinking that this is typcial dp problem in such that if you select one number in the array, then you can choose either - number or positive number. Then, I was thinking you don't really have to approach this problem with dp, just simple bfs or dfs can be possible


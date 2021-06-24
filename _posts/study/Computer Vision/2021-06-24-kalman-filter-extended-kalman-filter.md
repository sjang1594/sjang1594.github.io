---
title: Kalman Filter / Extended Kalman Filter
layout: post
bigtitle: Kalman Filter / Extennded Kalman Filter
date: '2021-6-24 4:00:00 +0900'
categories:
- Study
- Computer Vision
tags:
- SLAM
comments: true
published: true
---

## Kalman Filter / Extended Kalman Filter

> I studied little bit while I was pursuing to get the certification from Udacity. 

---

### **What is Kalman Filter and Extended Kalman Filter?**
Tracking is important in self-driving cars, this technique is crucial for estimating the state of a system. This is very similar to the probabilistic localization method(Monte Carlo localization). However, the difference in Kalman Filter estimates a continuous states whereas in Monte Carlo localization, it is forced to chop the world in the discrete places. As a result, the Kalman Filter happens to give us a uni-model distribution, whereas the Monte Carlo was fine with multi-model distributions. Both of these techniques are applicable to robot localization and tracking other vehicles. 

### Definition of Kalman Filter
A Kalman filter gives us a mathematical way to infer velocity from only a set of measured locations.

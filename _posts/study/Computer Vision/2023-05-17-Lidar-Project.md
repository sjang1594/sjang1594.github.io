---
title: Lidar Preprocessing Technique
layout: post
category: study
tags: [computer vision]
---

* this unordered seed list will be replaced by the toc
{:toc}

## Lidar Preprocessing Technique

1. DownSampling / Outlier Removal / Noise Filtering 
    - Find the data that are close to the ground level. To accomplish this, you would be ablel to find which lidar beam index points to the ground level
    - Remove the intensity value depending on the problems (mean filter / adaptive threshold)
     - 


## Segment the Point Cloud Data
1. Use a clustring algorithm such as DBSCAN (Density Based Spatial Clustering of Application with )

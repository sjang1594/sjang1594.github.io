---
title: Camera Intrinsic & Extrinsic
layout: post
category: study
tags: [computer vision]
---

## Camera Extrinsic

This represents starting with "Where is my Camera".

xyz - camera location
alpha, beta, gamma - where camera looking to

6 degree of freedom

## Camera Intrinsic

This sits inside of camera, describe how 3D world point on to the 2D image assuming that camera is sitting in 0 and zero orientation.

principal point / analog camera (sheer)

Direct Linear Transform (DLT)
- 11 degree of freedom (extrinsic + intrinsic)


6 control points allow us to estimate the intrinsics & extrinsics.

Additional parameters for lens distortions. (non-linear parameters)

x = PX

x 2d pixel coordinates
p matrix (intrisics / extrinsics)
X 3D world points

Estimate intrincs by using calibration
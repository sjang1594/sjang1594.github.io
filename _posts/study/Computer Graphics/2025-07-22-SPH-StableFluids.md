---
title: Smooth Particle Hydrodynamics(SPH) and Stable Fluids
layout: post
category: study
tags: [directx, computer graphics, hlsl]
published: false
---

## Particle Based Simulation


## Smooth Particle Hydrodynamics (SPH)

## Grid Based(Structure Grid) or Mesh Based Simulation

In particle-based simulations, a significant challenge arises from the need to locate all neighboring particles for each computation, since their positions are randomly distributed. This irregular spacing makes it hard to directly apply classic derivative formulas—as in grid-based approaches—and instead requires taking weighted averages over unevenly spaced neighbors. Consequently, not only does this complicate the mathematical approximation of derivatives, but it also substantially increases computational demands, since neighbor searching and kernel weight calculations must be adapted to the random geometry of the system. This is basic example (or equation) that this can be difficult to takes the gradient on random distributed particles is following:

$$
\nabla f_i \approx \sum_{j \in \mathcal{N}(i)} (f_j - f_i) \cdot w_{ij}
$$

* $fi$: Value of the field at particle i.
* ${N}(i)$ : Neighboring particles of i.
* ${W}{ij}$: Weight function dependent on the distance between particles i and j (calculated via a kernel). 

To make things easier is to put the particle into grid system. 

## Stable Fluids

Major Concepts in Stable Fluids are **Incompressibility** & **Viscosity**

## Resource
**Smooth Particle Hydrodynamics**
* [Paper](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://cg.informatik.uni-freiburg.de/publications/2014_EG_SPH_STAR.pdf)
* [The million dollor equation](https://www.youtube.com/watch?v=Ra7aQlenTb8&ab_channel=vcubingx)


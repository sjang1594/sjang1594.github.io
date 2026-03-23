---
title: Ray Marching
layout: post
category: study
tags: [computer graphics, deep learning]
published: true
---

### Ray Marching
Ray Marching is one of those techniques that seems simple on the surface - march along a ray, sample something, stop when you hit it. - but hides a surprising amount of depth in the detail. Afterr writing fragment shaders on Shadertoy, integrating SDFs(Signed Distance Fields) into deferred pipelines, and later reading NeRF source code, it became clear that ray marching is the conceptual backbone connecting classical real-time rendering to modern neural rendering.

This post covers two distinct favors of ray marching that a graphics engineer encounters:
1. **Sphere Tracing**: ray marching through a signed distance field (SDF) for implicit surface rendering. This is the classic "ray marching" technique popularized by Inigo Quilez and others, where the SDF provides a guaranteed lower bound on distance to the nearest surface, allowing for efficient traversal.
2. **Volumetric Ray Marching**: marching through a participating medium (fog, smoke, fire) wit htransmittance accumulation. This is the core of volumetric rendering and neural radiance fields (NeRF), where we integrate color and density along the ray to produce a final pixel color.


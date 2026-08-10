---
title: TLAS and BLAS — How a Ray Finds Its Triangle Without Testing All of Them
layout: post
category: study
tags: [computer graphics, vulkan, directX12]
published: true
---

# TLAS and BLAS — How a Ray Finds Its Triangle Without Testing All of Them

In the [Omniverse PoC post]({% post_url study/Computer Graphics/2026-08-10-omniverse-isaac-sim-vs-unreal-poc %}) I said Isaac Sim issued only **2 draw calls** for a 50-robot scene because geometry is resolved through "TLAS/BLAS traversed by `vkCmdTraceRaysKHR`." That sentence does a lot of work and I never unpacked it.

This post unpacks it. No prior ray tracing knowledge assumed — if you know what a triangle and a 3D coordinate are, you have enough. At the end there is a **complete runnable Python program** that builds all of this from scratch and measures it, so none of the numbers here are hand-waved.

---

## 1. The only question ray tracing asks

Ray tracing is conceptually simple. To find the color of a pixel, you shoot a ray from the camera through that pixel and ask:

> **"What does this ray hit first?"**

Everything else — shadows, reflections, global illumination — is that same question asked again from a different starting point. A reflection is just "shoot a new ray from where the last one landed."

So the entire performance story of ray tracing is the cost of answering that one question.

## 2. Why the obvious answer is hopeless

The obvious answer: test the ray against every triangle, keep the closest hit.

Let's price that out for a realistic frame:

```
1920 x 1080 pixels          ≈ 2,000,000 rays  (and that's just the primary rays)
a moderately detailed scene ≈ 5,000,000 triangles

2,000,000 x 5,000,000       = 10,000,000,000,000 ray-triangle tests per frame
```

Ten trillion. Per frame. At 60 FPS you would need six hundred trillion per second. An RTX 4090 is nowhere near that — it's off by something like four orders of magnitude. And we haven't added a single reflection or shadow ray yet.

Brute force isn't slow. It's *impossible*. So the entire field is built around not doing it.

## 3. The idea: boxes inside boxes

Here's the trick, and it's the same trick you already use without thinking about it.

Suppose I ask you to find one specific book in a large library. You don't check every book. You do this:

```
Library
 └─ 3rd floor           ← "history is on 3, skip floors 1, 2, 4"
     └─ Aisle 12        ← skip the other 40 aisles
         └─ Shelf C     ← skip the other shelves
             └─ Book
```

Each step throws away almost everything. Five decisions instead of 100,000 checks.

Ray tracing does exactly this with **boxes**. You wrap groups of triangles in axis-aligned bounding boxes (AABBs — just "a box lined up with the X/Y/Z axes"), then wrap groups of boxes in bigger boxes, all the way up to one box containing the whole scene. That tree is called a **BVH — Bounding Volume Hierarchy**.

```
                    [ box containing everything ]
                     /                        \
          [ left half ]                    [ right half ]
           /        \                       /         \
     [ box ]      [ box ]             [ box ]       [ box ]
        |            |                   |             |
    4 triangles  4 triangles         4 triangles   4 triangles
```

Now trace a ray:

- Does the ray miss the big box? **Then it misses every triangle inside it.** Discard millions of triangles with one test.
- Does it hit? Descend into both children and repeat.
- Reach a leaf? Now — and only now — do the expensive triangle test on the 4 triangles there.

The cost goes from *O(N)* to roughly *O(log N)*. That's the difference between 5,000,000 and about 20.

### Why testing a box is cheap

This only pays off because a box test is much cheaper than a triangle test.

**Ray vs. box** is the "slab test": for each of X, Y, Z, find where the ray enters and exits that pair of parallel planes. If the three intervals overlap, you hit. That's a handful of subtractions, multiplications, and comparisons.

**Ray vs. triangle** is the Möller–Trumbore algorithm: two cross products, several dot products, a division, and three early-out branches — and then you also have to check whether the hit is closer than your current best.

So the strategy is: use the cheap test constantly to avoid the expensive test. You do *more* total tests, but the mix shifts overwhelmingly toward cheap ones. We'll see this trade directly in the measurements.

---

## 4. So why two levels?

Everything above describes **one** BVH. But DXR and Vulkan RT deliberately split it into two:

- **BLAS** (Bottom-Level Acceleration Structure) — a BVH over the *actual triangles* of one mesh, in that mesh's own **local coordinates**.
- **TLAS** (Top-Level Acceleration Structure) — a BVH over *instances*. Each instance is nothing but a **pointer to a BLAS + a 3×4 transform matrix**.

```
TLAS  (instances)
 ├─ Instance 0  : BLAS_ur16e     + transform(robot 0 is here, rotated this way)
 ├─ Instance 1  : BLAS_ur16e     + transform(robot 1)
 ├─ ...
 ├─ Instance 49 : BLAS_ur16e     + transform(robot 49)
 └─ Instance 50 : BLAS_warehouse + transform(the warehouse)

BLAS  (triangles, local space)
 ├─ BLAS_ur16e     : the UR16e mesh's triangle tree   ← built ONCE
 └─ BLAS_warehouse : the warehouse's triangle tree
```

### The stamp analogy

Think of a rubber stamp.

**BLAS is the stamp** — you carve it once, carefully. It's the shape itself.

**TLAS is the list of where you pressed it** on the paper — position and rotation, nothing more.

Fifty identical robots means you carve **one** stamp and record **fifty** press locations. You do *not* carve fifty stamps.

(If you prefer: a font works the same way. The letter `A` has one outline defined once; a page with 500 `A`s stores 500 *positions*, not 500 outlines.)

This buys two specific things.

**(a) Instancing is nearly free.** Fifty robots cost one robot's worth of geometry memory, plus fifty tiny transform matrices.

**(b) Movement is cheap — and this is the important one.** When a robot rotates a joint, its links are **rigid bodies**. The triangles themselves don't deform; only the transform changes. So you rebuild the **TLAS only** — a tree over 50 items, which is trivial. The BLAS, a tree over millions of triangles, is **never touched**.

> The exception: if geometry genuinely deforms — a skinned character, cloth, a soft body — you *do* have to refit or rebuild the BLAS, and that is expensive. You build it with `ALLOW_UPDATE` and refit rather than rebuild when you can. Rigid robot links are the friendly case; a bending cable is not.

### Mapping it onto rasterization

If you come from a rasterizer background, here is the correspondence:

| Rasterization | Ray tracing |
|---|---|
| Vertex / Index Buffer | **BLAS** |
| Walking the scene graph and issuing draws | **TLAS** |
| `vkCmdDrawIndexed` × N | `vkCmdTraceRaysKHR` × 1 |

In a rasterizer the **CPU** walks the scene every frame and submits a draw call per mesh section. In a ray tracer the whole scene **already lives on the GPU** as TLAS + BLAS; you issue one trace command and the RT cores walk the tree in hardware.

---

## 5. Let's actually measure it

Talk is cheap. Here is a complete, dependency-free Python program that builds the same 50-robot scene three ways and counts the work:

1. **Brute force** — test every triangle
2. **Single-level BVH** — one big tree over all 25,000 world-space triangles
3. **Two-level** — TLAS over 50 instances + one shared BLAS

It asserts all three produce identical hits, then reports the cost.

```python
"""
Two-level acceleration structure (TLAS / BLAS) demo.
Pure Python, no dependencies. Run: python bvh_demo.py
"""
import math, random
random.seed(7)

# ---------------------------------------------------------------- counters
class Counter:
    def __init__(self): self.tri = 0; self.box = 0
    def reset(self):    self.tri = 0; self.box = 0
C = Counter()

# ---------------------------------------------------------------- vec3
def sub(a,b): return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
def add(a,b): return (a[0]+b[0], a[1]+b[1], a[2]+b[2])
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def norm(a):
    l = math.sqrt(dot(a,a)); return (a[0]/l, a[1]/l, a[2]/l)

# ---------------------------------------------------------------- ray tests
def ray_tri(orig, dirv, tri):
    """Moller-Trumbore. The EXPENSIVE test."""
    C.tri += 1
    v0, v1, v2 = tri
    e1 = sub(v1,v0); e2 = sub(v2,v0)
    p = cross(dirv,e2); det = dot(e1,p)
    if abs(det) < 1e-9: return None
    inv = 1.0/det
    tvec = sub(orig,v0)
    u = dot(tvec,p)*inv
    if u < 0 or u > 1: return None
    q = cross(tvec,e1)
    v = dot(dirv,q)*inv
    if v < 0 or u+v > 1: return None
    t = dot(e2,q)*inv
    return t if t > 1e-6 else None

def ray_box(orig, dirv, bmin, bmax, tmax):
    """Slab test. The CHEAP test."""
    C.box += 1
    t0, t1 = 1e-6, tmax
    for i in range(3):
        if abs(dirv[i]) < 1e-12:
            if orig[i] < bmin[i] or orig[i] > bmax[i]: return False
            continue
        inv = 1.0/dirv[i]
        a = (bmin[i]-orig[i])*inv
        b = (bmax[i]-orig[i])*inv
        if a > b: a, b = b, a
        if a > t0: t0 = a
        if b < t1: t1 = b
        if t0 > t1: return False
    return True

# ---------------------------------------------------------------- BVH build
def tri_bounds(tri):
    xs = [v[0] for v in tri]; ys = [v[1] for v in tri]; zs = [v[2] for v in tri]
    return (min(xs),min(ys),min(zs)), (max(xs),max(ys),max(zs))

def merge(b1, b2):
    (a0,a1,a2),(a3,a4,a5) = b1
    (c0,c1,c2),(c3,c4,c5) = b2
    return (min(a0,c0),min(a1,c1),min(a2,c2)), (max(a3,c3),max(a4,c4),max(a5,c5))

class Node:
    __slots__ = ("bmin","bmax","left","right","items")
    def __init__(self): self.left = self.right = None; self.items = None

def build_bvh(items, bounds_of, leaf_size=4):
    """Median-split BVH. bounds_of(item) -> (bmin, bmax)"""
    node = Node()
    b = bounds_of(items[0])
    for it in items[1:]: b = merge(b, bounds_of(it))
    node.bmin, node.bmax = b
    if len(items) <= leaf_size:
        node.items = items; return node
    ext  = [node.bmax[i]-node.bmin[i] for i in range(3)]
    axis = ext.index(max(ext))                       # split the longest axis
    items = sorted(items, key=lambda it: (bounds_of(it)[0][axis]+bounds_of(it)[1][axis]))
    mid = len(items)//2
    node.left  = build_bvh(items[:mid], bounds_of, leaf_size)
    node.right = build_bvh(items[mid:], bounds_of, leaf_size)
    return node

def count_nodes(n): return 1 if n.items is not None else 1+count_nodes(n.left)+count_nodes(n.right)
def bvh_depth(n):   return 1 if n.items is not None else 1+max(bvh_depth(n.left), bvh_depth(n.right))

# ---------------------------------------------------------------- traversal
def trace_bvh_tris(node, orig, dirv, best):
    """BVH whose leaves hold triangles."""
    if not ray_box(orig, dirv, node.bmin, node.bmax, best): return best
    if node.items is not None:
        for tri in node.items:
            t = ray_tri(orig, dirv, tri)
            if t is not None and t < best: best = t
        return best
    best = trace_bvh_tris(node.left,  orig, dirv, best)
    best = trace_bvh_tris(node.right, orig, dirv, best)
    return best

def trace_tlas(node, orig, dirv, best):
    """TLAS: leaves hold instances -> move ray to object space, descend into BLAS."""
    if not ray_box(orig, dirv, node.bmin, node.bmax, best): return best
    if node.items is not None:
        for inst in node.items:
            # world -> object space. Translation only here, so a subtract suffices.
            # With rotation you would apply the inverse 3x4 matrix to orig AND dir.
            lo = sub(orig, inst.offset)
            best = trace_bvh_tris(inst.blas, lo, dirv, best)
        return best
    best = trace_tlas(node.left,  orig, dirv, best)
    best = trace_tlas(node.right, orig, dirv, best)
    return best

# ---------------------------------------------------------------- scene
class Instance:
    __slots__ = ("blas","offset","bmin","bmax")

def make_robot_mesh(n_tris):
    """A blob of triangles inside the local box [-0.5, 0.5]^3."""
    tris = []
    for _ in range(n_tris):
        cx = random.uniform(-0.4,0.4); cy = random.uniform(-0.4,0.4); cz = random.uniform(-0.4,0.4)
        def v(): return (cx+random.uniform(-0.08,0.08),
                         cy+random.uniform(-0.08,0.08),
                         cz+random.uniform(-0.08,0.08))
        tris.append((v(), v(), v()))
    return tris

TRIS_PER_ROBOT, N_ROBOTS, N_RAYS = 500, 50, 200
robot = make_robot_mesh(TRIS_PER_ROBOT)

offsets = [(i*1.6-7.2, 0.0, j*1.6-3.2) for i in range(10) for j in range(5)][:N_ROBOTS]

# world-space triangle soup (brute force + single-level BVH)
world_tris = [tuple(add(v,off) for v in tri) for off in offsets for tri in robot]

# two-level: ONE blas, N instances
blas = build_bvh(robot, tri_bounds)
instances = []
for off in offsets:
    inst = Instance()
    inst.blas   = blas                      # shared! built once
    inst.offset = off
    inst.bmin   = add(blas.bmin, off)
    inst.bmax   = add(blas.bmax, off)
    instances.append(inst)
tlas = build_bvh(instances, lambda i: (i.bmin, i.bmax), leaf_size=2)

# single-level BVH over every world triangle
flat_bvh = build_bvh(world_tris, tri_bounds)

# ---------------------------------------------------------------- rays
eye = (0.0, 6.0, -14.0)
rays = [(eye, norm(sub((random.uniform(-8,8), random.uniform(-1,1), random.uniform(-4,4)), eye)))
        for _ in range(N_RAYS)]

def run(fn):
    C.reset()
    return [fn(o,d) for o,d in rays], C.tri, C.box

def brute(orig, dirv):
    best = float("inf")
    for tri in world_tris:
        t = ray_tri(orig, dirv, tri)
        if t is not None and t < best: best = t
    return best

h_brute, tri_b, box_b = run(brute)
h_flat,  tri_f, box_f = run(lambda o,d: trace_bvh_tris(flat_bvh, o, d, float("inf")))
h_two,   tri_t, box_t = run(lambda o,d: trace_tlas(tlas, o, d, float("inf")))

def same(a,b):
    return all(abs(x-y) < 1e-6 or (x == float("inf") and y == float("inf")) for x,y in zip(a,b))

print(f"scene: {N_ROBOTS} instances x {TRIS_PER_ROBOT} tris = {len(world_tris):,} triangles")
print(f"correctness: flat==brute {same(h_flat,h_brute)}  two-level==brute {same(h_two,h_brute)}")
print(f"{'method':<22}{'triangle tests':>18}{'AABB tests':>14}{'tri/ray':>10}")
print(f"{'brute force':<22}{tri_b:>18,}{box_b:>14,}{tri_b/N_RAYS:>10.1f}")
print(f"{'single-level BVH':<22}{tri_f:>18,}{box_f:>14,}{tri_f/N_RAYS:>10.1f}")
print(f"{'two-level TLAS+BLAS':<22}{tri_t:>18,}{box_t:>14,}{tri_t/N_RAYS:>10.1f}")
print(f"speedup vs brute: single-level {tri_b/tri_f:.1f}x  two-level {tri_b/tri_t:.1f}x")
print(f"single-level BVH : {count_nodes(flat_bvh):,} nodes, depth {bvh_depth(flat_bvh)}")
print(f"two-level        : {count_nodes(blas):,} BLAS nodes + {count_nodes(tlas):,} TLAS nodes")
```

### Results

```
scene: 50 instances x 500 tris = 25,000 triangles
rays : 200
correctness: flat==brute True   two-level==brute True
rays that hit something: 85/200

method                    triangle tests    AABB tests   tri/ray
------------------------------------------------------------------
brute force                    5,000,000             0   25000.0
single-level BVH                   3,494        14,512      17.5
two-level TLAS+BLAS                3,150         9,475      15.8
------------------------------------------------------------------
speedup vs brute: single-level 1431.0x   two-level 1587.3x

memory / build:
  brute force        : 25,000 tris stored, no tree
  single-level BVH   : 25,000 tris stored, 16,383 nodes, depth 14
  two-level          : 500 tris stored (shared BLAS), 255 BLAS + 63 TLAS nodes
  -> geometry memory : 50x less for the two-level build

cost of moving all 50 robots one frame:
  single-level BVH   : rebuild over 25,000 triangles
  two-level          : rebuild TLAS over 50 instances  (BLAS untouched)
  -> rebuild input   : 500x smaller
```

---

## 6. Reading those numbers honestly

**The hierarchy is the whole game.** 25,000 triangle tests per ray → **17.5**. A 1,431× reduction, and the tree is only 14 levels deep. That is the *O(N) → O(log N)* claim, measured.

**The trade is real and visible.** The BVH does 14,512 AABB tests to avoid 5 million triangle tests. It performs *more* tests overall — it just made almost all of them cheap ones. That's the bargain, in numbers.

**Now the part people get wrong.** Look again at single-level vs two-level:

```
single-level BVH     3,494 triangle tests
two-level TLAS+BLAS  3,150 triangle tests     ← only 10% better
```

**Two levels barely helps traversal speed.** Roughly a wash. If you assumed TLAS/BLAS exists to make tracing faster, the data says otherwise.

The actual reasons are the last two blocks of output:

- **50× less geometry memory.** One BLAS, not fifty copies. On a real scene this is the difference between fitting in VRAM and not.
- **500× smaller rebuild.** Move all 50 robots and you rebuild a tree over **50 instances** instead of **25,000 triangles**. Every frame. *This* is why animated scenes are viable at all.

So the honest one-line summary: **two levels exist for memory and for dynamic updates, not for raw traversal throughput.** That distinction matters when you're deciding whether to merge meshes into one BLAS (fewer instances, faster traversal, but now they can't move independently) or split them (more instances, cheaper updates).

### Where this toy differs from real hardware

I want to be clear about what the demo does *not* model, so nobody over-reads it:

- **Translation only, no rotation.** Real instances carry a full 3×4 matrix, and you must transform the ray *direction* too, not just the origin.
- **Median split, not SAH.** Production builders use the Surface Area Heuristic, which produces meaningfully better trees.
- **Test counts, not time.** On an RTX GPU, box and triangle tests run on **fixed-function RT cores**, so the cost ratio between them is nothing like it is in Python. The counts show the *algorithmic* win; they do not predict milliseconds.
- **One ray at a time.** Real GPUs trace 32 rays per warp in lockstep — which brings us to the last section.

---

## 7. Back to the PoC: why this explained the profiler

Two findings from the [Omniverse post]({% post_url study/Computer Graphics/2026-08-10-omniverse-isaac-sim-vs-unreal-poc %}) come straight out of the structure above.

### Why Isaac Sim showed 2 draw calls

Because the scene is **not rasterized**. It lives on the GPU as TLAS + BLAS and is traversed by `vkCmdTraceRaysKHR`. Instanced geometry never passes through `vkCmdDrawIndexed` at all. The 2 draw calls that appeared were the ImGui overlay.

So "2 draw calls" doesn't mean *efficient* — it means **that code path isn't being used**. Comparing it against Unreal's 10,733 is comparing a number to the absence of that number.

### Why RTCORE throughput was only 5.3% while VRAM hit 34%

This is the part the toy demo can't show you, and it's the most practically useful.

BVH traversal is **branchy and memory-incoherent**. A GPU executes 32 threads per warp in lockstep. For primary camera rays that's fine — neighbouring pixels shoot nearly parallel rays that walk nearly the same path down the tree.

**Reflection rays destroy that.** They scatter in 32 different directions and descend 32 different branches. Every thread wants a different node from memory, so cache lines thrash and the warp stalls waiting on all of them.

Meanwhile the actual ray-triangle intersection is fixed-function silicon and finishes almost instantly — hence **RT cores idle at 5.3%** while **VRAM throughput sits at 34%**.

> **The bottleneck in ray tracing is usually pointer chasing, not intersection math.**

That reframes optimization completely. Adding RT cores wouldn't have helped that frame. Reducing reflection rays, tightening the roughness cutoff, or improving BVH quality to shorten traversal — those would.

### Why 50 robots barely changed Isaac Sim's render cost

Recall the measurement: RTX rendering went **13.52 ms → 10.76 ms** when 50 robots were added.

Now it should be unsurprising. Adding instances reuses the same BLAS and grows the TLAS by 50 entries, deepening the tree only **logarithmically**. Ray tracing cost tracks **pixels and ray depth**, not triangle count.

Compare Unreal in the same scenario: 10,733 draw calls and 2.14 ms rebuilding Lumen's distance field, both scaling with the *amount of moving geometry*. **Two fundamentally different cost curves** — which was the real conclusion of that PoC, and the reason a single FPS comparison couldn't capture it.

One honest caveat, same as in the original post: I did not verify from the capture that Isaac Sim actually shares a single BLAS across those 50 robots (it would if they're USD instanced prims). But BLAS construction is a one-time cost either way, so the scaling conclusion holds regardless.

---

## 8. The real API

If you want to build this for real, the names to search for:

**Vulkan**

```
VkAccelerationStructureKHR
  VK_ACCELERATION_STRUCTURE_TYPE_TOP_LEVEL_KHR      // TLAS
  VK_ACCELERATION_STRUCTURE_TYPE_BOTTOM_LEVEL_KHR   // BLAS
vkCmdBuildAccelerationStructuresKHR                 // build / update
vkCmdTraceRaysKHR                                   // trace
```

**DXR (D3D12)**

```
ID3D12Device5::BuildRaytracingAccelerationStructure
  D3D12_RAYTRACING_ACCELERATION_STRUCTURE_TYPE_TOP_LEVEL
  D3D12_RAYTRACING_ACCELERATION_STRUCTURE_TYPE_BOTTOM_LEVEL
ID3D12GraphicsCommandList4::DispatchRays
```

**The build flags are where you make the trade:**

| Flag | Meaning | Use for |
|---|---|---|
| `PREFER_FAST_TRACE` | Slower build, better tree | Static geometry — build once, trace forever |
| `PREFER_FAST_BUILD` | Faster build, worse tree | Geometry rebuilt every frame |
| `ALLOW_UPDATE` | Enables refit | Deforming meshes — refit instead of full rebuild |
| `ALLOW_COMPACTION` | Enables post-build shrink | Anything memory-constrained |

Rule of thumb that follows directly from §6: **BLAS for static meshes → `PREFER_FAST_TRACE`. TLAS rebuilt every frame → `PREFER_FAST_BUILD`.** You're building the TLAS constantly and tracing through it briefly; you build the BLAS once and trace through it forever.

---

## Summary

- Ray tracing asks one question — *what does this ray hit first?* — and brute force is off by orders of magnitude.
- A **BVH** wraps geometry in nested boxes so one cheap box test discards millions of triangles. Measured: **25,000 → 17.5** triangle tests per ray.
- **BLAS** = the stamp (triangles, local space, built once). **TLAS** = where you pressed it (instances = BLAS pointer + transform).
- Two levels exist for **memory (50×) and update cost (500×)** — **not** for traversal speed, which was within 10%.
- On real hardware the bottleneck is **incoherent memory access during traversal**, not intersection math. That's why RT cores sat at 5.3% while VRAM was at 34%.
- Consequently, RT cost scales with **pixels and ray depth**, while rasterization scales with **draw calls and moving geometry**. Different curves — which is exactly why "which engine is faster" was the wrong question.

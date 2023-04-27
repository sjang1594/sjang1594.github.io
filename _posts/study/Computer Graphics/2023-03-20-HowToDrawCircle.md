---
title: How to draw the Circle
layout: post
category: study
tags: [computer graphics]
---

### Prep
Graphics 를 다루기 앞서서, glm 과 imgui 가 필요하다는걸 말씀드리고 싶다. vcpkg 로 설치가 편하니, [vcpkg](https://vcpkg.io/en/packages.html) 찾아보기 바란다.

### How to draw the Circle in Image Coordinates (2D)

일단 Image Coordinates 에서는 쉽게 far left corner 이 (0, 0) 을가지고 있고, far right corner in bottom 은 (width - 1, height -1) 로 되어있다. 어떠한 Point 가 원안에 있는지 확인을 하려면, 어떠한 Point 와 `x_center` 값의 절대값이 r 보다 크기 비교를 하면 된다.

일단 Circle 이라는 class 를 만들어보자. 일단 편의성을 위해 접근지정자를 public 으로 해놓고 보면 된다. 그리고 생성자(Constructor)는 원에 필요한 인자로 받는다.

첫번째 방법 같은 경우는 약간 Brute-Force 처럼 곱셈을 할수 있다. 다른 방법같은경우 glm 을 사용해서 point - center 를 뺀값의 distance 를 구하는 방법이 있고, 더 최적화 하는 방법은 `radius squared` 한값을 가지고 `distance squared` 를 비교하는 방법이 있다.

```c++
#include <glm/glm.hpp>
#include <glm/gtx/string_cast.hpp>
#include <glm/gtx/norm.hpp>

class Circle
{
public:
    glm::vec2 center;
    float radius;
    glm::vec4 color; 

    Circle(const glm::vec2& center, const float radius, const glm::vec4& color)
        : center(center), color(color), radius(radius)
    {}

    bool IsInside(const glm::vec2& point)
    {
        const float distance = (point.x - center.x) * (point.x - center.x) + (point.y - center.y) * (point.y - center.y);
        
        // 최적화 방법은 여러가지
        // const float distance = glm::length(point - center) or 
        
        // const float distanceSquared = glm::dot(point - center, point - center);
        

        if(distance <= radius){
            return true;
        }
        else{
            return false;
        }
    }
}
```

### How to draw the Circle for Transformation (2D)

### How to draw the Sphere

### Resource

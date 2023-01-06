---
title: Dynamic Allocation in C++
layout: post
category: study
tags: [c++]
---

### Dynamic Allocation

동적 할당은 진짜 C++ 에서 정말 중요도가 너무 높다. 동적 할당을 알려면 메모리의 구조도 알아야 할 필요가 있다. 메모리 구조에대해서 잠깐 복습을 해보자.

일단 샐행할 코드가 저장되는 영역은 코드 영역 이라고 한다. 전역(global) / 정적 (static) 변수는 데이터 영역에 저장이되고 마지막으로 지역 변수 / 매개 변수는 스택영역에 사용이된다. 하지만 위에 이미지를 보면, 다른 영역들도 보인다. 그러면 왜 구지 다른 영역들을 사용할까? 라는 질문이 떠오르긴 한다.

만약에 실제 상황에서 MMORPG 에서 동시 접속이 1 만명 더많게는 10 만명이 있고, 몬스터도 500만 마리가 될수 있다. 아래의 코드를 실행해보면, stack overflow 라고 하면서 에러를 내뱉는걸 볼수 있다. 

```c++
class Monster
{
public:
    int _hp;
    int _x;
    int _y;
    int _z;
}

int main()
{
    Monster monster[500 * 10000000];
    return 0;
}
```

### Type Conversion

### Shallow Copy vs Deep Copy

### Resource
- [Inflearn: UnrealEngine Game Dev](https://www.inflearn.com/course/%EC%96%B8%EB%A6%AC%EC%96%BC-3d-mmorpg-1)

### Source Code 
- [Dynamic_Allocation](https://github.com/sjang1594/self-study/tree/master/game_dev/cpp/dynamic_allocation)
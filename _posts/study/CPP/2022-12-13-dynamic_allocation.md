---
title: Dynamic Allocation in C++
layout: post
category: study
tags: [c++]
---

### Dynamic Allocation

동적 할당은 진짜 C++ 에서 정말 중요도가 너무 높다. 동적 할당을 알려면 메모리의 구조도 알아야 할 필요가 있다. 메모리 구조에대해서 잠깐 복습을 해보자.

전체적인 그림에서 주로 어떤 OS 든지, 유저영역과 커널 영역(ex: Windows 핵심 코드) 나누어져있다. 유저영역에서는 어플리케이션들이 유저영역에서 실행된다. 만약에 유저 애플리케이션이 서로가 서로의 메모리를 공유해서 쓰거나, 서로의 영역을 침범한다면 정말 망할것이다. 유저 애플리케이션은 서로 서로 독립적으로 메모리를 커널영역에 요청을 한다. 즉 유저영역에서, 운영체제에서 제공하는 API 를 호출한다. 그런 다음 커널영역에서 메모리를 넘겨준다.

일단 샐행할 코드가 저장되는 영역은 코드 영역 이라고 한다. 전역(global) / 정적 (static) 변수는 데이터 영역에 저장이되고 마지막으로 지역 변수 / 매개 변수는 스택영역에 사용이된다. 하지만 위에 이미지를 보면, 다른 영역들도 보인다. 그러면 왜 구지 다른 영역들을 사용할까? 라는 질문이 떠오르긴 한다.

만약에 실제 상황에서 MMORPG 에서 동시 접속이 1 만명 더많게는 10 만명이 있고, 몬스터도 500만 마리가 될수 있다. 아래의 코드를 실행해보면, stack overflow 라고 하면서 에러를 내뱉는걸 볼수 있다. 근데 이게 항상 최대 상한선에서의 이야기이였던거 였다. 실제 게임에서는 한번에 만드는게 아니라, 가끔씩 시간에 지남에 따라서 생성되고 죽음을 맞이 해야할것이다. 그렇다면 메모리 구조에서 조금만 더 생각해보자.

스택 영역에서는 함수가 끝나면 같이 정리되서, 조금 불안정한 메모리라고 볼수 있ㄷ다. 그래서 잠시 함수에 매개변수를 넘긴다거나, 하는 용도로는 좋다. 그리고 그에 따른 메모리영역은 무조건 사용이된다고 볼수 있다. 그렇다면 우리가 위에서 하고 있었던 목적으로 메모리를 필요할때만 사용하고, 필요없을때 반납할수 있는 그런 메모리와 스택과는 다르게 우리가 생성 / 소멸 시점을 관리할 수 있는 그런 아름다운 메모리를 바로 힙영역이다.


그렇다면, C++ 에서 이 힙영역을 건들려면 어떤 Keyword 를 살펴보아야 하나면 `malloc`, `calloc`, `realoc`, `free`, `new`, `delete`, `new[]`, `delete[]` 이 있다. 그렇다면 아까 잠깐 언급한 유저영역과 커널영역에서의 관점을 보자면 C++ 에서는 어떻게 힙영역을 사용할까? C++ 에서는 기본적으로 CRT(C RunTime Library)의 힙관리자를 통해서 힙영역을 사용한다. 단, 정말 원한다면 우리가 직접 API 를 통해 힙을 생성하고 관리할 수도 있다. 예를 들어서 MMORPG 서버 메모리 풀링을 사용할수 있다.

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

일단 `malloc` 의 signature 을 봐보면 `size_t` 를 볼수 있는데 F11 을 타서 봐보면 typedef 로 unsigned int 를 `size_t` 로 되어있는걸 볼수 있다. 그리고 return 값을 보면 pointer 로 보인다. 그래서 `void* pointer = malloc(1000)` 볼수 있다. 이때 1000 byte 만큼을 메모리 관리자로부터 요청해서, 메모리를 할당 후 시작 주소를 가르키는 포인터를 반환해준다. 잠깐 확인 해야 할 필요가 있는게, `void* pointer` 라는거라는게 뭘까? 라는걸 확인해야 할 필요가 있다. 앞서 포인터를 타고 가면 아무것도 없다라는게 아니라, 타고 가면 패ㅑㅇ 뭐가 있는지 모르겠으니까 너가 적당히 반환해서 사용해라라는 느낌으로 `void` 라는게 붙어져있다. 그래서 위의 `Monster` 를 사용하자면, `Monster* m1 = (Monster*)pointer;` 이렇게 변환해서 사용할 수 있다. 그래서 `m1` 에다가 `_hp` 나 세팅이 가능하게 되는것이다. 근데 1000 byte 는 너무 과하고 딱 Monster 객체만큼 받고 싶다면 `sizeof(Monster)` 사용하면 될것이다. 

그렇다고 한다면 우리가 빌려쓰고 이제 반환하는 과정을 보려고 한다. 일단 결론적으로 `malloc` 이라는 키워드를 사용한다면 `free` 라는 keyword 같이 따라오는데, 이게 반환하는 과정이라고 생각하면 된다. `free` 는 `malloc`, `calloc`, `realoc` 메모리로 요청한것들을 반환하거나 풀어주는거라고 생각하면된다. 조금 궁금한점이 있다면, 메모리를 요청 할떄는 얼마만큼 요청했는지를 알수 있는데, 왜 풀어줄때는 메모리를 얼마나 풀어주는지를 따로 요청 하지 않는다. 이는 메모리를 요청할때 Header 라는게 있는데 이게 얼마만큼 요청했는지를 Tracking 할수 있어서 free 를 할때 이걸 보고 메모리를 풀어주는것이다.

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
    void* pointer = mallocs(sizeof(Monster));
    Monster* m1 = (Monster*)pointer;
    m1._hp = 100;
    m1._x = 0;
    m1._y = 0;
    m1._z = 0;

    free(pointer);
    return 0;
}
```

메모리를 건들다 보면, 이제 stackoverflow 처럼, Heap 영역에서 요구한만큼을 더 사용했을 경우에 heapoverflow 가 생긴다. 즉 유효환 힙 범위를 초과했을때 corruption 이 생긴다. 만약에 `free()` 를 사용하지 않고, malloc 을하면 live(RunTime) 일때 Memory Lick(메모리 누수)가 날수 있다. 계속 요청만하고 풀어주지 않아서 문제가 생기는것이다. 즉 반납을해야 지속적으로 사용하거나 재사용을 할수 있다. 그렇다면 free 를 두번 하면 될까? 라는 질문이 생길수 있다. 첫번쨰 free 를 했을때, 그 Header 에 얼마나 할당받았는지를 알수 있는데 free 를 할때 그정보도 날려주기 때문에 두번째에 free 를 했을때 엉뚱한값을 free 하려고 해서 문제가 생긴다.

그렇다면 어떤게 정말 큰 잘못일까? 라고 생각을 하면, 바로 `use-after-free` 라는 것이다. 아래의 코드를 보면 이 케이스를 볼수 있다. free 를 이미 했으면 그 메모리를 건들면 안되는데, `m1` 이라는 메모리를 건드는걸 볼 수 있다. pointer 는 살아있기때문에, 건드릴수 있는데 crash 가 날때가 있고 없을때도 있다. 근데 없을때가 정말 큰일이나는 거다. 즉 엉뚱한 메모리를 건들게되면 위험하기때문에, 동적할당을 사용할때는 사용자가 잘사용해야된다는것이다. 그래서 일단 방지 할수 있는거는 `pointer=null` 을 할수 있다.

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
    void* pointer = mallocs(sizeof(Monster));
    Monster* m1 = (Monster*)pointer;
    m1._hp = 100;
    m1._x = 0;
    m1._y = 0;
    m1._z = 0;

    free(pointer);
    // m1._hp = 100;
    // m1._x = 0;
    // m1._y = 0;
    // m1._z = 0;
    pointer = null;     
    return 0;
}
```

### Type Conversion

### Shallow Copy vs Deep Copy

### Resource
- [Inflearn: UnrealEngine Game Dev](https://www.inflearn.com/course/%EC%96%B8%EB%A6%AC%EC%96%BC-3d-mmorpg-1)

### Source Code 
- [Dynamic_Allocation](https://github.com/sjang1594/self-study/tree/master/game_dev/cpp/dynamic_allocation)
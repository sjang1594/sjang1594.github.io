---
title: Objected Orietned Programming in C++
layout: post
category: study
tags: [c++]
---

### Obejcted Oriented Programming
Objected Oriented Programming 이란 객체지향 프로그래밍을 의미하며, 기존에 있던 절차지향 프로그래밍 같은경우에는 코드가 분산되서, readability 도 떨어지면서, 사용자에게 배려하는 느낌이 전혀 없어진다. 근데 객체지향에서의 귀찮은 점도 존재한다. 예를들어서 "참, 두세줄이면 끝날 코드인데, 꼭 이렇게 까지 내가 해야할까?" 라는 생각도 들수도 있다. 하지만 객체 지향을 통해서 사용자의 편의성을 극대화 하며, 사용자의 실수를 최대한 제작자가 차단을 해야한다라는 가정하에 객체지향적 프로그래밍을 해야한다.

일단 바로 코드로 넘어가자. 일 단 아래와 같이 Knight 에 대한 간단한 class 를 생성했다. class 생성할떄 Modify 할수 있는 조건이있는데 그게 바로 `public` 과 `private` 이있다. 그 이외에건 지금은 생략하고, Inheritance 에서 더 자세하게 설명을 할건데. 지금은 `public` 은 공공으로 사용할수 있는 변수나 함수(method) 라고 하자. `public` 으로 기본으로 지정된 Member Variable 과 Methods 가 존재한다. 

생각을해보자 클래스라는건 빵틀이라고 생각하면 된다. 예를들어서 Knight 이라는 틀은 기본적으로 Health bar, Attack Attributes, and its position 을 들고 있을거다. 그리고 움직일수도있고, 공격할수도 있고, 죽을수도 있다. 그렇게해서 여러개의 Knight 을 만들수 있을것이다. 

```c++
class Knight
{
public:
// Member Variable
    int _hp;
    int _attack;
    int _posX;
    int _poxY;

// Member Function
    void Move(int y, int x);
    void Attack();
    void Die(int hp)
    {
        _hp = 0;
        cout << "Die " << endl;
    }
};

void Move(Knight* knight, int y, int x)
{
    knight->_posX = x;
    knight->_posY = y;
}

void Knight::Move(int y, int x)
{
    _posY = y;
    _posX = x;
    cout << "Move" << endl;
}

void Knight::Attack()
{
    cout << "Attack" << endl; 
}

int main()
{
    // Instantiation
    Knight knight;

    // setting the `knight` member variable
    knight._hp = 100;
    knight._attack = 10;
    knight._posX = 0;
    Knight._posY = 0;
    return 0;
}
```


### Constructor & Destructor

### Inheritance

### Hiding

### Polymorphism

### Initializing the List

### Operation Overloading

- [Inflearn: UnrealEngine Game Dev](https://www.inflearn.com/course/%EC%96%B8%EB%A6%AC%EC%96%BC-3d-mmorpg-1)
- [Objected Oriented Programming in C++](https://github.com/sjang1594/self-study/tree/master/game_dev/cpp/opp) Github repo 폴더에 파일이 있다.
---
title: Singleton
layout: post
category: study
tags: [c++]
---

## Singleton

어쩌다보니 Logging System 을 만들고, 기록은 해놓아야 할 것 같아서, `Singleton` 패턴에 대해서 c++ 로 정리 하려고 한다. Singleton 이라는건 Class 를 딱 하나만 생성한다 라고 정의한다라는게 정의된다. static 으로 정의를 내릴수 있다. 그리고 객체가 복사가 이루어지면 안된다. 일단 싱글톤을 만든다고 하면, 하나의 설계 패턴이므로 나머지에 영향이 안가게끔 코드를 짜야된다. 일단 Meyer's implementation 을 한번 봐보자.

```c++
class Singleton
{
public:
    static Singleton& getInstance();
    {
        static Singleton instance;
        return instance;
    }

private:
    Singleton(){}       // no one else can create one
    ~Singleton(){}      // prevent accidental deletion

    // disable copy / move 
    Singleton(Singleton const&) = delete;
    Signleton(Singleton&&) = delete;
    Singleton& operator=(Singleton const&) = delete;
    Singleton& operator=(Singleton&&) = delete
};
```

그렇다면 더확실하게 생성과 파괴의 주기를 확실하게 보기위해서는 아래와 같이 사용할수 있다.

```c++
class Singleton
{
public:
    static std::shared_ptr<Singleton> getInstance();
    {
        static std::shared_ptr<Signleton> s{ new Singleton };
        return s;
    }
private:
    Singleton(){}       // no one else can create one
    ~Singleton(){}      // prevent accidental deletion

    // disable copy / move 
    Singleton(Singleton const&) = delete;
    Signleton(Singleton&&) = delete;
    Singleton& operator=(Singleton const&) = delete;
    Singleton& operator=(Singleton&&) = delete
};
```

예제를 들어보자, 뭔가 기능상으로는 Random Number Generator 라고 하자. 아래와 같이 구현을 하면 좋을 같다.

```c++
class Random
{
public:
    static Random& Get()
    {
        static Random instance;
        return instance;
    }

    static float Float() { return Get().IFloat(); }
private:
    Random(){}
    ~Random();
    Random(const Random&) = delete;
    void operator=(Random const&) = delete;
    Random& operator=()
    float IFloat() { return m_RandomGenerator; } // internal
    float m_RandomGenerator = 0.5f;
};

int main()
{
    // auto& instance = Singleton::Get();   // this is good practice
    // Single instance = Singleton::Get();  // Copy this into new instance; Just want a single instance.

    float number = Random::Get().Float();
    return 0;
}
```

## Resource
* [Singleton Design Pattern](https://stackoverflow.com/questions/1008019/how-do-you-implement-the-singleton-design-pattern/1008289#1008289)
* [Meyer's Discussion](https://www.drdobbs.com/cpp/c-and-the-perils-of-double-checked-locki/184405726)
* [Lecture Note](https://websites.umich.edu/~eecs381/lecture/IdiomsDesPattsCreational.pdf)
* [The Cherno - Youtube](https://www.youtube.com/watch?v=PPup1yeU45I)
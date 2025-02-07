---
title: CallBack Function in C++
layout: post
category: study
tags: [c++]
---

### Function Pointer

함수 선언이나 변수 선언을 할때, 항상 앞에는 타입이 존재했다. return 받을 타입이나, 아니면 이 타입으로 저장한다는 식으로. 그렇다면 함수를 변수로 사용할수 있을까? 의 질문의 시작이 함수 포인터의 시작이다.

일단 함수를 뭔가 변수로 설정하려고 한다면, 함수의 signature 이 중요하다. 일단은 사실상 함수의 이름은 신경 써주지 않는다고하고 아래의 코드를 보면 `int(int a, int b)` 이런식으로 된다. 근데 어떻게 이름을 줄까? 라는 생각을 해보는데. 이건 `typedef` 로 생각하면 된다.

그래서 signature 은 `typedef int(FUNC_TYPE)(int a, int b)` 이런식으로 주면 된다. 하지만 Modern C++ 에서는 더 편한걸로 `using` 을 사용해서, `using FUNC_TYPE = int(int a, int b)` 이런식으로 표현이 가능하기도 하다. 그런다음에 `FUNC_TYPE* fn` 이라고 생성하면 함수의 포인터라고 할수 있다.

```c++
int Add(int a, int b)
{
    return a + b;
}

int main()
{
    int Add(int a, int b);
    return 0;
}
```

아래의 코드를 봐보기전에, 뭔가 함수의 return 값을 봐보면, 함수의 시작 주소가 있다는걸 힌트를 알수 있다. 그 말은 즉슨 포인터를 이용해, 그 함수를 point 하게 둘수 있다는 말이다. 아래와 같이 `fn` 즉 FUNC_TYPE 의 signature 만 맞으면, 함수를 호출이 가능하다는 소리이다. 그리고 아래의 `(*fn)` 이 signature 같은 경우는 fn 을 타고 들어가서 (1, 2) 를 넣어준다라고 생각하면 될것 같다.

```c++
int Add(int a, int b)
{
    return a + b;
}

int main()
{
    typedef int(FUNC_TYPE)(int, int);
    FUNC_TYPE* fn;
    fn = Add;

    int result = fn(1, 2);
    int result = (*fn)(1, 2);
}
```

근데 구지 생각을 해보면, 왜 이렇게 까지 써야되냐? 라는 질문을 할 수 있는데, 그 이유는 함수의 signature 가 동일하게 되면 쉽게 스위칭이 가능하다 라는 말이다. 아래의 코드를 한번 봐보자. `Add` 를 다 쓴 이후 `Sub` 으로 바로 스위칭이 가능하다. 어떻게 보면 나머지를 고칠 필요 없이, 강력한 Tool 로 쓸수 있다.

```c++
int Add(int a, int b)
{
    return a + b;
}

int Sum(int a, int b)
{
    return a - b;
}

int main()
{
    typedef int(FUNC_TYPE)(int, int);
    FUNC_TYPE* fn;
    fn = Add;
    // add.. 를 다 쓴이후
    fn = Sub;
    // sub 처리
}
```

또 다른 예제를 알아보자. 아래의 Item 클래스를 만들어줬고 Item pointer 를 return 해주는 코드가 있다고 하자. 뭔가 같은 기능을 계속 인자만 바꿔서 주는게 굉장히 코드가 길어지고, 유지 보수가 좋지 않다. 그래서 인자값으로 함수의 안전체크나 조건문들을 넘겨주게 된다면 이 코드의 유지 보수성은 더 올라갈것이다. 

```c++
class Item
{
public:
    Item() : _itemId(0), _rarity(0), _ownerId(0){}
public:
    int _itemId;
    int _rarity;
    int _ownedId;
};

Item* FindItemByItemId(Item items[], int itemCount, int itemId)
{
    for(int i = 0; i < itemCount; i++)
    {
        Item* item = &items[i];
        if (item->_itemId == item)
            return item;
    }

    return nullptr;
}

Item* FindItemByRarity(Item items[], int itemCount, int rarity)
{
    for(int i = 0; i < itemCount; i++)
    {
        Item* item = &items[i];
        if (item->_rarity == rarity)
            return item;
    }

    return nullptr;
}
```

그래서 더 낳은 코드를 한번 봐보겠다. 그리고 이번엔 rarity 를 체크 해보겠다.

```c++
class Item
{
public:
    Item() : _itemId(0), _rarity(0), _ownerId(0){}
public:
    int _itemId;
    int _rarity;
    int _ownedId;
};

void IsRareItem(Item* item)
{
    return item->_rarity >= 2;
}

Item* FindItem(Item items[], int itemCount, bool(*selector)(Item*item))
{
    for(int i = 0; i < itemCount; i++)
    {
        Item* item = &items[i];
        if (selector(item))
            return item;
    }

    return nullptr;
}

int main()
{
    Item item[10] = {};
    item[3]._rarity = 2;
    Item* rareItem = FindItem(items, 10, IsRareItem);
}
```

그런데, 물론 장점도 있지만 단점도 있다. 아까 계속 언급한 함수의 signature 가 달라진다면 물론 다르게 표현을 해야된다. 아래의 코드를 보면 실패하게 된다 왜냐하면 `isOwnerItem` 의 signautre 가 아까 `IsRareItem` 과 다르기 때문이다. 그래서 아래의 코드를 보면 같이 맞춰지게 int 값도 따로 추가해주면 된다. 즉 꼬리의 꼬리물기가 되서, 뭔가 함수의 인자수가 많아져서 좋지 않은 구조가 된다. 즉 결론은 함수도 주소가 있어서 함수포인터를 사용해서 함수의 call 바로 할수 있다.

```c++
class Item
{
public:
    Item() : _itemId(0), _rarity(0), _ownerId(0){}
public:
    int _itemId;
    int _rarity;
    int _ownedId;
};

void IsRareItem(Item* item, int)
{
    return item->_rarity >= 2;
}

bool isOwnerItem(Item* item, int ownderId)
{
    return item->_ownderId == ownderId;
}

Item* FindItem(Item items[], int itemCount, bool(*selector)(Item*item, int), int value)
{
    for(int i = 0; i < itemCount; i++)
    {
        Item* item = &items[i];
        if (selector(item, value))
            return item;
    }

    return nullptr;
}

int main()
{
    Item item[10] = {};
    item[3]._rarity = 2;
    Item* rareItem = FindItem(items, 10, isOwnerItem);
}
```

사실은 블로그를 커버하다가, 한번도 typedef 에 대해 설명을 하지 않았다. typedef 그냥 형태 만 봤을때 `typedef [] []` 이런식으로 생겼다. 하지만 봤을때 오른쪽이 커스텀 타입을 정의를 했었다. 근데 이걸 더 정확하게 보면, 선언 문법에서 typedef 를 앞에다 붙이는쪽으로 왔었다. 아래와 같이 선언을 하면, 바로 앞에 `typedef` 를 붙여지는거다. 그래서 Code Segment 를 봤을때 아래를 보면 함수의 Signature 은 `(int, int)`의 인자를 받고 `int` 로 받고, 그다음에 함수의 포인터이기때문에 `(*PFUNC)` 라는걸 선언을 한거다. 그다음에 `typedef` 를 넣으면 된다.

```c++
int INTEGER;
int *POINTER;
int FUNC();

int (*PFUNC)(int, int);
```

근데 또 단점이 있다. 위와같이 사용할때는 전역함수 / 정적함수만 담을 수 있다. 즉 호출 규약이 정해져있다는 소리이다. 아래처럼 Member Function 에서는 에러가 나온다는걸 확인할수있다.

```c++
typedef int(*PFUNC)(int, int);

class Knight
{
public:
    // Static Function
    static void HelloWorld(){}
    
    // Member Function
    int GetHP(){ return _hp; }

    int _hp = 100;
}

int main()
{
    PFUNC fn;
    // fn = GetHP; // 에러
    // fn = &Knight::GetHp;
    return 0;
}
```

그래서 이걸 멤버함수에 속한다라는걸 보여주어야기 때문에 아래의 코드 처럼 하면된다. 아래에 보면, 주소값을 달라는 표시도 해주어야한다. 이건 C 언어의 호환성 때문에 한다.

```c++

class Knight
{
public:
    // Static Function
    static void HelloWorld(){}
    
    // Member Function
    int GetHP(){ return _hp; }

    int _hp = 100;
}

typedef int(Knight::*MEMBERPFUNC)(int, int);

int main()
{
    PMEMFUNC mfn;
    mfn = &Knight::GetHp;

    Knight k1;
    (k1.*mfn)(1, 1);

    Knight* k2 = new Knight();
    (k2->*mfn)(1,1);
    delete k2;

    return 0;
}
```

일반적으로 자신과 다른 클래스가 있고 멤버함수가 동일하다고 하더라도, 이미 지정해주었기 때문에, 객체를 바꾸더라도 실행이 안된다는거에 주의하자.

### Functor

함수 객체는 함수처럼 동작하는 객체를 뜻하는데, 위와 같이 함수 포인터의 단점이 너무 잘보였었다. 일단 함수의 signature 가 동일한 친구들 만 사용됬었고 다르다고 하다면, 인자를 늘려가야하는 큰단점, 즉 generic 하게 사용하지 못한다는 점이 큰 단점이 였다. 또 다른 큰 단점은 자세하게 debug 하지 않으면 객체의 상태의 유지성을 모른다는거다. 예를 들어서 `Knight` 의 객체 안에 `_hp` 라는 field 가 있는데, 함수 포인터 같은 경우는 인자만 넘기지, 그 field 가 뭘하는지, 유지 됬는지 잘모른다는 뜻이다.

함수처럼 동작하는 객체라는게 뭘까라는 걸 알아보자. 일단 함수 처럼 작동하려면 힌트는 `()` 이런 연산자가 필요하다. `()` 연산자 오버로딩이 필요하다는거다.

```c++
class Functor
{
public:
    void operator() ()
    {
        cout << "Functor Test1" << endl;
    }
    bool operator() (int num)
    {
        cout << "Functor Test2" << endl;
        _value += num;
        cout << _value << endl;
    }
private:
    int _ value = 0;
}

int main()
{
    Functor functor;
    functor();

    bool ret = functor(3);
    return 0;
}
```

예시로 보여준건 MMO 에서 함수 객체를 사용하는 예시가 있다. 게임은 클라와 서버가 있는데, 서버같은 경우는 클라가 보내준 네트워크 패킷을 받아서 처리하는데 만약에, 클라가 (5,0) 으로 좌표로 이동 시켜줘! 라고 서버한테 요청을 했다고 하자. 실시간 MMO 라고 하면 클라가 정말 많을텐데, 이때 처리할때 사용할수 있다. 이때, Functor 만들어준 시점과 그리고 실제 실행할 시점을 분리 시키는걸 볼수 있다. 아래가 바로 Command Pattern 을 비슷하게 사용해서 Tracking 이 가능할거다.

```c++
class MoveTask
{
public:
    void operator()()
    {
        // TODO
        cout << "Move" << endl;
    }
public:
    int _playerId;
    int _posX;
    int _posY;
}

int main()
{
    MoveTask task;
    task._playerId = 100;
    task._posX = 5;
    task._posY = 3;

    // 나중에 여유될때 일감을 실행
    task();
    return 0;
}
```

### Template Basics

Template 이란 함수나 클래스를 찍어내는 툴이라고 생각하면 된다. 템플릿의 종류는 Function Template 과 Class Template 이 존재한다.
일단 예시같은 경우는 이런거다 여러 다른 타입들을 받는 똑같은 함수가 존재한다고 하자. 다 똑같은 기능을 가지고 있지만 인자값으로 다르게 존재 하는걸 볼수 있다. 이거를 한번에 묶을수 있는 존재가 있을까? 라는 생각이든다. 그게 바로 형식을 틀로 잡을수 있는 template 이 있다. 즉 조커 카드이다.

```c++
#include <iostream>
using namespace std;
void Print(int a){ cout << a << endl;}

void Print(float a){ cout << a << endl; }

void Print(double a){ cout << a << endl; }
```

Template 에 대해서 한번 봐보자. 일단 아래의 코드처럼 `typename T` 라고 지정해준걸 볼수 있다. 그리고 그 인자의 type 을 `Print()` 함수에 넣어진걸 확인 할 수 있다. 즉 어떤 타입이 들어오든지 T 로 들어와서 컴파일러가 각각 type 을 정해주는걸로 볼수 있다. 아래 처럼 코드를 실행 해보았을때, 잘 빌드가 성공된걸 볼수 있다. 그리고 맨 아래에 보면 Print 뒤에 `<double>` 이란게 나와있다. 이거 같은 경우는 컴파일러에 맡기는것보다 내가 이런 형식을 원한다라는걸 강제적으로 줄수도 있다. 이말은 즉슨 컴파일러에게 힌트를 주는거다. 그리고 아래의 `Add` 함수를 봐보자. 여기에서는 인자가 같을때 즉 (int, int), (double, double), 이런식으로 타입이 같은 인자가 들어왔을때도 줄일수도 있고, return 값으로도 `T` 를 줄수도 있다. 이 말은 또 각기 다른 타입의 인자를 넣어줄수도 있다. `PrintMultiple()` 을 참고하자. 그리고 객체의 있는걸 Type 으로 넘겨준다고 하면 실행 되지 않는다. 그 이유는 `Knight` 라는 클래스는 프로그래머가 만든 커스텀 한 타입이기때문에 지원되지 않아서 `ofstream` 에 있는걸 가져다가 오버로딩을 해줘야한다.

```c++
template<typename T>
void Print(T a)
{
    cout << a << endl;
}

template<typename T>
T Add(T a, T b)
{
    return a + b;
}

template<typename T1, typename T2>
void PrintMultiple(T1 a, T2 b)
{
    cout << a << " " << b << endl;
}

class Knight
{
public:
    // ...
public:
    int _hp = 100;
};

// 연산자 오버로딩 (전역함수)
ofstream& operator<<(ofstream& os, const Knight& k)
{
    os << k._hp << endl;
    return os;
}

int main()
{
    Print(50);
    Print(50.0f);
    Print<double>(50.0);

    ret = Add(2, 3);

    PrintMultiple("Hello", 3);

    Knight k1;
    Print(k1); // 연산자 오버로딩이 없으면 안됨
    return 0;
}
```

위와 같이 template 은 조커카드였다. 하지만 어떤객체에 대해서 특수 조커 카드를 만들려고 했을때, 어떻게 해야될까? 라는 질문을 할수 있다. 즉 어떤 규칙을 따르는 template 을 template 특수화라고 한다.아래의 코드를 봐보자. 아래와 같이 어떤 특정한걸 주고 싶을때는 객체를 인자로 넘겨주고 temmplate 안에 있는거는 비어있게 해줘야 template 의 특수화가 된다.

```c++
tempalte<>
void Print(Knight a)
{
    cout << "Knight" << endl; 
    cout << a._hp << endl;
}

int main()
{
    Knight k1;
    Print(k1);
    return 0;
}
```

이제 class template 을 보기위해 아래 코드를 봐보자. 일단 `RandomBox` 라는 클래스가 있고, 만약에 GetRandomData() 가 만약에 Float 로 내뱉는 return 이 필요하다고 하면 float 데이터를 담을수 있는 바구니가 필요하면서, float 을 return 하는 GetRandomData() version 을 만들어야할것이다. 그래서 이 다음 코드를 봐보면 template 이 적용된걸 볼 수 있다.

```c++
class RandomBox
{
public:
    int GetRandomData()
    {
        int idx = rand() % 10;
        return _data[idx];
    }
public:
    int _data[10];
}

int main()
{
    srand(static_cast<unsigned int>(time(nullptr)));
    RandomBox rb1;
    for (int i = 0; i < 10; i++)
    {
        rb1._data[i] = i;
    }
    int value1 = rb1.GetRandomData();
    cout << value1 << endl;
    
    RandomBox rb2;
    for (int i =0; i< 10; i++)
    {
        rb2._data[i] = i;
    }
    int value2 = rb2.GetRandomData();
    cout << value2 << endl;
    return 0;
}
```

```c++
template<typename T>
class RandomBox
{
public:
    T GetRandomData()
    {
        int idx = rand() % 10;
        return _data[idx];
    }
public:
    T _data[10];
}

int main()
{
    srand(static_cast<unsigned int>(time(nullptr)));
    RandomBox<int>rb1;
    for (int i = 0; i < 10; i++)
    {
        rb1._data[i] = i;
    }
    int value1 = rb1.GetRandomData();
    cout << value1 << endl;
    
    RandomBox<float> rb2;
    for (int i =0; i< 10; i++)
    {
        rb2._data[i] = i + 0.5f;
    }
    float value2 = rb2.GetRandomData();
    cout << value2 << endl;
    return 0;
}
```

그런데 `typename` 을 무조건 붙여야되는건 아니다. 즉 다시 말해서 template 안에 들어가는건 골라줘야하는 목록 이라고 볼수 있다. 예를들어서 아래의 코드를 봐보자. `SIZE` 에다가 인자를 아무거나 주되 `int` type 인자를 받아야하는 어떤 설정을 따로 해줄수 있다. 하지만, `rb1`, `rb2` 가 같이 instantiate 했지만, 서로 다른 객체라는걸 알수 있어서 함수의 인자의 signature 이 같다고 하더라도, 객체는 다르게 이루어졌다고 볼수 있다. 위와 같이 함수에서 템플릿 특수화를 썻던것처럼, 클래스에서도 template 특수화를 사용할수 있다.

```c++
template<typename T, int SIZE>
class RandomBox
{
public:
    T GetRandomData()
    {
        int idx = rand() % SIZE;
        return _data[idx];
    }
public:
    T _data[SIZE];
}

int main()
{
    srand(static_cast<unsigned int>(time(nullptr)));
    RandomBox<int, 10>rb1;
    for (int i = 0; i < 10; i++)
    {
        rb1._data[i] = i;
    }
    int value1 = rb1.GetRandomData();
    cout << value1 << endl;
    
    RandomBox<int, 20> rb2;
    for (int i =0; i< 20; i++)
    {
        rb2._data[i] = i;
    }
    int value2 = rb2.GetRandomData();
    cout << value2 << endl;

    //rb1 = rb2; // 서로 다른 객체
    return 0;
}
```

템플릿 특수화를 한번 보자. 위의 코드에서 무조건 double 로 return 하는 값들로만 모아보자. 아래와 같이 보면 double 로 뭔가 규약을주고, 사이즈와 관련된것들은 int 로 아무인자나 받게 보여진다. 만약 double 로 호출을 한다고 하면 `RandomBox<double, int SIZE>` 가 호출이 되고, 그 외의 것들은 `RandomBox` 가 호출이 될거다.

```c++
template<int SIZE>
template<typename T, int SIZE>
class RandomBox
{
public:
    T GetRandomData()
    {
        int idx = rand() % SIZE;
        return _data[idx];
    }
public:
    T _data[SIZE];
}

class RandomBox<double, int SIZE>
{
public:
    double GetRandomData()
    {
        int idx = rand() % SIZE;
        return _data[idx];
    }
public:
    double _data[SIZE];
}

int main()
{
    srand(static_cast<unsigned int>(time(nullptr)));
    RandomBox<int, 10>rb1;
    for (int i = 0; i < 10; i++)
    {
        rb1._data[i] = i;
    }
    int value1 = rb1.GetRandomData();
    cout << value1 << endl;
    
    RandomBox<double, 20> rb2;
    for (int i =0; i< 20; i++)
    {
        rb2._data[i] = i + 0.5;
    }
    double value2 = rb2.GetRandomData();
    cout << value2 << endl;

    //rb1 = rb2; // 서로 다른 객체
    return 0;
}
```

### Callback Function

Callback 함수 같은 경우는 결국 다시 호출하다. 약간 Call me back 과 같다. 또는 다시 역으로 호출하다라는 느낌이다. Functor 와 마찬가지로 어떤 상황이 일어나면 이 기능을 호출해줘 라는 느낌으로 사용하면 된다.

```c++
class Item
{
public:
    int _itemId = 0;
    int _rarity = 0;
    int _ownderId = 0;
}

class FindByOwnderId
{
public:
    bool operator()(const Item* item) // 수정이 필요없음
    {
        return (item->_ownerId == _ownderId);
    }
public:
    int _ownerId;
}

class FindByRarity
{
public:
    bool operator()(const Item* item) // 수정이 필요없음
    {
        return (item->_rarity == _rarity);
    }
public:
    int _rairty;
}

template<typename T>
Item* FindItem(item items[], int itemCount, T selector)
{
    for (int i = 0; i < itemCount; i++)
    {
        Item* item = &items[i];
        // TODO Condition
        if (selector(item))
            return item;
    }
    return nullptr;
}

int main()
{
    Item Items[10];
    items[3]._ownerId = 100;
    items[5]._rarity = 1;
    FindByOwnderId functor1;
    functor1._ownerId = 100;

    FindByRarity functor2;
    functor2._rarity = 1;

    Item* item1 = FindItem(items, 10, functor1);
    Item* item2 = FindItem(items, 10, functor2);
    
    return 0;
}
```

### Resource

- [Inflearn: UnrealEngine Game Dev](https://www.inflearn.com/course/%EC%96%B8%EB%A6%AC%EC%96%BC-3d-mmorpg-1)

### Source Code

- [CallBack_Function](https://github.com/sjang1594/self-study/tree/master/game_dev/cpp/call_back_function)
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

### Callback Function

### Functional Object

### Template Basics

### Resource

- [Inflearn: UnrealEngine Game Dev](https://www.inflearn.com/course/%EC%96%B8%EB%A6%AC%EC%96%BC-3d-mmorpg-1)

### Source Code

- [CallBack_Function](https://github.com/sjang1594/self-study/tree/master/game_dev/cpp/call_back_function)
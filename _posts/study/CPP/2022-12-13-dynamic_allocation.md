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
};

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
};

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
};

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

사실 `malloc`, `calloc`, `realoc` 은 C 에서 사용되는 부분이였다. 그래서, C++ 에서 자주 사용되는 `new` 와 `delete` 를 알아보자. 일단 넘어가기전에 `malloc`, `calloc`, `realoc` 이들은 함수였다. 하지만 C++ 에서 동적할당을하는 `new` 와 `delete` 연산자(operator)이다.

아래의 코드를 봐보자. new 를 했을때 타입을 넣어준다. 이때 타입의 크기만큼을 동적할당을 해준다. 앞에서 `malloc` 과 `free` 가 같이 있듯이, `new` 와 `delete` 같이 묶여 다니는걸 볼수 있다. 버그의 케이스도 위의 `malloc` 과 같다. 그러면 우리가 Monster 를 여러마리를 만들고 싶을때는 아래의 코드를 보면 `new Monster[5]` 를 사용해서 5 마리의 몬스터를 만든것을 볼수 있다.

```c++
class Monster
{
public:
    int _hp;
    int _x;
    int _y;
    int _z;
};

int main()
{
    Monster* m1 = new Monster;
    m1._hp = 100;
    m1._x = 0;
    m1._y = 0;
    m1._z = 0;
    delete m1;

    Monster* m2 = new Monster[5];
    delete[] m2;
    return 0;
}
```

그렇다면 `malloc / free` 그리고 `new / delete` 의 Use-Case 같은경우는 사용 편의성에서는 확실이 `new / delete` 이게 좋지만, 타입에 상관없이 특정한 크기의 메모리 영역을 할당받으려면 `malloc / free` 이 좋다. `정말 가장 중요한 근본적인 차이는 또 new / delete 는 생성타입이 클래스일 경우, 생성자 / 소멸자를 호출해준다.` 즉 위의 코드에서 Monster 를 여러개 만들때 생성자와 소멸자가 5번 호출을 해주고, 만약에 `delete` 를 한번 했었을때, 에러를 뱉어내는걸 확인할수 있다.

```c++
class Monster
{
public:
    Monster(){ cout << "Monster()" << endl;}
    ~Monster(){ cout << "~Monster()" << endl;}
    int _hp;
    int _x;
    int _y;
    int _z;
};

int main()
{
    Monster m1 = new Monster;
    delete m1;
    return 0;
}

```

마지막 예를 보자. 아래의 코드를 봐보면, 실제 stack 에서 Item 을 instantiate 했을때는, 생성자가 호출이 되는걸 확인 할수 있는데 pointer 로 Item 이라는걸 생성할때는 생성자가 호출이 될수도 있고 안될수도 있다. 아래의 같이 pointer 로 배열을 만들경우 타입만 선언을 했기때문에 그리고 초기에는 아무것도 없기 때문에 생성자가 없을 수 도 있다. 그래서 아래와 같이 객체생성을 하기위해서 loop 을 돌면서 생성을 하고 그 다음에 소멸자도 마찬가지로 소멸을 시키면 소멸자가 호출이된다.

```c++
class Item
{
public:
	Item(){cout << "Item()" << endl;}
	Item(const Item& item){cout << "Item(const: item&" << endl;}
	~Item(){ cout << "~Item()" << endl;}
public:
	int _itemType = 0;
	int _itemObid = 0;

	char _dummy[4096] = {};
};

void TestItem(Item item){ /* 복사생성자 호출 */ }

void TestItemPtr(Item* item){ /*원본을 건드리기때문에 원격*/}

int main()
{
    Item item;
    Item* item2 = new Item();

    TestItem(item);
    TestItem(*item2);

    TestItemPtr(&item);
    TestItemPtr(item2);

    Item item3[100] = {};

    // 실질적으로 아무것도 없을수 있음
    Item* item4[100] = {};

    for(int i=0; i<100; i++)
        Item4[i] = new Item();

    for(int i=0; i<100; i++)
        delete Item4[i];
    delete item2;
    return 0;
}
```

### Type Conversion

위에서 보았듯이 `malloc / free` 를 사용했을때 void 값으로 설정을 해준 이후 타입을 변환한걸 확인 할수 있었다.

일단 타입 변환에도 유형(비트열 재구성 여부)이 있다.
1. 값 타입 변환
   1. 의미를 유지하기 위해서, 원본 객체의 다른 비트열 재구성.
2. 참조 타입 변환
   1. 비트열을 재구성하지 않고 관점만 바꾸는 것

```c++
int main()
{
    {
        // 값 타입 변환
        int a = 123456789;
        float b = (float)a;
    }
    {
        // 참조 타입 변환
        int a = 123456789;
        float b = (float&)a;
    }
    return 0;
}
```

타입 변환에서는 변환이 안전하게 변하게 되는 경향과 불안전하게 변환되는게 있다. 예를 들어서 Upcasting 즉 작은 메모리를 타입을 가지고 있는걸, 큰거에다가 변환시켰을때에 안전하게 변환되는걸 확인할수 있다. 그렇다면 불완전하게 되는 경향은 이거에 반대되는 상황일다. 이럴 경우 데이터의 손실을 불러 일으킨다.

또 프로그래머의 암시적변환과 명시적 변환이존재한다. 암시적 변환 같은 경우는 컴파일러에게 알아서 변환 인거고, 명시적인거는 프로그래머가 따로 괜찮으니까 타입캐스팅을 해줘라는 느낌이다.

그렇다면 객체 클래스가 나온다고 했을때는 어떻게 타입변환을 어떻게 해야할까? 라는 질문을 할 수 있다.
일반적으로는당연히 타입변환이 되지 않는다. 하지만 예외적인 케이스는 있다. 타입 변환생성자를 만들어주게 되면, 타입변환이 가능하다. 그리고 타입 변환 연산자로 타입변환이 가능하다. 아래의 코드를 참고하자.

```c++
class Knight
{
public:
	int _hp = 10;
};

class Dog
{
public:
	Dog(){}
    // 타입 변환 생성자
	Dog(const Knight& knight){ _age = knight._hp;}

	// 타입 변환 연산자 (return type 이 없음)
	operator Knight()
	{
		return (Knight)(*this);
	}
public:
    int _age = 1;
    int _cuteness = 2;
};

int main()
{
    Knight knight;
    Dog = dog (Dog)knight; 
}
```

그리고 또 연관없는 클래스 사이의 참조 타입변환을 알아보자. 아래의 코드를 봐보면 `(Dog&)` 이게 knight 앞에 없으면 에러를 내뱉는다. 이건 일단 기본적으로 서로 타입이 안맞기 때문이다. 그리고 문법적으로 봤을때는 일단 참조기 때문에 주소값을 타고 가면 Dog 가 있을꺼야라고하는게 사실을 문법적으로 맞다. 하지만 사실적으로는 Knight 이 있는거다. 즉 문법적으로 통과할지라도, 사실의 값이 다르다는건 명시적으로는 괜찮다.

```c++
class Knight
{
public:
	int _hp = 10;
};

class Dog
{
public:
	Dog(){}
    // 타입 변환 생성자
	Dog(const Knight& knight){ _age = knight._hp;}

	// 타입 변환 연산자 (return type 이 없음)
	operator Knight()
	{
		return (Knight)(*this);
	}
public:
    int _age = 1;
    int _cuteness = 2;
};

int main()
{
    Knight knight;
    Dog& dog = (Dog&)knight; 
}
```

그렇다면 마지막으로 볼수 있는게 클래스에서 중요했던 상속관계에 있는 클래스 사이의 변환은 어떻게 될까? 첫번째는 상속 관계 클래스의 값타입변환이 있다. 아래의 코드를 보면 bulldog 은 dog 를 상속 받고 있기때문에, 말에 일리가 있다. 즉 자식의 타입변환을 해서 부모님에게 저장하는건 가능하다 라는 말이다.

```c++
class Dog
{
public:
	Dog(){}
    // 타입 변환 생성자
	Dog(const Knight& knight){ _age = knight._hp;}

	// 타입 변환 연산자 (return type 이 없음)
	operator Knight()
	{
		return (Knight)(*this);
	}
public:
    int _age = 1;
    int _cuteness = 2;
};

class BullDog : public Dog
{
public:
    bool IsFrench;
};

int main()
{
    BullDog bulldog;
    Dog dog = bulldog;
}
```

마지막으로는 상속관계 클래스의 참조 타입 변환이다. 아래의 코드를 확인했을때 자식에서 부모의 타입변환은 Ok 지만, 부모에서 자식으로 할때 암시적으로는 안돼지만, 명시적으로는 Ok 한다.
```c++
class Dog
{
public:
	Dog(){}
    // 타입 변환 생성자
	Dog(const Knight& knight){ _age = knight._hp;}

	// 타입 변환 연산자 (return type 이 없음)
	operator Knight()
	{
		return (Knight)(*this);
	}
public:
    int _age = 1;
    int _cuteness = 2;
};

class BullDog : public Dog
{
public:
    bool IsFrench;
};

int main()
{
    Dog dog;
    BullDog& bulldog = (BullDog&)dog; 
}
```

### Pointer Type Conversion

위와같이 Type Conversion 을 연이어 해보자. 일단 연관성이 없는 클래스 사이의 포인터 변환을 해보자.
아래의 코드에서 보면 명시적으로는 Ok 지만 암시적인것은 컴파일러에서 에러를 내뱉는걸 확인할수있다. 이걸 해석해보자면 item 의 주소를 타고 가면 Item 이 있다라는걸 명시해주는데, 사실상 틀린거라고 확인할수있다. 그런데 여기서 문제점은 실제 Knight() 안에 _hp 가 4 byte 일텐데 item->_ItemType 을 했을때까지는 괜찮다. 왜냐하면 같은 4 byte 일테니까. 하지만 두번째 _ItemDbId 를 넣을경우 엉뚱한곳에다가 메모리의 값을 수정하다보니 메모리오염이 있을수가 있다. 또 이건 에러로 내뱉지도 않으니, 그냥 지나칠수 있는 치명적인 메모리의 오염의 주범이 될거다.

```c++
class Knight
{
public:
    int _hp;
};

int main()
{
    Knight* knight = new Knight();
    // Item* item = knight; 암시적 NO
    // 명시적 OK
    Item* item = (Item*)knight;
    item->_ItemType = 2;
    item->_ItemDbId = 1;
    delete knight;
    return 0;
}
```

그렇다면 상속관계에서의 포인터 타입 변환관계를 알아보자. 여기에서도 명시적으로 하면 Ok 지만, 사실 엉뚱한 메모리를 바꿀수 있는 위험이 있다. 하지만, 논리적으로 생각했을때 자식에서 부모 변환테스트는 암시적으로는 된다. 당연히 Weapon 은 Item 이 맞기 때문이다. 즉 명시적으로 타입변환을 할때는 항상 조심해야한다.

그렇다면 항상모든게 명시적으로 하는게 좋지 않느냐라는 질문을 할수 있지만 아래의 코드를 보면, 자식에서 부모로 가는건 설계적인 면에서 많은 이득을 볼수 있기때문에, Inventory 라는 pointer array 를 사용해서 추가할수 있다.

```c++
class Item
{
public:
	Item(){cout << "Item()" << endl;}
	Item(int itemType) : _itemType(_itemType) {};
	Item(const Item& item){cout << "Item(const: item&" << endl;}
	~Item(){ cout << "~Item()" << endl;}
	virtual void Test(){cout << "Test Item " << endl;}
public:
	int _itemType = 0;
	int _itemdbid = 0;

	char _dummy[4096] = {};
};

class Weapon : public Item
{
public:
	Weapon() : Item(IT_WEAPON){ cout << " Weapon() " << endl; _damage = rand() % 100 + 1;} 
	~Weapon(){ cout << "~Weapon()" << endl; }
public:
	int _damage = 0;
};

class Armor : public Item
{
public:
	Armor() : Item(IT_ARMOR){ cout << " Armor() " << endl;}
	~Armor(){ cout << " ~Armor() " << endl;}
public:
	int _defence = 0;
};

int main()
{
    // Parent -> child
    Item* item = new Item();
    // item 은 무기냐? --> 아니다. 다른거일수도 있잖아!
    Weapon* weapon = item;

    Weapon* weapon1 = new Weapon();
    Item* item = weapon;

    delete item;
    delete weapon;
    

    Item* inventory[20] = {};
	srand((unsigned int) time(nullptr));
	for (int i=0; i < 20; i++)
	{
		int randValue = rand() % 2; 

		switch(randValue)
		{
			case 0:
			inventory[i] = new Weapon(); 
			break;

			case 1:
			inventory[i] = new Armor();
			break;
		}
	}
    return 0;
}

for (int i =0; i < 20; i++)
	{
		Item* item = inventory[i];
		if (item == nullptr)
			continue;

		if (item->_itemType == IT_WEAPON)
		{
			Weapon* weapon = (Weapon*)item;
			cout << "Weapon Damage: " << weapon->_damage <<endl;
		}

	}
```

### Shallow Copy vs Deep Copy

### Casting

### Resource
- [Inflearn: UnrealEngine Game Dev](https://www.inflearn.com/course/%EC%96%B8%EB%A6%AC%EC%96%BC-3d-mmorpg-1)

### Source Code 
- [Dynamic_Allocation](https://github.com/sjang1594/self-study/tree/master/game_dev/cpp/dynamic_allocation)
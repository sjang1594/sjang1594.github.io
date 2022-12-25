---
title: Objected Orietned Programming in C++
layout: post
category: study
tags: [c++]
---

### Obejcted Oriented Programming
Objected Oriented Programming 이란 객체지향 프로그래밍을 의미하며, 기존에 있던 절차지향 프로그래밍 같은경우에는 코드가 분산되서, readability 도 떨어지면서, 사용자에게 배려하는 느낌이 전혀 없어진다. 근데 객체지향에서의 귀찮은 점도 존재한다. 예를들어서 "참, 두세줄이면 끝날 코드인데, 꼭 이렇게 까지 내가 해야할까?" 라는 생각도 들수도 있다. 하지만 객체 지향을 통해서 사용자의 편의성을 극대화 하며, 사용자의 실수를 최대한 제작자가 차단을 해야한다라는 가정하에 객체지향적 프로그래밍을 해야한다.

일단 바로 코드로 넘어가자. 일 단 아래와 같이 Knight 에 대한 간단한 class 를 생성했다. class 생성할떄 Modify 할수 있는 조건이있는데 그게 바로 `public` 과 `private` 이있다. 그 이외에건 지금은 생략하고, Inheritance 에서 더 자세하게 설명을 할건데. 지금은 `public` 은 공공으로 사용할수 있는 변수나 함수(method) 라고 하자. `public` 으로 기본으로 지정된 Member Variable 과 Methods 가 존재한다. 

생각을해보자 클래스라는건 빵틀이라고 생각하면 된다. 예를들어서 Knight 이라는 틀은 기본적으로 Health bar, Attack Attributes, and its position 을 들고 있을거다. 그리고 움직일수도있고, 공격할수도 있고, 죽을수도 있다. 그렇게해서 여러개의 Knight 을 만들수 있을것이다. 이제 구현부에 대해서 이야기 하자. Member Function 또는 Method 같은 경우는 구현부를 `Knight` class 안에다가 구현할수 있으며, 또는 `Knight::Attack` 이렇게 구현할수 있는데, 이말은 Knight 클래스 안에 속해 있는 함수다라는 말이다. 똑같은 함수인 `move` 가 있다고 보여지는데, 하나는 `Knight::Move` 이고 다른 하나는 parameter 로 Knight 의 주소값을 가져온다고 보여진다. `void Move(Knight*)` 이 signature 같은 경우, 다른 Knight 를 instantiate 했을때 사용할수 있고, `Knight::Move` 그 객체가 들고 있는 built-in 함수라고 생각하면 된다.

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
앞에서 말했듯이, 클래스에 '소속'된 함수들을 Member Functions 또는 Methods 라고 한다. 이중에 특별한 친구들이 있다. 바로 `[시작]` 과 `[끝]` 을 알리는 함수들이 있다. 즉 탄생과 소멸을 칭하는 `생성자` 가 있고 `소멸자` 가있다. 생성자 같은 경우 여러가지로 존재할수 있고, 소멸자는 단 1개만 가능하다. 생성자같은 경우 그냥 틀이기 때문에 return 값이 없다.

바로 코드를 봐보자. 기본적으로 생성자를 만들때에는 `Knight()` 라는 생성자를 만들면서, 주로 Member Variable 을 초기화 시켜주는 역활을 한다. 방금 전 생성자는 여러개의 생성자가 존재할수 있다고 했다. 초기에 parameter 를 받을수 있는 생성자가 있을수도 있고(기타 생성자), 그리고 다른 객체를 Copy 할수 있는 생성자가 될수도 있고, 그리고 타입 변환 생성자인 경우도 있다.

아래와 같이 봐보면, `Knight()` 기본 생성자 같은 경우 member variable 을 세팅 하는걸 볼수 있고 그 기타 생성자 같은 경우는, 객체를 생성할때 parameter; hp, attack, posX and posY 값을 받아오는 생성자가있다.

Copy Constructor(복사 생성자)는 생성자는 생성자인데, 자기 자신의 참조 타입을 인자로 받는다. 클래스를 생성할때, input 값을 받을때, 자기 자신을 받는다고 생각하면 된다. 즉 이 복사 생성자를 만들때는, '똑같은' 데이터를 지닌 객체가 생성되길 원할때, 복사 생성자를 만든다고 생각하면된다.

아래의 코드에 K2 를 생성할때 보자. K1 을 인자로 Copy Constructor 로 인해서 k2 생성해준다. 결과적으로 클론을 하는거나 마찬가지이다. 그렇다면 복사생성자가 없다는 가정하에 k2(k1) 를 빌드 했었을때, 빌드가 된다. default 로 암시적으로 복사생성자가 만들어진다고 생각하면 된다. 그렇다면 왜 명시적으로 만들까? 만약에 인자로 참조값이나 포인터로 요구하는 인자값이 들어갔으면 어떻게할까? 라는 질문에 해답이 있다.

잠시 코드 아래에 k4 를 생성하는것과 k3 를 생성하는것을 보자. 엄연히 같게 보이지만, 서로 다른 역활을 하고 있다. k4 는 기본생성자로 만들졌고, k1 에다가 k4 를 복사 한다고 생성하고, k3 같은 경우 생성을 하는 동시에 복사를 한다. 즉 k3 는 복사생성자로 호출 되는거고, k4 는 기본생성자로 만들어준다음에, 복사를 하는거다.

생성자를 지금 까지 봐보았는데, 이게 생성자를 명시적으로 만들지 않으면, 암시적(implicit) 생성자가 된다. 즉 아무 인바도 받지 않는 [기본 생성자]가 컴파일러에 의해 자동으로 만들어진다. 그러나, 명시적(explicit) 으로 아무생성자 하나 만들면, 자동으로 만들어지던 [기본 생성자] 는 더이상 만들어지지 않는다. 아래의 코드를 실행했을때 `main` 에 있는 knight instantiate 했을때 기본생성자를 만들지 못하게 된다. k5 같은 경우 명시적으로 만든 생성자가 call 하게 된다.

마지막으로 잠깐 언급했던 기타 생성자를 봐보자. 기타 생성자 같은 경우 앞에 말했다싶이 여러가지 인자를 받으면서 객체를 생성하는것으로 볼수 있었다. 그중에 인자를 1개만 받는 기타 생성자는 `타입 변환 생성자` 라고 한다. Type Conversion Constructor 같은 경우에는, hp 를 넣어주는거에 더불어, k5 = 1 이라고 만들면 객체를 생성할수 있다. 하지만 여기서 암시적으로 생성된 생성자가 문제가 생긴다. 왜냐하면 k5 = 1 은 우리가 원치 않을수도 있기 때문이다. 그래서 타입변환 생성자에 `explicit` 즉 명시적인걸로 막아줘야한다. 즉 명시적으로 call 할때도 `k5 = (knight)1` 이런식으로 해야 더 코드가 명료해진다고 볼수 있다.

```c++
class Knight
{
public:
    // Constructor.
    Knight()
    { 
        cout << "Knight() 기본생성자 called" << endl;
        _hp = 100;
        _attack = 10;
        _posX = 0;
        _posY = 0;
    }

    // Type Conversion Constructor  
    // explicit!
    explicit Knight(int hp)
    {
        cout << "Knight(int ) called" << endl; 
        _hp = hp;
        _attack = 10;
        _posX = 0;
        _posY = 0;
    }
    
    // Etc Constructor
    Knight(int hp, int attack, int posX, int posY)
    {
        _hp = hp;
        _attack = attack;
        _posX = posX;
        _posY = posY;
    }
    
    // Copy Constructor
    Knight(const Knight& knight)
    {
        _hp = knight._hp;
        _attack = knight._attack;
        _posX = knight._posX;
        _posY = knight._posY;
    }
    
    // Destructor
    ~Knight(){cout << "Knight() 소멸자 called" << endl;}

    void Move(int y, int x);
    void Attack();
    void Die(int hp)
    {
        this->_hp = 0;
        cout << "Die" << endl;
    }

public:
    int _hp;
    int _attack;
    int _posX;
    int _posY;
};

int main()
{
    Knight k1;
    k1._hp = 100;
    k1._attack = 20;

    // 1) Copy Constructor
    Knight k2(k1);
    
    // 2) Copy Constructor
    Knight k3 = k1;

    // 3) Copy Constructor
    Knight k4;
    k4 = k1;

    // 4) explicit
    Knight k5(10);

    // 5) Type Conversion Constructor
    // implicit version -> compliler will automatically switch
    int num = 1;
    float f = num; // explicit version float f = (float)num;

    Knight k6;
    k6 = 1; // ? 

    return 0;
}
```

### Inheritance
객체 지향 프로그래밍에서 중요한 속성들이 있는데 아래와 같다.
1. 상속성 
2. 은닉성
3. 다형성

만약 지금까지 배워온거라고 한다면, 클래스는 하나의 설계도 인데, 그러면 여러가지 instance 를 만들어야한다고 가정했을때, 똑같은 데이터 같은경우는 struct 로 관리하면 된다고 치지만, 똑같은 기능이 있는 클래스도 다시 만들어줘야하느냐? 라는 질문도 할수 있다. 그렇다고 한다면, 뭔가 설계도를 더 계층 구조로 짜면 어떨까? 라는 질문에서 비롯된게 상속성(Inheritance)을 볼수있다. 여기에서는 상속성(Inheritance)를 살펴보자.

상속이라는 단어는 결국 부모가 있고, 그 자식에게 유산을 물려주는것으로 볼수 있다. 즉 기능등을 물려줄수 있다고 한다. 아래의 코드를 봐보자. 클래스에서 상속을 받고 있다 라는 문법을 쓰자면 `class Knight : public Player` 이렇게 사용할수 있는것으로 볼수 있다. 즉 Player 의 member variable 과 functions 를 상속받을수 있게된다. 그렇다면 궁금할수 있는게, 메모리에 어떻게 잡혀질까? 라고 궁금해 할수 있다. 메모리 관점에서 보면 [ Kinght ] 안에 [ Player ] 가 있다고 생각하면 된다.

코드를 잠깐 봐보면, 일단 부모님에서 정의 한 method 를 Knight 에서 재정의 해서 사용할수 있다는것을 볼수 있고, 부모님의 본래의 함수를 call 을 하려면, k::Player::Move() 라고 사용할수 있을거다.

```c++
class Player
{
public:
    Player(){ _hp=0; _attack=0, _defence=0; cout << "player constructor" << endl; }
    Player(int hp){ _hp = hp; }
    ~Player(){ cout << "player destructor" << endl; }
    void Move() { cout << "Player " << endl; }
    void Attack() { cout << "Player Attack" << endl; }
    void Die() { cout << "Player Die " << endl; }

public:
    int _hp;
    int _attack;
    int _defence;
};

class Knight : public Player
{
public:
    Knight() {
        _stamina=0;
        cout << "Knight Constructor" << endl;
    }
    Knight(int stamina) : Player(100)
    {
        _stamina=stamina;
        cout << "Knight Constructor" << endl;
    }
    ~Knight() {cout << "Knight Desturctor" << endl; }

    // redefined : 부모님의 유산을 거부하고 새로운 이름으로 만듬
    void Move() { cout << "Knight Move" << endl; }
public:
    int _stamina;
};

class Mage : public Player
{
public:
    int _mp;
};

int main()
{
    Knight k;
    k._hp = 100;
    k._attack = 20;
    k._defence = 10;
    k.Attack();
    k.Player::Move(); // player move (parent)
    k.move(); // knight move (child)
    return 0;
}
```

그렇다고 한다면, constructor / destructor 측면에서 한번 다시 생각해보자. constructor 같은 경우 여러개의 constructor 을 생성할수 있고, destructor 같은 경우 하나만 존재한다는 언급을 했었다.

그렇다면 위의 코드를 한번 봐보자, 일단 child 나 parent 의 기본 생성자와 소멸자를 만들었다. 그렇다면 궁금즘은 이거다 생성자는 class 가 instantiate 했을때, 또는 탄생했을때 호출되는 함수라고 했었다. 그렇다고 한다면 `Knight` 를 생성했을때, `Player` 의 생성자가 호출이 될지 `knight` 의 생성자가가 호출 될지 궁금증이 생긴다.
결론적인 답은 둘다 호출하자 이렇게 생성이된다. 그리고 생성이되는 순서는 부모님 먼저 호출이 되고 그다음에 child 가 호출이 된다음에 소멸될때에는 자식이 먼저 호출이 되고, 그다음 부모님이 호출이 된다고 볼수 있다.

### Hiding

### Polymorphism

### Initializing the List

### Operation Overloading

### Resource
- [Inflearn: UnrealEngine Game Dev](https://www.inflearn.com/course/%EC%96%B8%EB%A6%AC%EC%96%BC-3d-mmorpg-1)

### Source Code
- [Objected Oriented Programming in C++](https://github.com/sjang1594/self-study/tree/master/game_dev/cpp/opp)
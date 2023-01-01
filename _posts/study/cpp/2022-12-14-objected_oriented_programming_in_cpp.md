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

좀더 자세하게 child class 의 생성자가 언제 call 되는 영역이 어딘지 확인해보자. 아래와 같이 볼수 있다. 일단 Child 가 Instantiate 했을때, Knight 의 생성자 `Knight()` 이거나 `Knight(int stamina)` 가 call 이되면서, 선처리 영역에서 부모의 생성자가 호출이 된다. 그래서 부모인 `Player()` 가 호출이 되고 `cout` 으로 생성자가 호출 됬다는걸 확인 할 수 있다. 생성자와 달리 소멸자같은 경우는, `~Knight()` 가 호출이 되고, 즉 child 가 호출이 된다음, 후처리 영역에서 Parent 인 `~Player()`  소멸자가 호출 되는걸 볼수 있다. 그리고 추가해야할 문법은, 부모님의 생성자를 다른걸 선택? 하고 싶으면
`Knight(int stamina) : Player(100)` 이런식으로 해서 선처리 영역에서 `Player(int hp)` 를 호출 하게끔 하면 된다.

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
        /*
         * 선(처리) 영역
         * - 여기서 Player() 생성자 호출
         */
        _stamina=0;
        cout << "Knight Constructor" << endl;
    }
    Knight(int stamina) : Player(100)
    {
        //

        /*
         * 선(처리) 영역
         * - 여기서 Player() 생성자 호출
         */
        _stamina=stamina;
        cout << "Knight Constructor" << endl;
    }
    ~Knight() {cout << "Knight Desturctor" << endl; }
    /*
     * 후처리영역
     * - 여기서 Player() 소멸자 호출
     */
    void Move() { cout << "Knight Move" << endl; }
public:
    int _stamina;
};

int main()
{
    Knight k;
    return 0;
}
```

결국에는 상속을 쓰면, 코드가 간결해지고 가독성이 높아진다는걸 알수 있다.

### Hiding

Hiding 은 한마디로 은닉성(Data Hiding) 또는 Encapsulation 이라고 한다. 여기서 이야기하는건 데이터의 권한 문제라고 생각하면 된다. 그렇다면 왜 숨기고 이걸 보호 해야하냐 라는 질문을 할 수 있다.
대표적인 이유는 중 하나는 정말 위험하고 유저가 함부러 건드리면 안되는 경우가 있고, 나머지 하나는 다른 경로로 접근하길 원하는 경우가 있다.
예를 들어서, 자동차가 있다 유저가 실제로 보고 작동할수 있는건, Handle, Excel Pedal, and Break 가 있다. 물론 자동차를 관리하는 사람들을 제외 하고, 일반인들은 엔진이나 엔진에 묶여있는 와이어를 손을 덴다고 하면, 차가 쉽게 망가지기 마련이다. 어떤부분은 유저들에게 안보여지게 하고, 다른 부분들은 보여지는거다.
그러면 이런것을 어떻게 문법으로 적용을 할것인가? 라는 질문을 할수있다. 이걸 `접근 지정자` 라고 한다. 접근지정자 같은 경우 아래 세가지가 있고, 그에 관한 설명이 있다. 코드를 한번봐보자.

- public    : 누구한테나 실컷 사용하세요
- protected : 나의 자손들한테만 허락
- private   : 나만 사용할께 (즉 자신 내부에서만)

```c++
class Car
{
public: // 접근 지정자
    void MoveHandle() {}
    void PushPedal() {}
    void OpenDoor() {}

    void TurnKey(){ RunEngine(); }

protected:
    void DisassembleCar() {}
    void RunEngine() {}
    void ConnectCircuit() {}
};
```
위의 코드 같이, `MoveHandle`,`PushPedal`,`OpenDoor`,`TurnKey` 같은 경우는 유저가 자동차의 겉표면? 쉽게 사용할수 있는 기능들이다. 하지만 `DisassembleCar`, `RunEngine`, `ConnectCircuit` 같은 경우는 `private` 으로 class 내부에서만 사용할수 있지만, 상속을 받을수 있기 때문에 protected 로 보호할수있다. 또 `TurnKey()` 내부 함수에서 `protected` 로 지정된 함수를 call 할수 있게 해놓았다.

```c++
class Car
{
public: // 접근 지정자
    void MoveHandle() {}
    void PushPedal() {}
    void OpenDoor() {}

    void TurnKey(){ RunEngine(); }

protected:
    void DisassembleCar() {}
    void RunEngine() {}
    void ConnectCircuit() {}
};

class SuperCar : public Car // 상속 접근 지정자
{
public:
    void PushRemoteController(){ RunEngine(); }
};

int main()
{
    Car car;
    return 0;
}
```

그렇다면 위에서 이야기 했던 상속 부분을 좀 더 생각해보자. 접근 지정자가 있다고 한더라면, 상속 접근 지정자를 빼먹을수 있다.
상속 접근 지정자 같은 경우, 다음 세대에 어떻게 부모님의 유산을 어떻게 물려줄지? 가 테마라고 생각하면된다. 즉 부모님한테 물려받은 유산을
꼭 나의 자손한테도 똑같이 물려줘야하지 않는다는 뜻이다. 멤버 접근 지정자처럼 상속 접근 지정자에 대한 설명을 해볼까 한다.

- pubilc    : 공개적으로 상속? 부모님의 유산 설계 그대로! (public -> public / protected -> protected)
- protected : 보호받는 상속? 내 자손들한테만 물려줄꺼야!  (public -> protected / protected -> protected )
- private   : 개인적인 상속? 나까지만 잘쓰고 -> 자손들에게 아예 안물려 줄꺼야! (public -> private / protected -> private)

아래의 코드를 한번 봐보자. 일단 SuperCar 라는 클래스는 Car 로 부터 private 으로 상속받았기 때문에 만약 SuperCar 라는 상속받은 아이는
Car 에 대한것을 접근할수 있다. 즉 SuperCar는 자기까지만 욕심많게 상속을 받고 물려주지 않은것으로 보여진다. 이 코드에서 만약 상속 접근 지정자를 안했을 경우
private 으로 인식하게 된다.

```c++
class SuperCar : private Car // 상속 접근 지정자
{
public:
    void PushRemoteController(){ RunEngine(); }
};

class TestSuperCar : SuperCar
{
    void Test()
    {
        DisassembleCar(); // Cannot access
    }
};

class SuperSuperCar : private Car
{
public:
    void PushRemoteController(){ RunEngine(); }
};


class TestSuperSuperCar : public SuperSuperCar
{
public:
    void Test() { /* .. Can't call DisassembleCar(); */}
};
```


이유중에 2번째: `다른 경로로 접근` 이라는게 있다. 이거에 대한 예를 들어보자. 아래의 코드를 보면, main 함수에서
버서커를 instantiate 한다음에, _hp를 바꾸는데, 버서커모드의 출력창이 안나온다. 그 이유는 일단 _hp 를 접근해서 바꾸는건 위험하고
또 다른건 클래스는 그냥 틀에 불과 하기 때문에 설계를 잘못했다고 말을 할수 있다. 그래서 이 부분에서 `encapsulation` 에 대한 이야기를
할까 싶다. 캡슐화는 한마디로 `연관된 데이터와 함수를 논리적으로 묶어 놓은것`이라고 볼수 있다.


```c++
class Berserker
{
public:
    void SetBerserkerMode(){ cout << "Getting Stronger" << endl; }
public:
    int _hp = 100;
};

int main()
{
    Berserker berserker;
    berserker._hp = 10;
}
```

Encapsulate 된 클래스 구조를 코드로 확인 해보자. 일단 _hp 를 쉽게 건들수 없게 `private` 으로 막아놓으면, 일단 외부에서는
접근을 못하게 막아 놓았다. 주로 member variable 을 가지고 나올때는 getter 와 setter 을 쓰기 때문에, `GetHp()` 와 `SetHp()`
를 만들어준다. 그래서 일단 우리가 만들고 싶은거는 뭔가 hp 가 세팅이 됬을때, 버서커모드로 될지 안될지를 체크를 해주면 된다. 또 외부에서
버서커 모드를 키게 하면 안되니까 `private` 으로 막아줬다.

```c++
class Berserker
{
public:
    int GetHp() { return _hp; }
    void SetHp(int hp)
    {
        _hp = hp;
        if (_hp <= 50) SetBerserkerMode();
    }

private:
    int _hp = 100;
    void SetBerserkerMode(){ cout << "Getting Stronger" << endl; }
};

int main()
{
    Berserker berserker;
    berserker.SetHp(20);
    return 0;
}
```

### Polymorphism
Polymorphism 이라는건 결국 다양한 형태로 존재 한다 라고 생각하면 된다. 즉 쉽게 말해서 겉은 똑같은데, 기능이 다르게 동작한다고 말할수 있다. 두가지로
대표적으로 2 가지를 말을 할수 있다.

1. 오버로딩(Overloading) = 함수 중복 정의 = 함수 이름의 재사용
2. 오버라이딩(Overriding) = 재정의 = 부모 class method 를 사용해서 자식클래스에서 재정의

잠깐 오버로딩에 대해서 이야기를 해보자. 바로 코드를 보겠다. 아래는 `Move()` 라는 함수를 이용해서 같은 이름이지만 signature 이 다른 함수인
`Move(int)` 로 함수를 중복 정의 한걸 볼수 있다. 이게 바로 대표적인 오버로딩에 대한 예이다. 이와같이 오버로딩은 되게 간단하다고 볼수있다.

```c++
class Player
{
public:
    Player() {_hp = 100;}
    void Move(){cout << "Move()" << endl;}
    void Move(int step){cout << "Move(int)" << endl;}
};

int main()
{
    Player player;
    player.Move();
    player.Move(20);
    return 0;
}
```

오버라이딩 같은 경우가 굉장히 polymorphism 에서 중요한 부분인데 한번 알아보자. 아래와 같이 오버라이딩에 대한 간단한 예라고 볼수 있다
부모 클래스인 `Player()` 에서 상속받은 `Knight` 나 `Mage` 같은 경우 `Move()` 함수를 재정의 해서 사용한걸 볼수있다.

```c++

class Player()
{
public:
    void Move(){ cout << "Move() " << endl; }
public:
    int _hp;
};

class Knight : public Player
{
public:
    Knight() {_stamina = 100; }
    void Move(){ cout << "Knight Move()" << endl; }

public:
    int _stamina;
};

class Mage : public Player
{
public;
    void Move() {cout << "Mage Move()" << endl; }
public:
    int _mp;
};

int main()
{
    Knight k;
    k.Move();

    Mage m;
    m.Move();
    return 0;
}
```

상속받아서 하는 클래스를 설계하는건 아주 중요한 스킬중에 하나인데, 그중에 또하나의 장점이 있다. 아래의 코드를 봐보자. Move 라는 기능의 함수를 클래스 별로 만들었다.
여기에서 만약에 `MoveKnight()` 안에 player 의 주소값을 넣어주면 어떻게 될까? 호환이 되지 않는다. 일단 기존에 `PlayerMove()` 안에 넣었던걸 번역?을 하자면,
플레이어는 플레이어다라고 말을 할수 있는데, 플레이어가 기사냐라고 물어봤을때, 지금 계층 구조에서는 의미가 맞지 않는다. 즉 플레이어는 Mage 일수도 있고, Knight 도 될수도 있다.
그러면 그 반대의 케이스로 `MovePlayer()` 안에 Knight 의 주소값을 넣어줬다고 하면 어떨까? 앞의 해석에 의해서 빌드가 된다. 그렇다면 해석을 구지 하자면, Knight 는 Player 가 맞다.
바로 이 점을 사용해서, MoveKnight() 나 MoveMage() 함수를 따로 안만들어주고, MovePlayer() 로 관리 할수 있게된다. 상속관계를 잘알게 된다면, 확실히 코드가 간결해진다.

그렇다면, 여기서 더나아가서 MovePlayer() function 만 사용한다고 했을때, 과연 어떤 클래스에서 `Move()` method 를 사용할까? 라는 의문점이든다.
실행을 해보면, 부모안에 있는 `Move()` 가 실행되는걸 확인 할수 있다. 그러면 이게 문제가 된다. overriding 을 사용해서 Knight `Move()` 를 만들었는데.. 라고 물을수 있다.
그 이유는 바로 `Binding(바인딩)` 이라는 개념과 연관된다.

`Binding(바인딩)` 은 결국 어떤걸 묶는다라는 걸 볼수 있는데, 정적 바인딩과 동적 바인딩이 있다. 아래의 정의를 잠깐 봐보자

- Static Binding(정적 바인딩)  : compiler 시점에 결정
- Dynamic Binding(동적 바인딩) : run time 에 결정

주로 일반함수는 정적바인딩에 속한다. 즉 MovePlayer() 가 compiler 에서 봤을때는 Player 의 주소값을 받는 타입이 있으니까, 원본데이터가 Knight 였을지여도, Player 의
`Move()` 함수가 실행되는거다. 그렇다면 이걸 어떻게 해결할까? 는 예상대로 동적바인딩을 사용하면 된다. 그렇다면 동적 바인딩을 사용하려면 조건이 필요하다.
virtual(가상) 함수가 필요하다.

```c++
class Player()
{
public:
    void Move(){ cout << "Move() " << endl; }
public:
    int _hp;
};

class Knight : public Player
{
public:
    Knight() {_stamina = 100; }
    void Move(){ cout << "Knight Move()" << endl; }

public:
    int _stamina;
};

class Mage : public Player
{
public;
    void Move() {cout << "Mage Move()" << endl; }
public:
    int _mp;
};

void MovePlayer(Player* player)
{
    player->Move();
}

void MoveKnight(Knight* knight)
{
    knight->Move();
}

void MoveMage(Mage* mage)
{
    mage->Move();
}

int main()
{
    Player p;
    p.Move(&p);
    Kngiht k;
    k.Move(&k);
    return 0;
}
```

가상함수를 사용하려면 어떻게 사용해야할까는 method 앞에 `keyword` 를 사용하면 된다. 그렇다면 위의 코드를 조금 정리해서 봐보자.
일단 동적바인딩을 사용해서, `VMove()` 그리고 `VAttack()` 을 만들었다. 상속관계에서 virtual function 을 사용하면, virtual 함수인거다.


```c++
class Player
{
public:
    Player() {_hp =100 ;}
    virtual void VMove() { cout << "VMove" << endl;}
    virtual void VAttack();
public:
    int _hp;
};

class Knight : public Player
{
public:
    Knight() {_stamina = 100; }
    virtual void VMove() { cout << "VMove Knight" << endl;}
    virtual void VAttack(){cout << "VAttack Knight" << endl;}
public:
    int _stamina;
};

void MovePlayer(Player* player)
{
    player->VMove();
}

int main()
{
    Knight k;
    MovePlayer(&k);
    return 0;
}
```

앞에서 본건 구현방법이였다. 하지만 더 자세하게 보려면 어셈블리를 까봐서 어떻게 구현되어있는지 정확하게 필요가 있다. 일단 break point 를 걸어서 실행을 해보면
Knight 앞 메모리에 뭔가가 추가 되었다는게 보인다. 즉 이 추가된게 가상함수의 어떤 플래그라는걸 알수있다. 즉 실제 객체가 어떤 타입읹지 어떻게 알고
있어서 가상함수를 호출하는지를 찾아보면, 바로 가상함수 테이블(vftable) 이라는게 존재해서 그렇다. 그러면 가상함수 테이블에서 잠깐 보면
가상함수 테이블(.vftable) 는 32 bit 에서는 4 바이트를 차지하고, 64 bit 에서는 8 바이트를 차지한다. 메모리 구조에서는 [VMove][] 즉 테이블 주소로 되어있다는 거다.
즉 가상함수 테이블을 통해서 가상함수들을 관리 한다는걸 확인할수 있다. 그렇다면 가상함수를 쓰는 주체는 누구인가? 라는 질문도 할수 있다. 정답은 생성자에서 한다.
생성자의 선처리 영역에서 vftable 을 채워넣는다.

signature 만 가지고 있는 가상함수를 순수 가상함수라고 하는데, 이 가상함수는 구현은 없고 `interface` 만 전달하는 용도로 사용하고 싶을때 사용된다
순수 가상함수를 만들었을 경우, 빌드를 시켰을때, 그 method 가 있는 클래스 abstract class 가 된다. 여기서 abstract class 가 뭐냐고 묻는다면, 순수 가상함수가
1 개이상 존재하거나 포함되면 바로 추상클래스로 간주되고, 직접적으로 객체를 instantiate 하지 못하게 된다.

순수 가상함수일경우에는 그 가상함수를 표현할때 `virtual void Attack() = 0` 이런식으로 표현한다. 모던 c++ 에서는 `virtual void Attack() abstract` 라고 표현된다.
이렇게 순수가상함수가 표현되면, 거의 무조건 상속받는 친구들은 무조건 재정의가 필요해 이렇게 말을하는거다.

### Initializing the List
초기화를 하는 이유는 여러가지가 있다. 일단 초기화를 통해서 디버깅도 쉬어지고, 또한 초기화를 함에 따라서 어떤 값이 들어갔는지 확인이 가능하다. 즉 버그를 예방을 할수 있고, 포인트나 주소값이 연루 되어있다고 한다면 더더욱 중요시 생각해야한다. 아래의 코드를 한번 봐보자. 일단 `k._hp` 를 출력 한다고 가정하면, 엉뚱한 메모리값을 가지고 있다는걸 확인 할수 있다. 이렇게 초기화를 안한 상태에서, if statement 로 넘어간다면, 이제 Knight 가 죽었다는 사실을 들고 있다. 이런 실수를 방지 하고자 Initializing 을 할 필요가 있다.

```c++
#include <iostream>
using namespace std;
class Knight
{
public:
    int _hp;
};

int main()
{
    Knight k;
    cout << k._hp << endl;
    if (k._hp < 0 )
    {
        cout << "Knight is Dead" << endl;
    }
    return 0;
}
```

초기화 방법은 여러가지가 있지만, Object Oriented Programming 관점에서의 초기화는 일단 생성자 안에서 초기화를 하는 방법이 있고, 그리고 초기화 리스트가 있으며, c++11 에서 추가된 문법이 있다. 이거에 대해서 더 상세 하게 이야기를 할려고 한다. 일단 아래의 코드를 보자. `Knight` 클래스는 `Player` 클래스로 부터 상속을 받았고, 생성자에서 부모 클래스의 초기화를 했고, 또한 Knight 클래스의 member 변수인 `_hp` 를 100 으로 초기화 한걸 볼수있다. 또한 `Knight` 생성자 내에서 멤버 변수인 `_hp` 도 `_hp = 100` 이런식으로 초기화가 가능하다. 

C++11 에서는 바로 class 내부에서 `int _hp = 100` 으로 설정이 가능하다.

```c++
class Player
{
public:
    Player(){}
    Player(int id){}
};

class Knight : public Player
{
public:
    Knight() : Player(1), _hp(100)
    // 선처리 영역 // 
    {

    }

public:
    int _hp;
};
```

일단 초기화 리스트 같은경우, 상속 관계에서 원하는 부모를 생성자 호출할때 필요하다. 더나아가서 생성자내에서 초기화를 하는게 있고, 초기화 리스트의 비교를 따로 해보자. 일단 일반 변수 같은경우는 별 차이가 없으며, 만약 멤버 타입이 클래스인 경우 차이가 난다.

일단 이걸 더 판별하기 위해서, `Is-A(Knight Is-A Player?)` 와 `Has-A(Knight Has-A Inventory)` 스스로에게 질문을 해보면 된다. 아래의 코드를 한번 봐보면 `Is-A` 같은 경우는 기사는 플레이어다 라고 생각해서 맞다고 하면, 상속관계 이다. 또 다른 예를 찾아보면 `Is-A` 를 사용해서 기사는 인벤토리냐 라고 묻는다면, 상속관계가 아닌 포함관계라는걸 볼수 있다. 큰그림을 그려보자면, 이렇게 생각하는 이유는 처음에 코드를 설계할때의 유용하기 때문이다.

또 여기서 문제가 될게 있다. 만약 생성자 내부안에서 Inventory 를 만들어서 초기화를 할 경우, 각 다른 생성자를 한번씩 한번씩 호출이되고, 소멸자는 두번이 호출된거를 볼수 있는데, 멘붕이 올수 있다. 이부분은 선처리 영역에서 `Inventory` 를 만들었는데 생성자에 들어와서, 기존에 있던 기본 생성자를 날려버리고 `Inventory(int)` 의 생성자로 덮어씌우는 동시에 소멸자가 호출되면서, 코드가 끝나게 되면, 다시 소멸자가 호출이된다. 이럴 경우에는 애초에 선처리영역에서 아래와 같이 초기화를 하는걸 볼수 있다.

```c++
class Inventory
{
public:
    Inventory(){ cout << "inventory()" << endl; }
    Inventory(int size){ _size = size; }
    ~Inventory(){ cout << "~Inventory()" << endl; }
public:
    int _size = 10;
};

class Player
{
public:
    Player(){}
    Player(int id){}
};

class Knight : public Player
{
public:
    Knight() : Player(1), _hp(100), _inventory(20)
    // 선처리 영역 // 
    // inventory() // 
    {

    }

public:
    int _hp;
    Inventory _inventory;
};
```

또 정의함과 동시에 초기화가 필요한 경우가 있다. 주로 참조 타입이나 const 타입일 경우가 있다. 아래의 코드를 봐보자. 일단 테스트를 위해서, `_hpRef`,`_hpConst` 가 있다해보자. Knight 클래스 내부에서 생성자에서 저 두 멤버변수를 바꾼다고 해도 의미가 없어진다. Const 같은 경우는 바꿀수 없는거고, Reference 는 누군가 하나를 가르키고 있어야 하는건데, 이미 Knight 클래스가 생성이 될시 즉 선처리영역에서 이미 했기때문에 다른값으로 수정이 불가능하다. 그래서 하고 싶을 경우에는 마찬가지로 선처리 영역에서 하면된다.

```c++
class Inventory
{
public:
    Inventory(){ cout << "inventory()" << endl; }
    Inventory(int size){ _size = size; }
    ~Inventory(){ cout << "~Inventory()" << endl; }
public:
    int _size = 10;
};

class Player
{
public:
    Player(){}
    Player(int id){}
};

class Knight : public Player
{
public:
    Knight() : Player(1), _hp(100), _inventory(20), _hpRef(_hp), _hpConst(100)
    // 선처리 영역 // 
    // inventory() // 
    {
        _hpRef = _hp; // 안됨
        _hpConst = 100; // 안됨
    }

public:
    int _hp;
    Inventory _inventory;
    int& _hpRef;
    const _hpConst;
};
```

### Operation Overloading


### Resource
- [Inflearn: UnrealEngine Game Dev](https://www.inflearn.com/course/%EC%96%B8%EB%A6%AC%EC%96%BC-3d-mmorpg-1)

### Source Code
- [Objected Oriented Programming in C++](https://github.com/sjang1594/self-study/tree/master/game_dev/cpp/opp)

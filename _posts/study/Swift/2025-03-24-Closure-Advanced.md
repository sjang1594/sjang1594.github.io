---
title: Closure Advanced
layout: post
category: study
tags: [swift, mobile dev]
published: true
---

## Closure Advanced 
마침 Closure => Functor (Lambda Expression), Capture 이 부분이 생각보다 까다롭지 않을까? 싶었는데, 완전 C++ Syntax 가 똑같다. 단지 어떤 타입에 따라서 복사를 하는가에 따라서 다르다. (ex: C++ 에서 는 & (reference) 로 보낼지, 그냥 복사 Capture로 부를지를 `[]` or `[&]` 이런식으로 사용할수 있다, 하지만 swift 에서는 struct 는 value type 이므로 => 복사, class 처럼 reference type 이면, 주솟값을 넣어주는 형태) 

### Escaping Closure
이 부분을 이해하기위해서는 함수의 끝남! 을 잘 알아야한다. 예를 들어서 어떤 함수에서, closure() 가 바로 실행된다고 한다고 하자. 우리가 기대하고 있는거는 함수가 실행되고, closure 가 실행되는 방식으로 한다고 하자. 그러면 잘 작동이 될거다. 하지만 만약 비동기 처리가 이루어진다면 어떻게 되는걸까? 함수안에 내부 closure 는 실행이 될때까지 기다리고 있지만, 이미 그함수는 끝난 상태가 되버릴수있다. 그러면, 함수 내부에서 비동기 처리가 되는거가 아닌, 어떤곳에서 (ex: `main`) 에서 비동기 처리가 될거다. 그러면 빠져나가지도 못하는 상황이 되버린다. 이걸 방지할수 있는방법이 바로 `@escaping` 이라고 보면 된다. 기본적으로 closure 는 non-escaping 이다.

아래의 코드를 봐보자, 3 초 이후에 DispatchQueue 에서 비동기를 실시를 할건데, 이때 바로 들어가야하는게 `@escaping` keyword 이다. 즉 어떤 함수의 흐름에서, closure 가 stuc 한 부분을 풀어줘야 closure 의 끝맺음이 확실하다는것이다. (물론 함수 주기는 끝나게 된다.) 참고로 `@Sendable` Keyword 를 안쓴다면 Error 를 표출할것이다. 그 이유중에 하나는 일단 compleition (closure type) 은 referance type 이며, 이것을 비동기처리내에서 사용하려면, Thread Safe 라는걸 보장을 해야하는데, compiler 에서는 모른다. 그래서 명시적으로 Type 을 지정해줘야한다.

```swift
func performAfterDelay(seconds: Double, completion: @escaping @Sendable () -> ()) {
    DispatchQueue.main.asyncAfter(deadline: .now() + seconds) {
        completion()
    }
}
print("before")
performAfterDelay(seconds: 3, closure: {
    print("Hello")
})
print("after")
```

그리고 closure 측면에서는, 파라미터로 받은 클로저는 변수나 상수에 대입할수 없다. (이건 알아야 하는 지식중에 하나다, 가끔씩 compiler error 가 안날수도 있다.) 중첩 함수 내부에서, 클로저를 사용할 경우, 중첩함수를 return 할수 없다. 즉 함수의 어떤 흐름이 있다고 하면, 종료되기 전에 무조건 실행 되어야 한다는것이다. 근데 또 특이 한점 하나가 있다. 아래의 코드를 잠깐 봐보자.

```swift
func performAfterDelay(seconds: Double, completion: (@Sendable () -> Void)?) {
    DispatchQueue.main.asyncAfter(deadline: .now() + seconds) {
        completion?()
    }
}
```

자 거시적으로 봤을때는 closure 에 return 값을 기대할수도 있고, 없을수도 있다. 그걸 Optional(?) type 을 사용했다. Optional 을 사용한다고 하면, optional type argument 이기때문에 이미 `escaping` 처리가 될것이다. 라고 말한다. 즉 closure type 이 더이상 아니다. 그래서 자동적으로 escaping 한다고 보면 될것 같다. 

### Capture Ref & Caputer Value
이게 해깔릴수 있으니 정리를 해보자 한다. 일단 바로 코드 부터 보는게 좋을것 같다. 일단 Value Type 인 Struct 를 사용해서 구현을 해본다고 하자. 일단 Struct 가 Type 이 Value Type 이니까? 당연히 Capture 을 하면, 당연히 복사가 이뤄지기때문에 값이 안바뀐다고 생각은 할수 있다. 하지만, closure capture 자체가 기본이 변수의 메모리값을 참조 하기 때문에, person.age 의 주솟값을 reference 로 받기때문에 closure capture 가 reference 형태로 되는것이다. 그 아래의 것은 copy 다. 이건 capture 할 list 를 넘겨주는데, 이건 closure 가 생성하는 시점의 값을 하나 강하게 들고 있다고 볼수 있다. (즉 capture 한 값을 가지고 있다는것) 그러기때문에 capture list 를 사용할때는, 값으로 들어가기때문에 변경되지 않는다. `참고로 weak 를 사용하게 된다면, compiler 에서는 class 또는 class-bound protocol-types 라고 말할것이다. 즉 reference 타입일 경우에만 사용 가능 하다.`

```swift
struct Person {
    var name: String
    var age: Int
}

func captureRefTest() {
    var person = Person(name: "John", age: 30)
    var closure = {
        print(person.age)
    }
    
    closure()
    person.age = 40
    closure()
}

captureRefTest()

func captureCopyTest() {
    var person = Person(name: "Nick", age: 20)
    var closure = { [person] in
        print(person.age)
    }
    
    closure()
    person.age = 40
    closure()
}

captureCopyTest()
```

그렇다면 class 는 어떨가? 이건 애초에 가정이 reference type 이다. 그러기 때문에 애초에 값참조를 하지 않는다. 그러기때문에 Capture list 를 사용하더라도 reference 처럼 작동을 한다.

```swift
class Animal {
    var name: String
    var age: Int
    
    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }
}

func captureTest() {
    var animal = Animal(name: "Dog", age: 10)
    var closure = { [weak animal] in
        print(animal!.age)
    }
    
    closure()
    animal.age = 20
    closure()
}
captureTest()
```
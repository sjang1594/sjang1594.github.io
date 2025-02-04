---
title: Struct & Class
layout: post
category: study
tags: [swift, mobile dev]
published: true
---

## Intro to Struct vs Class in Swift

OPP 에서 중요한건 Class 사용 및 Struct 사용이다. Swift 에서 Struct 와 Class Type 들을 봐보겠다.

CPP 와는 비슷한면도 있고, 다른점도 있다. Swift 에서의 Struct 와 Class 는 아래의 특징을 가지고 있다.

**Struct**
* Stack 에 저장 
  * 메모리 할당 해제가 빠름 => Thread-Safe
  * 크기 자체는 Compile Time 에 결정
* inheritable X
* Data Usage

**Class (C++ Class 와 유사)**
* Heap 에 저장 
  * 메모리 오버해드 발생 => not Thread-Safe
  * [ARC](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting/#:~:text=Swift%20uses%20Automatic%20Reference%20Counting,think%20about%20memory%20management%20yourself.) 가 관리(Ref Count)
  * Virtual Memory 와 비슷, Paging 을 거쳐서, 주소값 조사 및 저장할곳을 정함, 그리고 메모리 할당해제 했을때, Memory Management Unit 업데이트를 해줘야함.
  * 크기 자체는 Run Time 에 결정
* inheritable
* Final Keyword 사용 가능

**Overall**
* 위와 같은 특징으로 인해서? Class 가 느릴수도 있지만, 관리 측면에서는 역시 Class 가 좋고, 그리고 Struct User Data Type 으로 사용하면 될것 같다.
---

## Intro to protocol

Swift 공식 홈페이지에서의 프로토콜의 정의는 아래와 같다.
```
A protocol defines a blueprint of methods, properties, and other requirements  that suit a particular task or piece of functionality. The protocol can then be adopted by a class, structure, or enumeration to provide an actual implementation of those requirements. Any type that satisfies the requirements of a protocol is said to conform to that protocol.
```

즉 결국엔 Protocol 이라는건 Enum, Struct, Class 의 어떤 Blueprint 에 해당되며, 이 Protocol 을 사용하기위해서는 어떠한 어떠한것들이 필요하다는걸 정의하는 것이다. 즉 요구사항 정리서 (Descriptor) 라고 볼수 있다. 그리고 구현은 Struct 나 Class 에서 직접하면 된다.

### Example

**Struct Example**
* CPP 와 비슷 하게 Operator 작성하면 됨
* 일반적으로 Swift 에서는 Equatable Protocol 을 작성해야 Instance 들의 비교가 가능

```swift
struct User : Equatable{
    // define property
    var name : String
    var age : Int
    
    static func == (lhs:User, rhs: User) -> Bool{
        return (lhs.name == rhs.name && lhs.age == rhs.age)
    }
}

let user1 = User(name: "Alice", age: 21)
let user2 = User(name: "Nick", age: 32)

print(user1 == user2)
```

**Class Example**
* Init 이 결국엔 Initializer (Constructor)
* 두가지의 class instance 생성이후에 비교를 했을때에 Property 가 변경 되더라도 같지 않다. 
* `var user4 = user3` 라고 하면 copy 를 만드는게 아니라, 인스턴스를 참조 (share) 하게된다. 즉 그냥 다른 참조(Pointer) 생성될뿐이다. 그러기 때문에 `user4` 의 name 을 변경했을때, user3 도 변경된다.
* Class 내부에 === protocol 를 Built-in 으로 가지고 있어서, 굳이 Equatable 사용 안해도 됨

```swift
class User{
    // define property
    var name : String
    var age : Int
    
    init(name: String, age: Int)
    {
        self.name = name
        self.age = age
    }
}

let user1 = User(name: "Alice", age: 21)
let user2 = User(name: "Nick", age: 32)

user2.name = "Alice"
user2.age = 21

print(user2.name, user2.age)

var user3 = User(name: "Jack", age: 23)
var user4 = user3

print(user1 === user2)
print(user3 === user4)

user4.name = "Kayle"
print(user3)
```

**Protocols Example**

```swift
protocol Greetable {
    func greet() -> String
}

struct Person{
    // define property
    var name : String
    var age : Int
    
    func greet() -> String {
        return "Hello, my name is \(name). Nice to meet you!"
    }
}

class Robot{
    var id : Int
    
    init(id: Int)
    {
        self.id = id
    }
    
    func greet() -> String {
        return "Hello, my special id  \(id). Nice to meet You!"
    }
}

let person = Person(name: "Alice", age:32)
print(person.greet())

let robot = Robot(id : 4)
print(robot.greet())
```

**Protocols Extension Example**

* 약간 Overloading 이랑 비슷한것 같기는한데, 일단 Protocol 에서 정의를 했었을때, 똑같은 Protocol 을, 다른 Objects 들이 중복적으로 사용하지 않으려면 사용.

* 구현된게 우선권을 얻으므로, `Person` 과 `Robot` 은 `greet()` 정의한대로 return, `Alien` 은 구현체가 없고 Extension 된 Protocol 로 채택

```swift
protocol Greetable {
    func greet() -> String
}

extension Greetable{
    func greet() -> String{
        return "Hello"
    }
}

struct Person : Greetable{
    // define property
    var name : String
    var age : Int
    
    func greet() -> String {
        return "Hello, my name is \(name). Nice to meet you!"
    }
}

struct Alien : Greetable{
}


class Robot : Greetable{
    var id : Int
    
    init(id: Int)
    {
        self.id = id
    }
    
    func greet() -> String {
        return "Hello, my special id  \(id). Nice to meet You!"
    }
}

let person = Person(name: "Alice", age:32)
print(person.greet())

let robot = Robot(id : 4)
print(robot.greet())

let alien = Alien()
print(alien.greet())
```

### Reference 
* [Other's Blog_1](https://hasensprung.tistory.com/181)
* [Other's Blog_2](https://babbab2.tistory.com/178)
* [Swift Docs](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting/)
* [How to compare two Struct objects?](https://stackoverflow.com/questions/46074718/how-to-compare-two-struct-objects)
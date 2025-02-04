---
title: Data Structure / Memory Management / ARC
layout: post
category: study
tags: [swift, mobile dev]
published: true
---

## Data Structure & Memory Management in Swift

일단 Swift 안에서는, Array, Queue, Stack 이 Data Structure 이 있다. 뭔가 c++ 처럼 Library 를 지원 queue 나 stack 을 지원하나 싶었는데? 없다고 한다 [ref](https://medium.com/geekculture/week-5-how-can-you-still-not-know-stack-and-queue-in-swift-b583946ebd53) 그래서 직접 구현하란다. 하지만 `Deque<Element>, OrderedSet<Element>, OrderedDictionary<key, value>, Heap` 은 [Collection Package](https://github.com/apple/swift-collections) 에 있다고 한다. 흠 왜? Array 하고 Sets 는 주면서? 조금 찾아 보니, `Array`, `Set` 의 최소한의 자료구조만 표준으로 제공하고, 다른건 Pacakaging 해서 쓰란다. 그리고 생각보다 Generic 도 잘되어있지만, 역시 CPP 하고 비교했을때는 불편한점이 있긴한것같다.

### Array & Sets

* 둘다 Randomly Accessible 하다. 이 말은 `Array` 같은 경우, 순차적으로 메모리에 저장되므로, 어떤 특정 Index 에서 접근 가능. `Set` 같은 경우, Hash Table 기반으로 구현되어 있어서 `var mySet: Set = [10, 20, 30]` `.contain()` 라는 함수로 있으면 True 없으면 False return 을 한다.
* 왜? 삽입/삭제시 성능 저하? => 찾아서 지워야할텐데, Element 가 마지막이면 O(n) 이니까, 그래서 `Set` 사용하면 되겠네
* Set 과 Array 의 차이점: Set 은 `unordered` array 는 `ordered`.

**Example Code**
```swift
import Dispatch
let array = Array(1...1_000_000)
let set: Set = Set(array)
let target = 999_999

let startArray = DispatchTime.now()
print(array.contains(target)) // O(n)
let endArray = DispatchTime.now()
let nanoTimeArray = endArray.uptimeNanoseconds - startArray.uptimeNanoseconds
let timeIntervalArray = Double(nanoTimeArray) / 1_000_000_000
print("Array Execution Time: \(timeIntervalArray) seconds")

let startSet = DispatchTime.now()
print(set.contains(target)) // O(1)
let endSet = DispatchTime.now()
let nanoTimeSet = endSet.uptimeNanoseconds - startSet.uptimeNanoseconds
let timeIntervalSet = Double(nanoTimeSet) / 1_000_000_000
print("Set Execution Time: \(timeIntervalSet) seconds")

### 결과 ### 
true
Array Execution Time: 0.044636319 seconds
true
Set Execution Time: 5.1e-06 seconds
```

### Queue & Stack
* 예제 코드들 보니까, [Generic](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/generics/) 도 사용할수 있다. 그리고 Swift 에서 특별하다고 생각했던게, 요청하지 않는 한 value type 인 애들의 속성값 변경을 허용하지 않는다는거, 즉 Instance method 에서 수정할수 없다는거, 특이하구나...

**Queue**
* FIFO (First In, First Out) 구조 (ex: printer & BFS)

**Example Code**
```swift
struct Queue<T>{
    // Generic Type(T) Array
    private var elements : [T] = []

    mutating func enqueue(_ value: T) {
        elements.append(value)
    }

    // std::optional T (null)  | swift (nil)
    mutating func dequeue() -> T? {
        // exception
        guard !elements.isEmpty else {
            return nil
        }
        return elements.removeFirst()
    }

    var head : T? {
        return elements.first
    }

    var tail : T? {
        return elements.last
    }
    
    func printQueue(){
        if elements.isEmpty {
            print("Queue is Empty")
        } else {
            print("Current Queue: \(elements)")
        }
    }
}

var queue = Queue<String>()
queue.enqueue("Nick")
queue.enqueue("Kayle")
queue.enqueue("Juan")

queue.printQueue()

if let serving = queue.dequeue() {
    print(serving) // Optional("Nick")
}
if let nextToServe = queue.head { //Optional("Kayle")
    print(nextToServe)
}

queue.printQueue()
```

**Stack**
* LIFO (Last In, Last Out) 구조 (call stack)

**Example Code**
```swift
struct Stack<T>{
    // Generic Type(T) Array
    private var elements : [T] = []

    mutating func push(_ value: T) {
        elements.append(value)
    }

    // std::optional T (null)  | swift (nil)
    mutating func pop() -> T? {
        // exception
        guard !elements.isEmpty else {
            return nil
        }
        return elements.popLast()
    }
    
    var top: T?{
        return elements.last
    }
    
    func printStack(){
        if elements.isEmpty{
            print("Stack is Empty")
        } else {
            print("Stack: \(elements)")
        }
    }
}

var cookieJar = Stack<String>()
cookieJar.push("chocolate")
cookieJar.push("walnut")
cookieJar.push("oreo")

cookieJar.printStack()

if let popItem = cookieJar.pop() {
    print(popItem)
}

cookieJar.printStack()

if let topItem = cookieJar.top {
    print(topItem)
}
```

### Memory Management in Swift
* IPhone 이라는 어떤한 Device 를 놓고 봤을때, Storing Data 의 방법은 두가지 있을것 같다.

1. Disk
2. RAM

* 만약 App 을 실행시킨다고 했을때, executable instructions 이 RAM 에 올라가고, system OS 에서 RAM 의 덩어리 일부분(Heap)을 Claim 하면서, App 을 실행시킨다. 그래서 앱에서 실행시키는 모든 Instance 들이 Life cycle 을 가지게 된다. C/CPP 에서도 마찬자기로 malloc / new / delete heap 영역에서의 memory management 를 프로그래머가 해주니까 뭐 말이된다.
* Swfit 에서는 Memory Management 는 [ARC](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting/) 에서 해준다.**결국에는 모든 Instance 들이 reference count 라는걸 가지고있고, 그 reference count 는 properties, constants, and variable 들에 strong reference 로 잡혀져 있다. 그래서 ref count 가 0 일이 될때 메모리 해제된다! 완전 Smart Pointer 잖아!** 또 궁금한게, Garbage Collection 이라는 Keyword 도 무시할수 없는건데, 이것도 [전부다 ARC 에서 한다고 한다](https://www.reddit.com/r/swift/comments/2pdabd/how_does_garbage_collection_work_in_swift/) 그리고 Ownership 도 생각해봐야할 문제 인것 같다.

### Reference -> Coupling -> Dependency

* Reference 를 생각하고 개발하다보면, 결국에 오는건 Coupling / Dependency / Circular Dependency 문제이다. 그래서 C++ 에서는 Interface 사용하거나, `weak_ptr` 사용해서, Strong Count 를 안하게 하는 방법이 있다.
* swift 에서는 Weak Reference 나 Unowned Reference 를 사용한다고 한다. 바로 예제코드를 보자.

```swift
class Person {
    var name: String
    var pet: Pet? // optional 
    init(name: String)
    {
        self.name = name
    }
    
    deinit {
        print("\(name) is destructed")
    }
}

class Pet {
    var name: String
    var owner: Person? // optional 
    
    init(name: String)
    {
        self.name = name
    }
    
    deinit {
        print("\(name) is destructed")
    }
}

var person: Person? = Person(name:"Nick")
var pet: Pet? = Pet(name: "Jack")

// Circular Dependency
person?.pet = pet
pet?.owner = person

person = nil
pet = nil
```

* 와 근데 아무런 Error 안나오는게 사실이냐...? 아니면 Online Compiler 라서 그런가보다 하고 넘기긴했는데.. 좋지는 않네. 뭐 근데 정확한건, deinit() 호출 안되니까 해제가 안됬음을 확인할수 있다.

* 해결하려면, `weak` 키워드 사용하면 된다. 아래의 코드를 보자.
```swift
class Pet {
    weak var owner: Person?
}
```
* 이걸로 변경하면, 서로의 deinit() 호출되면서 Nick 먼저 해제, 그 다음 Pet 해제 형식으로 된다. 

* 다른 하나방법은 `unowned` 키워드 사용하면 된다.
```swift
class Pet{
    unowned var owner: Person
}
```

### Difference Between `Unowned` and `weak`
* weak 는 Optional 이고, Optional 일 경우에는 Unwrapped 을 해줘야한다.(이말은 Optional 값이 nil 이 아닐 경우에 Safe 하게 unwrap 해줘야하는거) 참조된 객체가 해제되면 nil 로 설정된다. 즉 객체가 해제 되어야하는 상황에 쓸것이다.
* unowned 는 Optional 이 아니다. 그리고 참조된 객체가 해제되면 RunTime Error 가 발생한다. (즉 이말은 unowned reference 는 항상 Value 를 갖기를 원한다. = 이거 좋음), weak 와 다르게 unowned unwrap 할필요가없다. 항상 Value 를 가지고 있기 때문이다.
* 자세한건 [What Is the Difference Between Weak and Unowned References in Swift](https://cocoacasts.com/what-is-the-difference-between-weak-and-unowned-references-in-swift)

```swift
class Person {
    var name: String
    init(name: String) {
        self.name = name
    }
    
    deinit {
        print("\(name) is destructed")
    }
}

class Pet1 {
    var name: String
    weak var owner: Person?  // weak 참조는 옵셔널 타입

    init(name: String, owner: Person?) {
        self.name = name
        self.owner = owner
    }
    deinit {
        print("\(name) is destructed")
    }
}

class Pet2 {
    var name: String
    unowned var owner: Person
    init(name: String, owner: Person) {
        self.name = name
        self.owner = owner
    }
    deinit {
        print("\(name) is destructed")
    }
}

var person: Person? = Person(name: "Nick")
var pet1: Pet1? = Pet1(name: "weak dog", owner: person!)
var pet2: Pet2? = Pet2(name: "unowned dog", owner: person!)

// safe unwrap
if let owner = pet1?.owner {
    print(owner.name) 
}

print(pet2!.owner.name) 

person = nil
pet1 = nil
pet2 = nil
```

### Resource
* [Data Structure in Swift](https://benoitpasquier.com/data-structure-implement-queue-swift/)
* [Mutating KeyWord](https://seons-dev.tistory.com/entry/Swift-%EA%B8%B0%EC%B4%88%EB%AC%B8%EB%B2%95-%EB%A9%94%EC%84%9C%EB%93%9C-2-mutating)
* [Generics in Swift](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/generics/)
* [What Is the Difference Between Weak and Unowned References in Swift](https://cocoacasts.com/what-is-the-difference-between-weak-and-unowned-references-in-swift)
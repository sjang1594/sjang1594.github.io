---
title: Closure & OOP in swift
layout: post
category: study
tags: [swift, mobile dev]
published: true
---

## Closure & OOP

### Closure 을 알기 이전에...

C++ 에 있는 Function Type 을 이해하면 편하다. Swift 에서도 Function Type 이 존재한다. 아래의 코드를 보면 Function Type Declaration 이 존재한다. `(Int, Int) -> Int` 하고 addTwoInts 라는 함수를 참조한다. (여기에서 **참조**). 즉 swift 가 할당을 허락한다. 라는 뜻. 저 불편한 var 로 할당된걸, 함수로 표현하게 되면, `(Int, Int) -> Int` 자체를 함수의 Parameter 로 넘겨줄수도 있다.

```swift
// Function Type Example

func addTwoInts(_ a: Int, _ b: Int) -> Int {
    return a + b
}

func multiplyTwoInts(_ a: Int, _ b: Int) -> Int {
    return a * b;
}

func printHelloWorld() {
    print("hello, world")
}

var mathFunction: (Int, Int) -> Int = addTwoInts
print("Result : \(mathFunction(2, 3))")

func printMathResult(_ mathFunction: (Int, Int) -> Int, _ a: Int, _ b: Int) {
    print("Result: \(mathFunction(a, b))")
}
```

그리고 다른 함수의 반환 타입으로 함수 타입을 설정할수 있다. 반환하는 함수의 반환 화살표를 `->` 사용해서 함수타입으로 사용할수 있다.

```swift
// Function Type Example

func stepForward(_ input: Int) -> Int {
    return input + 1
}
func stepBackward(_ input: Int) -> Int {
    return input - 1
}

func chooseStepFunction(backward: Bool) -> (Int) -> Int {
    return backward ? stepBackward : stepForward
}

var currentValue = 3
let moveNearerToZero = chooseStepFunction(backward: currentValue > 0)
```

여기서 `(Int)` 라는 chooseStepFunction 안에 있는 함수의 Return 을 의미하고, Parameter 는 Boolean 값으로 넘겨주며, return 을 그 다음 화살표인 `Int` 로 한다는 뜻 이다.

아직 코드가 간결하지 않다, Nested 함수로 해보자. 함수안에 함수를 작성하는게 불필요할수도 있지만, Closure 을 이해하기전에 필요한 정보이다. 아래의 코드를 보면, currentValue > 0 이면 False 를 반환하고, chooseStepFunction(backward) 가 stepForward 함수를 반환한 이후, 반환된 함수의 참조값이 moveNearerToZero 에 저장된다.

```swift
func chooseStepFunction(backward: Bool) -> (Int) -> Int {
    func stepForward(input: Int) -> Int { return input + 1 }
    func stepBackward(input: Int) -> Int { return input - 1 }
    return backward ? stepBackward : stepForward
}

var currentValue = -4
let moveNearerToZero = chooseStepFunction(backward: currentValue > 0)

while currentValue != 0 {
    print("\(currentValue)... ")
    currentValue = moveNearerToZero(currentValue)
}
```

### Closure in Swift

C++ 에서 Closure 라고 하면, 주로 Lambda Expression (Lambda) 를 Instance 화 시켰다고 볼수있다. 즉 위에서 본것 처럼, swift 에서도 똑같은 의미를 가지고 있다. 자 중첩함수에서 본것 처럼 `chooseStepFunction` 이라는 함수 이름이 존재했다. 그리고 값을 (=) 캡쳐해서 `currentValue` 를 Update 하였다. `closure 는 결국 값을 캡처할수 있지만, 이름이 없는게 Closure 의 개념이다.`

Closure 의 Expression 은 아래와 같다. `(<#parameters#>) -> <#return type#>` Closure 의 Head 이며, `<#statements#>` 는 Closure 의 Body 이다. Parameter 와 Return Type 둘다 없을수도 있다.

```swift
{ (<#parameters#>) -> <#return type#> in
   <#statements#>
}
```

주의점이 하나 있는데, 예를들어서 아래의 코드를 본다고 하자. 첫번째 print 를 했을때는 `"Hello, Nick"` 이라는게 나온다. 하지만 두번째 Print 에서는 `error: extraneous argument label 'name:' in call
print(closure(name: "Jack"))` 라는 Error 가 뜬다. Closure 에서는 argument label 이 없다. 이 점에 주의하자. 일반 함수 Call 과 다르다. 여기에서 또 봐야할점은 Closure Expression 을 상수에 담았다.(***)

```swift
let closure = { (name: String) -> String in
    return "Hello, \(name)"
}

print(closure("Nick"))
print(closure(name: "Jack"))
```

그리고 Function Type 을 이해했다라고 한다면, Function Return Type 으로 Closure 을 return 할수 있으며, 함수의 Parameter Type 으로도 Closure 가 전달이 가능하다. 여기서 첫번째로는 아까 그냥 함수를 작성할때와는 다르게 Argument Label 이 없어야한다고 하지 않았나? 근데 실제 Arugment Label 이 없으면 `missing arugment label 'closure'` 이라는 Error 를 내뱉는다. 즉 에는 Argument Label 이 Parameter 로 전달됬다는걸 볼수 있다. 그리고 return 같은 경우는 위의 Function Type 을 이해했다면 충분히 이해할수 있는 내용이다.

```swift
// function Type: Closure as Parameter
func doSomething(closure: ()->()){
    closure()
}

doSomething(closure: {() -> () in print("Hello!")
})

// function Type: Closure as Return
func doSomething() -> () -> () {
    
    return { () -> () in
        print("Hello Nick!")
    }
}

var closure = doSomething()
closure()
```

클로져의 용도는 간단하면서 복잡한데, 주로 Multithreading 에서 안전하게 State 관리를 하기 쉽다. 하지만 관리 하기 쉽다는건 항상 뭔가의 Performance 가 조금 Expensive 하다는 점이다. 조금 더 자세한걸 알면 Functor 를 보면 될것 같다.

### Closure Example Code
```swift
// Closure 
let numbers = [1,3,5,7,9]
let doubled = numbers.map { $0 * 2 } // m
print(doubled)

var counter = 0
let incrementCounter = {
    counter += 1
}
incrementCounter()
incrementCounter()
print(counter) // 출력: 2
```

### OOP 
OOP 는 생각보다 간단하다. 객체 지향적이라는 말이긴한데. 결국엔 Class 로 Instance 들을 쉽게 관리한다라는 말이다. 반댓말로는 절차 지향적이라는 말이 있다.

원칙의로는 Encapsulation, Inheritance, Polymorphism, Abstraction 있다.

```swift
class Animal {
    var name : String
    
    init(name : String){
        self.name = name
    }

    func makeSound(){}
}

class Dog : Animal {
    override func makeSound(){
        print("Bark!")
    }
}

class Cat : Animal {
    override func makeSound(){
        print("Meow!")
    }
}

let cat = Cat(name: "jack")
cat.makeSound()

let dog = Dog(name: "Nick")
dog.makeSound()
```

### Reference
* [swift](https://bbiguduk.gitbook.io/swift/language-guide-1/functions)
* [Blogs](https://babbab2.tistory.com/81)
* [cpp-closure](https://leimao.github.io/blog/CPP-Closure/)
---
title: MultiThreading & Generic
layout: post
category: study
tags: [swift, mobile dev]
published: true
---

## MultiThreading & Generic in Swift

어떤 Language 가 됬든 일단 방대한 Data 를 Loading 을 해야하거나, 어떤 통신에 맞물려서 상태 return 받을 때 main thread 에서 모든걸 하게 되면, Performance 가 떨어진다. Swift 에서는 이걸 어떻게 해결하는지, 동작 방법 및 실제 구현해서 App 에서 어떻게 Profiling 을 하는지도 봐보자.

### GCD (Grand Centeral Dispatch)
일단 Multithreading 을 알기 이전에 [Grand Central Dispatch](https://en.wikipedia.org/wiki/Grand_Central_Dispatch) 에 대한 용어 부터 보자. wiki 에서 나와있는것 처럼 multi-core processor 와 other symmetric multiprocessing system 을 최적화하는걸 support 하기위해서 만들어졌고, Thread Pool Pattern 으로 Task 기반으로 병렬화를 진행한다. Thread Pool Pattern 생소할수 있는데, Thread Pool 은 결국에는 Thread(일용직) 들을 위한 직업 소개소라고 생각하면 된다. 여러개의 Thread ~~가~~ 대기 하고 있다가 할 일이 들어오면, 대기했던애가 들어와서 일(실행) 하게 되는거라고 볼수 있다. Thread Pool 은 Queue 기반으로 만들면된다. 그래서 Swift 에서는 DispatchQueue 를 사용해서 이를 해결한다. 쉽게 말해서 Task 에 대한 병렬 처리 또는 (비)동기 처리 를 총괄하는 것이 GCD 라고 볼수 있다. 아래의 그림을 보면 간략하게 GCD 가 뭔지를 대충 알 수 있고, `DispatchQueue`, `DispatchWorkItem`, `DispatchGroup`(thread group?) 등을 볼수 있다. (참고: [Ref](https://medium.com/@ayshindhe/simplifying-grand-central-dispatch-gcd-in-swift-cc3d4f681c43))

<img style="display: block; margin: auto;" src="../../../assets/img/photo/2-06-2025/image.png"/>

GCD 에서 제공 하는 Thread 를 살짝 살표 보자면 Main(Serial) 은 UiKit 이나 SwiftUI 의 모든 요소를 담당한다고 볼수 있고, Global(Concurrent) 같은 경우는 system 전체에서 공유가 되며, 병렬적으로 실행되지만 [QoS](https://developer.apple.com/documentation/dispatch/dispatchqos) 따라서 prioirity 를 지정할수 있다.

Priority 위의 그림에서 Interactive 가 Highest Priority 를 가지고, 아래로 갈수록 우선순위가 낮아진다. (참조: [Energy Efficiency Guide for iOS Apps](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/PrioritizeWorkWithQoS.html)) 참조한글을 보면 Use Case 별로 아주 잘 나와있다.

### DispatchQueue
Apple Developer Doc 에 찾아보다 보니 DisptchQueue 라는걸 이렇게 설명한다. `An ojbect that manages the execution of tasks serially or concurrently on your apps main thread on a background` 마치 [QT](https://www.qt.io/) 하고 비슷한 역활을 하는구나라고 볼수 있다. DispatchQueue 는 결국엔 어떤한 work 에 해당되는 item 들이 있다보면, 그 work 의 실행을 Thread Pool 에 넘겨서, executuion 된다고 볼수 있다. 

Thread 를 이야기할때는 내가 짠 프로그램이 Thread Safe 한지를 Check 를 해야하는데, 이 DispatchQueue 는 Thread-Safe 한다고 한다. (즉 Thread 들이 한곳에 접근 가능하다는 뜻이다.)

위에 GCD Image 를 보면 Serial 과 Concurrent 로 나눠지는데, 

### Reference
* [Simplifying Grand Central Dispatch (GCD) in Swift](https://medium.com/@ayshindhe/simplifying-grand-central-dispatch-gcd-in-swift-cc3d4f681c43)
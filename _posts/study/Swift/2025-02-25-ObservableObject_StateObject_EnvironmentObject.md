---
title: ObservableObject, StateObject, EnvironmentObject
layout: post
category: study
tags: [swift, mobile dev]
published: true
---

### Before we start
Let's review the `@State` keyword. In order for View to notice, that the value of @State change, the View is re-rendered & update the view. This is the reason why we can see the change of the value in the View. 

### StateObject & ObservableObject
Now, let's talk about `StateObject` & `ObservableObject`. If we have a ViewModel, called `FruitViewModel`, as below. Let's review the code. 
FruitViewModel is a class that conforms to `ObservableObject` protocol. It has two `@Published` properties: `fruitArray` & `isLoading`. This viewmodel will be instantiated in the `ViewModel` struct. This FruitViewModel also controls the data flow between the View and the ViewModel. Then we have navigation link to the `SecondScreen` struct. Then, we pass the `FruitViewModel` to the `SecondScreen` struct. In the `SecondScreen` struct, we have a button to go back to the `ViewModel` struct. In the `SecondScreen`, this can access the FruitViewModel's properties (which in this case, fruitArray mainly). 

There are two ways to instantiate the `FruitViewModel`. One is using `@StateObject` and the other is using `@ObservedObject`. For `@StateObject`, it's used for the object that is created by the View. For `@ObservedObject`, it's used for the object that is shared across the app. This means you can still use `@ObservedObject` for the object that is created by the View, but if it's observableobject, it's not going to be persisted. meaning the data will be changed when the view is changed. So, it will change everytime the view is changed where this wouldn't be our case. So, that's why we use `@StateObject` to keep the data persistence. 

```swift
class FruitViewModel : ObservableObject {
    @Published var fruitArray: [FruitModel] = [] // state in class (alert to ViewModel)
    @Published var isLoading: Bool = false
    
    init() {
        getFruits()
    }
    
    func getFruits() {
        let fruit1 = FruitModel(name: "Banana", count: 2)
        let fruit2 = FruitModel(name: "Watermelon", count: 9)
        
        isLoading = true
        DispatchQueue.main.asyncAfter(deadline: .now() + 3.0){
            self.fruitArray.append(fruit1)
            self.fruitArray.append(fruit2)
            self.isLoading = false
        }
    }
    
    func deleteFruit(index: IndexSet) {
        fruitArray.remove(atOffsets: index)
    }


struct ViewModel: View {
    @StateObject var fruitViewModel: FruitViewModel = FruitViewModel()
    
    var body: some View {
        NavigationView {
            List {
                if fruitViewModel.isLoading {
                    ProgressView()
                    
                } else {
                    ForEach(fruitViewModel.fruitArray) { fruit in
                        HStack {
                            Text("\(fruit.count)")
                                .foregroundColor(.red)
                            Text(fruit.name)
                                .font(.headline)
                                .bold()
                        }
                    }
                    .onDelete(perform: fruitViewModel.deleteFruit)
                }
            }
            .listStyle(.grouped)
            .navigationTitle("Fruit List")
            .navigationBarItems(
                trailing: NavigationLink(destination: SecondScreen(fruitViewModel: fruitViewModel), label: { Image(systemName: "arrow.right")
                    .font(.title)})
            )
        }
    }
}
}

struct SecondScreen : View {
    @Environment(\.presentationMode) var presentationMode
    @ObservedObject var fruitViewModel: FruitViewModel
    var body: some View {
        ZStack {
            Color.green.ignoresSafeArea()
            VStack {
                Button(action: {
                    presentationMode.wrappedValue.dismiss()
                }, label: {
                    Text("Go Back")
                        .foregroundColor(.white)
                        .font(.largeTitle)
                        .fontWeight(.semibold)
                })
                
                VStack {
                    ForEach(fruitViewModel.fruitArray) { fruit in
                        Text(fruit.name)
                            .foregroundColor(.white)
                            .font(.headline)
                    }
                }
            }
        }
    }
}
```

### EnvironmentObject

EnvironmentObject is a bit same as `@ObservedObject`. The difference is that it's used for the object that is shared across the app. This means you can still use `@ObservedObject` for the object that is created by the View, but if it's observableobject, only the subview can access the data. But if you use `EnvironmentObject`, the data will be shared across the app. Obviously there is downside to this, which means it's slower than `@ObservedObject`. So if we have a hierchical structure, we can use `EnvironmentObject` to share the data across the app. (if only needed). So that the child view can access the data from the parent view. Otherwise, you can easily use `@ObservedObject` and pass this to child view. 

The example code is as below

```swift
//
//  EnvironmentObject.swift
//  SwiftfulThinking
//
//  Created by Seungho Jang on 2/25/25.
//

import SwiftUI

// What if all child view want to access the Parent  View Model.
// Then use EnvironmentObject.
// You can certainly do pass StateObject / ObservedObject, but what
// if you have a hierchy views want to access the parent views.
// but might be slow
class EnvironmentViewModel: ObservableObject {
    @Published var dataArray: [String] = []
    
    init() {
        getData()
    }
    
    func getData() {
        self.dataArray.append(contentsOf: ["iPhone", "AppleWatch", "iMAC", "iPad"])
    }
}

struct EnvironmentBootCampObject: View {
    @StateObject var viewModel: EnvironmentViewModel = EnvironmentViewModel()
    
    var body: some View {
        NavigationView {
            List {
                ForEach(viewModel.dataArray, id: \.self) { item in
                    NavigationLink(
                        destination: DetailView(selectedItem: item),
                        label: {
                            Text(item)
                        })
                }
            }
            .navigationTitle("iOS Devices")
        }
        .environmentObject(viewModel)
    }
}

struct DetailView : View {
    let selectedItem: String
    var body: some View {
        ZStack {
            Color.orange.ignoresSafeArea()
            
            NavigationLink(
                destination: FinalView(),
                label: {
                    Text(selectedItem)
                        .font(.headline)
                        .foregroundColor(.orange)
                        .padding()
                        .padding(.horizontal)
                        .background(Color.white)
                        .cornerRadius(30)
                })
        }
    }
}

struct FinalView: View {
    @EnvironmentObject var viewModel: EnvironmentViewModel
    var body: some View {
        ZStack {
            LinearGradient(gradient: Gradient(colors: [.blue, .red]),
                           startPoint: .topLeading,
                           endPoint: .bottomTrailing)
            .ignoresSafeArea()
            
            ScrollView {
                VStack(spacing: 20) {
                    ForEach(viewModel.dataArray, id: \.self) { item in
                        Text(item)
                    }
                }
            }
            .foregroundColor(.white)
            .font(.largeTitle)
        }
    }
}
```

### At the end...

Why do we use `StateObject` & `EnvironmentObject`? It's matter of the lifecycle of the object as well as the MVVM Architecture. The MVVM Architecture is a design pattern that separates the UI, the data, and the logic. The `StateObject` is used for the object that is created by the View. The `EnvironmentObject` is used for the object that is shared across the app.

### Resource






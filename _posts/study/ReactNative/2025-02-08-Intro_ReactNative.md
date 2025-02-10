---
title: Introduction to React Native
layout: post
category: study
tags: [react native, mobile dev]
published: false
---

## React Native

### React Native 시작 및 동기부여

사실 Interactive Web 을 사용하고 싶었고, 뭔가 항상 가지고 있었던, Front-end 는 별로야. 너무 볼것도 많고, 디자인 할것도 많고, Core Value 가 없어보여.. 이런말만 했었는데, 요즘은 Spatial Computing 이 되게 중요하지 않나? 라고 생각해서 

### Setting up IOS Dev on Windows

이 부분은 굉장히 까다로웠다. 일단 기본적으로 환경설정을 고려할때, 굳이 macOS 를 Base 로 쓰고 싶지 않았다. [VMWare 설치 및 환경설정](https://cmeaning.tistory.com/77) (단 여기서, .iso file 은 unlocker 에 있는 .iso) 파일을 설치하도록 하자. 그리고 [Resolution Setting](https://sihloh4me.tistory.com/508) 여기를 확인해보자. 가끔씩 VMWare 가 금쪽이 같은 면 이있지만 App 을 Build 하고 코드 작성하는데 크게 문제가 있지는 않은것 같다. 그리고 XCode 를 혹시 모르니까 설치를 해놓자. 설치하는데 시간을 뻇기는건 어쩔수 없는거긴 하지만, 너무 비효율적이고, 길어진다. 인터넷 같은 경우에는 VMWare Player 세팅에서, `NAT: Used to share the host's IP address` 만 해놓으면 괜찮다. 

그리고 부가적으로, [Homebrew](https://brew.sh/) 를 설치하자. `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`. 그이후에 `https://reactnative.dev/docs/set-up-your-environment?os=macos&platform=ios` 여기에서 Environment 를 설정해주자. 그리고 아래의 Commands 로 확인을 해보자.

```
node - v
nvm - v
npm - v

vim ~/.zprofile

# add
export NVM_DIR="$HOME/.nvm"
[ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \. "/opt/homebrew/opt/nvm/nvm.sh"  # This loads nvm
[ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && \. "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"  # This loads nvm bash_completion

source ~/.zprofile 

nvm install --lts
node - v
nvm - v
npm - v
```

## Resource
* [Youtube](https://www.youtube.com/watch?v=wxaCOleAumk&list=PL60Uti4nULBN7EQYmgjksXJXnkufo0m-9&index=3)
---
title: dev-setting rust
layout: post
category: study
tags: [rust]
published: false
---

## Rust 개발환경 Setting
### Motivation
진짜 swift 해보고, Rust 도 개발 환경 세팅을 하려고 하는데, 확실히 macOS 뭔가 마음에 안들지만, 그래도 swift 나 react-native 의 강한 dependency 가 있다보니 정리를 해보는데, 설치 부터 약간 기분이 나쁜점이 있었고, 블로그도 너무 중구난방해서, 그걸 해결하고자 작성한다. 

### Basics.

Rust 공식 홈페이지에서 Cmd line 으로 설치
> curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

`rustup`: Rust 의 Version Manager (ex: conda, pyenv)
`cargo` : Rust Pacakage Manager for Project 
`clippy`: Rust Code Linter
`rust-doct`: rust doc
`rust-std`: rust standard library
`rustc`: rust complier

* 잘 설치가 되었다면, version check 및 env 에 잘들어갔는지 확인

```bash
rustc --version // rustc version
export source PATH="$HOME/.cargo/bin:$PATH" 
```

* Rust Compiler 잘 작동하는지 확인

```Bash
vi test.rs

$echo 'fn main() {
    println!("Hello, world!");
}

rustc test.rs
./test // Hello, world!
```

Visual Studio Code Extension Installation
- rust-analyzer
- CodeLLDB
- TOML Language Support (Even Better TOML)

Visual Studio Code Setting.json
```Json
// go to setting.json (for user and workspace), then insert this
    {
    "rust-analyzer.linkedProjects": [
        "./Cargo.toml",
        ]
    }
```
Also, click the rust-analyzer in VSExtension, then click `Settings`

add this into setting.json (user) can be right below "explorer.confirmDelete":false

```
"rust-analyzer.restartServerOnConfigChange": true,
"rust-analyzer.runnables.extraEnv": {"PATH": "${env:HOME}/.cargo/bin:${env:PATH"}}
```

then you can run it with rust-analyzer via Command Pallet->`rust-analyzer:Run`

find `everywhere` keyword in `setting.json`. Click `Debug:Allow Breakpoints Everywhere`. Then, you can enable the debug point on source code via vscode.

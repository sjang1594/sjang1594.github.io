---
title: Game Engine - Build System Generator
layout: post
category: study
tags: [build system generator]
published: True
--- 

내가 Build System 을 고려하다가 정리를 해본다.

| 특징            | Premake                                                  | CMake                                                    |
|----------------|---------------------------------------------------------|---------------------------------------------------------|
| 목적           | 프로젝트 파일 생성 (주로 IDE 지원)                        | Makefile이나 Visual Studio 프로젝트 등을 자동 생성        |
| 설정 파일 형식 | Lua 스크립트 (premake5.lua)                              | 독자적인 스크립트 언어 (CMakeLists.txt)                  |
| 언어           | Lua 스크립트 기반                                       | 자체 DSL (도메인 특화 언어)                              |
| 지원 플랫폼    | Windows, macOS, Linux                                   | 대부분의 플랫폼 및 툴체인 지원                           |
| 생성 파일      | Visual Studio, Xcode, GNU Make, Code::Blocks, gmake 등   | Visual Studio, Xcode, Ninja, Makefile 등 다양한 빌드 시스템 지원 |
| 학습 곡선      | Lua를 알고 있다면 비교적 간단                            | 자체 문법 학습이 필요, 복잡한 구조일 때 난이도 증가       |
| 사용 사례      | 게임 엔진, 그래픽 라이브러리 등 주로 C++ 프로젝트에 사용 | 오픈소스 프로젝트, 다양한 플랫폼 지원이 필요한 프로젝트    |
| 설정 방식      | Lua 스크립트를 통해 논리적 설정 가능                     | 선언형으로 프로젝트 기술, 간단하지만 복잡한 설정은 코드가 길어짐 |
| 빌드 속도      | 비교적 빠름                                             | Ninja와 같은 고속 빌드 툴과 함께 사용 가능                |
| 커뮤니티와 문서 | 상대적으로 작음                                         | 커뮤니티가 크고 문서가 방대                             |

#### **지원 플랫폼 및 유연성**
- **Premake:** 주로 Visual Studio, Xcode, GNU Make를 타겟으로 사용하며, 게임 엔진이나 그래픽 라이브러리 개발에 많이 사용됩니다.
- **CMake:** 거의 모든 플랫폼과 빌드 시스템을 지원합니다. 특히 `Ninja`와 함께 사용할 때 빌드 속도가 매우 빠릅니다.
####  **생태계와 커뮤니티 지원**
- **Premake:** 게임 엔진 및 일부 그래픽 라이브러리에서 주로 사용됩니다. 대표적으로 **LunaEngine**이나 **Unreal Engine**에서 사용합니다.
- **CMake:** 오픈소스 프로젝트에서 표준으로 사용됩니다. 예를 들어 **LLVM**, **Qt**, **OpenCV** 등이 CMake를 사용
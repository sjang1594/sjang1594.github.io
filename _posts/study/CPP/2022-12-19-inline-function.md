---
title: Inline Function
layout: post
category: study
tags: [c++]
published: true
---

### Inline Function

가끔씩 코드를 쓰다보면, 가독성과 최적화를 동시에 잡아야할 필요가 있다. 이럴때 C++ 에서는 대표적으로 inline 함수를 쓸수 있다. 바로 코드를 봐보자.

```c++
#include <iostream>
using namespace std;

inline int min(int x, int y)
{
    return x > y ? y : x;
}

int main()
{
    cout << min(5, 6) << endl;
    cout << min(3, 2) << endl;

    cout << (5 > 6 ? 6 : 5) << endl;
    cout << (3 > 2 ? 2 : 3) << endl;
    return 0;
}
```

위의 코드를 보면 일단 `main` 함수의 2번째 줄은 function call 을 하는게 보인다. 하지만 `inline` 이라는 키워드를 쓰게 되면 구현부를 구지 function call 하지 않고, 바로 함수의 능력을 바로쓸수 있다는 장점이 있다. 하지만 inline 을 물론 다 함수에 붙여놓으면 이상하고, 그런다고 성능이 좋아지지는 않는다. 왜냐하면 compiler 해결하는 속도는 계속 증가하다보니까, inline 을 쓰든 안쓰든 성능 보장이 없다.
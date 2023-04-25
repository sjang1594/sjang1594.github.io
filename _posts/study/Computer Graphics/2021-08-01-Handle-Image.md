---
title: Handling image with Memory
layout: post
category: study
tags: [computer vision, computer graphics]
---

### Handling Images
Image 를 처음으로 Screen 으로 봤을때, 2D 로 보일거다. OpenCV 를 사용했었더라면, `Image Watch` 로 봤을때, 각 pixel 값이 2D image 에 잘 저장이되어 보인다고 볼수 있다. 

사실은 내부적으로 어떻게 되는지? 를 궁금해할수있다. C++ 에서의 운영체제에서는 데이터를 받을때 1차원형태로 받는다. 만약에 image 의 pixel 값이 [0, 255] 을 값을 Normalize 를 0 과 1 사이로 한다면, 한 element 에 들어가는것은 바로 float 값일거다. 그래서 `float* myImg = new [width * height]` 이런식으로 해서 Image를 1D 로 보관한다. 즉 어떻게 Indexing 하느냐에 따라서 2D 로 배열을 바꿀수 있다.

주로 기초적인 질문일수 있지만, API 를 사용하다보면 놓칠수도 있다.
왼쪽 가로축으로 시작해서 오른쪽으로 한칸 한칸 움직이고(Column), 그 다음 row 에 가서 위와 같은 방법으로 indexing 을 할 수 있다. 예를들어서 (0, 0), (1, 0), (2, 0) .. 이런식으로 가다가 두번째 row 에서는 (0, 1) (1, 1), (2, 1) .. 이런식으로 가서 맨 아래의 element 에서는 (#column, #row) 가 되는식으로 될것이다.

그렇다면 다시 거꾸로 해서, 2D image 에서 (2, 3) 이라는 데이터가 있다고 가정하자. 그리고 (2,3) 에 가서 data 를 변경 한다고 가정하면, 우리에게 주어진건 1D data 이기 때문에, 17 번째의 Index 를 찾아야한다. 어떤 인덱스 (i, j) 에서 1차원 index 를 가지고 올수 있는 방법은 `i + width * j` 이다.

가끔씩 까먹을순 있지만, 계속 생각해보길 바란다.
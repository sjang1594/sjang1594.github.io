---
title: Visual SLAM 기술 개발 동향 리뷰
layout: post
category: review
tags: [visual-slam, slam, magazine]
---
# Title : Visual SLAM 기술 개발 동향 리뷰 또는 공부

요즘 Facebook 에 Robotics KR 또는 SLAM KR 에서, 열심히 눈팅하다가 보았던 Magazine 을 회사에서 프린트를 하고 보려던 참에 눈에 들어와서 읽어보았다. 

일단 SLAM 이라는 기술은 현재 autonomous vehicles and robot 에 사용되었다. 어제만해도, 로봇 청소기가 어떻게 Mapping 을 할 수 있을지가 궁금했었는지 말이다. SLAM (Simultaneous localization and Mapping) 또는 SfM(Structure from Motion) 이라는 기술은 지금 계속 연구되고 있다고 한다. 

3 차원 환경 지도를 만들고 위치 추정을 하려면, 여러가지의 sensor device 가 필요한데. 예를 들어서, 카메라(monocular and stereo camera), 레이저 센서, RGB-D 카메라가 있다. RGB-D 카메라 같은 경우, 내가 유튜브로 보다가 Amazon? 에서 나온 카메라를 본적은 있엇던것 같다. 레이저 센서는 너무 유명 하고도 유명한 LiDAR 이 있다. 2D LiDAR 와 3D LiDAR 가 있는데 이게 수직 해상도(vertical resolution)에 따라서 분류가 된다고 한다. 

여기서 정리 할 필요가 있는데, 한번 표로 정리를 해봐야겠다.

| 센서 종류                      | 센서의 장단점                                                |
| ------------------------------ | ------------------------------------------------------------ |
| 단일 카메라 (Monocular Camera) | 센서의 크기가 작고, 다양한 디바이스에 적용 가능. 하지만, 단일 영상으로 부터의 Depth 의 추정하기 위한 알고리즘이 따로 필요 |
| 양안 카메라 (Stereo Camera)    | 양쪽의 영상 또는 이미지로 부터 Registeration (정합)을 통해 거리 정보(depth)를 처리 가능하나, 이 처리를 하기위한 시간과 측정 가능한 거리가 카메라 사이의 거리에 따라서 제한된다. |
| RGB-D Camera or Sensor         | 따로 별다른 거리 측정 또는 계산이 필요가 없다. 왜냐하면 Depth 의 정보를 획득이 바로 가능하고, Stereo Camera 보다 속도가 더 빠르고, 조밀한(dense)한 지도 데이터를 구할수 있다. 하지만, 실외환경에서는 Camera 의 단점인 조명에 따른 Noise 가 생성 될수 있기 때문에, 어느정도 제한이 잇다. |
| 2D LiDAR                       | 가격이 저렴하다. 데이터양이 적어서 실시간 처리가 가능하지만 움직임의 자유도(Degree of Freedom)가 높은 경우 적용하기 힘들다 |
| 3D LiDAR                       | 많은수의 3D 포인트를 제공하기 때문에, 조밀한 3차원 복원 및 6 자유도의 움직임 추정이 가능하지만, 센서가 무겁고, 가격이 비싸다. |

사실 Stereo 와 Monocular Camera 를 이용한 딥러닝 Paper 를 읽어본 적 있으며, Unsupervised Way 나 ConvLSTM 을 사용해서 문제를 풀었던 문제를 읽곤 했었다. Depth Estimation 에 "거리" 라는건 굉장히 중요하고 카메라가 가격의 장점을 이용해서, 이 문제를 푸는건 아직도 큰 문제 인거 같긴하다.

사실 새롭게 알았던건, <u>카메라를 이용해서, SLAM 기법을 사용하면, 오차가 누적되기 때문에, 최종 생성된 지도와 위치 추정의 오차가 매우 커진다라는것과 이러한 오차를 해결한 방법은 Visual-SLAM 을 사용해서 문제를 풀어간다라는것이다.</u> 그렇다면 왜 오차가 누적되는냐 ? 라는 대답은 주변환경과 조도의 변화(Changes in illumination)에 따라서 센서 관측치(Observation)에 대한 Noise 또는 Ambiguity 가 존재 한다라는것이다. 사실 이거의 예가 올바를지 모르지만, 일단 클래식한 컴퓨터 비전 알고리즘을 사용한 예를 들자면, 사진과 영상은 빛에 너무 영향을 받기 때문에 Edge Detection 과 Face Recognition 이 Fail 할 가능성이 높다.

그렇다면, Visual-SLAM의 기법은 3가지로 나누어진다고 한다. 기하학적인 기법(Geometry), 학습을 이용한 기법, 두가지를 사용한 하이브리드 기법이 있다고 한다.

---

## 기하학적인 방법

이 Paper 에서 말한 기하학적인 방법의 배경설명은 이렇다. "임의의 환경에서 획득한 영상 Sequence 로 부터 기하학적 계산을 통해 카메라의 위치 및 3차원지도를 생성하면서 발생하는 오차 누적을 줄이기 위한 방법" 일단 기하학적으로 계산을 한다는 거 자체가 Overhead  가 있지 않을까라는 생각과도 잠시 Optimization 기법이 있다고 해서 안심했엇다. 이 오차 누적을 줄이기 위해서는 크게 Filtering 과 Optimization 기법이 있다고 한다. 

### Filtering Method

Filtering Method 의 방식은 카메라 자세와 3차원 지도에 대한 확률분포를 영상 데이터를 획득할 때마다 새롭게 갱신하는 방법으로 확률분포의 정의에 따라서 Kalman Filter 와 Particle Filter 의 기법으로 나누어진다고 한다. 여기서의 카메라의 위치는 로봇의 그 자체가 될수 있다라는것도 주의해볼만 하다. <u>여기서 내리는 Kalman Filter 의 정의는, 카메라의 자세와 지도를 구성하는 3차원 Landmark 의 위치를 가우시안 분포로 가정하고 영상 데이터를 획득할 때마다 가우시안 분포를 표현하는 평균 벡터와 공분산을 새롭게 갱신하면서 SLAM을 수행한다고 한다.</u> 사실 Kalman Filter 의 정의와 Method 는 잘 알고 있었다. u 값과 sigma 값을 로봇의 위치가 update 할때마다, 두개의 Gaussian Distribution 을 보며, 평균을 구하는 정도의 Background 는 얼추 알고 있었다. 

여기서 새롭게 나온 Method 를 인용했었는데, 꼭 읽업봐야겠다 라는 생각이 들었다. Unscented Kalman Filter[Robust Real-Time Visual SLAM using Scale Prediction and Exemplar Based Feature Description] 또 Particle Filtering 의 예시로 보여준 Rao-Blackwellized Particle Filtering 과 Key Frame Method 를 사용해서 성능과 처리 속도를 개선했다고 하는 [Bayesian Filtering for Keyframe-based visual SLAM] 이라는 Paper 를 꼭 읽어봐야겠다.



### Optimization Method

Optimization method 는 크게 두가지로 표현된다고 하였다.

1. 영상으로부터 특징점을 추출하고 이를 영상 Sequence 에서 추적하여 초기 카메라의 위치를 계산하고, 3차원 지도를 생성한다. 그리고 3차원 지도를 구성하는 Landmark의 위치들은 카메라의 추정된 자세로 투영(Reprojection)시켜서 영상으로부터 추적된 특징점의 좌표와의 거리를 최소화 하도록 update 한다라는 것이다. [A Versatile and Accurate Monocular SLAM System]
2. 두 장의 영상으로부터 카메라의 움직임과 환경에 대한 3차원 정보를 획득하기 위해서 첫 번째 영상을 두 번째 위치에서의 영상으로 변환하였을대 실제 획득한 두 번째 영상과의 밝기 차이를 최소화하도록 최적화를 수행하여 개선하는 Direct SLAM 기법이 있다고 한다. [Direct Space Odometry]

사실 Optimization Method 란, 내 생각에는 어느 한 domain 을 기준으로 해서, 문제를 Optimization 하는것 같다. 생각을 해보면 첫번째 방법은 특징점을 추출하고 3D Map 을 만들어서, 다시 재투영한 결과의 Map 과의 차이점을 최소화하는 기법인것 같고, 두번째는 두개의 카메라를 사용해서, 실제 Pixel Intensity 의 차이를 가지고 최소화 하는것 같아 보였다.

특징점 기반 즉 첫번째 기반 같은 경우 영상에서 특정 화소들을 이용하여 카메라 위치를 추정하고 3차원 지도를 생성함으로써 빠르다는 장점이 있다고 한다. 그리고 특징점의 False Matching 으로 발생되는 문제들을 RANSAC(Random Sample Consensus) 기반의 방법을 활용하여 제거 하는 것이 가능하다고 한다. RANSAC 같은 경우는 내가 급히 SLAM 이 쪽으로 취직방향을 잡기 위해서, 잠깐 공부했었는데 역시 쉽게 얻어가는건 쉽게 잊혀진다고 하지 않았나 싶다. 

두번째 기법인 Direct SLAM 기법은 처리속도가 느리나 환경을 조밀하게 모델링하는게 가능해서, 특징점이 없는 균질한(Homogeneous) 한 환경에서 성능이 우수하다고 하였다. 

---

## Deep Learning Based Visual SLAM

사실, 여기에도 굉장히 관심이 많다. Computer Vision 을 공부하면서, 여기에 답이 있다고 생각을 많이 했었다. 하지만, 딥러닝이 풀수 없는 문제도 정말 많다. 앞서 말했다 싶이 illumination 문제는 너무나도 사진이나 영상에 치명적인 오차를 준다고 개인적으로 생각하기 때문에, 어떻게 문제를 풀어갈지도 너무 궁금하다. 

여기서 말하는 딥러닝 기반의 알고리즘은 이렇게 표현했다. "딥러닝 기반 알고리즘의 경우 학습된 지식을 통해 응용 분야에 맞게끔 모델을 자동으로 설계한다." 이러면서 딥러닝의 강점인 특징을 이야기했는데, "학습 기반 방법의 장점은 복잡한 모델과 고차원의 특징 정보들을 사람의 정의 없이 학습 데이터로부터 자동으로 계산할 수 있으므로 다양한 환경 변화 및 특징 정보가 부족한 환경에서도 **강인성** 을 확보 할수 있다." 최근들어서 머신러닝, 딥러닝 분야가 확실히 뜨고 있는건 사실이다. 하지만, 불확정한 학습데이터와 모델을 설명할수 없는(unexplained 된 Deep Learning Model) 이 정말 많고, 배우는데 많이 기초가 잡혀지지 않을수 있다.

딥러닝 기반의 SLAM 기술들은 크게 Odometry 추정과 Mapping 으로 분류 된다고 한다. Odometry 추정은 두 영상 사이의 상대적인 자세 변화를 추정하는 기술이고, Mapping 은 주변 환경에 대한 공간 모델을 생성하는 것을 의미한다고 말한다. [A Sruvey on Deep Learning for Localization and Mapping: Towards the Age of Spatial Machine Intelligence]

난 처음에 Odometry 라는 영단어가 쉽게 들리면서, SLAM 의 개념적으로 어떻게 적용(Apply)이 되는지 몰랐었다. 그래서 여기서 한번 정의를 내리자.

### What is the Odometry ?

앞서 말했다싶이 Odometry 는 예를 들어서, 우리가 자동차를 타다 보면, 앞에 속도와 주행거리를 나타내주는 계기판이 있다. 여기서 주행거리를 보여주는 작은 장치를 Odometry 라고 한다. 또한 이걸 주행 기록계 라고 한다.  그렇다면 어떻게 이게 Robotics 와 SLAM 에 연관된다라는게 나의 큰 질문이다. 

왜 Odometry 와 SLAM 이 연관 되느냐. 일단 Odometry 를 로보틱스에 관점을 들자면, 일단 차의 바퀴가 회전할 것이다. 그렇다면, 바퀴의 회전수에 따른 주행거리를 구할 수 있는 Parameter 가 생긴다. 이 후 주행거리를 구하기 위해서 이 값에 바퀴의 둘레를 곱하여 측정하는 것이다. 그리고 단순히 주행거리만 측정하는 것 뿐만 아니라, 로봇 또는 자동차가 갔었던? 주행했었던? 전체적인 궤적을 구할수 있다. 그렇다면, 로봇의 위치는 어떻게 구할수 있는건가? 로봇의 완전한 위치를 알려주는 벡터값 [x<sup>t</sup>, y<sup>t</sup>, z<sup>t</sup>, a<sup>t</sup>, b<sup>t</sup>, r<sup>t</sup>] 가 있다고 한다. 여기서 a(alpha), b(beta), r(gamma) 는 오일러 각이라고 알려져 있고, x, y, z 는 Cartesian Coordinate 정보라고 한다. 즉 Odometry 추정이라는 건, 로봇이 주행한거리를 추정 하는거 뿐만아니라 로봇이 움직였던 궤적을 추정할수 있다는 것이다.

### Odometry 추정

딥러닝 기반의 Odometry 추정 기술은 지도 학습과 비지도 학습으로 분류 된다고 한다. 지도 학습은 연속적인 영상과 그에 대응하는 카메라 자세 변화에 대한 학습데이터가 존재하는 경우, **입력 영상에 대한 자세 변화의 출력을 제공하는 end-to-end 딥러닝 기술**이라고 한다 지도 학습 기반의 방법으로 영상에서 특징 정보를 추출하기 위한 CNN(Convolutional Neural Network)와 순차적 자세 변화 추정을 위한 RCNN(Recurrent Convolutional Neural Network) 를 이용하여 입력 영상 sequence 에 대한 카메라 자세를 출력하는 기술이 제안되었다고 한다. 역시 영상 sequence 라는 건 시간(t) 가 하나의 Parameter 또는 dependent 한거니까, RCNN 을 써야 한다는 생각이들었다. [Towards End-to-End visual Odometry with Deep Recurrent Convolutional Neural Network]

비지도 학습 기반의 방법은 주어진 영상 sequence 에 대한 자세 학습데이터가 없는 경우 depth 정보를 추출하고 자세 변화를 추정하기 위한 딥러닝 기술로서 계산된 자세 변화와 depth 로 부터 다른 시점의 영상을 합성하여 그 시점의 실영상과 비교를 통해 손실함수를 정의하고 학습한다.[Unsupervised Learning of Depth and Ego-Motion from Video]. 사실 이 Paper 는 굉장히 유명하다. 특히나 Unsupervised Learning 을 사용해서, Depth 를 추정하는것도 굉장히 흥미로웠던 논문이다.

### Mapping

Mapping 이란 센서 데이터를 이용하여 주변 환경에 대한 3차원 형상 또는 구조를 표현하는 기술로서 지도를 구성하는 기본 요소에 따라서 depth, point, mesh, voxel 로 표현 한다고 한다. 사실 Point Cloud 라는 말은 흔히 들어봤다. 그리고 이게 실제 Mapping 하는 기술에도 많이 쓰인다고 종종 들었다. 영상 정보로부터 커리를 획득하는 방법은 Streo Camera 를 사용하거나 Video Sequence 를 사용하는 게 일반적이었으나 최근 Monocular Camera 로부터 depth information 를 추출할 수 있는 딥러닝 기술들이 활발히 연구되고 있다고 한다. Depth 생성 기술은 지도학습 또는 비지도학습으로 나누어진다고 한다. 대표적인 Paper 는 [Depth map prediction from a single image using a multi-scale deep network] and [Unsupervised monocular depth estimation with left-right consistency]. 사실 첫번째 Paper 같은 경우, 되게 많이 사용된다. 내가 첫 Conference 를 갔었을때 Human Right 에 관했던 Conference 였는데, Human Trafficking 을 방지하고자  이 비슷한 Architecture 을 통해서 인권매매를 하는 호텔들이 어디에 있는지 추측하는 그런 interesting 한 발표가 있었었다. The second paper is also very popular when it comes to depth estimation by using the monocular camera. 

지도 학습 방법은 방대한 양의 영상과 해당 depth information 를 학습하여 입력영상으로 부터 바로 depth 를 예측하는 기술로 전역과 지역적으로 depth 를 예측하는 두개의 Network 를 사용하여 정확도를 개선하는 기술이 제안되었다고 한다. [Depth map prediction from a single image using a multi-scale deep network]. 하지만, 늘 말하지만 딥러닝은 도깨비 방망이가 아니듯이, accurate depth video sequence 를 확보하는게 어렵다. 이 문제를 해결하기 위해 비지도 학습 방법에서는 depth sequence 대신에, stereo camera 로 부터 획득한 영상을 학습 데이터로 활용한다. 구체적으로는 왼쪽 영상을 오른쪽 영상으로 변환하기 위해서 disparity와 오른쪽 영상을 왼쪽 영상으로 변환하는 시차를 계산하고 이른 왼쪽-오른쪽 일관성(left-right consistency) 제약조건을 이용하여 네트워크를 구성함으로써 향상된 Depth Map 을 생성했다. 사실 disparity 를 이용해서 딥러닝 문제를 푸는건 굉장히 많은데에서 사용된다. 내가 처음에 일했었던 교수는 protein depth map 를 deep learning 을 사용해서 만들었었는데, 이때 disparity map 을 사용하면서, protein contact map 을 만드는데 성공했었던게 기억이 난다.

---

## Hybrid Visual SLAM Method

여기서 말하는 하이브리드 방식은 Visual SLAM 을 구성하고 있는 여러 단계 중 일부를 딥러닝 방법으로 계산하고 다른일부는 고전적인 기하학적 방법을 활용한다. 딥러닝 기반의 방법은 영상에서 특징 정보를 추출하기 어려운 환경에서 더 나은 결과를 제공하지만, 특징 정보가 풍부한 환경에서는 고전적인 방법의 성능이 우수하다. 사실, 이거에 대한 합리적인 의심이 들지만, 꼭 기하학적인 방법으로 한번 구현해봐야겠다라는 생각이들었다. 이 Paper [Scale recovery for monocular visual odometry using depth estimated with deep convolutional neural fields] 에서는 monocular visual odometry 를 deep learning based method 로 풀어 냈었고, 입력 영상으로부터 자세 변화를 추정하는 부분을 기하학적 Odometry 추정방법을 채택하였다고 한다. 생성된 초기 depth 와 Camera Pose 는 CRF(Conditional Random Field)를 이용해서 정확도를 향상시켰다고 한다. 

또 다른 Paper [Visual Odometry revisited: What should be learnt?] 에서는 depth 와 optical flow 를 딥러닝 기반의 학습으로 부터 계산을 하고, 이 결과물을 기하학적 odometry 알고리즘에 적용하여 카메라의 자세 변화를 추정하였다. 또 다른 방법으로는 딥러닝 기술로 부터 움직이거나 또는 변화가 있는 부분을 검출하여 기존 특징점 기반과 Direct. SLAM 의 성능을 개선하는 방법도 제안되었다고 한다. [Driven to distraction: self-supervised distractor learning for robust monocular visual odometry in urban environments].

최근에는 딥러닝 기술과 기존 필터링 기반의 방법이 융합된 SLAM 기술로서 칼만 필터와 입자 필터를 딥러닝으로 학습하는 기술이 개발됬다고 한다. [Backprop kf: Learning discriminative deterministic state estimators] and [Differentiable SLAM-net: Learning Particle SLAM for Visual Navigation]


---
사실 이 Paper 를 읽고 많은 흥미로운 사실과 더 공부해야할 이유 또는 motivation 이 생겼다. SLAM 이 어려운 학문이고, 정말 Fusion 음식같이 어렵고, 복잡한것 같다. 풀기 위한 방법은 여러가지 일것 같으며, 어떤 problem domain 인가에 따라서 새로운 문제를 풀수 있다라는 걸 느끼게 되었다.

---

Reference : 

1. Visual SLAM 기술개발 동향 - 김정호(한국전자기술연구원)
2. [초보자를 위한 Visual Odometry - 시작부터 튜토리얼 까지](https://snacky.tistory.com/96)


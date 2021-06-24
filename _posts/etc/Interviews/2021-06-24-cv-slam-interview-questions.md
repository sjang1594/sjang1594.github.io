---
title: CV & SLAM Interview Questions
layout: post
bigtitle: CV & SLAM Interviews
date: '2020-12-31 12:45:51 +0900'
categories:
- etc
- interviews
tags:
- interviews
comments: true
published: true
---

# CV / SLAM Interview Questions

---

## Basic Concepts




----

## Questions

**1. What is Image Projection and Process**

3D 공간에서 2D 이미지로 변환하는 과정을 image projection이라고 합니다. 3D 공간 위의 어떤 위치를 [X,Y,Z,1]<sup>T</sup>로 표현하고, 2D 이미지 위의 픽셀 위치를 [u,v,1]<sup>T</sup> 로 표현하겠습니다. `X,Y,Z`는 3D coordinate고, `u,v`는 픽셀 coordinate 위의 column, row를 의미하며, 1은 euclidean space가 아닌 projective space 에서의 변환을 고려하기 위한 homogeneous coordinate 표기법 때문에 붙었습니다.

카메라가 이 3D 포인트를 바라보고 있을 때, 카메라의 optical centre와 3D 포인트 사이의 직선을 그리면 image plane 을 통과할 것입니다. 이 때, 카메라의 optical centre에 위치한 카메라의 coordinate frame과 World의 coordinate frame의 회전과 이동 (rotation / translation)을 Euclidean space에서의 SE(3)로 표현하면 3x4 매트릭스 형태를 가집니다. 이 매트릭스를 Extrinsic matrix라고 부르며, [X,Y,Z,1]<sup>T</sup> 에 이 매트릭스를 곱하면, 카메라의 coordinate frame에서 [X,Y,Z,1]<sup>T</sup> 의 위치를 알 수 있습니다.

이후, Intrinsic matrix를 이용해서 [X,Y,Z,1]<sup>T</sup>를 2차원 평면에 투영시킬 수 있습니다. Intrinsic matrix는 Focal Length (fx, fy)와 Principal point (cx, cy) 정보를 가지고 있습니다. Focal length는 normalized scale에서 pixel scale로 변환을 할 수 있게 해줍니다. cx와 cy는 보통 중앙 픽셀의 위치 값을 가지는데, 이는 coordinate frame을 optical centre (또는 이미지 중앙)이 아닌, 좌측 상단에 올려놓기 위함입니다. 하지만 카메라가 실제로 만들어지면서 완벽하게 중앙에 위치하지 않기 때문에, 몇픽셀의 차이는 있을 수 있습니다. Intrinsic matrix의 3번 row는 [0, 0, 1]인데, 이는 homogeneous coordinate를 맞추려는게 아니고, 3차원→2차원 축소를 위함입니다.

이 계산이 끝나면 [su, sv, s]<sup>T</sup>이 결과 값으로 나오는데, s는 homogeneous coordinates의 영향으로 나온 scale 값입니다. 그러므로 s * [u, v, 1]로 normalize를 시켜주면 pixel coordinate 값이 나오게 됩니다.

**2. Advantages and Disadvantage of Monocular SLAM**

- Advantages
  - It's cheap because it's using one camera
  - 다중 카메라 시스템에 비해 처리해야하는 이미지 양이 적다.
  - 수많은 제품이 1개의 카메라를 사용한다. (e.g. 스마트폰)
  - 다중 카메라에서 필요한 캘리브레이션 과정이 축약된다. Intrinsic 캘리 브레이션 한번만 하면 된다
- Disadvantages
  - 알고 있는 geometry 를 사용하지 않는 이상, Epipolar geometry 계산 시 Scale 을 구할수 없다. 이 경우 metric scale 복원이 불가능하다
  - Monocular image 에서 depth 추정이 불가능하다. 상대적 거리를 알기 위해서는 무조건 multiple view reconstruction 이 필요하다
  - 360 카메라나 어안렌즈와 같은 특수한 렌즈 구성을 사용하지 않는 이상 field of view 가 작다
- Resolutions to Disadvantages
  - Scale 과 Depth 를 구하기 위해서는 스트레오 카메라 또는 다중 카메라 시스템을 구축하면 된다
  - Scale 을 구하기 위해 IMU를 함께 사용하는 방법이 있다. IMU 는 metric scale 복원이 가능하다.
  - 마커와 같이 이미 알고있는 랜드마크 물체를 사용해 scale 추정을 할 수 있다.
  - 최근 딥러닝 기반 monocular depth estimation, 또는 single image monocular depth estimation 기술을 사용해 depth 정보를 추출하기도 한다. 아직 엄청나게 정확한 편은 아니지만, CNN-SLAM 의 경우 depth estimation 프론트엔드에 LSD-SLAM 백엔드를 사용해서 SLAM 시스템을 만들기도 했다.

**3. Advantages and Disadvantage of LiDAR, RADAR**

* **LiDAR:**

  * 가격이 (아직) 비싼편
  * 레이저 반사와 TOF 를 이용해서 카메라보다 훨씬 먼 거리임에도 정확한 Depth 추정이 가능. 하지만 눈이나 비, 안개가 낀 상황에 성능이 급격하게 떨어짐
  * LiDAR SLAM 이 가능
  * 딥러닝 기술을 이용하여 object detection 도 가능

* **RADAR:**

  * Doppler 효과를 이용해서 움직이는 장애물의 속도 추정 가능
  * 데이터에 잡음이 엄청 많음
  * 안 좋은 날씨에는 라이다나 카메라보다 잘됨

* **Camera:**

  * The price is cheap
  * 딥러닝 기반 detection 등을 이용해서 장애물을 구분한다던지, 차선을 본다던지, 신호등 신호를 구분할 수 있음
  * 다중 카메라로 꾸밀 경우 depth 정보 추출 가능하나, 단안 카메라로는 불가능함. 다중 카메라를 사용해도 라이다보다 훨씬 거리가 작음
  * 어둡거나, 눈/비/안개 등으로 인해 보이지 않을 경우 성능이 급격하게 떨어짐

  **Comments: ** 안전을 위해서는 모두 다 쓸 것 같음. GPS(Global Positioning System) 와 IMP(Inertial Measurement Unit) Sensor 같이 씀. 카메라가 60Hz, 라이다가 10Hz, 레이더가 100Hz, IMU가 200Hz, GPS가 5Hz 라서 속도가 다 다를텐데, Extended Kalman Filter 등을 사용해서 퓨전을 할 것 같음. 물론 센서들의 특성을 분석하고 퓨전을 함.

**4. Explain what is RANSAC and Discuss about advantages and disadvantages**

* RANSAC 은 Fischer 와 Balls의 예엣날 논문으로써 Random sample consensus 의 약자이다. 모델 추정을 할때 outlier 가 끼어있으면 정확한 모델 추정이 불가능한데, RANSAC을 통해 수많은 데이터로부터 outlier 를 제거 하고 (확률적으로) 올바른 모델을 찾을수 있다. 
* The basic assumption of the RANSAC algorithm is that the sample contains correct data(inliers, data that can be described by the model) and abnormal data (outliers, data that deviates far from the normal range and cannot adapt to the mathematical model), that is, the dataset contains noise. These abnormal data may be caused by wrong measurements, wrong assumption, wrong calculations, etc. At the same time, RANSAC also assumes that given a set of correct data, there are methods that can calculate model parameters that conform to these data
* RANSAC 이 진행되는 방법은 다음과 같다. 우선 모델을 구성할 수 있는 minimal set 의 데이터를 무작위로 뽑는다. 예를 들어, homography 의 경우 4 개의 feature match 를, p3p 인 경우 3 개를 고르는 것 같다. 뽑은 데이터로 부터 모델을 만들고, 이 모델을 사용할 때 다른 데이터들이 얼마나 에러를 가지는지를 구한다. 이 때, 이 에러가 지금 까지 찾은 모델들보다 낮다면 (i.e. best model 이라면), 그 정보를 저장한다 (물론 첫 iter 에서는 항상 best model이다). 그 다음에 또 다시 minimal set 의 데이터를 무작위로 뽑고, 그 모델이 best model 인 경우 모델 정보를 저장, 그게 아니라면 정보를 버린다. 이렇게 해서 정해놓은 iteration, 또는 정해놓은 error threshold에 도달할 때 까지 돌리는데, 랜덤한 성격을 가지고 있다보니 예정보다 빨리 끝날 때도 있고, 주어진 시간 안에 해결 하지 못할 때도 있다.
* Advantages of RANSAC:
  * 통계적으로 대충 몇 iteration 이면, 몇 %의 확률로 좋은 모델이 나올 지 추정을 할 수 있다는 것이다. 그렇기에 알고리즘 planning 할때 유용하다. 또, 수많은 경우의 수에서 빠르게 모델을 추정할 수 있다. 개량된 RANSAC (e.g. Lo-RANSAC 이나 PROSAC) 등을 이용할 경우, 더욱 더 빠르게 답을 찾을수 있다.
  * The advantage of the RANSAC algorithm is that it can estimate model parameters robustly. For example, it can estimate high-precision parameters from a dataset containing a large number of outliers. 
* Disadvantages of RANSAC
  * 첫째는, 랜덤하게 샘플을 뽑기 때문에, 거의 대부분의 경우 매번 다른 모델이 추정된다. 이때문에 SLAM 알고리즘의 정확도에 대해 계산할 때, 매번 다른 결과가 나오게된다. Deterministic test 도 믿기 조금 어려울 때가 있다. (random seed 를 고정해도, 그냥 그 seed가 않좋아서... 운이 안좋아서 결과가 잘 안나오는건지, 아니면 진짜 내)

---

### Reference

1. [50 개의 CV/SLAM 직무 기술면접](https://cv-learn.com/50-CV-SLAM-a6c06c0fbd824bc98572169a5a5e6793)
2. [Common SLAM Interview Questions](https://zhuanlan.zhihu.com/p/46696986?fbclid=IwAR22PFL-bD4DEgejO3aifX9HBDeUWvxnLRO4c5JeX5naaW51CU-bEyXSf1Q)

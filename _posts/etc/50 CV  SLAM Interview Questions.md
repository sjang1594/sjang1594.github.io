# CV / SLAM Interview Questions

---

**1. What is Image Projection and Process**

3D 공간에서 2D 이미지로 변환하는 과정을 image projection이라고 합니다. 3D 공간 위의 어떤 위치를 $[X,Y,Z,1]^T$로 표현하고, 2D 이미지 위의 픽셀 위치를 $[u,v,1]^T$ 로 표현하겠습니다. $X,Y,Z$는 3D coordinate고, $u,v$는 픽셀 coordinate 위의 column, row를 의미하며, 1은 euclidean space가 아닌 projective space 에서의 변환을 고려하기 위한 homogeneous coordinate 표기법 때문에 붙었습니다.

카메라가 이 3D 포인트를 바라보고 있을 때, 카메라의 optical centre와 3D 포인트 사이의 직선을 그리면 image plane 을 통과할 것입니다. 이 때, 카메라의 optical centre에 위치한 카메라의 coordinate frame과 World의 coordinate frame의 회전과 이동 (rotation / translation)을 Euclidean space에서의 $SE(3)$로 표현하면 3x4 매트릭스 형태를 가집니다. 이 매트릭스를 Extrinsic matrix라고 부르며, $[X,Y,Z,1]^T$ 에 이 매트릭스를 곱하면, 카메라의 coordinate frame에서 $[X,Y,Z,1]^T$ 의 위치를 알 수 있습니다.

이후, Intrinsic matrix를 이용해서 $[X,Y,Z,1]^T$를 2차원 평면에 투영시킬 수 있습니다. Intrinsic matrix는 Focal Length (fx, fy)와 Principal point (cx, cy) 정보를 가지고 있습니다. Focal length는 normalized scale에서 pixel scale로 변환을 할 수 있게 해줍니다. cx와 cy는 보통 중앙 픽셀의 위치 값을 가지는데, 이는 coordinate frame을 optical centre (또는 이미지 중앙)이 아닌, 좌측 상단에 올려놓기 위함입니다. 하지만 카메라가 실제로 만들어지면서 완벽하게 중앙에 위치하지 않기 때문에, 몇픽셀의 차이는 있을 수 있습니다. Intrinsic matrix의 3번 row는 $[0, 0, 1]$인데, 이는 homogeneous coordinate를 맞추려는게 아니고, 3차원→2차원 축소를 위함입니다.

이 계산이 끝나면 $[su, sv, s]^T$이 결과 값으로 나오는데, $s$는 homogeneous coordinates의 영향으로 나온 scale 값입니다. 그러므로 $s * [u, v, 1]$로 normalize를 시켜주면 pixel coordinate 값이 나오게 됩니다.

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
  - 

---

### Reference

1. [50 개의 CV/SLAM 직무 기술면접](https://cv-learn.com/50-CV-SLAM-a6c06c0fbd824bc98572169a5a5e6793)
2. [Common SLAM Interview Questions](https://zhuanlan.zhihu.com/p/46696986?fbclid=IwAR22PFL-bD4DEgejO3aifX9HBDeUWvxnLRO4c5JeX5naaW51CU-bEyXSf1Q)
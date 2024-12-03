## 모션

-   어떻게 움직이는 물체를 검출하고 움직이는 방향과 속도, 몸짓 등의 정보를 빠르고 정확하게 알아낼까?
    -   빈약한 움직임 데이터도 강한 지각을 불러일으킬 수 있음

## 동적 비전

-   동적 비전이 처리하는 연속 영상(동영상)
    -   시간 축 샘플링 비율
        -   보통 30 프레임/초 (30 fps)
        -   특수한 경우, 수천 프레임/초 또는 60 프레임/시

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/fadc8385-311d-45e1-9d6b-20e934f43812/image.png)

## 움직임이 발생하는 원인

-   영상 처리 과정에서의 3가지 요소
    -   광원, 객체, 카메라
    -   위의 셋 중 하나가 변하는 경우 움직임이 발생
        -   Static camera, moving objects (surveillance)
        -   Moving camera, static scene (3D capture)
        -   Moving camera, moving scene (sports, movie)
        -   Static camera, moving objects, moving light (time lapse)

## 동적 비전의 기술 난이도

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/09c8a38e-c948-42cc-93aa-e9d8d7e37389/image.png)

## 모션 정보의 추출

-   Feature-tracking
    -   시각적 특징(코너, 텍스처가 있는 영역)을 추출하고 여러 프레임에 걸쳐 이를 추적
-   Optical flow (광류)
    -   공간-시간적 이미지 밝기 변화를 이용하여 각 픽셀에서 이미지 움직임을 복원

## Feature-tracking의 어려움

-   어떤 특징을 추적할 수 있을지 파악해야 함
-   프레임 간의 해당 특징을 효율적으로 추적해야 함
-   일부 특징점은 시간에 따라 외형이 변할 수 있음
    -   회전, 그림자 영역으로의 이동 등
-   외형 모델을 업데이트하면서 작은 오류가 축적될 수 있음
-   특징점이 나타나거나 사라질 수 있음
    -   추적하는 특징점을 추가/삭제할 수 있어야 함

## 차 영상

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/caddb092-957e-43ef-a97f-3736f3680d6a/image.png)

## 차 영상을 이용한 움직임 추출

-   배경과 물체의 색상에 큰 변화가 없는 상황에서만 동작
    -   Ex. 공장의 벨트 컨베이어, 조명이 고정된 실내 등

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8048c668-b55e-4039-a3fb-fb66ec16ab38/image.png)

## 모션 필드

-   3차원 모션 벡터 v3 복원 불가능
    -   수없이 많은 3차원 벡터가 2차원의 동일한 벡터로 투영되는데, 주어진 정보는 2차원
    -   시점이 다른 여러 대의 카메라를 사용해야 함
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5f3350c8-5d6f-40b8-8d8e-3bfabc25588e/image.png)
-   2차원 모션 벡터 추정
    -   대부분 연구는 두 장의 이웃 영상에서 2차원 모션 벡터를 추정하는 일로 국한

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4e242181-e973-4952-b9f6-c528642e62c9/image.png)

## Optical Flow (광류)

-   광류
    -   모션 필드의 근사 추정치
-   광류 알고리즘
    -   모든 화소의 모션 벡터 v=(v, u)를 추정
        -   모션 벡터를 추정해 기록한 맵 → 광류
-   모션 벡터 추정의 어려움
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7ed037f9-a7c6-4750-8144-fea859deeec1/image.png)

## Optical Flow의 활용

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/40856d76-3999-4417-abae-a3548c05b653/image.png)

## Optical Flow의 추정

-   Feature matching을 통한 방법
    -   Sparse할 수 있음
    -   Alignment가 정확하지 않을 수 있음
        -   낮은 정확도

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ddae3224-f419-47be-902f-71ef2195f794/image.png)

-   두 연속적인 frame에서 점들의 이동을 추정
-   주요 가정
    -   Brightness constancy (밝기 항상성)
    -   Small motion (시간의 흐름에 따라 천천히 변함)
    -   Spatial coherence (이웃한 화소들은 유사한 모션 벡터를 가져야 함)

## Brightness Constancy

-   물체의 같은 점은 다음 영상에서 같은(유사한) 명암 값을 가져야 함
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e67c3df6-737a-4d00-8143-be2d51bc535d/image.png)
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8b86e732-e5d8-4fe3-a704-b33c65cf3add/image.png)

## 광류 조건식 예시

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2f0bebba-613e-408a-b7c2-d0ef7f96acef/image.png)

## 추가 가정을 통한 광류 계산

-   Lucas-Kanade
    -   이웃 화소는 유사한 모션 벡터를 가져야 한다는 지역 조건 사용
-   Horn-Schunck
    -   영상 전체에 걸쳐 모션 벡터는 천천히 변해야 한다는 광역 조건 사용

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/770c0249-7c1e-474b-a3c3-81e0a940a925/image.png)

## Spatial coherence

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/27b5cc15-e9e2-4926-b31b-5243eef9c8a9/image.png)

## Conditions for solvability

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8cfe441d-c643-44a7-8cbd-ff43b16c2ed8/image.png)

## Edge

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e512ee0a-9f9d-4153-ac43-b91888d62c9b/image.png)

## Low Texture Region

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/905a96f6-f788-4ad9-8b9b-785e930fc9f0/image.png)

## High Texture Region

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/eecc64ab-0455-4d87-9a38-62984a46ce17/image.png)

## Lucas-Kanade 알고리즘의 오류

-   언제 Lucas-Kanade 알고리즘에서 오류가 발생?
    -   A^TA는 가역적이라고 가정
    -   이미지에 noise가 거의 없다고 가정
-   3가지 가정이 위배되는 경우
    -   밝기 보존 가정이 충족되지 않는 경우
    -   움직임이 작지 않은 경우 (small motion)
    -   한 점이 이웃 점들과 같이 움직이지 않는 경우
        -   윈도우 크기가 너무 큰 경우
            -   클수록 큰 움직임을 알아낼 수 있지만 smoothing 효과로 motion vector의 정확성이 낮아짐
-   해결책 → 피라미드 활용

## The aperture problem

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/991f3b89-c903-4e94-bf2b-404ca9ee3fc9/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d2bbda46-eca4-4fbc-9d0b-54f7122c8a26/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7416dca5-79a8-45e0-9682-39f0548166ec/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/45f2fa61-ea14-4cdd-963b-d81bc1ac4807/image.png)

## Coarse-to-fine optical flow estimation

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9b9cd9e9-f074-42f9-bd90-34f7596cbb85/image.png)

## 광류 추정 결과

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ac0f157d-9d0d-4f27-b3af-225799bf3ce8/image.png)

## Horn-Schunck method

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/17ab6692-0d58-4c92-b49a-af657d8e5c66/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2d16d1d7-b8ba-4027-af0c-83ace09358e8/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/3d661514-4be2-45ef-9637-d527e0d16bd1/image.png)

## Optical Flow 추정 알고리즘

-   Lucas-Kanade는 지역적, Horn-Schunck는 전역적
    -   LK는 값이 정해지지 않은 곳이 군데군데 발생 (명암 변화가 적은 데에서 심함)
    -   HS는 반복 과정에서 값이 파급되어 밀집된 광류 맵 생성
    -   정확도 면에서는 LK가 뛰어남
-   두 알고리즘의 장점을 결합한 아이디어
    -   Bruhn2005
-   제곱 항을 절댓값으로 대치하여 물체 경계선이 불분명한 단점을 극복
    -   Zach2007

## 물체 추적

-   Lucas-Kanade 광류 알고리즘을 개조한 물체 추적 알고리즘
-   KLT 추적 알고리즘
    -   Kanade, Lucas, Tomasi의 앞 글자를 땀
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/23a12390-423a-4bb1-ae95-d259f2cd70d2/image.png)

```python
import numpy as np
import cv2 as cv

cap = cv.VideoCapture('slow_traffic_small.mp4')

feature_params = dict(maxCorners=100, qualityLevel=0.3,
	minDistance=7, blockSize=7)
lk_params = dict(winSize=(15, 15), maxLevel=2,
	criteria=(cv.TERM_CRITERIA_EPS|cv.TERM_CRITERIA_COUNT, 10, 0.03))

color = np.random.randint(0, 255, (100, 3))

ret, old_frame = cap.read() # 첫 프레임
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

mask = np.zeros_like(old_frame) # 물체의 이동 궤적을 그릴 영상

while(1):
    ret, frame = cap.read()
    if not ret:
        break

    new_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    p1, match, err = cv.calcOpticalFlowPyrLK(old_gray,
	    new_gray, p0, None, **lk_params) # 광류 계산

    if p1 is not None: # 양호한 쌍 선택
        good_new = p1[match==1]
        good_old = p0[match==1]

    for i in range(len(good_new)): # 이동 궤적 그리기
        a, b = int(good_new[i][0]), int(good_new[i][1])
        c, d = int(good_old[i][0]), int(good_old[i][1])
        mask = cv.line(mask, (a, b), (c, d), color[i].tolist(), 2)
        frame = cv.circle(frame, (a, b), 5, color[i].tolist(), -1)

    img = cv.add(frame, mask)
    cv.imshow('LTK tracker', img)
    cv.waitKey(30)

    old_gray = new_gray.copy() # 이번 것이 이전 것이 됨
    p0 = good_new.reshape(-1, 1, 2)

cv.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/78efed08-c5b1-4ce7-b2bc-d115c71710d6/image.png)

## 큰 이동 추적

-   큰 이동이 발생하는 상황에서의 어려움
    -   순간적으로 크게 이동한 손과 팔에서 모션 벡터 추정 실패
-   대응점 찾기 알고리즘 적용
    -   이웃한 두 영상에서 대응점을 찾은 후, 대응점을 잇는 벡터를 모션 벡터로 취함
        -   한계점 존재 (희소한 특징점, Outlier, …)
-   Brox2011
    -   대응점 찾기 적용 후, Horn-Schunck로 밀집된 맵을 구하는 2단계 처리
-   Weinzaepfel2013
    -   Brox2011과 비슷한 접근 사용
    -   유연한 SIFT 아이디어를 추가로 사용
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e75e4231-415f-4704-8a44-9ccd0a057f12/image.png)

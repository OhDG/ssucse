# 영상의 필터링

---

## 필터링 연산

---

-   필터링(Filtering)
    -   영상에서 원하는 정보만 통과시키고 원치 않는 정보는 걸러내는 작업
        -   Ex) 잡음(noise) 제거 → 깔끔하게
        -   Ex) 부드러운 느낌의 성분을 제거 → 더 날카로운 느낌
-   영상의 필터링은 보통 마스크(mask)라고 부르는 작은 크기의 행렬을 이용

### 마스크(mask)

---

-   필터링의 성격을 정의하는 행렬
-   커널(kernel), 윈도우(window)라고도 부름
-   마스크 자체를 필터라고 부르기도
-   다양한 크기와 모양으로 정의 가능
-   행렬의 원소는 보통 실수로 구성

### 필터링 연산 방법

---

-   여러 가지 모양의 필터 마스크 중에서 3 x 3 정방형 행렬이 가장 널리 사용

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/53e82c86-a300-4297-b8d3-68de1d4cdca6/image.png)

-   필터 마스크에서 진한 색으로 표시한 위치는 고정점(anchor point)
    -   고정점은 현재 필터링 작업을 수행하고 있는 기준 픽셀 위치를 나타냄
    -   대부분 마스크 행렬 정중앙을 고정점으로 사용
-   연산의 결과는 마스크 행렬의 모양과 원소 값에 의해 결정
    -   마스크 행렬을 어떻게 정의하는가 → 부드럽게, 날카롭게
    -   잡음을 제거하거나 에지(edge) 성분만 나타나도록 만들수도
-   마스크를 이용한 필터링
    -   입력 영상의 모든 픽셀 위로 마스크 행렬을 이동시키면서 마스크 연산을 수행

## 마스크 연산

---

-   마스크 행렬의 모든 원소에 대하여 마스크 행렬 원소 값과 같은 위치에 있는 입력 영상 픽셀 값을 서로 곱한 후, 그 결과를 모두 더하는 연산
-   마스크 연산의 결과를 출력 영상에서 고정점 위치에 대응되는 픽셀 값으로 설정
-   마스크 행렬 m의 중심이 입력 영상의 (x, y) 좌표 위에 위치
    -   결과 영상의 픽셀 값 g(x, y)
        -   g(x, y) = m(0, 0)f(x-1, y-1) + m(1, 0)f(x, y-1) + m(2, 0)f(x+1, y-1) + m(0, 1)f(x-1, y) + m(1, 1)f(x, y) + m(2, 1)f(x+1, y) + m(0, 2)f(x-1, y+1) + m(1, 2)f(x, y+1) + m(2, 2)f(x+1, y+1)

## 마스크를 이용한 필터링

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/fbe6ece3-d7b1-461e-805e-78992178c65e/image.png)

## 가장자리 픽셀의 처리

---

-   가장자리 픽셀
    -   영상에서 가장 왼쪽 또는 오른쪽 열, 가장 위쪽 또는 아래쪽 행에 있는 픽셀을 의미
-   영상의 가장자리 픽셀에 대해 필터링을 수행 → 특별한 처리
-   OpenCV는 영상의 가장자리 픽셀을 확장하여 영상 바깥쪽에 가상의 픽셀을 만듦
    -   가장자리 픽셀에 대해서도 문제없이 필터링 연산을 수행
-   BorderTypes라는 이름의 열거형 상수 중 일부
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a490c0ef-0238-4887-a7a9-352761578ac6/image.png)

## 필터링 연산

---

-   OpenCV에서 필터 마스크를 사용하는 일반적인 필터링
    -   filter2D() 함수를 이용
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/fc35b5ee-e27c-42b2-9d71-046fa25a9cfd/image.png)
    -   filter2D() 함수는 src 영상에 kernel 필터를 이용하여 필터링을 수행하고, 그 결과를 dst에 저장
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/97e4e733-5714-4ce9-9deb-880e44848798/image.png)
    -   ddepth는 결과 영상의 깊이를 지정하는 용도로 사용
    -   ddepth에 -1을 지정하면 출력 영상의 깊이는 입력 영상과 같게 설정됨
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2999c72f-68a3-4468-a171-fb32c8715858/image.png)
    -   anchor, delta, borderType 인자는 기본값을 가지고 있어서 생략 가능
    -   Anchor 인자는 커널 행렬에서 고정점으로 사용할 좌표
        -   기본값인 Point(-1, -1)을 지정하면 커널 행렬 중심 좌표를 고정점으로 사용
    -   delta 인자에는 필터링 연산 후 결과 영상에 추가적으로 더할 값을 지정할 수 있음, 기본값은 0

## 엠보싱 필터링

---

-   엠보싱 필터
    -   입력 영상을 엠보싱 느낌이 나도록 변환하는 필터
-   보통 입력 영상에서 픽셀 값 변화가 적은 평탄한 영역은 회색으로 설정
-   객체의 경계 부분은 좀 더 밝거나 어둡게 설정 → 엠보싱 느낌이 남

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c42eec26-c860-46a4-aefd-556496983c74/image.png)

-   필터링을 수행하면 대각선 방향으로 픽셀 값이 급격하게 변하는 부분에서 결과 영상 픽셀 값이 0보다 훨씬 크거나 또는 0보다 훨씬 작은 값을 가지게 됨
-   입력 영상에서 픽셀 값이 크게 바뀌지 않는 평탄한 영역 → 결과 영상의 픽셀 값이 0에 가까운 값을 가지게 됨
-   결과 영상에서 음수 값은 모두 포화 연산에 의해 0이 되어 버림 → 입체감이 줄어듦
-   엠보싱 필터를 구현할 때 → 결과 영상에 128을 더하는 것이 좋음

```python
import numpy as np
import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    exit()

emboss = np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1], np.float32])

dst = cv2.filter2D(src, -1, emboss, delta=128)

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()
```

-   dst 영상에서 장미꽃 경계 부분이 입체감 있게 표현됨
-   픽셀 값이 완만하게 바뀌는 부분 → 필터링 결과 영상이 대체로 밝기 값 128에 가까운 회색으로 표현됨

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/16847c26-40c2-404c-b2fb-911b376a3f5c/image.png)

# 블러링 : 영상 부드럽게 하기

---

## 블러링(Blurring)

---

-   마치 초점이 맞지 않은 사진처럼 영상을 부드럽게 만드는 필터링 기법
    -   스무딩(smoothing)이라고도 함
-   영상에서 인접한 픽셀 간의 픽셀 값 변화가 크지 않은 경우 부드러운 느낌을 받을 수 있음
-   블러링은 거친 느낌의 입력 영상을 부드럽게 만드는 용도로 사용
-   입력 영상에 존재하는 잡음의 영향을 제거하는 전처리 과정으로도 사용됨

## 평균값 필터

---

-   입력 영상에서 특정 픽셀과 주변 픽셀들의 산술 평균을 결과 영상 픽셀 값으로 설정하는 필터
-   평균값 필터에 의해 생성되는 결과 영상은 픽셀 값의 급격한 변화가 줄어들어 날카로운 에지가 무디어지고 잡음의 영향이 크게 사라지는 효과
-   너무 과도하게 사용할 경우
    -   사물의 경계가 흐릿해지고 사물의 구분이 어려워질 수 있음
-   각각의 행렬은 모두 원소 값이 1로 설정
    -   행렬의 전체 원소 개수로 각 행렬 원소 값을 나누는 형태로 표현
-   평균값 필터는 마스크의 크기가 커지면 커질수록 더욱 부드러운 느낌의 결과 영상을 생성
    -   그 대신 연산량이 크게 증가
-   OpenCV에서는 blur() 함수를 이용하여 평균값 필터링을 수행
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/f5bea144-b6bb-4c47-aeb4-c6b516073915/image.png)
    -   blur() 함수는 src 영상에 ksize 크기의 평균값 필터 마스크를 이용하여 dst 출력 영상을 생성
    -   anchor 인자와 borderType 인자는 기본값을 가짐 → 함수 호출 시 생략 가능
    -   blur() 함수에서 사용하는 커널은 다음과 같은 형태
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/75514983-6643-480d-900f-92d34ebe380b/image.png)
-   blurring_mean() 함수는 3x3, 5x5, 7x7 크기의 평균값 필터를 이용하여 rose.bmp 장미 영상을 부드럽게 변환
-   평균 값 필터의 크기가 커질수록 결과 영상이 더욱 부드럽게 변경

```python
def blurring_mean():
    src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        exit()

    cv2.imshow('src', src)

    for ksize in range(3, 9, 2):
        dst = cv2.blur(src, (ksize, ksize))

        desc = "Mean: %dx%d" % (ksize, ksize)
        cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA)

        cv2.imshow('dst', dst)
        cv2.waitKey()

    cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/856a1bfc-9d8c-4ca9-83d3-f573f1296034/image.png)

## 가우시안 분포

---

-   평균을 중심으로 좌우 대칭의 종 모양(bell shape)을 갖는 확률 분포
    -   정규 분포(normal distribution)라고도 함
    -   자연계에서 발생하는 대부분의 사건은 가우시안 분포를 따름
-   가우시안 분포는 평균과 표준 편차에 따라 분포 모양이 결정됨
-   영상의 가우시안 필터에서는 주로 평균이 0인 가우시안 분포 함수를 이용
-   평균이 0이고 표준 편차가 시그마인 1차원 가우시안 분포
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/94288c5a-d838-4f15-8d77-d873f3942709/image.png)
-   세 개의 그래프가 모두 평균이 0 → x = 0에서 최댓값
    -   표준 편차가 작으면 그래프가 뾰족한 형태
    -   표준 편차가 크면 그래프가 넓게 퍼지면서 완만한 형태
-   가우시안 분포 함수 값은 특정 x가 발생할 수 있는 확률
    -   그래프 아래 면적을 모두 더하면 1이 됨
-   평균이 0인 1차원 가우시안 분포 함수 그래프
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c6a23666-e3bb-45df-9b32-54638d97bcca/image.png)

## 가우시안 필터

---

-   가우시안 분포를 따르는 2차원 필터 마스크 행렬을 생성 → 2차원 가우시안 분포 함수를 근사해야 함
-   2차원 가우시안 분포 함수는 x와 y 두 개의 변수를 사용
-   분포의 모양을 결정하는 평균과 표준 편차도 x축과 y축 방향에 따라 따로 설정
-   평균이 (0, 0)이고 x축과 y축 방향의 표준 편차가 각각 시그마\_x, 시그마\_y인 2차원 가우시안 분포 함수
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/17ef6c29-c356-4eae-9ee8-fa5eb2e3c34a/image.png)
-   평균이 (0, 0)이므로 그래프는 (0, 0)에서 최댓값, 평균에서 멀어질수록 함수가 감소
-   2차원 가우시안 분포 함수의 경우 → 함수 그래프 아래의 부피를 구하면 1
-   가우시안 필터는 이러한 2차원 가우시안 분포 함수로부터 구한 마스크 행렬을 사용
-   가우시안 분포 함수는 연속 함수이지만 이산형의 마스크를 만들기 위해서 x와 y값이 정수인 위치에서만 가우시안 분포 함수 값을 추출하여 마스크를 생성
-   평균이 0이고 표준 편차가 시그마인 가우시안 분포는 x가 -4시그마 부터 4시그마 사이인 구간에서 그 값의 대부분이 존재 → 가우시안 필터 마스크의 크기는 보통 (8시그마 + 1)로 결정
-   시그마\_x = 시그마\_y = 1.0 인 경우의 가우시안 필터 마스크
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8c730fc9-654a-43c4-b3bb-a2db6b2a3877/image.png)
-   필터 마스크를 이용하여 마스크 연산을 수행 → 필터링 대상 픽셀 근처에는 가중치를 크게 줌
-   필터링 대상 픽셀과 멀리 떨어져 있는 주변부 → 가중치를 조금만 줌 → 가중 평균(weighted average)을 구하는 것과 같음
-   가우시안 필터 마스크가 가중 평균을 구하기 위한 가중치 행렬 역할을 함
-   2차원 가우시안 분포 함수는 1차원 가우시안 분포 함수의 곱으로 분리
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/272b37a5-5460-4b5b-b46e-881648d02c1f/image.png)
    -   x축과 y축 방향의 1차원 가우시안 분포 함수의 곱으로 분리
    -   각각 1차원 마스크 연산을 수행
        -   표준 편차가 1.0인 1차원 가우시안 함수로부터 1x9 가우시안 마스크 행렬 g
        -   g의 전치 행렬로 필터링
        -   픽셀 하나에 대해 필요한 곱셈 연산 횟수가 18번으로 감소
-   가우시안 필터링을 수행하려면 GaussianBlur() 함수를 사용
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b71487c2-9dab-44af-b5d9-07fd68300bc6/image.png)
-   blurring_gaussian() 함수는 가우시안 표준 편차를 1부터 5까지 정수 단위로 증가 → rose.bmp 장미 영상에 대해 가우시안 필터링 수행
-   표준 편차 값이 커질수록 결과 영상이 더욱 부드럽게 변경

```python
def blurring_gaussian():
    src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    cv2.imshow('src', src)

    for sigma in range(1, 6):
        dst = cv2.GaussianBlur(src, (0, 0), sigma)

        desc = "Gaussian: sigma = %d" % (sigma)
        cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA)

        cv2.imshow('dst', dst)
        cv2.waitKey()

    cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/769e438a-f8f4-428f-8e69-12a3272b5391/image.png)

-   GaussianBlur() 함수 내부에서 가우시안 필터링을 구현할 때 → x축 방향과 y축 방향에 따라 1차원 가우시안 필터 마스크를 각각 생성하여 필터링을 수행
-   1차원 가우시안 필터 마스크를 생성하기 위해 OpenCV에서 제공하는 getGaussianKernel() 함수를 사용
    -   사용자가 지정한 표준 편차를 따르는 1차원 가우시안 필터 마스크 행렬을 생성하여 반환
    -   표준 편차가 sigma인 1차원 가우시안 분포 함수로부터 ksizex1 크기의 필터 마스크 행렬을 생성하여 반환
    -   ksize는 (8\*sigma + 1)보다 같거나 크게 지정하는 것이 좋음
    -   이 행렬의 원소에 저장되는 값은 다음 수식을 따름
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/368e26ef-41ea-49b6-8f2e-ee03a387c65f/image.png)
        -   i는 0부터 ksize-1 의 범위를 가짐, alpha는 G_i의 합 = 1 이 되도록 만드는 상수

# 샤프닝 : 영상 날카롭게 하기

---

## 언샤프 마스크 필터

---

-   샤프닝(sharpening)
    -   영상을 날카로운 느낌이 나도록 변경하는 필터링 기법
    -   날카로운 느낌의 영상
        -   초점이 잘 맞은 사진처럼 객체의 윤곽이 뚜렷하게 구분되는 영상
-   영상 에지 근방에서 픽셀 값의 명암비가 커지도록 수정
-   샤프닝을 구현하기 위해 블러링된 영상을 사용함
    -   블러링이 적용된 영상, 즉 날카롭지 않은 영상을 언샤프(unsharp)하다고 말함
-   언샤프한 영상을 이용하여 역으로 날카로운 영상을 생성하는 필터를 언샤프 마스크 필터(unsharp mask filter)라고 함

### 언샤프 마스크 필터의 동작 방식

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/eed07cc2-c2ed-477e-b1d2-e41631f8f67d/image.png)

-   g(x, y)는 입력 영상에서 블러링된 영상을 뺀 결과
    -   입력 영상에서 오직 날카로운 성분만을 가짐
-   입력 f(x, y)에 g(x, y)를 더함 → 날카로운 성분이 강조된 최종 영상 h(x, y)
-   g(x, y)에 실수 가중치를 곱한 후 더하면 날카로운 정도를 사용자가 조절 가능
    -   h(x, y) = f(x, y) + alpha\*g(x, y)
    -   alpha에 1.0을 지정 → 날카로운 성분을 그대로 한 번 더함
    -   alpha에 1.0보다 작은 값을 지정 → 조금 덜 날카로운 영상
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9efeaa02-4194-4289-ab07-3c59346d75fd/image.png)
-   OpenCV는 언샤프 마스크 필터 함수를 따로 제공하지 않음
-   /f(x, y)는 입력 영상에 블러링이 적용된 영상 → 평균값 필터, 가우시안 필터 사용해서 구함
-   가우시안 필터로 /f(x, y) 영상을 생성 → 가우시안 분포의 표준 편차를 어떻게 지정하느냐가 샤프닝 결과에 영향을 줌
-   rose.bmp 장미 영상을 다양한 표준 편차 값으로 가우시안 필터를 적용, 블러링된 영상을 이용하여 샤프닝 결과 영상을 생성
-   dst 영상이 장미꽃 경계 부분이 좀 더 뚜렷하게 구분이 됨
-   sigma 값이 커짐에 따라 다소 과장된 느낌의 샤프닝 결과 영상이 만들어질 수도 있으니 주의

```python
src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    exit()

cv2.imshow('src', src)

for sigma in range(1, 6):
    blurred = cv2.GaussianBlur(src, (0, 0), sigma)

    alpha = 1.0
    dst = cv2.addWeighted(src, 1 + alpha, blurred, -alpha, 0.0)

    desc = "sigma: %d" % sigma
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA)

    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/fe85ae03-9aff-4f62-ac4b-921fc308a3ae/image.png)

# 잡음 제거 필터링

---

## 영상과 잡음 모델

---

-   신호 처리 관점에서 잡음(noise)이란 원본 신호에 추가된 원치 않은 신호를 의미
-   영상에서 잡음은 주로 영상을 획득하는 과정에서 발생
-   디지털 카메라에서 사진을 촬영
    -   광학적 신호를 전기적 신호로 변환하는 센서(sensor)에서 주로 잡음이 추가됨
-   디지털 카메라에서 카메라 렌즈가 바라보는 장면을 원본 신호 s(x, y), 여기에서 추가되는 잡음을 n(x, y)
    -   f(x, y) = s(x, y) + n(x, y)
-   잡음이 생성되는 방식을 잡음 모델(noise model)이라고 함
    -   대표적인 잡음 모델은 가우시안 잡음 모델(Gaussian noise model)
        -   보통 평균이 0인 가우시안 분포를 따르는 잡음을 의미
-   표준 편차가 작은 가우시안 잡음 모델일수록 잡음에 의한 픽셀 값 변화가 적음
-   OpenCV 함수를 이용하여 영상에 가우시안 모델을 따르는 잡음을 인위적으로 추가
-   randn() 함수는 가우시안 잡음으로 구성된 행렬을 생성하여 반환
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/528e92bd-0041-4b58-ba1b-fc744865f3f3/image.png)
-   평균이 0인 가우시안 잡음을 생성
    -   양수와 음수가 섞여 있는 난수가 발생 → CV_32S, CV_32F처럼 부호 있는 자료형 행렬을 사용
-   noise_gaussian() 함수는 레나 영상에 평균이 0이고 표준 편차가 각각 10, 20, 30인 가우시안 잡음을 추가
    -   잡음이 추가된 결과 영상 dst가 거칠고 지저분해 보임
    -   표준 편차 stddev 값이 증가함 → 잡음의 영향이 커짐
    ```python
    def noise_gaussian():
        src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

        if src is None:
            print('Image load failed!')
            exit()

        cv2.imshow('src', src)

        for stddev in [10, 20, 30]:
            noise = np.zeros(src.shape, np.int32)
            cv2.randn(noise, 0, stddev)

            dst = cv2.add(src, noise, dtype=cv2.CV_8UC1)

            desc = 'stddev = %d' % stddev
            cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA)
            cv2.imshow('dst', dst)
            cv2.waitKey()

    cv2.destroyAllWindows()
    ```
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/41690dbe-af6f-40aa-b134-ca474813d2ca/image.png)

## 양방향 필터

---

-   가우시안 잡음을 제거하기 위해 가우시안 필터를 사용
-   입력 영상에서 픽셀 값이 크게 변하지 않는 평탄한 영역에 가우시안 필터가 적용될 경우
    -   주변 픽셀 값이 부드럽게 블러링되면서 잡음의 영향도 크게 줄어듦
-   픽셀 값이 급격하게 변경되는 에지 근방에 동일한 가우시안 필터가 적용되면
    -   잡음뿐만 아니라 에지 성분까지 함께 감소
    -   객체의 윤곽이 흐릿하게 바뀜
-   에지 정보는 그대로 유지하면서 잡음만 제거하는 에지 보전 잡음 제거 필터(edge-preserving noise removal filter)에 대해 연구함
-   양방향 필터(bilateral filter)는 에지 성분은 그대로 유지하면서 가우시안 잡음을 효과적으로 제거하는 알고리즘

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/569ec699-d025-4a14-9edd-826ffebc7fac/image.png)

-   f는 입력 영상, g는 출력 영상, p와 q는 픽셀의 좌표
-   f_p와 f_q는 각각 p점과 q점에서의 입력 영상 픽셀 값, g_p는 점 p에서의 출력 영상 픽셀 값
-   G*시그마s와 G*시그마r는 각각 표준 편차가 시그마\_s와 시그마\_r인 가우시안 분포 함수
-   S는 필터 크기, W_p는 양방향 필터 마스크 합이 1이 되도록 만드는 정규화 상수
-   두 개의 가우시안 함수 곱으로 구성된 필터
-   앞 가우시안 함수는 두 점 사이의 거리에 대한 가우시안 함수, 가우시안 필터와 완전히 같은 의미로 동작
-   뒤 가우시안 함수는 두 점의 픽셀 값 차이에 의한 가우시안 함수
    -   두 점의 픽셀 밝기 값의 차이가 적은 평탄한 영역에서는 큰 가중치를 가짐
    -   반면에 에지를 사이에 두고 있는 두 픽셀에 대해서는 가우시안 함수는 거의 0에 가까운 값이 됨
-   양방향 필터 수식이 픽셀 값의 차이에 의존적 → 양방향 필터 마스크는 영상의 모든 픽셀에서 서로 다른 형태를 가짐
-   모든 픽셀 위치에서 주변 픽셀과의 밝기 차이에 의한 고유의 필터 마스크 행렬을 만들어서 마스크 연산을 수행
-   일반적인 가우시안 블러링이 모든 위치에서 일정한 가우시안 마스크 행렬을 사용하는 것과 차이가 있음
-   양방향 필터는 가우시안 블러링보다 훨씬 많은 연산량을 필요로 함
-   OpenCV에서는 bilateralFilter() 함수를 이용하여 양방향 필터를 수행
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ae088038-fbf4-4458-bcd5-079130ecc451/image.png)
    -   sigmaSpace는 일반적인 가우시안 필터링에서 사용하는 표준 편차와 같은 개념
        -   값이 클수록 더 많은 주변 픽셀을 고려하여 블러링
    -   sigmaColor는 주변 픽셀과의 밝기 차이에 관한 표준 편차
        -   값을 작게 지정할 경우
            -   픽셀 값 차이가 큰 주변 픽셀은 블러링이 적용되지 않음
        -   값을 크게 지정하면
            -   픽셀 값 차이가 조금 크더라도 블러링이 적용됨
        -   sigmaColor 값을 이용하여 어느 정도 밝기 차를 갖는 에지를 보존할 것인지 조정할 수 있음

```python
def filter_bilateral():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    noise = np.zeros(src.shape, np.int32)
    cv2.randn(noise, 0, 5)
    cv2.add(src, noise, src, dtype=cv2.CV_8UC1)

    dst1 = cv2.GaussianBlur(src, (0, 0), 5)
    dst2 = cv2.bilateralFilter(src, -1, 10, 5)

    cv2.imshow('src', src)
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.waitKey()
    cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6d2a53e1-ff51-4032-86d2-0df5369dbf04/image.png)

-   src는 lenna.bmp 영상에 평균이 0이고 표준 편차가 5인 가우시안 잡음이 추가된 영상
-   src에 대해 표준 편차가 5인 가우시안 필터링을 수행한 결과가 dst1 영상
    -   지글거리는 잡음의 영향을 줄음, 머리카락, 모자, 배경 사물의 경계 부분이 함께 블러링되어 흐릿하게 변경됨
-   양방향 필터가 적용된 dst2는 사물의 경계는 그대로 유지됨

## 미디언 필터

---

-   입력 영상에서 자기 자신 픽셀과 주변 픽셀 값 중에서 중간값(median)을 선택하여 결과 영상 픽셀 값으로 설정하는 필터링 기법
-   마스크 행렬과 입력 영상 픽셀 값을 서로 곱한 후 모두 더하는 형태의 연산을 사용하지 않음
    -   주변 픽셀 값들의 중간값을 선택하기 위해 내부에서 픽셀 값 정렬 과정이 사용됨
-   미디언 필터는 특히 잡음 픽셀 값이 주변 픽셀 값과 큰 차이가 있는 경우에 효과적으로 동작
-   영상에 추가되는 잡음 중에 소금&후추 잡음(salt & pepper noise)은 픽셀 값이 일정 확률로 0 또는 255로 변경되는 형태의 잡음
    -   소금&후추 잡음이 추가된 영상에 미디언 필터를 적용하면
        -   대부분 소금&후추 잡음이 아닌 원본 영상에 존재하는 픽셀 값이 중간값으로 선택 → 잡음 효과적으로 제거
-   픽셀 값을 일렬로 늘여 세운 후 픽셀 값 크기 순으로 정렬
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/94466da6-d83a-4569-8f97-466de98cd9c2/image.png)
-   OpenCV에서는 medianBlur() 함수를 이용하여 미디언 필터링을 수행
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/f7b471ce-dffd-4e3e-9c49-323b089fd1f2/image.png)
    -   ksize x ksize 필터 크기를 이용하여 필터링을 수행
    -   다채널 영상인 경우 각 채널별로 필터링을 수행
    -   내부적으로 BORDER_REPLICATE 방식으로 가장자리 외곽 픽셀 값을 설정하여 필터링을 수행
-   filter_median() 함수는 입력 영상 전체 크기의 10%에 해당하는 픽셀에 소금&후추 잡음을 추가
-   가우시안 필터와 미디언 필터를 수행한 결과
    -   가우시안 블러링을 적용하여도 여전히 영상이 지저분
    -   미디언 필터를 적용한 dst2 영상에서는 잡음에 의해 추가된 흰색 또는 검은색 픽셀이 효과적으로 제거
    ```python
    def filter_median():
        src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

        if src is None:
            print('Image load failed!')
            return

        for i in range(0, int(src.size / 10)):
            x = random.randint(0, src.shape[1] - 1)
            y = random.randint(0, src.shapep[0] - 1)
            src[x, y] = (i % 2) * 255

        dst1 = cv2.GaussianBlur(src, (0, 0), 1)
        dst2 = cv2.medianBlur(src, 3)

        cv2.imshow('src', src)
        cv2.imshow('dst1', dst1)
        cv2.imshow('dst2', dst2)
        cv2.waitKey()
        cv2.destroyAllWindows()
    ```
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/37acffb3-f7f5-4fe1-8936-f79ea18ae361/image.png)

# 영상의 밝기 조절

---

-   그레이스케일 영상 다루기
    -   IMREAD_GRAYSCALE 플래그를 설정
    ```cpp
    Mat img1 = imread("lenna.bmp", IMREAD_GRAYSCALE);
    ```
    -   프로그램 동작 중 그레이스케일 영상을 저장할 새로운 공간을 생성하려면 CV_8UC1 타입으로 생성
    ```cpp
    Mat img2(480, 640, CV_8UC1, Scalar(0));
    ```
    -   컬러 영상을 변환하기 위해서는 cvtColor() 함수 사용
    ```cpp
    Mat img3 = imread("lenna.bmp", IMREAD_COLOR);
    Mat img4;
    cvtColor(img3, img4, COLOR_BGR2GRAY);
    ```
-   cvtColor() 함수
    -   OpenCV에서는 BGR 순서로 컬러 정보를 저장
    -   전달하는 인자는 차례대로 입력 영상, 출력 영상, 컬러 변환 코드
    -   COLOR_BGR2GRAY : BGR 3채널 컬러 영상을 1채널 그레이스케일 영상으로 변환
-   영상의 밝기(brightness) 조절
    -   영상의 전체적인 밝기를 조절하여 좀 더 밝거나 어두운 영상을 만드는 작업
-   영상의 밝기를 조절하려면
    -   입력 영상의 모든 픽셀에 일정 값을 더하거나 빼는 작업을 수행
    -   양수 값을 더하면 영상이 밝아지고
    -   반대로 양수 값을 빼면 영상이 어두워짐
-   영상의 밝기 조절을 수식으로 표현
    -   dst(x, y) = src(x, y) + n
    -   src : 입력 영상, dst : 출력 영상, n : 조절할 밝기 값
-   영상의 밝기 조절 함수의 그래프
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d278dabb-fdb8-4991-a700-94d86fc9e4c6/image.png)
    -   가로축은 입력 영상의 그레이스케일 값
    -   세로축은 출력 영상의 그레이스케일 값
-   원소 자료형이 가질 수 있는 값의 범위를 벗어나는 경우
    -   해당 자료형의 최솟값 또는 최댓값으로 원소 값을 설정하는 연산
        -   OpenCV에서 포화(saturate) 연산
        -   uchar 자료형을 사용하는 그레이스케일 영상에 대해 포화 연산
            -   saturate(x) = 0 ( x < 0 )
            -   = 255 ( x > 255 )
            -   = x ( 그 외 )
        -   실제로 영상의 밝기 조절을 구현할 때에는 포화 연산과 함께 고려한 수식을 사용
            -   dst(x, y) = saturate(src(x, y) + n)

```python
import numpy as np
import cv2

def brightness1():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    dst = cv2.add(src, 100)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
```

-   cv2의 add 함수 활용
    -   만약 영상을 전체적으로 어둡게 만들고 싶다면 뺄셈 적용
        ```python
        dst = cv.subtract(src, 100)
        ```

## 영상의 밝기 조절 직접 구현하기

---

```python
def brightness2():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    dst = np.empty(src.shape, src.dtype)
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = src[y, x] + 100

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
```

-   모든 픽셀을 방문하면서 픽셀 값에 일정한 상수를 더하거나 빼면 밝기 조절이 적용됨
-   사용자가 직접 결과 영상의 픽셀 값을 설정하기 위해서는
    -   적절한 크기와 타입의 결과 영상을 미리 생성해야함
-   밝기 조절을 직접 구현하기 위하여 이중 for 반복문을 이용
-   밝은 픽셀 주변에서 급격하게 어두운 픽셀이 나타나는 것은 포화 연산을 수행하지 않았기 때문
    -   정수 256을 16진수로 표현하면 0x00000100
    -   이 값을 unsigned char 자료형에 대입하면 하위 1바이트만 대입해서 0x00이 저장됨
    -   255보다 큰 값이 되는 픽셀은 오히려 픽셀 값이 0에 가까운 어두운 픽셀로 바뀌게 됨

```python
import numpy as np
import cv2

def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0

    return value

def brightness3():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    dst = np.empty(src.shape, src.dtype)
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = saturated(src[y, x] + 100)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
```

## 트랙바를 이용한 영상의 밝기 조절

---

```python
def brightness4():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    def update(pos):
        dst = cv2.add(src, pos)
        cv2.imshow('dst', dst)

    cv2.namedWindow('dst')
    cv2.createTrackbar('Brightness', 'dst', 0, 100, update)
    update(0)

    cv2.waitKey()
    cv2.destroyAllWindows()
```

# 영상의 명암비 조절

---

## 기본적인 명암비 조절 방법

---

-   명암비
    -   영상에서 밝은 영역과 어두운 영역 사이에 드러나는 밝기 차이의 강도
    -   명암 대비 또는 contrast 라고도 함
-   전반적으로 어둡거나 또는 전반적으로 밝은 픽셀로만 구성된 경우, 명암비가 낮다고 표현
    -   일반적으로 명암비가 낮은 영상은 객체 간의 구분이 잘 되지 않아서 전반적으로 흐릿함
-   밝은 영역과 어두운 영역이 골고루 섞여 있는 영상은 명암비가 높다고 말함
    -   사물의 구분이 잘 되며 선명한 느낌
-   수식에서 s = 0.5인 경우와 s = 2인 경우의 그래프
    -   dst(x, y) = saturate(s \* src(x, y))
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/fbe2d887-78b7-4bf0-b207-636821793a42/image.png)
-   입력 영상의 모든 픽셀 값에 2를 곱하여 결과 영상 생성

```python
def contrast1():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    s = 2.0
    dst = cv2.multiply(src, s)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
```

-   cv2의 multipy 함수를 사용하여 포화 연산을 함께 수행
-   전체적으로 픽셀 값이 포화 → 흰색으로 나타나는 영역이 너무 많아서 사물의 윤곽 구분이 더 어려워짐
    -   일정 상수를 단순히 곱하여 명암비를 조절하는 방식은 실전에서는 잘 사용되지 않음

## 효과적인 명암비 조절 방법

---

-   밝은 픽셀은 더욱 밝게, 어두운 픽셀은 더욱 어두워지게 변경
    -   픽셀 값이 밝고 어둡다의 기준을 어떻게 설정 → 결과 영상의 품질 차이 발생
-   Ex1) 그레이스케일 범위 중간값인 128을 기준으로 설정
-   Ex2) 영상의 평균 밝기를 구하여 기준으로 설정
-   픽셀 값 변경 방식을 수식으로 정리한 결과
    -   dst(x, y) = src(x, y) + (src(x, y) - 128)\*alpha
        -   항상 (128, 128) 좌표를 지나고 알파에 의해 기울기가 변경되는 직선의 방정식
        -   알파의 범위가 -1 ≤ 알파 ≤ 0 이면 기울기가 0부터 1 사이의 직선이 됨 → 명암비를 감소시키는 변환
        -   알파 > 0 이면 기울기가 1보다 큰 직선의 방정식 → 명암비를 증가시키는 변환
    -   수식에 의해 계산되는 결과 영상의 픽셀 값은 0보다 작거나 255보다 커지는 경우가 발생할 수 있으므로 포화 연산 필요
        -   dst(x, y) = saturate(src(x, y) + (src(x, y) - 128)\*alpha)
-   알파 = -0.5 인 경우와 알파 = 1.0 인 경우의 함수 그래프
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/26a5ac90-2737-4504-8738-fce1adae03ba/image.png)
-   alpha 값 1.0을 사용하여 레나 영상의 명암비를 증가시킴

```python
def contrast2():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    alpha = 1.0
    dst = cv2.convertScaleAbs(src, alpha=1+alpha, beta=-128*alpha)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
```

# 히스토그램 분석

---

## 히스토그램 구하기

---

-   영상의 히스토그램(histogram)
    -   영상의 픽셀 값 분포를 그래프 형태로 표현한 것
-   그레이스케일 영상의 경우
    -   각 그레이스케일 값에 해당하는 픽셀의 개수를 구하고 이를 막대 그래프 형태로 표현함
-   컬러 영상
    -   세 개의 색상 성분 조합에 따른 픽셀 개수를 계산
-   각각의 밝기에 해당하는 픽셀 개수를 세어서 막대그래프 형태로 표현한 히스토그램
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/24cc5856-47bd-446e-bdfe-cb21e5211917/image.png)
-   히스토그램 그래프에서 가로축을 히스토그램의 빈(bin)이라고 함
    -   원본 영상이 0부터 7 사이의 픽셀 값을 가질 수 있기 때문에 8개의 빈
-   그레이스케일 영상
    -   256개의 빈을 갖는 히스토그램을 구하는 것이 일반적
-   경우에 따라서는 히스토그램의 빈 개수를 픽셀 값 범위보다 작게 설정할 수도 있음
    -   빈 개수가 줄어들면 히스토그램이 표현하는 영상의 픽셀 값 분포 모양이 좀 더 대략적인 형태로 바꾸미
    -   빈 개수가 많으면 세밀한 픽셀 값 분포 표현이 가능
-   OpenCV에서 영상의 히스토그램을 구하려면 calcHist() 함수를 사용
    -   한 장의 영상뿐만 아니라 여러 장의 영상으로부터 히스토그램 도출 가능
    -   여러 채널로부터 히스토그램을 구할 수도 있음
    -   히스토그램 빈 개수도 조절할 수 있음

### calcHist() 함수

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/659063e9-fd5d-4edf-82ff-aa7880417819/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/02aea9e1-d0a9-4d17-82af-4afa6ff42278/image.png)

-   등간격 히스토그램
    -   빈(bin)이 표현하는 밝기 값 간격이 균일하다는 의미
-   Python의 경우 위 의 호출 형식보다 간결함
-   여러 장의 영상을 입력으로 받을 수 있음 → 영상들의 list 형태로 전달
-   채널의 경우에도 multi channel인 경우가 있음 → list 형태로 전달
-   hintSize의 경우 각 차원별 히스토그램의 크기를 나타냄 → list 형태로 전달

```python
def calcGrayHist(img):
    channels = [0]
    hintSize = [256]
    hintRange = [0, 256]

    hist = cv2.calcHist([img], channels, None, hintSize, hintRange)

    return hist
```

-   calcGrayHist() 함수는 내부에서 OpenCV 함수 calcHist()를 이용하여 그레이스케일 영상의 히스토그램을 표현하는 행렬 hist를 구하여 반환
    -   반환되는 hist는 CV_32FC1 타입을 갖는 256x1 크기의 행렬
    -   hist 행렬의 행 개수는 256이고, 열 개수는 1
-   calcGrayHist() 함수로 구한 히스토그램 행렬을 막대그래프 형태로 나타내려면
    -   직접 hist 행렬을 참조하여 막대그래프 영상을 생성해야 함
-   getGrayHistImage() 함수는 히스토그램 그래프에서 최대 빈도수를 표현하는 막대그래프 길이가 100픽셀이 되도록 그래프를 그림
    -   흰색으로 초기화 된 256 x 100 크기의 영상 imgHist를 생성
    -   for문과 line() 함수를 이용하여 그래프를 그림
    -   히스토그램 영상 imgHist를 반환
    ```python
    def getGrayHistImage(hist):
        _, histMax, _, _ = cv2.minMaxLoc(hist)

        imgHist = np.ones((100, 256), np.uint8) * 255
        for x in range(imgHist.shape[1]):
            pt1 = (x, 100)
            pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
            cv2.line(imgHist, pt1, pt2, 0)

        return imgHist
    ```
    -   hist 행렬 원소의 최댓값을 찾기 위해 minMaxLoc() 함수를 사용
        -   관심이 없는 최솟값 등의 경우 \_로 받아서 처리
    -   히스토그램 행렬의 최댓값 위치에서 100픽셀에 해당하는 검은색 직선을 그림
    -   나머지 히스토그램 막대그래프는 100픽셀보다 짧은 길이의 직선으로 표현됨
-   calcGrayHist() 함수와 getGrayHistImage() 함수를 사용하여 camera.bmp 카메라맨 영상의 히스토그램을 화면에 출력
    ```cpp
    Mat src = imread("camera.bmp", IMREAD_GRAYSCALE);
    Mat hist = calcGrayHist(src);
    Mat hist_img = getGrayHistImage(hist);

    imshow("src", src);
    imshow("srcHist", hist_img);
    ```

## 히스토그램 분석

---

-   히스토그램의 픽셀 분포 그래프는 영상의 밝기와 명암비를 가늠할 수 있는 유용한 도구

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/23ef38c2-a171-495d-a64a-4f898493ed15/image.png)

-   영상 특성에 따른 히스토그램 분석

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a39934e4-3b76-497b-9185-f154fe09d01a/image.png)

## 히스토그램 스트레칭

---

-   영상의 히스토그램이 그레이스케일 전 구간에 걸쳐서 나타나도록 변경하는 선형 변환 기법
-   히스토그램을 마치 고무줄을 잡아 늘이듯이 펼쳐서 히스토그램 그래프가 그레이스케일 전 구간에서 나타나도록 변환하는 기법
-   히스토그램 스트레칭을 수식으로 표현
    -   dst(x, y) = ( src(x, y) - G_min ) / ( G_max - G_min ) x 255
-   src와 dst는 각각 입력 영상과 출력 영상
-   G_min과 G_max는 입력 영상의 픽셀 값 중에서 가장 큰 그레이스케일 값과 가장 작은 그레이스케일 값
-   원본 영상의 히스토그램 분포는 G_min과 G_max 사이에서만 나타남
    -   이를 양방향으로 늘려서 G_min → 0, G_max → 255로 변환
-   (G_min, 0)과 (G_max, 255)를 지나는 직선의 방정식을 구해서 이를 변환함수로 사용
    -   직선의 기울기 → 255 / (G_max - G_min)
    -   Y 절편 → -255 x G_min / (G_max - G_min)
-   히스토그램 스트레칭을 위한 함수는 OpenCV에서 따로 제공 안함
-   G_min과 G_max 값은 minMaxLoc() 함수를 사용해서 구함

```python
def histogram_stretching():
    src = cv2.imread('hawkes.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    gmin, gmax, _, _ = cv2.minMaxLoc(src)

    dst = cv2.convertScaleAbs(src, alpha=255.0/(gmax - gmin), beta=-gmin * 255.0/(gmax - gmin))

    cv2.imshow('src', src)
    cv2.imshow('srcHist', getGrayHistImage(calcGrayHist(src)))

    cv2.imshow('dst', dst)
    cv2.imshow('dstHist', getGrayHistImage(calcGrayHist(dst)))

    cv2.waitKey()
    cv2.destroyAllWindows()
```

-   히스토그램 스트레칭이 수행된 결과 영상 dst는 어두운 영역과 밝은 영역이 골고루 분포
-   dstHist 창에 나타난 결과 영상의 히스토그램은 입력 영상의 히스토그램이 양 옆으로 늘어난 듯한 형태

## 히스토그램 평활화

---

-   영상의 픽셀 값 분포가 그레이스케일 전체 영역에서 골고루 나타나도록 변경하는 알고리즘
-   히스토그램 그래프에서 특정 그레이스케일 값 근방에서 픽셀 분포가 너무 많이 뭉쳐있는 경우 이를 넓게 펼쳐 주는 방식으로 픽셀 값 분포를 조절
-   히스토그램 균등화 또는 히스토그램 평탄화라는 용어로도 사용
-   h(g)는 영상에서 그레이스케일 값이 g인 픽셀 개수
-   히스토그램 평활화를 계산하기 위해서는 h(g)로부터 히스토그램 누적 함수 H(g)를 구해야함
-   H(g) 값의 범위가 보통 그레이스케일 값의 범위(0~255)보다 훨씬 크기 때문에 함수의 최댓값이 255가 되도록 정규화
-   입력 영상의 픽셀 개수를 N, 영상이 가질 수 있는 최대 밝기를 L_max, 일반적으로 그레이스케일 영상은 L_max = 255
    -   dst(x, y) = round( H(src(x, y)) x L_max / N )
    -   round() 는 반올림 함수
-   OpenCV는 그레이스케일 영상의 히스토그램 평활화를 수행하는 equalizeHist() 함수를 제공

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/79d0445f-e37d-469f-a1ce-989ac4098094/image.png)

-   그레이스케일 영상만 입력으로 받음
    -   3채널로 구성된 컬러 영상을 equalizeHist() 함수 입력으로 전달하면 에러 발생

```python
def histogram_equalization():
    src = cv2.imread('hawkes.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    dst = cv2.equalizeHist(src)

    cv2.imshow('src', src)
    cv2.imshow('srcHist', getGrayHistImage(calcGrayHist(src)))

    cv2.imshow('dst', dst)
    cv2.imshow('dstHist', getGrayHistImage(calcGrayHist(dst)))

    cv2.waitKey()
    cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a1ced79b-bb89-47ff-ac87-56c025097abf/image.png)

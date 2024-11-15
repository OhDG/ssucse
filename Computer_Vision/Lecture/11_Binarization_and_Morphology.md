# 영상의 이진화

## 이진화 (Binarization)

-   영상의 각 픽셀을 두 개의 분류로 나누는 작업
    -   주요 객체 영역 ↔ 배경 영역
    -   중요도가 높은 관심 영역(ROI, Region Of Interest) ↔ 그렇지 않은 비관심 영역
-   디지털 컴퓨팅 분야에서 이진화
    -   입력 값을 0 또는 1로 설정
-   영상의 이진화
    -   픽셀 값을 0 또는 255로 설정
-   이진화가 적용된 이진 영상
    -   보통 흰색과 검은색 픽셀로만 구성됨
-   영상의 이진화는 기본적으로 영상의 각 픽셀 값을 이용
    -   영상의 픽셀 값이 특정 값보다 크면 255로
    -   작으면 0으로 설정
    -   각 픽셀과의 크기 비교 대상이 되는 값을 임계값(threshold) 또는 문턱치라고 함
        -   임계값은 그레이스케일 범위인 0~255 사이의 정수
            -   사용자의 경험에 의해 임의로 지정
            -   영상의 특성을 분석하여 자동으로 결정
        -   임계값은 영상의 이진화를 수행하는 목적에 따라 적절하게 결정해야 함

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4cbb0f0b-d54c-49df-be91-6b2bf9665fd6/image.png)

-   OpenCV에서 이진화는 threshold() 함수를 이용
    -   임계값을 이용한 다양한 연산을 지원
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7e2f013d-ede5-4a65-b9c0-9979c443c55c/image.png)
-   주요 ThresholdTypes 열거형 상수
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5eeb5183-cbb4-49d1-9a27-d2a7886d1f9b/image.png)
-   threshold() 함수를 이용하여 영상을 이진화 → maxval 인자에 255를 지정함
-   THRESH_BINARY 또는 THRESH_BINARY_INV를 지정
-   THRESH_BINARY_INV 방법으로 이진화 == THRESH_BINARY 방법으로 이진화를 수행한 후 영상을 반전
-   문서 영상을 임계값 128을 이용하여 이진화를 수행

    ```cpp
    Mat src = imread("document.bmp", IMREAD_GRAYSCALE);

    Mat dst;
    threshold(src, dst, 128, 255, THRESH_BINARY);
    ```

-   OpenCV에서는 객체를 흰색, 배경을 검은색으로 취급하는 경우가 많음
    -   상황에 따라 THRESH_BINARY와 THRESH_BINARY_INV를 적절하게 선택
-   THRESH_OTSU와 THRESH_TRIANGLE는 임계값을 자동으로 결정할 때 사용
    -   영상의 픽셀 값 분포를 분석 → 임계값을 자동으로 결정
    -   보통 논리합 연산자(|)를 이용하여 앞선 다섯 개의 ThresholdTypes 상수와 함께 사용함
    -   자동 이진화를 수행할 경우
        -   threshold() 함수 내부에서 임계값을 자체적으로 계산하여 사용
        -   threshold() 함수의 세 번째 인자로 전달한 thresh 값은 사용되지 않음
    -   자동 임계값 결정 방법은 CV_8UC1 타입의 영상에만 적용할 수 있음
-   THRESH_OTSU
    -   오츠(Otsu)가 제안한 자동 이진화 임계값 결정 알고리즘을 이용
    -   입력 영상의 픽셀 값 분포가 두 개의 부류로 구분되는 경우에 최적
-   camera.bmp 영상에 대해 오츠 방법으로 임계값을 결정하여 자동 이진화를 수행

    ```cpp
    Mat src = imread("camera.bmp", IMREAD_GRAYSCALE);

    Mat dst;
    int th = (int)threshold(src, dst, 0, 255,
    	THRESH_BINARY | THRESH_OTSU);
    ```

## (실습) 이진화 (Binarization)

```python
def on_threshold(pos):
    _, dst = cv2.threshold(src, pos, 255,
	    cv2.THRESH_BINARY)
    cv2.imshow('dst', dst)

filename = 'neutrophils.png'
if len(sys.argv) > 1:
    filename = sys.argv[1]

src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    exit()

cv2.imshow('src', src)

cv2.namedWindow('dst')
cv2.createTrackbar('Threshold', 'dst', 0, 255,
	on_threshold)
cv2.setTrackbarPos('Threshold', 'dst', 128)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

## 적응형 이진화

-   전역 이진화(global binarization)
    -   영상의 모든 픽셀에 같은 임계값을 적용하여 이진화를 수행하는 방식
    -   영상의 특성에 따라서 전역 이진화를 적용하기 어려운 경우가 있음
-   적응형 이진화(adaptive binarization)
    -   각 픽셀마다 서로 다른 임계값을 사용
    -   영상의 모든 픽셀에서 정해진 크기의 사각형 블록 영역을 설정 → 블록 영역 내부의 픽셀 값 분포로부터 고유의 임계값을 결정하여 이진화

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6b9dc353-50f0-424a-b6e8-2d854bedb395/image.png)

-   OpenCV에서 적응형 이진화는 adaptiveThreshold() 함수를 이용
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d5df5602-ae7b-41c7-8022-7a2c72337f7c/image.png)

## (실습) 적응형 이진화

```python
def on_trackbar(pos):
    bsize = pos
    if bsize % 2 == 0:
        bsize = bsize - 1
    if bsize < 3:
        bsize = 3

    dst = cv2.adaptiveThreshold(src, 255,
	    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
		    bsize, 5)

    cv2.imshow('dst', dst)

src = cv2.imread('sudoku.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    exit()

cv2.imshow('src', src)

cv2.namedWindow('dst')
cv2.createTrackbar('Block Size', 'dst', 0, 200,
	on_trackbar)
cv2.setTrackbarPos('Block Size', 'dst', 11)

cv2.waitKey()
cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a8b02f71-96cf-403b-bfea-9d5e6c6553ab/image.png)

-   (a) : 입력 영상
-   (b) : 블록 크기가 11
-   (c) : 블록 크기가 51

# 모폴로지 연산

## 모폴로지 (Morphology)

-   형태 또는 모양에 관한 학문
-   영상 처리 분야에서 모폴로지
    -   영상에서 객체의 형태 및 구조에 대해 분석하고 처리하는 기법
    -   수학적 모폴로지(mathematical morphology)라고도 함
-   모폴로지 기법
    -   그레이스케일 영상과 이진 영상에 대하여 모두 적용할 수 있음
    -   주로 이진 영상에서
        -   객체의 모양을 단순화
        -   잡음을 제거
-   구조 요소(structuring element)를 정의
    -   구조 요소는 모폴로지 연산의 동작을 결정하는 작은 크기의 행렬

## 구조 요소

-   대부분의 모폴로지 연산
    -   3x3 정방형 구조 요소를 사용
-   각각의 구조 요소 행렬에서 진한 색으로 표시한 원소
    -   모폴로지 연산 결과가 저장될 위치를 나타내는 고정점(anchor point)
-   대부분의 경우 구조 요소의 중심을 고정점으로 사용

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/76189602-2efb-4cd6-9b0e-0d7b3ef2b0a6/image.png)

## 침식(erosion)과 팽창(dilation)

-   영상의 모폴로지 기법 중에서 가장 기본이 되는 연산
-   이진 영상의 침식 연산
    -   객체 영역의 외곽을 골고루 깎아내는 연산
    -   전체적으로 객체 영역은 축소, 배경은 확대
    -   구조 요소를 영상 전체에 대해 스캔
    -   구조 요소가 객체 영역 내부에 완전히 포함될 경우
        -   고정점 위치 픽셀을 255로 설정함
-   이진 영상의 팽창 연산
    -   객체 외곽을 확대하는 연산
    -   객체 영역은 확대, 배경 영역은 줄어듦
    -   구조 요소를 영상 전체에 대해 이동시키면서
        -   구조 요소와 객체 영역이 한 픽셀이라도 만날 경우
            -   고정점 위치 픽셀을 255로 설정함

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/98216f84-2e91-4848-b123-ff7b7bdf2367/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/3bc76e87-8c45-4c36-87c1-58fdf60ebd89/image.png)

-   (c) : 침식 연산
    -   객체 윗부분에 작게 튀어나온 부분 제거됨
-   (d) : 팽창 연산
    -   객체 아래쪽에 작게 패인 부분 메워짐
-   OpenCV에서 구조 요소
    -   원소 값이 0 또는 1로 구성된 CV_8UC1 타입의 Mat 행렬로 포현
        -   구조 요소 행렬에서 값이 1인 원소만을 이용하여 구조 요소의 모양을 결정
    -   getStructuringElement() 함수
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c5cf11bd-767d-48f7-b7f2-5af2c611905a/image.png)
        -   구조 요소의 크기는 ksize 인자를 통해 지정 - 가로와 세로 크기를 모두 홀수로 지정
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2c245407-e7db-4f43-ae4d-357e36a80d72/image.png)
-   OpenCV에서 영상의 침식 연산
    -   erode() 함수
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1d186f1e-021b-4a3e-ba0d-02f68241ee9d/image.png)
-   OpenCV에서 팽창 연산
    -   dilate() 함수
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8f4f3764-59ac-4f3e-b80d-2cdb9697d924/image.png)

## (실습) 이진 영상의 침식과 팽창

```python
def erode_dilate():
    src = cv2.imread('milkdrop.bmp',
	    cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    _, src_bin = cv2.threshold(src, 0, 255,
	    cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    dst1 = cv2.erode(src_bin, None)
    dst2 = cv2.dilate(src_bin, None)

    plt.subplot(221), plt.axis('off'),
	    plt.imshow(src, 'gray'), plt.title('src')
    plt.subplot(222), plt.axis('off'),
	    plt.imshow(src_bin, 'gray'), plt.title('src_bin')
    plt.subplot(223), plt.axis('off'),
	    plt.imshow(dst1, 'gray'), plt.title('erode')
    plt.subplot(224), plt.axis('off'),
	    plt.imshow(dst2, 'gray'), plt.title('dilate')
    plt.show()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/668bdbb8-cf48-4d93-8284-fa757d0c4ea4/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/61b34fa2-0587-4e02-a213-76adc2a7266a/image.png)

## 이진 영상의 열기와 닫기

-   열기 연산
    -   입력 영상에 대하여 침식 연산을 수행한 후, 다시 팽창 연산을 수행하는 연산
    -   침식 연산 먼저 수행 → 한두 픽셀짜리 영역이 제거된 후, 팽창 연산이 수행됨
    -   입력 이진 영상에 존재하는 작은 크기의 객체가 효과적으로 제거됨
-   닫기 연산
    -   팽창 연산을 먼저 수행한 후, 다시 침식 연산을 수행하는 연산
    -   팽창 연산 먼저 수행 → 객체 내부의 작은 구멍이 메워진 후, 침식 연산이 수행됨
    -   객체 내부의 작은 구멍을 제거함
-   열기와 닫기 연산은 각각 침식과 팽창 연산이 한 번씩 적용 → 객체 영역의 크기가 크게 바뀌지 않음
    -   침식과 팽창 연산을 적용하는 순서에 따라 서로 다른 효과 발생

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b9860ad2-719f-4078-9e91-30ee5736a30f/image.png)

-   (b) : 열기 연산
    -   큰 객체 외곽에 돌출된 한두 픽셀이 제거됨
    -   두 개의 객체를 연결하는 가느다란 선도 제거됨
    -   한두 픽셀짜리 독립된 객체도 깔끔하게 제거됨
-   (c) : 닫기 연산
    -   객체 내부의 작은 구멍이 사라짐
    -   오른쪽 객체 외곽에 한 픽셀 오목하게 들어간 부분이 매끈하게 채워짐
-   OpenCV에서 열기와 닫기 연산
    -   morphologyEx() 함수
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7e5bace7-94cb-41b9-b2a3-f66f082e2cda/image.png)
    -   MORPH_GRADIENT 상수
        -   팽창 결과 영상에서 침식 결과 영상을 빼는 연산을 수행
        -   객체의 외곽선이 추출되는 효과
    -   MorphTypes 열거형 상수
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7fa8d51e-d17c-41d7-8c48-b91f3c3713db/image.png)

## (실습) 이진 영상의 열기와 닫기

```python
def open_close():
    src = cv2.imread('milkdrop.bmp',
	    cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    _, src_bin = cv2.threshold(src, 0, 255,
	    cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    dst1 = cv2.morphologyEx(src_bin,
	    cv2.MORPH_OPEN, None)
    dst2 = cv2.morphologyEx(src_bin,
	    cv2.MORPH_CLOSE, None)

    plt.subplot(221), plt.axis('off'),
	    plt.imshow(src, 'gray'), plt.title('src')
    plt.subplot(222), plt.axis('off'),
	    plt.imshow(src_bin, 'gray'), plt.title('src_bin')
    plt.subplot(223), plt.axis('off'),
	    plt.imshow(dst1, 'gray'), plt.title('open')
    plt.subplot(224), plt.axis('off'),
	    plt.imshow(dst2, 'gray'), plt.title('close')
    plt.show()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e996d034-9743-420f-b058-7dead372feed/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b9bbba82-ffb0-4b6f-9392-8d85aa6b800c/image.png)

-   (c) : 열기 연산
    -   우측 하단에 있던 자잘한 한두 픽셀 영역이 효과적으로 제거
-   (d) : 닫기 연산
    -   흰색 객체 내부의 한두 픽셀짜리 구멍이 사라짐

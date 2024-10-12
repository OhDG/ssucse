# OpenCV

---

## OpenCV의 역사

---

-   1999 : 개발 시작
    -   인텔 주도로 개발 시작
    -   이후 오픈 소스로 전환됨
-   2006 : OpenCV 1.0
    -   C로 구현 : 함수 & 구조체
    -   IpIImage 구조체
-   2009 : OpenCV 2.0
    -   C++로 전환 : 클래스
    -   Mat 클래스
-   2015 : OpenCV 3.0
    -   OpenCV 프로젝트 구조 개선
    -   GPU, IPP 활용 확대
-   2017 : OpenCV 3.3
    -   DNN 모듈 지원
-   2018 : OpenCV 4.0
    -   C++ 11/14/17 지원
    -   DNN 지원 강화

## OpenCV 모듈

---

-   OpenCV 라이브러리는 다수의 모듈(module)로 구성
    -   모듈은 다양한 클래스와 함수를 그 기능과 성격에 따라 모아서 만들어 놓은 OpenCV의 부분 라이브러리

## OpenCV로 이미지 불러오기

---

-   imread() 함수
    ```python
    import cv2 as cv

    img = cv.imread('lenna.bmp')

    if img is None:
    	print('Image load failed!')
    	exit()

    cv.imshow('image', img)
    cv.waitKey()
    ```
    -   filename 영상 파일을 불러와 Mat 객체로 변환하여 반환
    -   filename 인자의 타입으로 지정된 String은 std::string의 이름 재정의
    -   두 번째 인자 flags는 영상 파일을 불러올 때 사용할 컬러 모드와 영상 크기를 지정하는 플래그
    -   flags 인자에는 ImreadModes 열거형 상수를 지정 가능
    -   flags 인자는 기본값으로 IMREAD_COLOR가 지정되어 있음

## OpenCV 주요 함수

---

-   imwrite() 함수
    -   저장되어 있는 영상 데이터를 파일로 저장하기 위해서 사용

# Matrix 연산

---

## 이미지 타입 확인하기

---

```python
import numpy as np
import cv2 as cv

def func1():
	img1 = cv.imread('cat.bmp', cv.IMREAD_GRAYSCALE)

	if img1 is None:
		print('Image load failed!')
		return

	print('type(img1):', type(img1))
	print('img1.shape:', img1.shape)

	if len(img1.shape) == 2:
		print('img1 is a grayscale image')
	elif len(img1.shape) == 3:
		print('img1 is a truecolor image')

	cv.imshow('img1', img1)
	cv.waitKey()
	cv.destroyAllWindows()

func1()
```

-   cv.IMREAD_GRAYSCALE
    -   흑백으로 로드
-   img1의 type?
    -   numpy.ndarray
-   img1의 shape?
    -   (480, 640)
-   Shape의 len으로 타입 확인 가능

## 행렬의 초기화

---

```python
import numpy as np
import cv2 as cv

def func2():
	img1 = np.empty((480, 640), np.uint8) # grayscale image
	img2 = np.zeros((480, 640, 3), np.uint8) # color image
	img3 = np.ones((480, 640), np.int32) # 1's matrix
	img4 = np.full((480, 640), 0, np.float32) # Fill with 0.0

	mat1 = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]).astype(np.uint8)
	mat1[0, 1] = 100 # element at x=1, y=0
	mat1[2, :] = 200
	print(mat1)

func2()
```

## 행렬의 복사

---

```python
import numpy as np
import cv2 as cv

def func3():
	img1 = cv.imread('cat.bmp')

	img2 = img1
	img3 = img1.copy()

	img1[:, :] = (0, 255, 255) # yellow

	cv.imshow('img1', img1)
	cv.imshow('img2', img2)
	cv.imshow('img3', img3)
	cv.waitKey()
	cv.destroyAllWindows()

func3()
```

## 부분 행렬 추출

---

```python
import numpy as np
import cv2 as cv

def func4():
	img1 = cv.imread('lenna.bmp', cv.IMREAD_GRAYSCALE)

	img2 = img1[200:400, 200:400]
	img3 = img1[200:400, 200:400].copy()

	img2 += 20

	cv.imshow('img1', img1)
	cv.imshow('img2', img2)
	cv.imshow('img3', img3)
	cv.waitKey()
	cv.destroyAllWindows()

func4()
```

## 부분 행렬 추출 후 반전

---

-   색상 반전 → 255 - 원래 값

## 행렬 연산하기

---

```python
import numpy as np
import cv2 as cv

def func6():
	mat1 = np.ones((3, 4), np.int32) # 1's matrix
	mat2 = np.arrange(12).reshape(3, 4)
	mat3 = mat1 + mat2
	mat4 = mat2 * 2

	print("mat1:")
	print(mat1)
	print("mat2:")
	print(mat2)
	print("mat3:")
	print(mat3)
	print("mat4:")
	print(mat4)

func6()
```

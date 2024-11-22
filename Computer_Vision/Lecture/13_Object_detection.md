# 템플릿 매칭

## 템플릿 매칭

-   영상에서 작은 크기의 부분 영상 위치를 찾아내고 싶은 경우
    -   템플릿 매칭(template matching) 기법을 사용
-   템플릿(template)
    -   찾고자 하는 대상이 되는 작은 크기의 영상
-   템플릿 매칭
    -   작은 크기의 템플릿 영상을 입력 영상 전체 영역에 대해 이동하면서 가장 비슷한 위치를 수치적으로 찾아내는 방식
    -   템플릿 영상과 입력 영상 부분 영상과의 유사도(similarity) 또는 비유사도(dissimilarity)를 계산

## 템플릿 매칭 동작 원리

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/f3b31036-efc8-4007-a50b-3e92b8b5d953/image.png)

-   (b) : 입력 영상의 모든 위치에서 템플릿 영상과의 유사도를 계산
    -   결과를 그레이스케일 영상 형태로 나타냄
    -   가장 밝은 픽셀 위치가 템플릿 영상과 가장 유사한 부분

## 템플릿 매칭

-   OpenCV에서는 matchTemplate() 함수
    -   템플릿 매칭을 수행할 수 있음
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5cb80556-01fe-4dec-a135-f3c4c30ac92b/image.png)
    -   템플릿 영상과 입력 영상 간의 비교 방식
        -   method 인자로 설정
    -   TM_SQDIFF : 제곱차(squared difference) 매칭 방법
        -   두 영상이 완벽하게 일치 → 0
        -   서로 유사하지 않으면 → 0보다 큰 양수
    -   TM_CCORR : 상관관계(correlation) 매칭 방법
        -   두 영상이 유사하면 → 큰 양수
        -   유사하지 않으면 → 작은 값
    -   TM_CCOEFF : 상관계수(correlation coefficient) 매칭 방법
        -   두 영상을 미리 평균 밝기로 보정한 후 상관관계 매칭을 수행
        -   두 영상이 유사하면 → 큰 양수
        -   유사하지 않으면 → 0에 가까운 양수 또는 음수
    -   TM_SQDIFF, TM_CCORR, TM_CCOEFF 방법에 대해 각각 영상의 밝기 차이 영향을 줄여 주는 정규화 수식을 추가
        -   TM_SQDIFF_NORMED, TM_CCORR_NORMED, TM_CCOEFF_NORMED
        -   TM_CCORR_NORMED
            -   매칭 결과값이 0에서 1 사이의 실수로 나타남
        -   TM_CCOEFF_NORMED
            -   매칭 결과값이 -1에서 1 사이의 실수로 나타남
        -   TM_CCORR_NORMED, TM_CCOEFF_NORMED
            -   1에 가까울수록 매칭이 잘 되었음을 의미

## TemplateMatchModes 열거형 상수

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0bab01c0-d96d-4de8-81b7-6266e0b9f2e5/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/686e5d11-58c3-4209-aa38-75714aad39c9/image.png)

## 템플릿 매칭

-   정규화된 상관계수 매칭 방법 → 좋은 결과를 제공하는 것으로 알려짐
    -   계산 수식이 가장 복잡 → 실제 동작 시 연산량이 많을 수 있음
-   제곱차 매칭 방법을 사용
    -   result 결과 행렬에서 최솟값 위치를 가장 매칭이 잘 된 위치로 선택해야 함
-   상관관계 또는 상관계수 매칭 방법을 사용
    -   result 결과 행렬에서 최댓값 위치가 가장 매칭이 잘된 위치
-   result 행렬에서 최솟값 위치 또는 최댓값 위치
    -   OpenCV의 minMaxLoc() 함수를 이용

## (실습) 템플릿 매칭

```python
img = cv2.imread('circuit.bmp', cv2.IMREAD_COLOR)
temp1 = cv2.imread('crystal.bmp', cv2.IMREAD_COLOR)

if img is None or temp1 is None:
    print('Image load failed!')
    sys.exit()

img = img + (50, 50, 50)

noise = np.zeros(img.shape, np.int32)
cv2.randn(noise, 0, 10)
img = cv2.add(img, noise, dtype=cv2.CV_8UC3)

res = cv2.matchTemplate(img, temp1,
	cv2.TM_CCOEFF_NORMED)
res_norm = cv2.normalize(res, None, 0, 255,
	cv2.NORM_MINMAX, cv2.CV_8U)

_, maxv, _, maxloc = cv2.minMaxLoc(res)
print('maxv:', maxv)

(th, tw) = temp1.shape[:2]
cv2.rectangle(img, maxloc,
	(maxloc[0] + tw, maxloc[1] + th), (0, 0, 255), 2)

cv2.imshow('temp1', temp1)
cv2.imshow('res_norm', res_norm)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/583f063c-3136-42e5-86e5-155afb412de9/image.png)

-   (a) : 입력 영상인 circuit.bmp
-   (b) : 템플릿인 crystal.bmp

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/94508b8a-7fba-48bb-9eea-88820536bf57/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/eccc425c-b78d-4383-8a39-fa444522469c/image.png)

-   (b) : 템플릿 매칭으로 계산된 유사도 행렬을 그레이스케일 형식 영상으로 나타낸 res_norm 영상
    -   TM_CCOEFF_NORMED 방식으로 템플릿 매칭을 수행 → 템플릿 매칭 결과 행렬 res는 -1부터 1 사이의 실수
    -   이를 0부터 255 사이의 정수 범위로 정규화한 결과가 res_norm
    -   res_norm 영상에서 가장 밝게 나타나는 위치 → 템플릿 영상과 가장 유사한 부분
-   콘솔창에는 “maxv: 0.976276” 문자열이 출력
    -   템플릿 매칭으로 검출된 위치에서 정규화된 상관계수 값
    -   이 값이 1에 가까운 실수 → 매칭이 잘 되었음

# 캐스케이드 분류기와 얼굴 검출

-   OpenCV에서 제공하는 얼굴 검출 기능
    -   2001년에 비올라(P. Viola)와 존스(M. Jones)가 발표한 부스팅(boosting) 기반의 캐스케이드 분류기(cascade classifier) 알고리즘을 기반으로 만듦
        -   Boosting
            -   Ensemble 기법 중 하나
                -   동일한 학습 알고리즘을 사용해서 여러 모델을 학습
                -   Weak learner들을 결합 → single learner보다 나아진다는 아이디어에 기반
            -   Weak learner들을 계속 이어 나가면서 기존 모델의 성능을 개선해 나가는 형태
-   비올라-존스 얼굴 검출 알고리즘
    -   기본적으로 영상을 24x24 크기로 정규화함
    -   유사-하르 필터(Haar-like filter) 집합으로부터 특징 정보를 추출 → 얼굴 여부를 판별
-   유사-하르 필터
    -   흑백 사각형이 서로 붙어 있는 형태로 구성된 필터
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/57d07a6b-f4c5-4cb5-af66-6aacf39a9179/image.png)
    -   흰색 영역 픽셀 값은 모두 더함
    -   검은색 영역 픽셀 값은 모두 빼서 하나의 특징 값을 도출
    -   사람의 정면 얼굴 형태가 전형적으로
        -   밝은 영역(이마, 미간, 볼 등)
        -   어두운 영역(눈썹, 입술 등)
    -   유사-하르 필터로 구한 특징 값 → 얼굴을 판별하는 용도

## 유사-하르 특징값의 활용

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/11ddc0e2-31ea-4d11-a964-79c7c025e17c/image.png)

## 캐스케이드 분류기와 얼굴 검출

-   24x24 크기에서 다양한 크기의 유사-하르 필터를 대략 16만 개 생성할 수 있음
-   픽셀 값의 합과 차를 계산하는 것
    -   복잡하지는 않지만 시간이 오래 걸린다는 점이 문제
    -   비올라와 존스는 에이다부스트(AdaBoost) 알고리즘과 적분 영상(integral image)를 이용 → 문제 해결
-   AdaBoost 알고리즘
    -   수많은 유사-하르 필터 중에서 얼굴 검출에 효과적인 필터를 선별하는 역할을 수행함

## 픽셀값들의 합과 차

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/609621ff-0d57-4187-8b28-1b48af22aa31/image.png)

## Integral Image

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/48ba6f08-6200-4c03-9a48-31b599042f5b/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e74fd51c-9998-4e77-bc62-b7af0fe6e044/image.png)

## 캐스케이드 분류기와 얼굴 검출

-   에이다부스트 알고리즘에 의해 24x24 부분 영상에서 검사할 특징 개수가 약 6000개로 감소함
    -   입력 영상 전체에서 부분 영상을 추출하여 검사해야 하기 때문에 여전히 연산량이 부담
    -   나타날 수 있는 얼굴 크기가 다양 → 보통 입력 영상의 크기를 줄여 가면서 전체 영역에 대한 검사를 다시 수행해야 함
-   비올라와 존스는 대부분의 영상에 얼굴이 한두 개, 나머지 대부분은 얼굴이 아니라는 점에 주목
    -   비올라-존스 알고리즘에서는 캐스케이드(cascade) 구조
        -   얼굴이 아닌 영역을 빠르게 걸러 내는 방식

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c22cf52b-0a57-4141-844f-409cfcbf5bb9/image.png)

-   얼굴이 아닌 영역을 걸러 내는 캐스케이드 구조
    -   캐스케이드 구조 1단계
        -   얼굴 검출에 가장 유용한 유사-하르 필터 하나를 사용
        -   얼굴이 아니라고 판단되면 이후의 유사-하르 필터 계산은 수행하지 않음
    -   2단계
        -   유사-하르 필터 다섯 개를 사용하여 얼굴이 아닌지를 검사함
        -   얼굴이 아니라고 판단되면 이후 단계의 검사는 수행하지 않음
    -   이러한 방식으로 얼굴이 아닌 영역을 빠르게 제거함 → 비올라-존스 얼굴 검출
    -   동시대의 다른 얼굴 검출 방식보다 약 15배 빠르게 동작하는 성능을 보임
-   OpenCV는 비올라-존스 알고리즘을 구현하여 객체를 분류할 수 있는
    -   CascadeClassifier 클래스를 제공
        -   미리 훈련된 객체 검출 분류기 XML 파일을 불러오는 기능
        -   주어진 영상에서 객체를 검출하는 기능
-   CascadeClassifier 클래스를 이용하여 객체를 검출하려면
    -   먼저 CascadeClassifier 객체를 생성해야 함
    -   CascadeClassifier 객체를 생성한 후에는 미리 훈련된 분류기 정보를 불러올 수 있음
        -   분류기 정보는 XML 파일 형식으로 저장되어 있음
    -   CascadeClassifier::load() 멤버 함수를 이용하여 분류기 XML 파일을 불러올 수 있음
-   OpenCV는 미리 훈련된 얼굴 검출, 눈 검출 등을 위한 분류기 XML 파일을 제공
    -   하나의 검출 대상에 대해 서로 다른 방법으로 훈련된 여러 개의 XML 파일이 제공됨
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7d5608a3-9ddc-4a74-bc9d-5c92076d1138/image.png)
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/30e64fa5-d638-4acb-9b8f-4262103c3321/image.png)
    -   CascadeClassifier::load() 함수를 이용 → 정면 얼굴 검출을 위한 XML 파일을 불러오려면
        ```cpp
        CascadeClassifier classifier;
        classifier.load("haarcascade_frontalface_default.xml");
        ```
        ```cpp
        CascadeClassifier classifier("haarcascade_frontalface_default.xml");
        ```
-   XML 파일을 불러오는 코드를 수행한 후에는 XML 분류기 파일이 정상적으로 불러졌는지를 확인할 때 사용하는 함수
    -   CascadeClassifier::empty() 멤버 함수
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/fd78f594-4d7f-40ae-8c46-b06e1f260dbf/image.png)
-   XML 파일을 정상적으로 불러왔다면 이제 CascadeClassifier::detectMultiScale() 멤버 함수를 이용하여 객체 검출을 실행
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9f22794f-c471-4b19-a725-4adcd52e03d9/image.png)

## (실습) 캐스케이드 분류기와 얼굴 검출

```python
def detect_face():
    src = cv2.imread('kids.png')

    if src is None:
        print('Image load failed!')
        return

    classifier =
	    cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    if classifier.empty():
        print('XML load failed!')
        return

    faces = classifier.detectMultiScale(src)

    for (x, y, w, h) in faces:
        cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 255), 2)

    cv2.imshow('src', src)
    cv2.waitKey()
    cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/45a856e1-6164-4336-a775-7a8209a02a96/image.png)

```python
def detect_eyes():
    src = cv2.imread('kids.png')

    if src is None:
        print('Image load failed!')
        return

    face_classifier =
	    cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')

    if face_classifier.empty() or eye_classifier.empty():
        print('XML load failed!')
        return

    faces = face_classifier.detectMultiScale(src)

    for (x1, y1, w1, h1) in faces:
        cv2.rectangle(src, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 255), 2)

        faceROI = src[y1:y1 + h1, x1:x1 + w1]
        eyes = eye_classifier.detectMultiScale(faceROI)

        for (x2, y2, w2, h2) in eyes:
            center = (int(x2 + w2 / 2), int(y2 + h2 / 2))
            cv2.circle(faceROI, center, int(w2 / 2),
	            (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('src', src)
    cv2.waitKey()
    cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4efc6ad6-9987-4bc6-81ff-1038a7bd7073/image.png)

# HOG 알고리즘과 보행자 검출

## HOG 알고리즘과 보행자 검출

-   HOG(Histograms of Oriented Gradients)
    -   그래디언트 방향 히스토그램을 의미
-   다랄(Dalal)과 트릭스(Triggs)는 사람이 서 있는 영상에서 그래디언트를 구함
    -   그래디언트의 크기와 방향 성분을 이용 → 사람이 서 있는 형태에 대한 특징 벡터를 정의
    -   머신 러닝의 일종인 서포트 벡터 머신(SVM, Support Vector Machine) 알고리즘을 이용 → 입력 영상에서 보행자 위치를 검출하는 방법을 제안

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ef885a99-991f-4c04-b57d-6fd88933e02d/image.png)

-   보행자 검출을 위한 HOG는 기본적으로 64x128 크기의 영상에서 계산
-   HOG 알고리즘은 입력 영상으로부터 그래디언트를 계산
    -   그래디언트는 크기와 방향 성분으로 계산, 방향 성분은 0’부터 180’까지로 설정 (unsigned gradients)
-   그 다음은 입력 영상을 8x8 크기 단위로 분할 → 각각의 8x8 부분 영상을 셀(cell)이라고 부름
    -   64x128 영상에서 셀은 가로 방향을 8개, 세로 방향으로 16개
-   각각의 셀로부터 그래디언트 방향 성분에 대한 히스토그램을 구함
    -   이때 방향 성분을 20’ 단위로 구분 → 총 아홉 개의 빈으로 구성된 방향 히스토그램이 만들어짐
-   인접한 네 개의 셀을 합쳐서 블록(block)이라고 정의

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1bf8a6e5-660e-4b91-a536-4ae66ca69bfb/image.png)

-   (a) : 64x128 크기의 입력 영상
-   (b)에서
    -   노란색 실선은 셀을 구분하는 선
    -   빨간색 사각형은 블록 하나
    -   하나의 블록에는 네 개의 셀이 있고 각 셀에는 아홉 개의 빈으로 구성된 히스토그램 정보가 있음
    -   블록 하나에서는 총 36개의 실수 값으로 이루어진 방향 히스토그램 정보가 추출됨
    -   블록은 가로와 세로 방향으로 각각 한 개의 셀만큼 이동하면서 정의함
        -   64x128 영상에서 블록은 가로 방향으로 7개, 세로 방향으로 15개 정의할 수 있음
        -   총 105개의 블록이 추출
        -   전체 블록에서 추출되는 방향 히스토그램 실수 값 개수는 105x36=3780
            -   이 3780개의 실수 값이 64x128 영상을 표현하는 HOG 특징 벡터 역할을 함
-   (c) : 각 셀에서 계산된 그래디언트 방향 히스토그램을 비주얼하게 표현
-   다랄(Dalal)과 트릭스(Triggs)
    -   수천 장의 보행자 영상과 보행자가 아닌 영상에서 HOG 특징 벡터를 추출
    -   이 두 특징 벡터를 구별하기 위해 SVM 알고리즘을 사용
        -   SVM은 두 개의 클래스를 효과적으로 분리하는 능력을 가진 머신 러닝 알고리즘
        -   수천 개의 보행자 특징 벡터와 보행자가 아닌 특징 벡터를 이용하여 SVM을 훈련시킴
-   HOG와 SVM을 이용한 객체 검출 기술
    -   보행자 검출뿐만 아니라 다양한 형태의 객체 검출에서도 응용됨
-   OpenCV는 HOG 알고리즘을 구현한
    -   HOGDescriptor 클래스를 제공함
        -   특정 객체의 HOG 기술자를 쉽게 도출
        -   보행자 검출을 위한 용도로 미리 계산된 HOG 기술자 정보를 제공
-   HOGDescriptor 클래스를 이용하려면 먼저 HOGDescriptor 객체를 생성
    -   보행자 검출이 목적 → HOGDescriptor 클래스의 기본 생성자를 이용하여 객체를 생성
    -   HOGDescriptor 클래스의 기본 생성자
        -   검색 윈도우 크기를 64x128, 셀 크기는 8x8, 블록 크기는 16x16, 그래디언트 방향 히스토그램 빈 개수는 9로 설정
        -   HOG 기술자 하나는 3780개의 float 실수로 구성됨
-   HOGDescriptor 클래스는 미리 계산된 보행자 검출을 위한 HOG 기술자 정보를 반환하는 정적 멤버 함수
    -   HOGDescriptor::getDefaultPeopleDetector()를 제공함
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ccd41d1f-c768-4a76-b8b5-29167c5a6ba4/image.png)
    -   정적 멤버 함수 → 소스 코드 작성 시에 클래스 이름과 함께 사용
-   HOGDescriptor 클래스를 이용하여 원하는 객체를 검출하려면
    -   먼저 검출할 객체에 대해 훈련된 SVM 분류기 계수를 HOGDescriptor::setSVMDetector() 함수에 등록해야 함
-   HOG 기술자를 이용하여 실제 입력 영상에서 객체 영상을 검출하려면
    -   HOGDescriptor::detectMultiScale() 멤버 함수를 사용
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8282bf3b-db73-4ad0-a613-16f3921b491c/image.png)
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a5f0cf22-05bd-43f1-a8e6-7b0ad14943e0/image.png)

## (실습) HOG 알고리즘과 보행자 검출

```python
cap = cv2.VideoCapture('vtest.avi')

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    ret, frame = cap.read()

    if not ret:
        break

    detected, _ = hog.detectMultiScale(frame)

    for (x, y, w, h) in detected:
        c = (random.randint(0, 255),
	        random.randint(0, 255), random.randint(0, 255))
        cv2.rectangle(frame, (x, y), (x + w, y + h), c, 3)

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
```

-   HOG 알고리즘에 의한 보행자 검출
    -   꽤 많은 연산량을 필요로 함 → 가급적 Debug 모드가 아닌 Release 모드로 실행해야 빠른 검출 결과를 확인할 수 있음

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/eaa8fce1-05e3-42d3-b3e7-f8ebbe46e5dd/image.png)

# QR 코드 검출

## QR 코드 검출

-   QR 코드
    -   흑백 격자 무늬 모양의 2차원 바코드 일종
    -   숫자, 영문자, 8비트 문자, 한자 등의 정보를 저장할 수 있음
-   입력 영상에서 QR 코드를 인식하려면
    -   먼저 QR 코드 세 모서리에 포함된 흑백 정사각형 패턴을 찾아 QR 코드 전체 영역 위치를 알아내야 함
    -   검출된 QR 코드를 정사각형 형태로 투시 변환
    -   QR 코드 내부에 포함된 흑백 격자 무늬를 해석 → 문자열을 추출
    -   일련의 연산은 복잡하고 정교한 영상 처리를 필요로 함
-   OpenCV에서 QR 코드를 검출하고 해석하는 기능
    -   QRCodeDetector 클래스에 구현
    -   먼저 QRCodeDetector 객체를 생성해야 함
    ```cpp
    QRCodeDetector detector;
    ```
-   QRCodeDetector 객체를 생성한 후에는
    -   QRCodeDetector 클래스 멤버 함수를 이용하여 QR 코드를 검출하거나 문자열을 해석할 수 있음
-   입력 영상에서 QR 코드 영역을 검출하기 위해서는
    -   QRCodeDetector::detect() 함수를 사용
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/192ad256-a7e0-4818-bbfa-07e169f12cfd/image.png)
-   검출된 QR 코드 영역에서 QR 코드에 저장된 문자열을 추출할 때에는
    -   QRCodeDetector::decode() 함수를 사용
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e5d1f03c-e3b3-44f9-8b9d-e40fbf27bbe9/image.png)
-   입력 영상에서 QR 코드 검출과 해석을 한꺼번에 수행하려면
    -   QRCodeDetector::detectAndDecode() 멤버 함수를 사용
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2b24380a-751c-4476-9908-b298906d1500/image.png)

## (실습) QR 코드 검출

```python
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

detector = cv2.QRCodeDetector()

while True:
    ret, frame = cap.read()

    if not ret:
        print('Frame load failed!')
        break

    info, points, _ = detector.detectAndDecode(frame)

    if points is not None:
        points = np.array(points, dtype=np.int32).reshape(4, 2)
        cv2.polylines(frame, [points], True, (0, 0, 255), 2)

    if len(info) > 0:
        cv2.putText(frame, info, (10, 30),
	        cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), lineType=cv2.LINE_AA)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/72858518-5f12-4b22-af81-5435d2246c44/image.png)

-   QR 코드 영역을 빨간색 사각형으로 정확하게 표시
-   카메라 프레임 출력 창 상단에 QR 코드에 포함된 문자열이 제대로 출력됨

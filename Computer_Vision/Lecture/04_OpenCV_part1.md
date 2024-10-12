# 카메라와 동영상 파일 다루기

---

## 동영상의 처리

---

-   동영상 : 일련의 정지 영상을 압축하여 파일로 저장한 형태
    -   프레임(Frame) : 저장되어 있는 일련의 정지 영상
-   동영상을 처리하는 순서
    1. 프레임 추출
    2. 각각의 프레임에 영상 처리 기법을 적용
-   컴퓨터에 연결된 카메라 장치
    -   카메라로부터 일정 시간 간격으로 정지 영상 프레임을 받아와서 처리
-   OpenCV에서는 VideoCapture라는 하나의 클래스를 이용
    -   카메라 또는 동영상 파일로부터 정지 영상 프레임을 받아올 수 있음

## VideoCapture 클래스

---

-   동영상 파일을 불러오기 위해서 VideoCapture 객체를 생성할 때
    -   생성자에 동영상 파일 이름을 지정

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/66831d71-4028-482e-8125-ee6da2e7328a/image.png)

-   Python에서는 open 없이 바로 사용 가능
    -   isOpened() 호출을 통해 제대로 불러왔는지 확인 필요
-   cap.get(…)
    -   현재 열려 있는 카메라 장치 또는 동영상 파일로부터 여러 가지 정보를 받아오기 위해 사용

```python
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Camera open failed!")
    exit()

print('Frame width:', int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
```

-   filename 인자에는 동영상 파일 이름을 전달
    -   _.avi, _.mpg, \*.mp4 등의 확장자를 갖는 파일
-   카메라 장치를 열 경우 VideoCapture의 생성자에 문자열이 아니라 정수 값을 전달
    -   전달하는 정수 값 index = camera_id + domain_offset_id
    -   컴퓨터에 한 대의 카메라만 연결 → camera_id 값은 0
    -   2대 이상의 카메라가 연결 → 각각의 카메라는 0보다 같거나 큰 정수를 ID로 가짐
    -   domain_offset_id는 카메라 장치를 사용하는 방식을 표현하는 정수
        -   대부분 사용 방식을 자동 선택(CAP_ANY) → index와 camera_id가 같은 값
-   VideoCapture의 read()
    -   카메라 또는 동영상 파일로부터 다음 프레임을 받아 옴
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ad33d80d-d408-4d13-935b-ce8722e3feec/image.png)
    -   Return 값을 통해 제대로 프레임을 받아왔는지 확인

```python
while True:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame # (255 - frame)과 같음

    cv.imshow('frame', frame)
    cv.imshow('inversed', inversed)

    if cv.waitKey(10) == 27:
        break

cv.destroyAllWindows()
```

-   사용자로부터 키 입력을 받아서 ESC 인 경우 loop를 종료
    -   27 = ESC
-   waitKey(int)
    -   키 입력을 받을 때까지 대기할 시간을 지정
-   destroyAllWindows()

```python
print('Frame width:', int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
```

-   Get 함수에서는 카메라/동영상의 정보를 받아올 수 있음

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1d084e19-a39b-4258-a0ea-e212f4df1e01/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b9a92652-8eb5-4a1f-af3a-4c3068a5d2b5/image.png)

## 동영상 파일 처리하기

---

-   대부분의 동영상 파일은 고유의 코덱(codec)을 이용하여 압축된 형태로 저장됨
-   OpenCV는 MPEG-4, H.264 등의 코덱에 대한 해석 기능을 제공
    -   VideoCapture 클래스를 활용하여 동영상 파일을 쉽게 불러와서 사용 가능
-   카메라 입력 처리와 매우 유사
-   동영상 파일은 초당 프레임 수(FPS : frames per second) 값을 가짐
    -   FPS 값을 고려하지 않을 경우 동영상이 너무 빠르거나 느리게 재생됨
    -   FPS 값을 확인하기 위해서는 CAP_PROP_FPS 를 활용
    ```python
    fps = cap.get(cv.CAP_PROP_FPS)
    print('FPS:', fps)
    ```
-   FPS 값을 이용하면 매 프레임 사이의 시간 간격을 계산 가능
    ```python
    delay = round(1000 / fps) # 1000ms = 1sec
    ```
    -   초당 30프레임을 재생할 경우 delay는 33ms
        -   각 프레임을 33ms 간격으로 출력해야함
        -   delay값을 추후 waitKey() 함수의 인자로 사용

```python
import cv2 as cv

cap = cv.VideoCapture('stopwatch.avi')
if not cap.isOpened():
    print("Video open failed!")
    exit()

print('Frame width:', int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
print('Frame count:', int(cap.get(cv.CAP_PROP_FRAME_COUNT)))

fps = cap.get(cv.CAP_PROP_FPS)
print('FPS:', fps)
delay = round(1000 / fps) # 1000ms = 1sec

while True:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame

    cv.imshow('frame', frame)
    cv.imshow('inversed', inversed)

    if cv.waitKey(delay) == 27:
        break

cv.destroyAllWindows()
```

-   cap.read()
    -   각 frame을 읽음
-   if not ret
    -   에러가 없을 경우
-   inversed = ~frame
    -   반전을 시킴
-   delay마다 화면에 출력

## 동영상 파일 저장하기

---

-   동영상 파일을 생성하고 프레임을 저장
    -   VideoWriter 클래스를 사용

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d287e885-5fa0-49e8-893d-e51c12af3e96/image.png)

-   인자 중 fourcc는 4-문자 코드(4-character code)의 약자
    -   4개의 문자로 구성된 코드
    -   동영상 파일의 코덱, 압축 방식, 색상 혹은 픽셀 포맷 등을 정의하는 정수 값
    -   코텍을 표현하는 네 개의 문자를 묶어서 생성
-   fourcc에 해당하는 정수 값
    -   fourcc() 함수를 사용하여 생성
    ```python
    fourcc = cv.VideoWriter_fourcc(*'DIVX')
    ```

### 주요 fourcc 코드와 의미

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/3b88b189-139a-4aa9-8985-155629f31ece/image.png)

-   VideoWriter 클래스의 초기화
    ```python
    outputVideo = cv.VideoWriter('output.avi', fourcc, fps, (w, h))
    ```
    -   ‘output.avi’ : 저장할 파일의 이름
    -   fps : 저장할 동영상의 FPS 값
    -   w : 프레임의 너비
    -   h : 프레임의 높이
-   write() 함수를 사용하여 프레임을 추가할 수 있음
    -   새로 추가하는 image 프레임의 크기
        -   동영상 파일을 생성할 때 지정했던 크기와 일치해야 함
-   stopwatch.avi를 읽어서 반전한 영상을 저장하기
    ```python
    import cv2 as cv

    cap = cv.VideoCapture('stopwatch.avi')

    if not cap.isOpened():
        print("Video open failed!")
        exit()

    w = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    h = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv.CAP_PROP_FPS)

    fourcc = cv.VideoWriter_fourcc(*'DIVX')
    delay = round(1000 / fps)

    outputVideo = cv.VideoWriter('output.avi', fourcc, fps, (w, h))
    if not outputVideo.isOpened():
        print('File open failed!')
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        inversed = ~frame
        outputVideo.write(inversed)

        cv.imshow('frame', frame)
        cv.imshow('inversed', inversed)

        if cv.waitKey(delay) == 27:
            break

    cv.destroyAllWindows()
    ```

# 다양한 그리기 함수

---

## 직선 그리기

---

-   line() 함수
    -   영상 위에 직선을 그릴 수 있음
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/569f00e7-553f-4a2f-91b9-eb5c1897967a/image.png)
    -   Python에서는 img가 numpy array
        ```python
        img = np.full((400 ,400, 3), 255, np.uint8)
        ```

### LineTypes

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/101a2d75-e0f1-41e3-976e-be686a933e39/image.png)

-   arrowedLine() 함수
    -   화살표 형태의 직선을 그려야 하는 경우 사용
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6e98b126-023c-48cf-b3c4-efcc392b487c/image.png)
-   drawMarker() 함수
    -   마커(marker)를 그리는 경우 사용
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/24645249-3f30-4212-894c-d40d26eae0ac/image.png)

### MarkerTypes

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5079e485-7b6d-444a-bca2-8642d9e60ab8/image.png)

## 다양한 그리기 함수 활용

---

-   수평 방향 직선, 대각선 방향 직선, 수평 방향 화살표, 마커

```python
import numpy as np
import cv2 as cv

img = np.full((400, 400, 3), 255, np.uint8)

cv.line(img, (50, 50), (200, 50), (0, 0, 255))
cv.line(img, (50, 100), (200, 100), (255, 0, 255), 3)
cv.line(img, (50, 150), (200, 150), (255, 0, 0), 10)

cv.line(img, (250, 50), (350, 100), (0, 0, 255), 1, cv.LINE_4)
cv.line(img, (250, 70), (350, 120), (255, 0, 255), 1, cv.LINE_8)
cv.line(img, (250, 90), (350, 140), (255, 0, 0), 1, cv.LINE_AA)

cv.arrowedLine(img, (50, 200), (150, 200), (0, 0, 255), 1)
cv.arrowedLine(img, (50, 250), (350, 250), (255, 0, 255), 1)
cv.arrowedLine(img, (50, 300), (350, 300), (255, 0, 0), 1, cv.LINE_8, 0, 0.05)

cv.drawMarker(img, (50, 350), (0, 0, 255), cv.MARKER_CROSS)
cv.drawMarker(img, (100, 350), (0, 0, 255), cv.MARKER_TILTED_CROSS)
cv.drawMarker(img, (150, 350), (0, 0, 255), cv.MARKER_STAR)
cv.drawMarker(img, (200, 350), (0, 0, 255), cv.MARKER_DIAMOND)
cv.drawMarker(img, (250, 350), (0, 0, 255), cv.MARKER_SQUARE)
cv.drawMarker(img, (300, 350), (0, 0, 255), cv.MARKER_TRIANGLE_UP)
cv.drawMarker(img, (350, 350), (0, 0, 255), cv.MARKER_TRIANGLE_DOWN)

cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ebd9e4f4-ceff-4459-b4cb-9924e56c7323/image.png)

-   세 수평선 중에서 맨 위의 빨간색 직선은 선 두께를 1로 지정
-   보라색과 파란색 직선은 선 두께를 각각 3과 10으로 지정
-   세 개의 사선 중에서 맨 위의 빨간색 사선은 직선 타입을 LINE_4로 지정
    -   보라색 사선은 LINE_8 타입
    -   파란색 사선은 LINE_AA
-   LINE_4 타입은 상하좌우 네 방향으로 픽셀이 연결
-   LINE_8 타입의 직선은 픽셀이 대각선 방향으로도 연결
-   LINE_AA로 그린 파란색 사선은 안티에일리어싱(anti-aliasing) 기법이 적용
    -   다소 부드럽게 직선이 그려짐

## 도형 그리기

---

-   외곽선으로 이루어진 도형 뿐만 아니라 내부가 채워진 도형도 그릴 수 있음
-   사각형 : rectangle()
    -   대각 위치에 있는 두 꼭지점 좌표를 이용
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4e6d245f-5f52-4d8f-9028-dfdacbbb89f0/image.png)
-   원 : circle()
    -   원의 중심점 좌표와 반지름을 지정해야 함
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e2cc54b4-1da5-4ec4-a6cc-156d141ef85a/image.png)
-   타원 : ellipse()
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d1ee810e-5cbe-40b1-a411-a1b6a88c36a6/image.png)
-   임의의 다각형 그리기 : polylines()
    -   다각형의 꼭지점 좌표를 전달
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/be17eb7d-5f0d-4161-9b9b-99ffffaa5bc9/image.png)
-   다양한 사각형, 원, 타원, 다각형
    ```python
    import numpy as np
    import cv2 as cv

    img = np.full((400, 400, 3), 255, np.uint8)

    cv.rectangle(img, (50, 50), (150, 100), (0, 0, 255), 2)
    cv.rectangle(img, (50, 150), (150, 200), (0, 0, 128), -1)

    cv.circle(img, (300, 120), 30, (255, 255, 0), -1, cv.LINE_AA)
    cv.circle(img, (300, 120), 60, (255, 0, 0), 3, cv.LINE_AA)

    cv.ellipse(img, (120, 300), (60, 30), 20, 0, 270, (255, 255, 0), cv.FILLED, cv.LINE_AA)
    cv.ellipse(img, (120, 300), (100, 50), 20, 0, 360, (0, 255, 0), 2, cv.LINE_AA)

    pts = np.array([[250, 250], [300, 250], [300, 300], [350, 300], [350, 350], [250, 350]])
    cv.polylines(img, [pts], True, (255, 0, 255), 2)

    cv.imshow("img", img)
    cv.waitKey()
    cv.destroyAllWindows()
    ```
    -   타원 → 0도부터 270도까지 내부를 채워서 그리기
    -   타원 → 0도부터 360도까지 두께 2의 녹색선으로 그리기
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/bb64b594-caae-4c93-b1f1-cf80236cedbe/image.png)

## 문자열 출력하기

---

-   표준 입출력을 활용하여 콘솔에 출력하는 것도 가능
-   그 외에 영상에 직접 처리 결과 및 추가 정보를 문자열 형태로 출력해야 할 경우 존재
-   OpenCV에서는 putText() 함수 활용
    -   대상 영상 및 출력할 문자열, 폰트 정보 등을 설정
    -   영문자와 숫자를 출력 가능 (한글은 출력 불가능)

### 문자열 출력 - putText()

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2363ea97-1b9c-4ef2-931a-efb6c6acab59/image.png)

### 문자열 출력하기 - 폰트 지정

---

-   FONT_ITALIC 상수는 논리합 연산자(|)를 이용하여 다른 HersheyFonts 상수와 함께 사용
    -   이 경우 해당 폰트가 기울어진 이탤릭체로 출력됨

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/cf32b46c-a226-438e-8708-f002eb3b9828/image.png)

```python
import numpy as np
import cv2 as cv

img = np.full((500, 500, 3), 255, np.uint8)

cv.putText(img, "FONT_HERSHEY_SIMPLEX", (20, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
cv.putText(img, "FONT_HERSHEY_PLAIN", (20, 100), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
cv.putText(img, "FONT_HERSHEY_DUPLEX", (20, 150), cv.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))
cv.putText(img, "FONT_HERSHEY_COMPLEX", (20, 200), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
cv.putText(img, "FONT_HERSHEY_TRIPLEX", (20, 250), cv.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0))
cv.putText(img, "FONT_HERSHEY_COMPLEX_SMALL", (20, 300), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0))
cv.putText(img, "FONT_HERSHEY_SCRIPT_SIMPLEX", (20, 350), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 0, 255))
cv.putText(img, "FONT_HERSHEY_SCRIPT_COMPLEX", (20, 400), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 255))
cv.putText(img, "FONT_HERSHEY_COMPLEX | FONT_ITALIC", (20, 450), cv.FONT_HERSHEY_COMPLEX | cv.FONT_ITALIC, 1, (255, 0, 0))

cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/07008a07-69c3-476e-9a16-766f3791d20b/image.png)

-   OpenCV에서는 문자열 출력을 위해 필요한 사각형 영역 크기를 가늠할 수 있는 getTextSize() 함수 제공
    -   문자열이 한쪽으로 치우치지 않도록 배치 가능
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/706a42eb-741a-4d77-aace-6c415e50b073/image.png)
-   출력할 문자열의 크기를 바탕으로 정중앙에 출력하기
    ```python

    import numpy as np
    import cv2 as cv

    img = np.full((200, 640, 3), 255, np.uint8)

    text = "Hello, OpenCV"
    fontFace = cv.FONT_HERSHEY_TRIPLEX
    fontScale = 2.0
    thickness = 1

    sizeText, _ = cv.getTextSize(text, fontFace, fontScale, thickness)

    org = ((img.shape[1] - sizeText[0]) // 2, (img.shape[0] + sizeText[1]) // 2)
    cv.putText(img, text, org, fontFace, fontScale, (255, 0, 0), thickness)
    cv.rectangle(img, org, (org[0] + sizeText[0], org[1] - sizeText[1]), (0, 255, 0), 1)

    cv.imshow("img", img)
    cv.waitKey()
    cv.destroyAllWindows()
    ```
    -   출력할 문자열이 차지할 사각형 영역 → sizeText
    -   img의 크기와 sizeText 정보를 이용하여 출력할 좌표 계산 → org
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/aefabbb9-4e73-441d-a4c9-5fb1b4c5318d/image.png)

# 이벤트 처리

---

## 키보드 이벤트 처리

---

-   키 입력을 확인하기 위해 사용한 함수 → waitKey()
    -   키보드 입력을 처리하는 기본적인 OpenCV 함수
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c0b6af0c-f5fb-4530-93c5-c7a031972fb0/image.png)
-   특정 키를 눌렀을 때에만 창을 닫게끔 하려면 waitKey() 함수의 반환값을 조사해야 함
    ```cpp
    Mat img = imread("lenna.bmp", IMREAD_GRAYSCALE);

    namedWindow("img");
    imshow("img", img);

    while (true) {
    	if (waitKey() == 27)
    		break;
    }

    destroyWindow("img");
    ```
-   여러 키 입력에 대해서 서로 다른 처리를 하고 싶은 경우
    -   I 또는 i
    -   Q 또는 q
    ```python
    import cv2

    img = cv2.imread('lenna.bmp')
    if img is None:
        print('Image load failed!')
        exit()

    cv2.namedWindow('img')
    cv2.imshow('img', img)

    while True:
        keycode = cv2.waitKey()
        if keycode == ord('i') or keycode == ord('I'):
            img = ~img
            cv2.imshow('img', img)
        elif keycode == 27 or keycode == ord('q') or keycode == ord('Q'):
            break

    cv2.destroyAllWindows()
    ```

## 마우스 이벤트 처리

---

-   영상 출력 창에서 발생하는 마우스 이벤트를 사용자에게 전달하는 기능을 제공
    -   이를 이용하여 마우스 클릭에 반응
    -   마우스 드래그를 통해 영상에 그림을 그리는 등의 동작 수행 가능
-   마우스 이벤트를 처리하려면 먼저 마우스 콜백(callback) 함수를 등록
    -   콜백 함수에 마우스 이벤트를 처리하는 코드를 추가
-   특정 창에 마우스 콜백 함수 등록할 때 setMouseCallback 함수 사용
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/62da52ce-76b4-4b31-baa0-c92eb01eaa1d/image.png)
    -   C++ → onMouse에 함수 포인터를 지정
        -   4개의 정수형과 하나의 void\* 타입
        -   함수명을 onMouse로 설정해야 하는 것은 아님
    ```cpp
    typedef void (*MouseCallback)(int event, int x, int y, int flags, void* userdata);
    ```
    -   int event
        -   MouseEventType으로 정의된 열거형 상수 중 하나를 전달
    -   int x, int y
        -   마우스 이벤트가 발생한 위치의 x좌표와 y좌표
    -   int flags
        -   MouseEventFlags 열거형 상수의 논리합 조합을 전달

### MouseEventTypes

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a1d20bba-0ce6-4a39-bac4-b502c81cfb3d/image.png)

### MouseEventFlags

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2d8db5e0-91b5-47fb-b82e-532fcf9b97a1/image.png)

## 마우스 이벤트 처리

---

-   마우스 왼쪽 버튼을 누르거나 뗀 좌표를 콘솔 창에 출력
-   왼쪽 버튼을 누른 상태로 마우스를 움직이면 궤적을 따라 영상 위에 노란색으로 표시
-   onMouse 함수를 선언하여 callback 함수로 저장

```cpp
import cv2

def on_mouse(event, x, y, flags, param):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' %(x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (0, 255, 255), 2)
            cv2.imshow('img', img)
            oldx, oldy = x, y

img = cv2.imread('lenna.bmp')

if img is None:
    print('Image load failed!')
    exit()

cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/690ecb70-2aa4-4fbf-a3c4-b5a907e05ed2/image.png)

## 트랙바 사용하기

---

-   프로그램 동작 중에 사용자 입력을 받을 수 있는 그래픽 사용자 인터페이스, 즉 GUI(Graphical User Interface)를 추가하고 싶을 때가 있음
-   Windows, Linux, Mac OS 운영 체제에서 공통으로 사용할 수 있는 트랙바(trackbar) 인터페이스를 제공
-   트랙바는 영상 출력 창에 부착되어 프로그램 동작 중에 사용자가 지정된 범위 안의 값을 선택할 수 있음

### 트랙바 인터페이스

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4b9e5a63-0b6a-4c04-96be-a877338776f5/image.png)

-   트랙바는 사용자가 지정한 영상 출력 창의 상단에 부착
    -   필요한 경우 창 하나에 여러 개의 트랙바 생성 가능
-   각각의 트랙바는 고유한 이름을 지정해야 함
    -   이름은 트랙바 왼쪽에 나타남
-   트랙바 위치는 사용자가 마우스를 이용하여 이동시킬 수 있음
    -   트랙바의 현재 위치는 트랙바 이름 옆에 함께 표시됨
-   트랙바가 가리킬 수 있는 최대 위치는 트랙바 생성 시 지정할 수 있음
    -   최소 위치는 항상 0으로 고정
-   트랙바를 생성할 때는 createTrackbar() 함수 사용
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5f9dfbda-f060-4ea1-9eff-64e39a3a4c2d/image.png)
-   함수의 onChange에 지정하는 트랙바 콜백 함수
    -   트랙바 위치가 변경될 때 자동으로 호출됨
    -   콜백 함수의 형식
        ```cpp
        typedef void (*TrackbarCallback)(int pos, void* userdata);
        ```
    -   첫 번째 인자(pos)에는 현재 트랙바의 위치 정보 전달
    -   두 번째 인자(userdata)에는 사용자 데이터의 포인터 값이 전달됨
    -   함수의 이름은 마음대로
    -   인자 목록과 반환형은 반드시 정해진 형태로
-   그레이스케일 레벨을 16단계로
    -   트랙바 위치(pos)에 16을 곱한 결과를 전체 픽셀 값으로 설정
    ```python
    import numpy as np
    import cv2

    def saturated(value):
        if value > 255:
            value = 255
        elif value < 0:
            value = 0

        return value

    def on_level_change(pos):
        img[:] = saturated(pos * 16)
        cv2.imshow('image', img)

    img = np.zeros((400, 400), np.uint8)

    cv2.namedWindow('image')
    cv2.createTrackbar('level', 'image', 0, 16, on_level_change)

    cv2.imshow('image', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    ```
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5dc0a19f-970b-4779-9b2b-3b2400aef2fe/image.png)
-   트랙바의 현재 위치를 알고 싶은 경우 → getTrackbarPos()
-   트랙바의 위치를 강제로 특정 위치로 옮기고 싶은 경우 → setTrackbarPos()

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2a0afa47-b89a-4d21-9e21-d07c6909d626/image.png)

# OpenCV 데이터 파일 입출력

---

-   영상 데이터는 imwrite() 함수를 이용하여 BMP, JPG, PNG 등 영상 파일로 저장 가능
-   uchar 자료형을 사용하는 영상 데이터가 아니라 int, float, double 등의 자료형을 사용하는 일반적인 행렬은 영상 파일 형식으로 저장 불가능
-   OpenCV에서는 이러한 일반적인 행렬을 범용적인 데이터 저장 방식으로 저장하고 불러오는 기능을 제공
    -   XML, YAML, JSON 등

## FileStorage 클래스

---

-   OpenCV에서 사용하는 데이터 파일 입출력 기능을 캡슐화하여 지원

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/435ce865-ed04-435c-9dcc-cab325b6ca0e/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/dc6e2f1b-ad86-44d5-9af7-93b1e8ca437c/image.png)

-   FileStorage 객체를 생성하여 데이터를 저장하거나 읽어 옴
-   생성자에서 두 번째 인자 flags는 파일 열기 모드를 결정
    -   Python의 경우 cv2.FILE_STORAGE_READ
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1a518d0e-aa11-4234-a263-89164787c6d6/image.png)
-   파일이 잘 열렸는지 확인하기 위해 isOpened() 함수 사용
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c1a73582-7bab-4b08-8331-362a726fb3cc/image.png)
-   사용하고 있는 파일을 닫고 메모리 버퍼를 해제하기 위하여 release() 함수 호출
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/07c9e2e8-87f8-4926-a1dc-a0e7e97f137a/image.png)

## 데이터 파일 저장하기

---

```python
import numpy as np
import cv2

filename = 'mydata.json'

def writeData():
    name = 'Jane'
    age = 10
    pt1 =(100, 200)
    scores = (80, 90, 50)
    mat1 = np.array([[1.0, 1.5], [2.0, 3.2]], dtype=np.float32)

    fs = cv2.FileStorage(filename, cv2.FILE_STORAGE_WRITE)

    if not fs.isOpened():
        print('File open failed!')
        return

    fs.write('name', name)
    fs.write('age', age)
    fs.write('point', pt1)
    fs.write('scores', scores)
    fs.write('data', mat1)

    fs.release()
```

-   mydata.json 파일
    -   각 데이터는 이름과 값이 콜론(:)으로 구분됨
    -   문자열과 정수형 데이터는 하나의 값 형태로 저장됨
    -   Tuple, list는 [] 대괄호를 이용한 JSON 배열 형태로 저장
-   XML 파일로도 가능

## 데이터 파일 불러오기

---

-   데이터 파일을 읽어 오기 위하여 FileStorage 객체를 생성하고 읽기 모드 열어야 함
-   XML/YAML/JSON 파일을 읽기 모드로 열면 파일 전체를 분석하여 계층적 구조를 갖는 노드(node) 집합을 구성
    -   Node는 이름과 값으로 구성되어 있는 하나의 데이터를 의미
    -   특정 이름으로 저장되어 있는 Node에 접근하려면 getNode() 함수 사용

```python
def readData():
    fs = cv2.FileStorage(filename, cv2.FileStorage_READ)

    if not fs.isOpened():
        print('File open failed!')
        return

    name = fs.getNode('name').string()
    age = int(fs.getNode('age').real())
    pt1= tuple(fs.getNode('point').mat().astype(np.int32).flatten())
    scores = tuple(fs.getNode('scores').mat().flatten())
    mat1 = fs.getNode('data').mat()

    fs.release()

    print('name:', name)
    print('age:', age)
    print('point:', pt1)
    print('scores:', scores)
    print('data:')
    print(mat1)
```

# 유용한 OpenCV 기능

---

## 마스크 연산

---

-   임의의 모양을 갖는 ROI(Region-of-Interest) 설정을 위하여 일부 행렬 연산 함수에 대하여 마스크(mask) 연산을 지원함
-   보통 입력 영상과 크기가 같고 깊이가 CV_8U인 마스크 영상을 함께 인자로 전달 받음
-   마스크 영상이 주어질 경우, 마스크 영상의 픽셀 값이 0이 아닌 좌표에 대해서만 연산이 수행됨
    -   일반적으로 사람의 눈으로도 구분이 쉽도록 픽셀 값이 0 또는 255로 구성된 흑백 영상을 사용

## 마스크 영상

---

-   영상의 일부 영역에 대해서만 픽셀 값을 노란색으로 설정
    ```python
    def mask_setTo():
        src = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)
        mask = cv2.imread('mask_smile.bmp', cv2.IMREAD_GRAYSCALE)

        if src is None or mask is None:
            print('Image load failed!')
            return

        src[mask > 0] = (0, 255, 255)

        cv2.imshow('src', src)
        cv2.imshow('mask', mask)
        cv2.waitKey()
        cv2.destroyAllWindows()
    ```
    -   사용된 mask 영상은 중앙에 웃는 얼굴 부분이 흰색
    -   나머지 영역은 픽셀 값이 0에 해당하는 검은색
    -   마스크 영상에서 흰색으로 표시된 영역에 대해서만 영상 픽셀이 노란색으로 설정됨
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1b619c20-f936-4f29-971a-ae2667f19cae/image.png)
-   마스크 영상에 의해 지정된 일부 영역만 복사
    ```python
    def mask_copyTo():
        src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
        mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
        dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

        if src is None or mask is None or dst is None:
            print('Image load failed!')
            return

        dst[mask > 0] = src[mask > 0]

        cv2.imshow('src', src)
        cv2.imshow('dst', dst)
        cv2.imshow('mask', mask)
        cv2.waitKey()
        cv2.destroyAllWindows()
    ```
    -   Mask는 그레이스케일 영상
        -   비행기가 있는 위치에서만 픽셀 값이 255
        -   나머지 영역은 픽셀 값이 0
    -   Mask 영상에서 흰색으로 표현된 위치에서만 src 영상의 픽셀 값이 dst 영상으로 복사됨
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ebc76826-a432-4571-bd09-886021644718/image.png)

## 연산 시간 측정

---

-   대부분의 영상 처리 시스템은 대용량 영상 데이터를 다루고 복잡한 알고리즘 연산을 수행
-   여러 단계로 구성된 영상 처리 시스템
    -   각 단계에서 소요되는 연산 시간을 측정
    -   시간이 오래 걸리는 부분을 찾아 개선하는 시스템 최적화 작업이 필수적
-   머신 비전 분야처럼 실시간 연산을 필요로 하는 시스템
    -   각 단계의 연산 시간을 제대로 측정하여 분석이 중요
-   Python에서는 TickMeter 클래스를 활용하여 특정 연산의 수행 시간을 측정
-   TickMeter 클래스의 사용
    -   초기화 후 start() 호출
    -   시간을 측정하고자 하는 연산이 끝난 후 stop 호출
    -   getTimeMilli 함수로 ms 단위로 시간을 측정 가능
        -   getTimeMicro(), getTimeSec() 함수 등도 사용 가능
    ```python
    tm = cv2.TickMeter()
    tm.start()

    for y in range(src.shape[0]):
    	for x in range(src.shape[1]):
    		dst[y, x] = 255 - src[y, x]

    tm.stop()
    ```

### TickMeter 클래스 정의

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/28b5b945-b8e9-4b15-881c-c20dc1cd0d35/image.png)

-   For문을 활용하여 영상을 직접 반전시키고, 이때 소요되는 시간을 측정하여 콘솔에 출력
    ```python
    def time_inverse():
        src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

        if src is None:
            print('Image load failed!')
            return

        dst = np.empty(src.shape, dtype=src.dtype)

        tm = cv2.TickMeter()
        tm.start()

        for y in range(src.shape[0]):
            for x in range(src.shape[1]):
                dst[y, x] = 255 - src[y, x]

        tm.stop()
        print('Image inverse implementation took %4.3f ms.' % tm.getTimeMilli())

        cv2.imshow('src', src)
        cv2.imshow('dst', dst)
        cv2.waitKey()
        cv2.destroyAllWindows()
    ```

## 유용한 OpenCV 함수 사용법

---

-   Numpy의 sum() 함수와 mean() 함수
    -   주어진 행렬의 전체 원소 합 or 평균을 구할 경우 사용
    -   4채널 이하의 행렬에 대해서만 동작
    -   합과 평균을 scalar 값으로 반환함
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/daa19b22-d6fc-4938-a886-ee3fd257ae9f/image.png)
    -   mean() 함수는 마스크 연산을 지원
        -   mask 영상을 지정하여 특정 영역의 원소 평균을 구할 수도 있음
        ```python
        def useful_func():
            img = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

            if img is None:
                print('Image load failed!')
                return

            sum_img = np.sum(img)
            mean_img = np.mean(img, dtype=np.int32)
            print('Sum:', sum_img)
            print('Mean:', mean_img)
        ```
-   minMaxLoc() 함수
    -   주어진 행렬의 최솟값, 최댓값을 찾는 함수
    -   해당 값이 있는 좌표 정보도 함께 알아낼 수 있음
    -   C++에서는 pointer를 통해 결과를 전달 받음
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/07804a86-49a4-4cb6-8464-f6364d385c14/image.png)
    -   Python에서는 tuple 형태로 결과를 전달 받음
        ```python
        minVal, maxVal, minPos, maxPos = cv2.minMaxLoc(img)
        print('minVal is', minVal, 'at', minPos)
        print('maxVal is', maxVal, 'at', mixPos)
        ```
-   normalize() 함수
    -   행렬의 norm값을 정규화 하거나 원소 값 범위를 특정 범위로 정규화 할 때 사용 가능
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5d09a807-0e84-450f-8c4a-e2b52d236af6/image.png)
    -   normalize() 함수는 norm_type 인자에 따라 동작이 결정됨
        -   norm_type이 NORM_INF, NORM_L1, NORM_L2 인 경우
            -   아래 수식이 만족하도록 입력 행렬 원소 값의 크기를 조정함
                ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e1d86e7d-cdc8-47bb-b501-ed46abe7e45f/image.png)
        -   L-infinity norm
            -   최대 크기를 반환
                -   Ex) X = [-6, 4, 2] 인 경우 norm은 6
        -   L1 Norm (= Manhattan Distance 또는 Taxicab norm) : 거리의 합
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/838d5081-57ae-4fd9-ac2a-7f82c81941cc/image.png)
        -   L2 Norm (= Euclidean norm) : 피타고라스
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ac19fec5-1011-4f3b-9ca2-036af6ecb606/image.png)
        -   만약 norm_type 인자가 NORM_MINMAX 인 경우
            -   src 행렬의 최솟값이 alpha, 최댓값이 beta가 되도록 모든 원소값 크기를 조절함
        -   많은 OpenCV 예제 코드에서 NORM_MINMAX 타입으로 normalize() 함수를 사용
            -   특히 실수로 구성된 행렬을 그레이스케일 영상 형태로 변환하고자 할 때 normalize() 함수를 사용하면 유용
            -   -1 에서 1 사이의 실수로 구성된 1x5 행렬을 0부터 255 사이의 정수 행렬로 변환하는 경우
                ```python
                src = np.array([[-1, -0.5, 0, 0.5, 1]], dtype=np.float32)
                dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX ,cv2.CV_8U)
                print('src:', src)
                print('dst:', dst)
                ```
                -   최솟값은 0, 최댓값은 255가 되도록 크기를 조정
                -   결과 행렬의 타입이 CV_8U가 되도록 변경
-   C++에서는 실수를 정수로 변환하기 위하여 OpenCV에서 제공하는 cvRound() 함수를 사용
-   Python에서는 built-in 함수인 round 사용
    ```python
    print('round(2.5) is', round(2.5))
    print('round(2.51) is', round(2.51))
    print('round(3.499) is', round(3.499))
    print('round(3.5) is', round(3.5))
    ```
    -   소수점 아래가 0.5보다 크면 올림
    -   0.5보다 작으면 내림
    -   정확하게 0.5인 경우 가장 가까운 짝수로 반올림을 수행

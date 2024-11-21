# 레이블링

## 레이블링의 이해

-   레이블링(labeling)
    -   각각의 객체를 구분하고 분석하는 작업이 필요 → 이때 사용하는 기법
    -   영상 내에 존재하는 객체 픽셀 집합에 고유 번호를 매기는 작업
    -   연결된 구성 요소 레이블링(connected components labeling)이라고도 함
    -   레이블링 기법을 이용 → 각 객체의 위치와 크기 등 정보를 추출하는 작업은 객체 인식을 위한 전처리 과정으로 자주 사용됨
-   영상의 레이블링
    -   일반적으로 이진화된 영상에서 사용
        -   검은색 픽셀은 배경, 흰색 픽셀은 객체로 간주
        -   입력 영상의 픽셀 값이 0이면 배경, 0이 아니면 객체 픽셀로 인식
    -   하나의 객체는 한 개 이상의 픽셀로 이루어짐
    -   하나의 객체를 구성하는 모든 픽셀에는 같은 레이블 번호가 지정됨
-   특정 픽셀과 이웃한 픽셀의 연결 관계
    -   특정 픽셀의 상하좌우로 붙어 있는 픽셀끼리 연결되어 있다고 정의
        -   4-방향 연결성(4-way connectivity)
    -   상하좌우로 연결된 픽셀뿐만 아니라 대각선 방향으로 인접한 픽셀도 연결되어 있다고 간주 - 8-방향 연결성(8-way connectivity)
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/65bfe4e1-8c68-410d-bc73-94ed5f28512a/image.png)
    -   (a) : 4-방향 연결성
    -   (b) : 8-방향 연결성
-   이진 영상에 레이블링을 수행
    -   각각의 객체 영역에 고유의 번호가 매겨진 2차원 정수 행렬이 만들어짐
        -   레이블 맵(label map)이라고 부름

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c1293c4c-e1b0-43a1-8abf-11968d86853a/image.png)

-   입력 영상에서 배경 픽셀은 레이블 맵 행렬에서 0으로 설정
-   각 객체 픽셀 영역에는 고유의 번호가 매겨짐
-   OpenCV에서 레이블링을 수행하는 기본적인 함수
    -   connectedComponents()
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/083a0e60-4885-4508-bf9c-2ba3544696b8/image.png)

## (실습) 레이블링

```python
def labeling_basic():
    src = np.array([[0, 0, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 0, 0, 1, 0],
                    [1, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 1, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]])
	                    .astype(np.uint8)

    src = src * 255

    cnt, labels = cv2.connectedComponents(src)

    print('src:')
    print(src)
    print('labels:')
    print(labels)
    print('number of labels:', cnt)
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b40d6d10-4a9b-42c8-9097-72b4d20a2b58/image.png)

## 레이블링 응용

-   기본적인 레이블링 동작
    -   입력 영상으로부터 레이블 맵을 생성하는 것
    -   레이블링을 수행한 후에는 각각의 객체 영역이 어느 위치에 어느 정도의 크기로 존재하는지 확인할 필요가 있음
-   OpenCV는 레이블 맵과 각 객체 영역의 통계 정보를 한꺼번에 반환
    -   connectedComponentsWithStats() 함수
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/3b4a6ca0-9e83-4391-9c92-feea3b7a8d5b/image.png)
    -   connectedComponents() 함수 인자에 stats와 centroids가 추가된 형태
    -   보통 stats와 centroids 인자
        -   Mat 자료형 변수를 지정
    -   입력 영상 src가 있을 때
        ```cpp
        Mat labels, stats, centroids;
        connectedComponentsWithStats(src, labels, stats,
        	centroids);
        ```
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/df3fe973-966e-40fc-9fa8-dc025ba5a9b5/image.png)
        -   stats 행렬에서 두 번째 행 원소 값이 [0, 0, 4, 3, 10]
            -   1번 객체를 감싸는 바운딩 박스가 (0, 0) 좌표에서 시작
            -   가로 크기 4, 세로 크기 3
            -   1번 객체 픽셀 개수 10
        -   centroids 행렬에서 두 번째 행 원소 값이 [1.7, 1.2]
            -   1번 영역의 무게 중심 좌표가 (1.7, 1.2)
            -   1번 객체 픽셀의 x좌표와 y좌표를 모두 더한 후 픽셀 개수로 나눔

## (실습) 레이블링 응용

```python
def labeling_stats():
    src = cv2.imread('keyboard.bmp',
	    cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    _, src_bin = cv2.threshold(src, 0, 255,
	    cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    cnt, labels, stats, centroids =
	    cv2.connectedComponentsWithStats(src_bin)

    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    for i in range(1, cnt):
        (x, y, w, h, area) = stats[i]

        if area < 20:
            continue

        pt1 = (x, y)
        pt2 = (x + w, y + h)
        cv2.rectangle(dst, pt1, pt2, (0, 255, 255))

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/70275282-b79f-4330-baa5-19067ee5c75c/image.png)

# 외곽선 검출

## 외곽선 검출

-   객체의 외곽선(contour)
    -   객체 영역 픽셀 중에서 배경 영역과 인접한 일련의 픽셀
    -   보통 검은색 배경 안에 흰색 객체 영역에서 가장 최외각에 있는 픽셀을 찾아 외곽선으로 정의
-   흰색 객체 영역 안에 검은색 배경 영역인 홀(hole)이 존재
    -   홀을 둘러싸고 있는 객체 픽셀들도 외곽선으로 검출
-   객체의 외곽선
    -   객체 바깥쪽 외곽선
    -   안쪽 홀 외곽선
-   객체 하나의 외곽선은 여러 개의 점으로 구성
-   객체 하나의 외곽선 정보 → vector<Point> 타입으로 저장
-   하나의 영상에는 여러 개의 객체 → 영상 하나에서 추출된 전체 객체의 외곽선 정보는 vector<vector<Point>> 타입으로 표현
-   OpenCV에서는 `vector<vector<Point>> contours;` 으로 변수를 선언
    -   Python의 경우 함수에서 list 형태로 결과를 return

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e3f892a6-91c3-45c3-b95a-0203753e7d36/image.png)

-   그림 (a) : 8 x 8 크기의 영상
-   이 영상에 대해 외곽선 검출을 수행 → 그림 (b)에서 녹색으로 표현한 픽셀들이 외곽선 점들로 검출됨
    -   검출된 외곽선 점들의 좌표 → contours 변수에 모두 저장됨
-   vector<Point> 타입의 데이터가 세 개 저장됨
-   contours 변수에 저장된 각각의 외곽선 → contour[0], contour[1], contour[2]
    -   contours[0] : [1, 1], [1, 2], [1, 3], [2, 4], [3, 3], [3, 2], [3, 1], [2, 1]
    -   contours[1] : [6, 1]
    -   contours[2] : [5, 4], [4, 5], [4, 6], [5, 6], [6, 6], [6, 5], [6, 4]
-   findContours() 함수
    -   OpenCV에서 영상 내부 객체들의 외곽선을 검출하는 함수
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/72382c30-8f29-464e-a93f-af33b4112c00/image.png)
    -   mode 인자에는 외곽선을 어떤 방식으로 검출할 것인지를 나타내는 검출 모드를 지정
        -   RetrievalModes 열거형 상수 중 하나를 지정
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4345a29b-5fb9-4b5a-9f57-88dd34e042ea/image.png)
    -   method 인자에는 검출된 외곽선 점들의 좌표를 근사화하는 방법을 지정
        -   저장되는 외곽선 점의 개수를 줄이고 싶음 → `CHAIN_APPROX_SIMPLE`
        -   `CHAIN_APPROX_TC89_L1` 또는 `CHAIN_APPROX_TC89_KCOS` → 점의 개수는 많이 줄어듦, 외곽선 모양에 변화가 생김
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/458cb2f9-04be-4e4b-8eef-bcd948435a40/image.png)

## 외곽선 계층 구조

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e03ca400-4234-4395-9f0b-b859b412b793/image.png)

-   검은색 배경에 큰 흰색 객체가 두 개
    -   각각의 객체 안에는 검은색 홀이 여러 개
-   홀 안쪽에는 다시 작은 흰색 객체가 있을 수 있음
-   외곽선의 계층 구조는 외곽선의 포함 관계에 의해 결정됨
-   0번 외곽선 안에는 1, 2, 3번 홀 외곽선
    -   0번 외곽선은 1, 2, 3번 외곽선의 부모 외곽선
    -   1, 2, 3번 외곽선은 0번 외곽선의 자식 외곽선
-   0번과 4번 외곽선 → 서로 포함 관계가 없이 대등함
    -   이전 외곽선 또는 다음 외곽선의 관계

## 외곽선 검출 모드

-   네 가지 외곽선 검출 모드
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ed786e03-3dae-43ae-87ee-10b325dcc9fb/image.png)
    -   화살표가 오른쪽 외곽선 번호를 가리키면 다음 외곽선
    -   화살표가 왼쪽 외곽선 번호를 가리키면 이전 외곽선
    -   화살표가 아래쪽을 가리키면 자식 외곽선
    -   화살표가 위쪽을 가리키면 부모 외곽선
-   findContours() 함수에서 RETR_EXTERNAL 외곽선 검출 모드 사용
    -   흰색 객체의 바깥쪽 외곽선만 검출
    -   객체 내부의 홀 외곽선은 검출되지 않음
    -   큰 객체 내부에 있는 작은 객체의 외곽선도 검출되지 않음
-   RETR_LIST 검출 모드 사용
    -   바깥쪽과 안쪽 홀 외곽선을 모두 검출
-   RETR_EXTERNAL 또는 RETR_LIST 모드 사용
    -   외곽선의 부모/자식 계층 정보는 생성되지 않음
-   RETR_CCOMP 검출 모드 사용
    -   모든 흰색 객체의 바깥쪽 외곽선을 먼저 검출함
    -   각 객체 안의 홀 외곽선을 자식 외곽선으로 설정
    -   상하 계층이 최대 두 개 층으로만 구성
    -   흰색 객체에 여러 개의 홀이 존재할 경우
        -   그 중 하나만 자식 외곽선으로 설정
        -   각각의 홀 외곽선은 객체 바깥쪽 외곽선을 모두 부모 외곽선으로 설정
-   RETR_TREE 검출 모드 사용
    -   외곽선 전체의 계층 구조를 생성
    -   객체 내부에 홀이 있고, 그 홀 안에 또 다른 작은 객체가 있다면
        -   작은 객체의 외곽선은 홀 외곽선의 자식으로 설정됨

## 외곽선 검출

-   findContours() 함수로 검출한 외곽선 정보를 이용 → 영상 위에 외곽선을 그리고 싶다면
    -   drawContours() 함수 사용
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c23c7fb9-499a-48b0-b5dc-5dbaee0cf320/image.png)

## (실습) 외곽선 검출

```python
def contours_basic():
    src = cv2.imread('contours.bmp',
    cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    contours, _ = cv2.findContours(src, cv2.RETR_LIST,
	    cv2.CHAIN_APPROX_NONE)

    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    for i in range(len(contours)):
        c = (random.randint(0, 255),
	        random.randint(0, 255),
		        random.randint(0, 255))
        cv2.drawContours(dst, contours, i, c, 2)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/bf24aa51-1f52-458c-abe9-4159e45122eb/image.png)

-   객체 바깥쪽 외곽선과 안쪽 홀 외곽선이 모두 임의의 색상으로 그려짐

```python
def contours_hier():
    src = cv2.imread('contours.bmp',
	    cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    contours, hierarchy = cv2.findContours(src,
	    cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

    idx = 0
    while idx >= 0:
        c = (random.randint(0, 255),
	        random.randint(0, 255),
		        random.randint(0, 255))
        cv2.drawContours(dst, contours,
	        idx, c, -1, cv2.LINE_8, hierarchy)
        idx = hierarchy[0, idx, 0]

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6a85ac68-fe64-4467-b82f-c7e9d3af1875/image.png)

-   RETR_CCOMP 모드를 사용 → 2단계로 구성된 계층 구조가 만들어짐

## 외곽선 처리 함수

-   boundingRect() 함수
    -   주어진 외곽선 점들을 감싸는 가장 작은 크기의 사각형, 즉 바운딩 박스를 구하고 싶다면 사용
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/15af0a5d-637c-4a60-a734-417ea41021e7/image.png)
    -   특정 객체의 바운딩 박스는 connectComponentsWithStats() 함수를 이용
    -   외곽선 정보를 가지고 있는 경우
        -   boundingRect() 함수를 이용하여 바운딩 박스를 구하는 것이 효율적
-   minAreaRect() 함수
    -   외곽선 또는 점들을 감싸는 최소 크기의 회전된 사각형을 구하고 싶을 때 사용
    -   특정 외곽선을 감싸는 가장 작은 면적의 사각형 정보를 반환
    -   RotatedRect 클래스 객체를 반환
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/67bade41-4a72-4152-a863-b68e64dbcf09/image.png)
        -   RotatedRect::angle 멤버 변수를 참조하여 객체의 대략적인 회전 각도를 가늠
-   minEnclosingCircle() 함수
    -   외곽선 또는 점들을 감싸는 최소 크기의 원을 구하고 싶을 때 사용
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d3e28671-7b49-4eb9-94d0-5d904598a3f3/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/73442b7a-6090-4544-b27f-1c50956d6fef/image.png)

-   빨간색 : 바운딩 박스
-   파란색 : 최소 크기 회전된 사각형
-   노란색 : 최소 크기 원
-   arcLength() 함수
    -   임의의 곡선을 형성하는 점들의 집합을 가지고 있을 때, 해당 곡선의 길이를 구하고 싶을 때 사용
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d8b80691-d5cb-4ce8-a223-6165c1e5f25e/image.png)
-   contourArea() 함수
    -   임의의 외곽선 정보를 가지고 있을 때, 외곽선이 감싸는 영역의 면적을 알고 싶을 때 사용
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b259c1a6-699f-4516-919a-972a4809e2f6/image.png)
-   approxPolyDP() 함수
    -   외곽선 또는 곡선을 근사화함
    -   주어진 곡선의 형태를 단순화하여 작은 개수의 점으로 구성된 곡선을 생성
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1767ab39-f32c-49ed-a09f-12486e6bd160/image.png)
    -   더글라스-포이커(Douglas-Peucker) 알고리즘을 사용
        -   입력 외곽선에서 가장 멀리 떨어져 있는 두 점을 찾아 직선으로 연결
        -   해당 직선에서 가장 멀리 떨어져 있는 외곽선 상의 점을 찾아 근사화 점으로 추가
        -   이러한 작업을 반복하다가 새로 추가할 외곽선 상의 점과 근사화에 의한 직선과의 수직 거리가 epsilon 인자보다 작으면 근사화를 멈춤
        -   epsilon 인자는 보통 입력 외곽선 또는 곡선 길이의 일정 비율로 지정 - ex) arcLength(curve, true) \* 0.02
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/27ac3953-5438-4b9f-8e61-f33462b8b0c1/image.png)

## (실습) 외곽선 처리 함수

```python
def setLabel(img, pts, label):
    (x, y, w, h) = cv2. boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN,
	    1, (0, 0, 255))

def main():
    img = cv2.imread('ploygon.bmp', cv2.IMREAD_COLOR)

    if img is None:
        print('Image load failed!')
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img_bin = cv2.threshold(gray, 0, 255,
	    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(img_bin,
	    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for pts in contours:
        if cv2.contourArea(pts) < 400:
            continue

        approx = cv2.approxPolyDP(pts,
	        cv2.arcLength(pts, True)*0.02, True)

        vtc = len(approx)

        if vtc == 3:
            setLabel(img, pts, 'TRI')
        elif vtc == 4:
            setLabel(img, pts, 'RECT')
        else:
            length = cv2.arcLength(pts, True)
            area = cv2.contourArea(pts)
            ratio = 4 * math.pi * area / (length * length)

            if ratio > 0.85:
                setLabel(img, pts, 'CIR')

    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
```

-   입력 영상에 있는 모든 도형 객체의 바깥쪽 외곽선을 찾고, 각 외곽선을 근사화
-   근사화된 외곽선이 점 세 개로 표현 → 삼각형, 점 네 개로 표현 → 시각형, 둘 다 아니면 원에 가까운 모양인지 검사
    -   외곽선 모양이 원에 가까운 형태인지를 판별 → 면적 비율 R은 0에서 1사이의 실수로 계산 → 원 모양에 가까울수록 1에 가까운 값

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/f89fe3de-fd32-4dad-ad5c-cbcca43d7824/image.png)

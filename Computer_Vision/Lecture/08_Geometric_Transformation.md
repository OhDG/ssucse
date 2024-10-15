# 어파인 변환(Affine Transformation)

---

## 기하학적 변환(Geometric Transform)

---

-   영상의 기하학적 변환(geometric transform)
    -   영상을 구성하는 픽셀의 배치 구조를 변경함 → 전체 영상의 모양을 바꾸는 작업
    -   픽셀 값은 그대로 유지하면서 위치를 변경하는 작업

## 어파인 변환(Affine Transformation)

-   영상을 평행 이동, 회전, 크기 변환 등을 통해 만들수 있는 변환을 통칭
    -   영상을 한쪽 방향으로 밀어서 만든 것 같은 전단 변환도 어차핀 변환에 포함
    -   직선은 그대로 직선으로 나타남
    -   직선 간의 길이 비율과 평행 관계가 그대로 유지
    -   직사각형 형태의 영상 → 어파인 변환에 의해 평행사변형에 해당하는 모양으로 변경

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c27627a8-efd6-4e0c-a7e9-6bbc73b165b1/image.png)

-   여섯 개의 파라미터를 이용한 수식으로 정의
-   입력 영상의 좌표 (x, y)가 결과 영상의 좌표(x’, y’)로 이동하는 수식
    -   x’ = f1(x, y) = ax + by + c
    -   y’ = f2(x, y) = dx + ey + f
    -   행렬을 이용하여 하나의 수식으로 표현
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4580b922-8bd7-45e3-9999-e868dd950025/image.png)
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7d7f2b9c-fe1b-49c5-9722-19bfe50e6cb9/image.png)
    -   여섯 개의 파라미터로 구성된 2x3 행렬을 어파인 변환 행렬(affinetransformation matrix)이라고 부름
    -   어파인 변환은 2x3 실수형 행렬 하나로 표현할 수 있음
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/66d17667-287d-43ab-a305-01a21419ecbb/image.png)
-   입력 영상과 어파인 변환 결과 영상으로부터 어파인 변환 행렬을 구하기 위해서는 최소 세 점의 이동 관계를 알아야 함
    -   점 하나의 이동 관계로부터 x 좌표와 y 좌표에 대한 변환 수식 두 개를 얻음 → 점 세 개의 이동 관계로부터 총 여섯 개의 방정식
-   직사각형 영상은 평행사변형 형태로 변환 → 입력 영상의 좌측 하단 모서리 점이 이동하는 위치는 자동으로 결정
    -   점 세 개의 이동 관계만으로 정의
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0a97f6a4-a88c-41f6-9428-3161cf7a9ce9/image.png)
-   OpenCV는 어파인 행렬을 구하는 함수와 어파인 변환 행렬을 이용하여 실제 영상을 어파인 변환하는 함수 모두 제공
-   getAffineTransform()
    -   어파인 변환 행렬을 구하는 함수
        -   입력 영상에서 세 점의 좌표와 이 점들이 이동한 결과 영상의 좌표 세 개를 입력으로 받아 2 x 3 어파인 변환 행렬을 계산
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c42c7a24-a33e-46f1-aa6d-6259d78e688f/image.png)
-   warpAffine()
    -   영상을 어파인 변환
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/63701c7c-4dc9-4681-8810-d2ce124eb456/image.png)
-   affine_transform() 함수는 tekapo.bmp 호수 영상을 평행사변형 형태로 변환
    -   입력 영상에서 세 점은 좌측 상단, 우측 상단, 우측 하단의 모서리 점을 선택
    -   이동할 결과 영상에서의 위치는 임의로 지정함

```python
def affine_transform():
    src = cv2.imread('tekapo.bmp')

    if src is None:
        print('Image load failed!')
        return

    rows = src.shape[0]
    cols = src.shape[1]

    src_pts = np.array([[0, 0], [cols- 1, 0], [cols - 1, rows - 1]]).astype(np.float32)
    dst_pts = np.array([[50, 50], [cols - 100, 100], [cols - 50, rows - 50]]).astype(np.float32)

    affine_mat = cv2.getAffineTransform(src_pts, dst_pts)

    dst = cv2.warpAffine(src, affine_mat, (0, 0))

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
```

-   입력 영상에서 세 모서리 점이 지정한 위치로 적절하게 이동
    -   어파인 변환된 결과 영상이 평행사변형 형태로 나타남
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5e05d444-ee48-4598-a124-c13c61100f22/image.png)
-   어파인 변환 행렬을 가지고 있을 때
    -   영상 전체를 어파인 변환하는 것이 아니라 일부 점들이 어느 위치로 이동하는지를 알고 싶다면 transform() 함수를 사용
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0160953e-526e-4914-84ca-04fe246e4926/image.png)

## 이동 변환(Translation Transformation)

---

-   영상을 가로 또는 세로 방향으로 일정 크기만큼 이동시키는 연산
    -   시프트(shift) 연산이라고도 함
-   입력 영상의 모든 좌표를 x 방향으로 a만큼, y 방향으로 b만큼 이동하는 변환을 수식
    -   x’ = x + a
    -   y’ = y + b
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/83769496-d3d9-43f3-9abb-812549fe5dd8/image.png)
-   영상을 x 방향으로 a만큼, y 방향으로 b만큼 이동하는 어파인 변환 행렬 M
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/10b1c00c-3640-4cbb-89c4-5b699df629b4/image.png)
-   OpenCV에서 영상을 이동 변환 → 2x3 실수 행렬 M을 만들고, 이를 warpAffine() 함수 인자로 전달

```python
def affine_translation():
    src = cv2.imread('tekapo.bmp')

    if src is None:
        print('Image load failed!')
        return

    affine_mat = np.array([[1, 0, 150], [0, 1, 100]]).astype(np.float32)

    dst = cv2.warpAffine(src, affine_mat, (0, 0))

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
```

-   결과 영상에서 호수 영상이 (150, 100) 좌표부터 나타남
    -   입력 영상의 픽셀 값이 복사되지 않은 영역은 검은색으로 채워짐

## 전단 변환(Shear Transformation)

---

-   직사각형 형태의 영상을 한쪽 방향으로 밀어서 평행사변형 모양으로 변형 (층밀림 변환)
    -   가로 방향 또는 세로 방향으로 각각 정의할 수 있음
    -   픽셀이 어느 위치에 있는가에 따라 이동 정도가 달라짐
-   입력 영상에서 원점은 전단 변환에 의해 이동하지 않고 그대로 원점에 머물러 있음

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/393da7ed-4e09-431b-88b8-0d1fc2db7eb6/image.png)

-   y 좌표가 증가함에 따라 영상을 가로 방향으로 조금씩 밀어서 만드는 전단 변환 수식
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b8307469-a829-4029-8c44-2cbbbe9ac206/image.png)
-   x 좌표가 증가함에 따라 영상을 세로 방향으로 조금씩 밀어서 만드는 전단 변환 수식
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/db6cd3e3-52d4-4d07-8b0a-0e356357c80f/image.png)
-   앞의 두 수식에서 mx와 my는 영상으로 각각 가로 방향과 세로 방향으로 밀림 정도를 나타내는 실수
-   전단 변환을 나타내는 2x3 어파인 변환 행렬 M
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2687bfe3-f7a3-45b2-a39f-017ec1675dc7/image.png)
-   affine_shear() 함수는 tekapo.bmp 호수 영상에 대해 y좌표가 증가함에 따라 0.3y에 해당하는 x 좌표에서 원본 영상 픽셀이 나타나기 시작하는 전단 변환을 수행
    ```python
    def affine_shear():
        src = cv2.imread('tekapo.bmp')

        if src is None:
            print('Image load failed!')
            return

        rows = src.shape[0]
        cols = src.shape[1]

        mx = 0.3
        affine_mat = np.array([[1, mx, 0], [0, 1, 0]]).astype(np.float32)

        dst = cv2.warpAffine(src, affine_mat, (int(cols + rows * mx), rows))

        cv2.imshow('src', src)
        cv2.imshow('dst', dst)
        cv2.waitKey()
        cv2.destroyAllWindows()
    ```
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e7ed1143-20f5-49e8-a8f0-c0595efd1583/image.png)
    -   입력 영상 일부가 잘리지 않도록 결과 영상 크기를 적절하게 확대함
    -   가로 방향으로 층밀림을 수행
    -   dst 영상의 가로 크기는 src.cols + src.rows \* mx로 설정함

## 크기 변환

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/23403c35-9a11-45e5-9528-6162afcd3545/image.png)

-   노란색 사각형 영역은 w x h 크기의 원본 영상
-   녹색으로 표시한 사각형 영역은 w’ x h’ 크기로 확대된 결과 영상
-   원본 영상의 가로 픽셀 크기가 w 이고 결과 영상의 가로 크기가 w’ → 크기 변환 비율 s_x = w’ / w
-   마찬가지로 s_y = h’ / h
-   입력 영상의 좌표 (x, y)로부터 크기 변환 결과 영상의 좌표 (x’, y’)를 계산하는 수식
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/3c0ec2fe-f427-484a-8a90-98d361f52cd2/image.png)
-   s_x 또는 s_y가 1보다 크면 영상이 확대, 1보다 작으면 축소
-   영상의 크기 변환을 나타내는 어파인 변환 행렬
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/67fb7587-11ac-4a60-b16f-1e7b456f531a/image.png)
-   어파인 변환 행렬을 생성하고 warpAffine() 함수를 이용 → 영상의 크기 변환 가능
-   OpenCV는 보다 간단하게 크기를 변경할 수 있는 resize() 함수를 제공
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/25f53a6a-0071-4d44-a061-1160805e0a5b/image.png)
    -   이 경우 결과 영상의 크기
        -   dst.rows = round(src.rows x fx)
        -   dst.cols = round(src.cols x fy)
        -   resize() 함수의 여섯 번쨰 인자 interpolation에는 보간법(interpolation) 알고리즘을 나타내는 InterpolationFlags 열거형 상수를 지정
            -   보간법은 결과 영상의 픽셀 값을 결정하기 위해 입력 영상에서 주변 픽셀 값을 이용하는 방식을 의미

### InterpolationFlags 열거형 상수

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b933ae37-756e-4eae-b008-906b2eeb6797/image.png)

### Interpolation

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/78e330e3-8e1d-45cf-b075-a1577cd9ee09/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/25bf1c89-e877-432e-b6b5-2ad91c28a7f2/image.png)

-   INTER_LINEAR 방법
    -   연산 속도가 빠르고 화질도 충분히 좋은 편이라서 널리 사용됨
    -   resize() 함수에서 기본값으로 설정됨
-   INTER_CUBIC, INTER_LANCZOS4 상수를 사용 → INTER_LINEAR 방법보다 더 좋은 화질
-   영상을 축소하는 경우 INTER_AREA 방법을 사용 → 무아레(moire) 현상이 적게 발생 → 화질 면에서 유리

### Moire effect

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d5fd5165-6dc5-49c7-a756-2c2ddad2f02c/image.png)

### Interpolation

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c64c2d71-e8f6-4f36-b1aa-bc7f876f0ec4/image.png)

```python
def affine_scale():
    src = cv2.imread('rose.bmp')

    if src is None:
        print('Image load failed!')
        return

    dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
    dst2 = cv2.resize(src, (1920, 1280))
    dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)
    dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)

    cv2.imshow('src', src)
    cv2.imshow('dst1', dst1[400:800, 500:900])
    cv2.imshow('dst2', dst2[400:800, 500:900])
    cv2.imshow('dst3', dst3[400:800, 500:900])
    cv2.imshow('dst4', dst4[400:800, 500:900])
    cv2.waitKey()
    cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d16d40a2-d8ed-4ee5-8a48-1e9d4f5f4e9d/image.png)

## 회전 변환(Rotation Transformation)

---

-   특정 좌표를 기준으로 영상을 원하는 각도만큼 회전하는 변환
-   영상의 회전 변환에 의해 입력 영상의 점 (x, y)가 이동하는 점의 좌표 (x’, y’)
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2fee55e3-8b7a-495a-abe6-e74561e40a80/image.png)

### 좌표계의 차이

---

-   일반 좌표계에서는 세타가 양수일 때 반시계 방향
-   Graphics에서는 세타가 양수일 때 시계 방향
-   반시계 방향으로 맞춰 주기 위해 -세타 로 처리
-   원점을 기준으로 영상을 반시계 방향으로 세타 만큼 회전하는 변환
-   노란색 사각형은 원본 영상, 녹색으로 표시한 사각형이 회전 변환으로 생성된 결과 영상

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e11dfc00-3bf3-4a63-9713-b5e4312fae53/image.png)

-   영상을 반시계 방향으로 세타 만큼 회전하는 어파인 변환 행렬 M
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/26a3e3d6-c1ad-46ad-9bb3-0229c5fa99e9/image.png)
-   cos() 함수와 sin() 함수를 이용하여 위의 행렬을 생성
    -   warpAffine() 함수를 사용하면 영상을 회전시킬 수 있음
-   OpenCV는 영상의 회전을 위한 어파인 변환 행렬을 생성하는 getRotationMatrix2D() 함수를 제공
    -   영상을 원점이 아닌 특정 좌표를 기준으로 회전, 필요한 경우 크기 변환까지 함께 수행하는 어파인 변환 행렬을 쉽게 만들 수 있음
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/96ffa745-6da1-422e-9ba6-46134fc20735/image.png)
-   getRotationMatrix2D() 함수가 반환하는 어파인 변환 행렬
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/562cdc13-f2a1-4b8e-aa60-7c203151aab4/image.png)
-   alpha = scale _ cos(angle), beta = scale _ sin(angle)
-   영상 중심을 기준으로 반시계 방향으로 20도 만큼 회전
    ```python
    def affine_rotation():
        src = cv2.imread('rose.bmp')

        if src is None:
            print('Image load failed!')
            return

        cp = (src.shape[1] / 2, src.shape[0] / 2)
        affine_mat = cv2.getRotationMatrix2D(cp, 20, 1)

        dst = cv2.warpAffine(src, affine_mat, (0, 0))

        cv2.imshow('src', src)
        cv2.imshow('dst', dst)
        cv2.waitKey()
        cv2.destroyAllWindows()
    ```
    -   입력 영상의 일부가 잘리지 않게 영상을 회전 → 결과 영상의 크기를 더 크게 설정하고 회전과 이동 변환을 함께 고려해야 함
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4814773a-341d-41fe-9ccc-a5edbb32638b/image.png)

## 특수한 회전 변환

---

-   OpenCV에서 영상을 90도 단위로 회전하고 싶을 경우에는 rotate() 함수를 사용
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0101dd1b-ce7b-46b6-827b-3bec02a066ec/image.png)

## 대칭 변환

---

-   영상의 좌우를 서로 바꾸거나 또는 상하를 뒤집는 형태의 변환
-   좌우 대칭 또는 좌우 반전 이라고 함
-   상하 대칭 또는 상하 반전이라고 함
-   대칭 변환은 입력 영상과 같은 크기의 결과 영상을 생성
-   입력 영상의 픽셀과 결과 영상의 픽셀이 일대일로 대응 → 보간법이 필요하지 않음
-   영상의 좌우 대칭 변환에 의한 좌표 변환 수식
    -   x’ = w - 1 - x
    -   y’ = y
    -   w는 입력 영상의 가로 크기
    -   행렬 형태로 표현
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9c13cb13-6893-459b-99e0-4b9f6ebf2b3d/image.png)
    -   영상을 x축 방향으로 -1배 크기 변환한 후 x축 방향으로 w-1만큼 이동 변환한 것
    -   좌우 대칭 변환도 어파인 변환의 일종
-   상하 대칭 변환도 비슷함
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/3dc11bf4-792a-40de-a0ed-dade0ec8e3a0/image.png)
    -   h는 입력 영상의 세로 크기
-   OpenCV는 영상의 대칭 변환을 수행하는 flip() 함수를 제공
    -   영상을 가로, 세로, 또는 가로와 세로 양 방향에 대해 대칭 변환한 영상을 제공
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9840689e-d384-4907-b872-62f80fe23c2c/image.png)
-   affine_flip() 함수는 영상을 좌우, 상하, 상하 및 좌우 대칭을 수행한 결과를 화면에 출력
    ```python
    def affine_flip():
        src = cv2.imread('eastsea.bmp')

        if src is None:
            print('Image load failed!')
            return

        cv2.imshow('src', src)

        for flip_code in [1, 0, -1]:
            dst = cv2.flip(src, flip_code)

            desc = 'flipCode: %d' % flip_code
            cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 1, cv2.LINE_AA)

            cv2.imshow('dst', dst)
            cv2.waitKey()

    cv2.destroyAllWindows()
    ```
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/904f4dbb-7299-4235-9245-95b7979c6699/image.png)

# 투시 변환(Projective Transformation)

---

## 투시 변환(Perspective Transform)

---

-   어파인 변환보다 자유도가 높은 투시 변환(perspective transform)이 있음
-   투시 변환은 직사각형 형태의 영상을 임의의 볼록 사각형 형태로 변경할 수 있는 변환
-   투시 변환에 의해 원본 영상에 있던 직선 → 결과 영상에서 그대로 직진성이 유지, 두 직선의 평행 관계는 깨어질 수 있음
-   점 네 개의 이동 관계에 의해 결정되는 투시 변환

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8cd65a8a-6d5a-4e81-acb9-5fedc2777c75/image.png)

-   투시 변환은 직선의 평행 관계가 유지되지 않기 때문에 결과 영상의 형태가 임의의 사각형으로 나타남
-   점 하나의 이동 관계로부터 x 좌표에 대한 방정식 하나와 y 좌표에 대한 방정식 하나를 얻음
    -   점 네 개의 이동 관계로부터 여덟 개의 방정식을 얻을 수 있음
    -   이 여덟 개의 방정식으로부터 투시 변환을 표현하는 파라미터 정보를 계산
-   투시 변환은 보통 3x3 크기의 실수 행렬로 표현
-   투시 변환은 여덟 개의 파라미터로 표현할 수 있지만, 좌표 계산의 편의상 아홉 개의 원소를 갖는 3x3 행렬을 사용
-   투시 변환을 표현하는 행렬을 M_p
    -   입력 영상의 픽셀 좌표 (x, y)가 행렬 M_p에 의해 이동하는 결과 영상 픽셀 좌표는 (x’, y’)
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/f6eadd02-afd1-4fc5-8213-dbe55bd007fe/image.png)
        -   입력 좌표와 출력 좌표를 (x, y, 1), (wx’, wy’, w) 형태로 표현
            -   동차 좌표계(homogeneous coordinates)라고 함
        -   w는 결과 영상의 자표를 표현할 때 사용되는 비례 상수
            -   w = p31x + p32y + p33
        -   x’, y’
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4ca16143-c3b2-4a4f-a5bc-8df8af9d699c/image.png)
-   OpenCV는 투시 변환 행렬을 구하는 함수와 실제 영상을 투시 변환하는 함수를 모두 제공
-   getPerspectiveTransform()
    -   투시 변환 행렬을 구하는 함수
        -   입력 영상에서 네 점의 좌표와 이 점들이 이동한 결과 영상의 좌표 네 개를 입력으로 받아 3x3 투시 변환 행렬을 계산
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/484f04a6-b534-4d8c-b3b6-f93d707470bb/image.png)
-   3x3 투시 변환 행렬을 가지고 있을 때, 영상을 투시 변환한 결과 영상을 생성하려면
    -   warpPerspective() 함수
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/25bbaaec-42bc-4331-9ddc-98b060809c78/image.png)
-   사용자가 마우스로 카드 모서리 좌표를 선택하면 해당 카드를 반듯한 직사각형 형태로 투시 변환
    ```python
    def on_mouse(event, x, y, flags, param):
        global cnt, src_pts
        if event == cv2.EVENT_LBUTTONDOWN:
            if cnt < 4:
                src_pts[cnt, :] = np.array([x, y]).astype(np.float32)
                cnt += 1

                cv2.circle(src, (x, y), 5, (0, 0, 255), -1)
                cv2.imshow('src', src)

            if cnt == 4:
                w = 200
                h = 300

                dst_pts = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]]).astype(np.float32)

                pers_mat = cv2.getPerspectiveTransform(src_pts, dst_pts)

                dst = cv2.warpPerspective(src, pers_mat, (w, h))

                cv2.imshow('dst', dst)

    cnt = 0
    src_pts = np.zeros([4, 2], dtype=np.float32)
    src = cv2.imread('card.bmp')

    if src is None:
        print('Image load failed!')
        exit()

    cv2.namedWindow('src')
    cv2.setMouseCallback('src', on_mouse)

    cv2.imshow('src', src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ```
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/cc44eafd-adc6-45cc-93d9-cb3289c6dbab/image.png)
    -   마우스를 이용한 좌표 선택 → 카드의 좌측 상단 모서리 점부터 시작하여 시계 방향 순서로 선택해야 함
    -   마우스로 클릭한 위치는 빨간색 원을 그려서 표시함
    -   일반적인 카드의 가로 대 세로 크기 비율이 2:3 → dst 창에 나타날 영상의 크기를 200x300으로 설정
    -   다이아 K 카드가 200x300 크기로 반듯하게 투시 변환
-   3x3 투시 변환 행렬을 가지고 있을 때
    -   일부 점들이 투시 변환에 의해 어느 위치로 이동할 것인지 알고 싶다면
        -   perspectiveTransform() 함수를 사용
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0e25eb89-b90f-4902-84b3-9a9fb1762e90/image.png)

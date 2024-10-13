# 영상의 산술 연산

---

-   영상은 일종의 2차원 행렬 → 행렬의 산술 연산(arithmetic operation)을 그대로 적용 가능
-   영상의 덧셈 연산 수식, 포화 연산도 함께 수행
    -   dst(x, y) = saturate(src1(x, y) + src2(x, y))
-   OpenCV에서는 add() 함수를 사용하여 영상의 덧셈을 수행
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c7b815fa-285d-42fa-9be7-603b2ddf7af1/image.png)
    -   영상/행렬 또는 정수, 실수 자료형 등을 전달
    -   src1과 src2가 모두 영상인 경우 일반적인 행렬의 덧셈 연산
    -   src1이 영상/행렬이고 src2는 정수, 실수라면 src1 행렬의 모든 픽셀 값에 src2 값을 더하여 결과 영상을 생성
    -   덧셈 결과가 dst 객체가 표현할 수 있는 자료형 범위를 벗어나면 자동으로 포화 연산을 수행
    -   add() 함수에서 mask 인자와 dtype 인자는 기본값을 가짐
        -   변경할 필요가 없다면 따로 지정 안해도 됨
-   덧셈 연산의 결과 영상은 두 입력 영상의 윤곽을 조금씩 포함
    -   전반적으로 밝게 포화되는 부분이 많음
-   두 영상을 더할 때 각 영상에 가중치를 부여하는 경우
    -   dst(x, y) = saturate(알파*src1(x, y) + 베타*src2(x, y))
    -   알파와 베타는 각각 src1과 src2 영상의 가중치를 의미하는 실수
    -   보통 알파 + 베타 = 1이 되도록 가중치를 설정
        -   알파=베타=0.5 : 두 입력 영상의 윤곽을 골고루
        -   알파+베타>1 : 결과 영상이 두 입력 영상보다 밝아짐, 255보다 커지는 포화 현상 발생
        -   알파+베타<1 : dst 영상은 두 입력 영상의 평균 밝기보다 어두운 결과 영상
-   OpenCV에서 가중치 합을 구할 때 addWeighted() 함수를 사용
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/954f1eaf-41a9-43e4-bdf7-0552a669ca99/image.png)
    -   addWeighted() 함수는 gamma 인자를 통해 가중치의 합에 추가적인 덧셈을 한꺼번에 수행 가능
        -   dst(x, y) = saturate( src1(x, y) _ alpha + src2(x, y) _ beta + gamma )
    ```cpp
    Mat src1 = imread("aero2.bmp", IMREAD_GRAYSCALE);
    Mat src2 = imread("camera.bmp", IMREAD_GRAYSCALE);

    Mat dst;
    addWeighted(src1, 0.5, src2, 0.5, 0, dst);
    ```
    -   두 입력 영상의 윤곽을 골고루 포함, 평균 밝기가 그대로 유지됨
-   두 개의 영상에 대하여 뺄셈 연산도 수행 가능
    -   dst(x, y) = saturate(src1(x, y) - src2(x, y))
    -   뺄셈의 결과가 0보다 작아지면 결과 영상의 픽셀 값을 0으로 설정하는 포화 연산을 수행
-   OpenCV에서는 subtract() 함수를 통해 두 영상의 뺄셈 연산을 수행
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b141de4e-1695-4a65-90a7-b6105ac34b48/image.png)
    -   뺄셈 연산은 뺄셈의 대상이 되는 영상 순서에 따라 결과가 달라짐
-   뺄셈 순서에 상관없이 픽셀 값 차이가 큰 영역을 두드러지게 나타내고 싶다면 차이 연산을 수행
    -   차이 연산은 뺄셈 연산 결과에 절댓값을 취하는 연산
    -   차이 연산으로 구한 결과 영상을 차영상(difference image)라고 함
-   OpenCV에서는 absdiff() 함수를 이용하여 차영상을 구함
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/64787a5c-3695-4d0e-b9fc-1b9b98694651/image.png)
    -   차이 연산을 이용하면 두 개의 영상에서 변화가 있는 영역을 쉽게 찾을 수 있음
    -   큰 변화가 없는 영역은 픽셀 값이 0에 가까운 검은색으로 채워짐
-   영상도 일종의 행렬 → 행렬의 곱셈 수행 가능
    -   영상을 이용한 행렬의 곱셈을 수행하는 경우는 거의 없음
-   OpenCV에서는 multiply() 함수와 divide() 함수를 제공
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6c75d60b-6bdf-41a1-95b1-c3065e762aba/image.png)
-   두 이미지 파일을 이용하여 덧셈, 뺄셈, 평균, 차이 영상을 생성

```python
src1 = cv2.imread('lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('square.bmp', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    exit()

dst1 = cv2.add(src1, src2)
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
dst3 = cv2.subtract(src1, src2)
dst4 = cv2.absdiff(src1, src2)

cv2.imshow('src1', src1)
cv2.imshow('src2', src2)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)
cv2.waitKey()
cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/766ff4b7-7d29-405d-acdc-dbaad70a6fa4/image.png)

# 영상의 논리 연산

---

-   픽셀 값을 이진수로 표현하여 각 비트(bit) 단위 논리 연산을 수행하는 것
-   OpenCV에서는 논리곱(AND), 논리합(OR), 배타적 논리합(XOR), 부정(NOT) 연산을 지원
    -   AND : 두 개의 입력 비트가 모두 1인 경우에 결과가 1
    -   OR : 두 개 중 하나라도 1이 있으면 결과는 1
    -   XOR : 두 개의 입력 비트 중 오직 하나만 1인 경우에 결과가 1이 되고, 입력 비트가 모두 0이거나 모두 1이면 결과가 0
    -   NOT : 하나의 입력 영상에 대해 동작하며 입력 비트가 0이면 결과가 1이 되고 입력 비트가 1이면 결과가 0이 됨
-   영상의 논리 연산은 각 픽셀 값에 대하여 비트 단위로 이루어짐
-   그레이스케일 영상
    -   한 픽셀을 구성하는 여덟 개의 비트에 모두 논리 연산이 이루어짐

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6b9e00e4-f189-4847-bae7-7808ac4f1eed/image.png)

-   OpenCV에서 제공하는 논리 연산 함수
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/62d07eb6-0ea7-4199-8f32-a90aca942077/image.png)
    -   bitwise_and(), bitwise_or(), bitwise_xor() 함수는 두 개의 영상을 입력으로 받음
    -   bitwise_not() 함수는 하나의 영상을 입력으로 받음
    -   각각의 함수들은 모두 mask 인자를 가짐
        -   mask 영상의 픽셀 값이 0이 아닌 위치에만 논리 연산을 수행하도록 설정할 수 있음
            -   Mask 인자를 따로 지정하지 않을 경우 영상 전체에 대해 논리 연산을 수행
    ```python
    src1 = cv2.imread('lenna256.bmp', cv2.IMREAD_GRAYSCALE)
    src2 = cv2.imread('square.bmp', cv2.IMREAD_GRAYSCALE)

    if src1 is None or src2 is None:
        print('Image load failed!')
        exit()

    dst1 = cv2.bitwise_and(src1, src2)
    dst2 = cv2.bitwise_or(src1, src2)
    dst3 = cv2.bitwise_xor(src1, src2)
    dst4 = cv2.bitwise_not(src1)

    cv2.imshow('src1', src1)
    cv2.imshow('src2', src2)
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.imshow('dst3', dst3)
    cv2.imshow('dst4', dst4)
    cv2.waitKey()
    cv2.destroyAllWindows()
    ```
    -   square.bmp 영상에서 가운데 사각형 영역의 픽셀 값은 255, 이진수로 표현하면 모든 비트가 1로 설정된 11111111(2)
        -   사각형 바깥 영영의 픽셀 값은 0, 이진수로 표현하면 00000000(2)
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2a17d15c-7552-497f-aca3-7fc21f8b737b/image.png)

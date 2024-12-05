# 머신 러닝과 OpenCV

## 머신 러닝 개요

-   머신 러닝(machine learning)
    -   주어진 데이터를 분석하여 규칙성, 패턴을 찾음
        -   이를 이용하여 의미 있는 정보를 추출하는 과정
    -   다수의 사과와 바나나 사진으로부터 사과와 바나나를 구분할 수 있는 특징 또는 규칙
        -   이를 이용하여 새로운 사진이 들어 왔을 때 이것이 사과인지 또는 바나나인지를 판별하는 작업이 머신 러닝이 하는 일
-   학습(train) 또는 훈련
    -   데이터로부터 규칙을 찾아내는 과정
-   모델(model)
    -   학습에 의해 결정된 규칙
-   예측(predict) 또는 추론(inference)
    -   새로운 데이터를 학습된 모델에 입력으로 전달하고 결과를 판단하는 과정
-   레이블(label)
    -   훈련 데이터에 대한 정답에 해당하는 내용
-   머신 러닝은 크게
    -   지도 학습(supervised learning)
    -   비지도 학습(unsupervised learning)
-   지도 학습
    -   정답을 알고 있는 데이터를 이용하여 학습을 진행하는 방식
    -   사과 사진과 바나나 사진을 구분하기 위해
        -   각각의 사진이 사과 사진인지 바나나 사진인지를 함께 알려 주어야 함
        -   머신 러닝 알고리즘은 사과 사진과 바나나 사진을 구분 지을 수 있는 규칙을 찾기 위해 수학적 또는 논리적 연산을 수행
-   영상 데이터는 픽셀로 구성
    -   이 픽셀 값을 그대로 머신 러닝 입력으로 사용하는 것은 그다지 흔하지 않음
    -   영상의 픽셀 값은 조명 변화, 객체의 이동 및 회전 등에 의해 매우 민감하게 변화
-   많은 머신 러닝 응용에서는
    -   영상의 다양한 변환에도 크게 변경되지 않는 특징 정보를 추출하여 머신 러닝 입력으로 전달
-   사과와 바나나 사진을 구분하는 용도
    -   영상의 주된 색상(hue) 또는 객체 외곽선과 면적 비율 등이 유효한 특징으로 사용될 수 있음
-   영상 데이터를 사용하는 지도 학습
    -   먼저 다수의 훈련 영상에서 특징 벡터를 추출
        -   이를 이용하여 머신 러닝 알고리즘을 학습시킴
    -   예측 과정에서도
        -   입력 영상으로부터 특징 벡터를 추출 - 이 특징 벡터를 학습 모델 입력으로 전달하면 입력 영상이 어떤 영상인지에 대한 예측 결과를 얻을 수 있음
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b1e56679-eb5b-4174-b0e5-f40a75dd3886/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7c1b5588-317d-4e11-ab62-b34efec05fdc/image.png)

-   지도 학습은 주로 회귀(regression) 또는 분류(classification)에 사용됨
-   회귀
    -   연속된 수치 값을 예측하는 작업
    -   기름 분사량에 따라 온도를 예측하는 모델
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2bb798c7-c3f6-4097-b364-9fb6397aabd8/image.png)

## 머신 러닝 개요 - 학습

-   훈련 집합에 있는 샘플을 최소 오류로 맞히는 최적의 가중치 값을 알아내는 작업
-   단순한 경우 방정식을 풀어 해결하는 분석적 방법(analytical method) 사용
-   기계학습은 오류를 조금씩 줄이는 과정을 반복하는 수치적 방법(numerical method) 사용
-   모델의 오류를 측정하는 손실 함수(loss function) 필요

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/eb425401-0584-4c22-b110-c7ca701f78de/image.png)

## 머신 러닝 개요

-   분류
    -   이산적인 값을 결과로 출력하는 머신 러닝
    -   사과를 0번 클래스, 바나나를 1번 클래스
        -   새로운 사진이 머신 러닝 입력으로 들어오면 결과를 0 또는 1로 나오게 설정하는 것
    -   입력 영상이 사과인지 바나나인지를 구분하는 것을 인식(recognition)이라고 부름
        -   결국은 분류 문제에 해당
-   검출, 분할, 추적 등의 다양한 문제
-   데이터 수집은 많은 비용 소요
-   공개 데이터 활용

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9463eb65-18ff-4875-9c7b-9e9df300e6ef/image.png)

-   비지도 학습
    -   훈련 데이터의 정답에 대한 정보 없이 오로지 데이터 자체만을 이용하는 학습 방식
    -   무작위로 섞여 있는 사과와 바나나 사진을 입력으로 전달
        -   전체 사진을 두 개의 그룹으로 나누도록 학습시키는 방식
        -   색상 정보만 적절하게 이용하여도 전체 사진을 사과 사진과 바나나 사진으로 구분 가능
        -   분리된 두 개의 사진 집합이 무엇을 의미하는지는 알 수 없음
        -   단지 두 사진 집합에서 서로 구분되는 특징을 이용하여 서로 분리하는 작업만 수행하는 것
        -   주로 군집화(clustering)에 사용됨
-   많은 머신 러닝 알고리즘이 지도 학습을 이용한 영상 분류 문제에 사용되고 있음
    -   사과와 바나나 영상을 구분하는 것
    -   0부터 9까지의 필기체 숫자를 인식하는 것
-   머신 러닝을 이용하여 분류를 수행하는 경우
    -   학습된 분류 모델이 얼마나 제대로 동작하는지를 확인해야 하는 경우가 있음
        -   학습된 모델의 성능이 좋지 않다면 다른 머신 러닝 알고리즘을 선택하거나 영상에서 다른 특징 벡터를 추출하는 것으로 고려해야 함

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6b239852-22c6-40c8-847a-ff3e0fbe42d7/image.png)

-   많은 사람이 사용할 수 있는 영상 데이터 전체를 학습에 사용하지 않음
    -   일부는 성능 측정을 위한 테스트 용도로 사용
    -   주어진 1만 개의 영상 중에서 8000개만 학습에 사용함
        -   나머지 2000개 영상으로는 테스트를 수행하여 머신 러닝 분류 정확도를 계산하는 방식
-   머신 러닝 알고리즘 종류에 따라서는 내부적으로 사용하는 많은 파라미터에 의해 성능이 달라지기도 함
    -   최적의 파라미터를 찾는 것이 해결해야 할 문제
    -   이런 경우에는 훈련 데이터를 k개의 부분 집합으로 분할
        -   학습과 검증(validation)을 반복하면서 최적의 파라미터를 찾을 수도 있음

## k-폴드 교차 검증(k-fold cross-validation)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ce4a478c-7371-41dd-8e3e-f8c0baf14b24/image.png)

-   훈련 데이터를 k개의 부분 집합으로 분할하여 학습과 검증을 반복하는 작업
    -   8000개의 훈련 영상을 800개씩 열 개의 부분 집합으로 분할
    -   이 중 아홉 개의 부분 집합으로 학습하고 나머지 한 개의 집합을 이용하여 성능을 검증
    -   검증을 위한 부분 집합을 바꿔 가면서 여러 번 학습과 검증을 수행
    -   이러한 작업을 다양한 파라미터에 대해 수행하면서 가장 성능이 높게 나타나는 파라미터를 찾을 수 있음

## 머신 러닝 개요

-   머신 러닝 알고리즘으로 훈련 데이터를 학습할 경우
    -   훈련 데이터에 포함된 잡음 또는 이상치(outlier)의 영향으로 고려해야 함
-   많은 머신 러닝 분류 알고리즘이 훈련 데이터를 효과적으로 구분하는 경계면을 찾으려고 함
    -   훈련 데이터에 잘못된 정보가 섞여 있다면
        -   경계면을 어떻게 설정하는 것이 좋은지 모호해질 수 있음

## 훈련 데이터에 이상치가 있을 경우

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b2d99951-1bb4-4722-beb6-7884ba2f7346/image.png)

-   빨간색 삼각형과 파란색 사각형 점을 구분하는 분류 문제
    -   두 가지 종류의 점을 완벽하게 구분하는 경계면 : 보라색 점선
        -   훈련 데이터에 대해서는 100% 정확하게 동작
            -   실제 새로운 입력 데이터에 대해서는 오히려 정확도가 떨어질 수 있는 가능성
            -   a와 b 점은 각각 빨간색 삼각형과 파란색 사각형 분포와 동떨어진 위치에 존재
            -   잡음 또는 잘못 측정된 값일 가능성
    -   녹색 실선 경계면을 사용

## OpenCV 머신 러닝 클래스

-   OpenCV에서 제공하는 머신 러닝 클래스
    -   주로 ml 모듈에 포함됨
    -   cv::ml::StatModel 추상 클래스를 상속받아 만들어짐
    -   StatModel 클래스 이름은 통계적 모델(statistical model)을 의미
-   StatModel 클래스
    -   머신 러닝 알고리즘을 학습시키는 StatModel::train() 멤버 함수와 학습된 모델을 이용함
    -   테스트 데이터에 대한 결과를 예측하는 StatModel::predict() 멤버 함수를 가지고 있음
    -   각각의 머신 러닝 알고리즘에 해당하는 train()과 predict() 기능을 재정의

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d6683c24-30f7-4e07-92c1-902b99af991f/image.png)

-   StatModel::train() 함수 원형
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d5bf5c18-a635-4957-ae62-aa59e9761a1e/image.png)
    -   SampleTypes 열거형 상수
        -   많은 경우 ROW_SAMPLE 방법을 사용
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/246f5727-110d-4ed7-9369-6233a6f66014/image.png)
    -   StatModel::train() 함수는 가상 함수로 선언됨
        -   StatModel 클래스를 상속받은 클래스 객체에서 train() 함수를 호출함
        -   각 알고리즘에 해당하는 방식으로 학습을 진행
-   StatModel::predict() 함수
    -   이미 학습된 모델에 대해 테스트 데이터의 응답을 얻고 싶을 때 사용
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a915ba73-0966-4990-b57f-83f5b8769aa9/image.png)
    -   StatModel::predict() 함수는 순수 가상 함수로 선언됨
    -   각각의 머신 러닝 알고리즘 구현 클래스는 자신만의 알고리즘을 이용한 예측을 수행하도록 predict() 함수를 재정의하고 있음
    -   일부 머신 러닝 알고리즘 구현 클래스는 predict() 함수를 대신할 수 있는 고유의 예측 함수를 제공
-   OpenCV 머신 러닝 클래스 이름과 의미
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7809ac0a-6c2c-4ebf-8982-22d290822ee5/image.png)
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6f9e0351-edf2-44c4-9655-c31dda756e19/image.png)
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b47ab8d0-f2af-4a09-87ed-d65bf18fd4d4/image.png)

## Gradient Descent

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/3fc5fb98-ca1b-4517-8321-1f2b42a52643/image.png)

-   **목적**: 손실 함수(Loss Function)를 최소화하여 모델이 데이터에 적합한 패턴을 학습하도록 함.
-   **경사(Gradient)**: 손실 함수의 기울기를 계산하여 파라미터가 얼마나 변해야 손실이 줄어드는지 방향과 크기를 결정.
-   **학습률(Learning Rate)**: 파라미터 업데이트 크기를 결정하는 하이퍼파라미터.

### 1. **Batch Gradient Descent**

-   **설명**:
    -   전체 데이터셋에 대해 손실 함수를 계산한 뒤, 평균 기울기를 사용하여 파라미터를 업데이트.
-   **특징**:
    -   파라미터 업데이트가 안정적이며 수렴 속도가 일정.
    -   계산 비용이 크며 대규모 데이터셋에서는 느릴 수 있음.
-   **장점**:
    -   전역 최소점으로 수렴 가능성이 높음.
-   **단점**:
    -   데이터가 클 경우 메모리와 연산 요구량이 큼.

### 2. **Stochastic Gradient Descent (SGD)**

-   **설명**:
    -   각 데이터 포인트마다 손실 함수의 기울기를 계산하고 파라미터를 업데이트.
-   **특징**:
    -   빠른 계산이 가능하며, 메모리 효율적.
    -   경로가 불안정하고 노이즈가 많아 수렴 경로가 요동침.
-   **장점**:
    -   빠른 업데이트와 낮은 메모리 사용.
    -   지역 최소점에서 벗어날 가능성이 있어 복잡한 손실 함수에서도 효과적.
-   **단점**:
    -   진동이 많아 수렴 속도가 느릴 수 있음.

### 3. **Mini-Batch Gradient Descent**

-   **설명**:
    -   데이터셋을 여러 개의 작은 배치로 나누어 배치 단위로 손실 함수의 기울기를 계산하여 파라미터를 업데이트.
-   **특징**:
    -   Batch Gradient Descent와 Stochastic Gradient Descent의 장점을 결합.
    -   업데이트가 효율적이고 비교적 안정적.
-   **장점**:
    -   계산 효율성과 수렴 안정성 모두 우수.
-   **단점**:
    -   배치 크기 설정에 따라 성능이 달라질 수 있음.

# k 최근접 이웃

## k 최근접 이웃 알고리즘

-   k 최근접 이웃(kNN, k-Nearest Neighbor) 알고리즘
    -   분류 또는 회귀에 사용되는 지도 학습 알고리즘의 하나
-   kNN 알고리즘을 분류에 사용할 경우
    -   특징 공간에서 테스트 데이터와 가장 가까운 k개의 훈련 데이터를 찾음
    -   k개의 훈련 데이터 중에서 가장 많은 클래스를 테스트 데이터의 클래스로 지정
    -   kNN 알고리즘을 회귀 문제에 적용할 경우
        -   테스트 데이터에 인접한 k개의 훈련 데이터 평균을 테스트 데이터 값으로 설정함

## kNN 알고리즘에 의한 점 분류

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a5d0aee9-ab18-4ca5-a0f9-a415ea648ae4/image.png)

-   새로 들어온 점과 가장 가까이 있는 훈련 데이터 점을 찾아, 해당 훈련 데이터 클래스와 같게 설정
    -   녹색 점과 가장 가까운 점은 빨간색 삼각형 → 녹색 점을 빨간색 삼각형 클래스로 지정
        -   최근접 이웃(NN)
-   녹색 점에서 가장 가까운 도형은 빨간색 삼각형이지만, 이 지점은 파란색 사각형이 더 많이 분포하는 지역이라고 판단
    -   녹색 점을 파란색 사각형 클래스로 지정하는 것이 더욱 합리적
        -   kNN 알고리즘

## k 최근접 이웃 알고리즘

-   kNN 알고리즘
    -   k를 1로 설정하면 최근접 이웃 알고리즘
    -   보통 k는 1보다 큰 값으로 설정
    -   k값을 어떻게 설정하느냐에 따라 분류 및 회귀 결과가 달라질 수 있음
    -   최선의 k 값을 결정하는 것은 주어진 데이터에 의존적임
        -   보통 k 값이 커질수록 잡음 또는 이상치 데이터의 영향이 감소함
        -   k 값이 어느 정도 이상으로 커질 경우 오히려 분류 및 회귀 성능이 떨어질 수 있음

## KNearest 클래스 사용하기

-   OpenCV에서 k 최근접 이웃 알고리즘은 KNearest 클래스에 구현되어 있음
-   KNearest 클래스
    -   ml 모듈에 포함되어 있음
    -   cv::ml 네임스페이스에 정의되어 있음
    -   KNearest 클래스를 이용하려면 먼저 KNearest 객체를 생성해야 함
-   KNearest::create() 정적 멤버 함수
    -   KNearest 객체 생성
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/756de7ef-52b2-4ba0-8a19-1277d04aed21/image.png)
-   KNearest는 기본적으로 k 값을 10으로 설정
    -   이 값을 변경하려면 KNearest::setDefaultK() 함수를 이용
    -   StatModel::predict() 함수 대신 KNearest::findNearest() 멤버 함수를 이용하여 테스트 데이터의 응답을 구할 경우 - k 값을 KNearest::findNearest() 함수 인자로 명시적으로 지정할 수 있음
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c321e628-4f3f-46d2-ad17-d9d734bf2738/image.png)
-   KNearest 객체는 기본적으로 분류를 위한 용도로 생성
    -   KNearest 객체를 분류가 아닌 회귀에 적용하려면
        -   KNearest::setIsClassifier() 멤버 함수에 false를 지정하여 호출
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/08b7e1c9-d3c8-4984-977a-71bfe6d08614/image.png)
-   KNearest 객체를 생성하고 속성을 설정한 후에는
    -   StatModel::train() 함수를 이용하여 학습을 진행
    -   KNearest 클래스의 경우에는 train() 함수에서 실제적인 학습이 진행되지는 않음
    -   단순히 훈련 데이터와 레이블 데이터를 KNearest 클래스 멤버 변수에 모두 저장하는 작업이 이루어짐
-   테스트 데이터에 대한 예측을 수행할 때에는 주로
    -   KNearest::findNearest() 멤버 함수를 사용
    -   KNearest 클래스에서도 StatModel::predict() 함수를 사용할 수 있음
    -   KNearest::findNearest() 함수가 예측 결과와 관련된 정보를 더 많이 반환하기 때문에 유용
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1da57199-90d3-4817-bb51-24c4f0f6bf6e/image.png)
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b7071884-f302-4167-bf61-e807276f4fda/image.png)

```python
train = []
label = []
k_value = 1

def on_k_changed(pos):
    global k_value

    k_value = pos
    if k_value < 1:
        k_value = 1

    trainAndDisplay()

def addPoint(x, y, c):
    train.append([x, y])
    label.append([c])

def trainAndDisplay():
    train_array = np.array(train).astype(np.float32)
    label_array = np.array(label)
    knn.train(train_array, cv2.ml.ROW_SAMPLE, label_array)

    for j in range(img.shape[0]):
        for i in range(img.shape[1]):
            sample = np.array([[i, j]]).astype(np.float32)

            ret, res, _, _ =
	            knn.findNearest(sample, k_value)

            response = int(res[0, 0])
            if response == 0:
                img[j, i] = (128, 128, 255)
            elif response == 1:
                img[j, i] = (128, 255, 128)
            elif response == 2:
                img[j, i] = (255, 128, 128)

    for i in range(len(train)):
        x, y = train[i]
        l = label[i][0]

        if l == 0:
            cv2.circle(img, (x, y), 5, (0, 0, 128),
	            -1, cv2.LINE_AA)
        elif l == 1:
            cv2.circle(img, (x, y), 5, (0, 128, 0),
	            -1, cv2.LINE_AA)
        elif l == 2:
            cv2.circle(img, (x, y), 5, (128, 0, 0),
	            -1, cv2.LINE_AA)

    cv2.imshow('knn', img)

img = np.zeros((500, 500, 3), np.uint8)
knn = cv2.ml.KNearest_create()

cv2.namedWindow('knn')
cv2.createTrackbar('k_value', 'knn', k_value, 5,
	on_k_changed)

NUM = 30
rn = np.zeros((NUM, 2), np.int32)

cv2.randn(rn, 0, 50)
for i in range(NUM):
    addPoint(rn[i, 0] + 150, rn[i, 1] + 150, 0)

cv2.randn(rn, 0, 50)
for i in range(NUM):
    addPoint(rn[i, 0] + 350, rn[i, 1] + 150, 1)

cv2.randn(rn, 0, 70)
for i in range(NUM):
    addPoint(rn[i, 0] + 250, rn[i, 1] + 400, 2)

trainAndDisplay()

cv2.imshow('knn', img)
cv2.waitKey()
cv2.destroyAllWindows()
```

## kNN 알고리즘을 이용한 2차원 점 분류

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b28e236b-664c-41c0-9ac3-2848b98738d6/image.png)

-   2차원 평면에서 세 개의 클래스로 구성된 점들을 kNN 알고리즘으로 분류
    -   (150, 150), (350, 150), (250, 400) 좌표를 중심으로 하는 가우시안 분포의 점을 각각 30개씩 생성하여 kNN 알고리즘 훈련 데이터로 사용
    -   (0, 0) 좌표부터 (499, 499) 좌표 사이의 모든 점에 대해 kNN 분류를 수행하여 그 결과를 빨간색, 녹색, 파란색 색상으로 나타냄
-   a : k 값이 1인 경우
    -   붉은색 영역에 가깝게 위치한 녹색 점과 녹색 영역에 가깝게 위치한 파란 점 때문에 클래스 경계면이 유난히 볼록하게 튀어나온 부분이 발생
-   b, c : k 값이 3 또는 5인 경우
    -   클래스 경계면이 다소 완만한 형태로 바뀜
    -   k 값이 증가함에 따라 잡음 또는 이상치에 해당하는 훈련 데이터 영향이 줄어드는 것

## kNN을 이용한 필기체 숫자 인식

-   머신 러닝으로 특정 문제를 해결하려면
    -   많은 양의 훈련 데이터가 필요
-   머신 러닝으로 필기체 숫자 인식을 수행하려면 충분히 많은 필기체 숫자 영상을 훈련 데이터로 사용해야 함
-   OpenCV는 5000개의 필기체 숫자가 적혀 있는 영상 파일을 제공
    -   필기체 숫자 영상(digits.png)
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9609e147-72f6-4cde-972f-7d5b2b6ee967/image.png)
    -   0부터 9까지의 숫자가 각각 가로로 100개, 세로로 5개씩 적혀 있음
    -   각각의 숫자는 20x20 픽셀 크기로 적혀 있음
    -   digits.png 숫자 영상의 전체 크기는 2000x1000
    -   머신 러닝 알고리즘을 학습시키려면 각각의 숫자 영상을 부분 영상으로 추출하여 훈련 데이터를 생성해야 함
-   보통 머신 러닝으로 영상을 인식 또는 분류할 경우
    -   영상으로부터 인식 목적에 적합한 특징 벡터를 추출하여 머신 러닝 입력으로 사용
-   이 예제에서는 단순히 20x20 숫자 영상 픽셀 값 자체를 kNN 알고리즘 입력으로 사용
    -   digits.png 숫자 영상에 적혀 있는 필기체 숫자들이 대체로 20x20 부분 영상 정중앙에 위치해 있음
    -   숫자 크기도 거의 일정
-   5000개의 숫자 영상 데이터를 훈련 데이터와 테스트 데이터로 구분하지 않고, 5000개 전체를 학습에 사용
-   숫자 영상 픽셀 값 자체를 이용하여 KNearest 훈련 데이터 행렬을 만드는 과정
    -   한 장의 숫자 영상은 20x20 픽셀 크기
    -   픽셀 값을 모두 일렬로 늘어놓으면 1x400 크기의 행렬
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a136ef3d-d60b-4a9d-83df-d5a17b2fbc3d/image.png)
    -   필기체 숫자 훈련 데이터 하나는 400개의 숫자 값으로 표현
        -   400차원 공간에서의 한 점
    -   영상에 있는 각각의 숫자 영상을 1x400 행렬로 변환
        -   이 행렬을 모두 세로로 쌓으면 전체 숫자 영상 데이터를 표현하는 5000x400 크기의 행렬
            -   이 행렬을 KNearest 클래스의 훈련 데이터로 전달함
-   kNN 알고리즘으로 필기체 숫자 영상을 학습시키려면
    -   각 필기체 숫자 영상이 나타내는 숫자 값을 레이블 행렬로 함께 전달해야 함
        -   이 레이블 행렬의 행 크기는 훈련 데이터 영상 개수와 같고, 열 크기는 1
        -   훈련 데이터 행렬에서 처음 500개 행은 숫자 0에 대한 데이터, 다음 500개 행은 숫자 1에 대한 데이터
        -   레이블 행렬도 처음 500개 행 원소는 0으로 설정, 그 다음 500개 행은 1로 설정
        -   이와 같은 방식으로 5000x1 행렬 원소를 모두 설정한 후, KNearest 클래스의 레이블 데이터로 전달

```python
oldx, oldy = -1, -1

def on_mouse(event, x, y, flags, _):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        oldx, oldy = -1, -1

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y),
	            (255, 255, 255), 40, cv2.LINE_AA)
            oldx, oldy = x, y
            cv2.imshow('img', img)

digits = cv2.imread('digits.png', cv2.IMREAD_GRAYSCALE)

if digits is None:
    print('Image load failed!')
    sys.exit()

h, w = digits.shape[:2]

cells = [np.hsplit(row, w//20)
	for row in np.vsplit(digits, h//20)]
cells = np.array(cells)
train_images = cells.reshape(-1, 400).astype(np.float32)
train_labels = np.repeat(np.arange(10),
	len(train_images)/10)

knn = cv2.ml.KNearest_create()
knn.train(train_images, cv2.ml.ROW_SAMPLE, train_labels)

img = np.zeros((400, 400), np.uint8)

cv2.imshow('img', img)
cv2.setMouseCallback('img', on_mouse)

while True:
    c = cv2.waitKey()

    if c == 27:
        break
    elif c == ord(' '):
        img_resize = cv2.resize(img, (20, 20),
	        interpolation=cv2.INTER_AREA)
        img_flatten = img_resize.reshape(-1, 400)
	        .astype(np.float32)

        _ret, res, _, _ = knn.findNearest(img_flatten, 3)
        print(int(res[0, 0]))

        img.fill(0)
        cv2.imshow('img', img)

cv2.destroyAllWindows()
```

-   on_mouse() 함수
    -   마우스 왼쪽 버튼을 누른 상태에서 마우스를 움직이면 해당 위치에 두께 40픽셀로 흰색 글씨를 쓸 수 있음
-   키보드 입력을 확인하여 사용자가 Space 키를 누를 때마다 사용자가 그린 글씨를 인식하여 콘솔 창에 출력
    -   사용자가 필기체 숫자를 img 창 중앙에 적당한 크기로 입력
        -   대체로 정확하게 숫자를 인식
    -   글씨 크기를 너무 크거나 작게 입력, 또는 중앙이 아닌 위치에 글씨를 입력
        -   인식 결과가 잘못될 수 있음

# 서포트 벡터 머신

## 서포트 벡터 머신(SVM)

-   기본적으로 두 개의 클래스로 구성된 데이터를 가장 여유 있게 분리하는 초평면(hyperplane)을 찾는 머신 러닝 알고리즘
-   초평면
    -   두 클래스의 데이터를 분리하는 N차원 공간 상의 평면
    -   2차원 공간 상의 점들을 분리하는 초평면 → 단순한 직선 형태로 정의
    -   3차원 공간 상의 점들을 분리하는 초평면 → 3차원 공간에서의 평면의 방정식으로 표현
-   SVM 알고리즘
    -   지도 학습의 일종
    -   분류와 회귀에 사용될 수 있음

## SVM 알고리즘으로 두 클래스의 점 분할

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/440a879e-7afe-49cd-825e-a8003ab40a67/image.png)

-   파란색 사각형과 빨간색 삼각형으로 표시된 두 클래스 점들의 분포
    -   두 클래스 점들을 구분하기 위한 직선은 매우 다양한 형태
    -   1번과 2번 직선은 모두 두 종류의 점들을 잘 분리함
    -   1번 직선은 조금만 왼쪽 또는 오른쪽으로 이동하면 분리에 실패할 수 있음
    -   2번 직선은 오른쪽으로 조금만 이동하면 분리에 실패
        -   1번과 2번 직선이 모두 입력 점 데이터에 너무 가까이 위치하고 있기 때문
    -   3번 직선은 두 클래스 점들 사이를 충분히 여유 있게 분할하고 있음
        -   3번 직선에 해당하는 초평면과 가장 가까이 있는 빨간색 또는 파란색 점과의 거리를 마진(margin)이라고 함
    -   SVM은 마진을 최대로 만드는 초평면을 구하는 알고리즘

## 서포트 벡터 머신 (SVM)

-   SVM 알고리즘은 기본적으로 선형으로 분리 가능한 데이터에 적용할 수 있음
-   실생활에서 사용하는 데이터는 선형으로 분리되지 않는 경우가 많음
    -   이러한 경우에도 SVM 알고리즘을 적용하기 위하여 SVM에서는 커널 트릭(kernel trick)이라는 기법을 사용
        -   적절한 커널 함수를 이용하여 입력 데이터 특징 공간 차원을 늘리는 방식
        -   원본 데이터 차원에서는 선형으로 분리할 수 없었던 데이터를 커널 트릭으로 고차원 특징 공간으로 이동 → 선형으로 분리 가능한 형태로 바뀔 수 있음

## 비선형 데이터에 커널 트릭 적용하기

-   데이터 특징 공간 차원을 증가시켜서 데이터를 선형 분리
-   2차원 좌표 평면 상의 점 집합 X = {(0, 0), (1, 1)} 와 Y = {(1, 0), (0, 1)}
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/191edb0e-28a6-48d5-9e76-312ceaa75e75/image.png)
    -   2차원 평면 상에서 X와 Y 두 클래스 점들을 분리할 수 있는 직선은 존재하지 않음
    -   입력 점들의 좌표에 가상의 z축 좌표를 zi = |xi - yi| 형태로 추가할 경우
        -   X = {(0, 0, 0), (1, 1, 0)} 와 Y = {(1, 0, 1), (0, 1, 1)} 형태로 3차원 공간 상에서의 점 집합으로 바뀜
    -   두 클래스 점들은 z = 0.5 평면의 방정식을 이용하여 효과적으로 분리할 수 있음
    -   2차원 평면에서 선형 분리할 수 없었던 X와 Y 데이터 집합 → 가상의 차원이 추가됨으로써 선형으로 분리할 수 있게 됨

## 다양한 SVM 커널

-   가장 널리 사용하는 커널
    -   방사 기저 함수
        -   𝛾 인자 값을 적절하게 설정해야 함
-   만약 입력 데이터가 선형으로 분리가 가능 → 선형 커널을 사용하는 것이 가장 빠르게 동작

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/cbebf011-c09f-4667-854f-af070baf6463/image.png)

## SVM 클래스 사용하기

-   OpenCV에서 SVM 알고리즘 → SVM 클래스에 구현되어 있음
-   SVM 클래스
    -   ml 모듈에 포함됨
    -   cv::ml 네임스페이스에 정의되어 있음
    -   유명한 오픈 소스 라이브러리인 LIBSVM을 기반으로 만들어짐
-   SVM 클래스를 이용하려면 먼저 SVM 객체를 생성해야 함
-   SVM 객체는 SVM::create() 정적 멤버 함수를 사용하여 생성
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7064b1d9-cd49-4e00-8428-16f032043553/image.png)
-   SVM 클래스 객체를 생성한 후
    -   훈련 데이터를 학습하기 전에 먼저 SVM 알고리즘 속성을 설정해야 함
    -   대표적으로 설정해야 할 SVM 클래스 속성 → 타입, 커널 함수 선택
-   SVM 타입을 설정
    -   SVM::setType() 함수 원형
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4d636b2b-6a8c-428c-aae3-cb9bd0d2a0fb/image.png)
    -   SVM 클래스는 기본적으로 SVM::Types::C_SVC 타입을 사용하도록 초기화됨
        -   SVM::Types::C_SVC 타입
            -   일반적인 N-클래스 분류 문제에서 사용되는 방식
    -   SVM::Types::C_SVC가 아닌 다른 타입을 사용 → SVM::setType() 함수를 이용하여 타입을 변경해야 함
    -   SVM::setType() 함수의 val 인자 → SVM::Types 열거형 상수 중 하나를 지정할 수 있음
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a48edf71-61d2-407f-9ae5-86d3bdd08437/image.png)
    -   SVM::Types::C_SVC 타입을 사용하는 경우
        -   SVM 알고리즘 내부에서 사용하는 C 파라미터 값을 적절하게 설정해야 함
            -   C 값을 작게 설정 → 훈련 데이터 중에 잘못 분류되는 데이터가 있어도 최대 마진을 선택
            -   C 값을 크게 설정 → 마진이 작아지더라도 잘못 분류되는 데이터가 적어지도록 분류
            -   만약 훈련 샘플 데이터에 잡음 또는 이상치 데이터가 많이 포함되어 있는 경우
                -   C 파라미터 값을 조금 크게 설정하는 것이 유리함
-   SVM 타입을 설정하였다면
    -   SVM 알고리즘에서 사용할 커널 함수를 지정해야 함
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1c4a78cc-a8d2-4bf1-bd04-83139e403ae8/image.png)
    -   SVM 클래스는 기본적으로 SVM::KernelTypes::RBF 커널을 사용하도록 초기화됨
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1b2d09ae-2e26-450b-b0d3-ef2c0be15881/image.png)
-   SVM 알고리즘 타입과 커널 함수 종류를 설정한 후
    -   각각의 타입과 커널 함수 정의에 필요한 파라미터를 설정해야 함
-   SVM 클래스에서 설정할 수 있는 파라미터
    -   C, Nu, P, Degree, Gamma, Coef() 등이 있음
        -   이들 파라미터는 차례대로 1, 0, 0, 0, 1, 0으로 초기화됨
        -   파라미터 이름에 해당하는 setXXX()와 getXXX() 함수를 이용하여 값을 설정하거나 읽어올 수 있음
        -   SVM::Types::C_SVC 타입을 사용하고 SVM::KernelTypes::RBF 커널을 사용할 경우
            -   SVM::setC() 함수와 SVM::setGamma() 함수를 사용하여 적절한 C와 Gamma 파라미터 값을 설정해야 함
-   SVM 객체를 생성하고 타입과 커널 함수 선택, 그리고 파라미터를 설정함
-   StatModel::train() 함수를 이용하여 학습시킬 수 있음
-   SVM에서 사용하는 파라미터를 적절하게 설정하지 않으면 학습이 제대로 되지 않는 경우가 발생
-   대부분의 훈련 데이터는 다차원간에서 다양한 분포와 형태를 가짐 → SVM 파라미터 값을 어떻게 설정해야 학습이 잘 될 것인지를 직관적으로 알기 어려움
-   OpenCV의 SVM 클래스는 각각의 파라미터에 대해 설정 가능한 값을 적용해 봄
    -   그 중 가장 성능이 좋은 파라미터를 자동으로 찾아 학습하는 SVM::trainAuto() 함수를 제공
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/f47f29e8-617d-4750-97b6-3540f25477f7/image.png)
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0d75ecd5-05d4-4365-8084-46d8981076e0/image.png)

```python
train = np.array([[150, 200], [200, 250],
                  [100, 250], [150, 300],
                  [350, 100], [400, 200],
                  [400, 300], [350, 400]])
	                  .astype(np.float32)

label = np.array([0, 0, 0, 0, 1, 1, 1, 1])

svm = cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_RBF)
# svm.setKernel(cv2.ml.SVM_LINEAR)
svm.trainAuto(train, cv2.ml.ROW_SAMPLE, label)

img = np.zeros((500, 500, 3), np.uint8)

for j in range(img.shape[0]):
    for i in range(img.shape[1]):
        test = np.array([[i, j]], dtype=np.float32)
        _, res = svm.predict(test)

        if res == 0:
            img[j, i] = (128, 128, 255)
        elif res == 1:
            img[j, i] = (128, 255, 128)

color = [(0, 0, 128), (0, 128, 0)]

for i in range(train.shape[0]):
    x = train[i, 0]
    y = train[i, 1]
    l = label[i]

    cv2.circle(img, (x, y), 5, color[l], -1, cv2.LINE_AA)

cv2.imshow('svm', img)
cv2.waitKey()
cv2.destroyAllWindows()
```

-   2차원 평면에서 두 개의 클래스로 구성된 점들을 SVM 알고리즘으로 분류
    -   두 점들을 효과적으로 분리하는 초평면을 구하여 화면에 나타냄
-   SVM 타입은 C_SVC로 설정
-   커널 함수는 방사 기저 함수를 사용
-   SVM 학습을 위한 입력으로는 train 행렬과 label 행렬을 지정
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4588e8b7-a00e-42da-85e3-67425009c9cc/image.png)
-   빨간색 원으로 표시된 점
    -   0번 클래스
-   녹색 원으로 표시된 점
    -   1번 클래스
-   img 영상 전체 픽셀 좌표를 학습된 SVM 분류기의 테스트 데이터로 사용하여 그 결과를 빨간색 또는 녹색으로 나타냄
-   방사 기저 함수를 SVM 커널로 사용 → 두 클래스 경계면이 곡선의 형태로 나타남
-   커널 함수를 SVM::KernelTypes::LINEAR로 변경할 경우
    -   두 점들을 세로로 양분하는 형태의 경계면이 만들어짐

## SVM 알고리즘을 이용한 2차원 점 분류

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/15e81a87-6b68-4922-aaff-7bda253b164d/image.png)

## HOG & SVM 필기체 숫자 인식

-   HOG
    -   입력 영상을 일정 크기의 셀(cell)로 나누고, 2x2 셀을 합쳐 하나의 블록(block)으로 설정
    -   필기체 숫자 영상 하나의 크기는 20x20
        -   셀 하나의 크기를 5x5로 지정
        -   블록 하나의 크기는 10x10 크기로 설정
    -   셀 하나에서 그래디언트 방향 히스토그램은 아홉 개의 빈으로 구성
    -   블록 하나에서는 9 x 4 = 36개의 빈으로 구성된 히스토그램 정보가 추출됨
    -   블록은 보통 하나의 셀 단위로 이동 → 가로로 세 개, 세로로 세 개 만들 수 있음
    -   필기체 숫자 영상 하나에서 만들어지는 HOG 특징 벡터의 차원 크기 → 36 x 9 = 324로 결정
    -   20x20 숫자 영상 하나에서 1x324 특징 벡터 행렬이 만들어짐
        -   이 행렬을 모두 세로로 쌓으면 5000x324 크기의 HOG 특징 벡터 행렬을 만들 수 있음
        -   이 행렬을 SVM 클래스의 훈련 데이터로 전달

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e64c2986-d351-42ce-af2a-5dd6c62fbd67/image.png)

-   필기체 숫자 영상에서 HOG 특징 벡터를 추출하려면
    -   HOGDescriptor 클래스를 사용
        -   임의의 영상에서 HOG 기술자를 추출하는 기능도 제공
        -   HOG 기술자를 추출하려면 HOGDescriptor 객체를 먼저 생성해야 함
        -   이때 HOGDescriptor 클래스 기본 생성자를 사용
-   20x20 영상에서 5x5 셀과 10x10 블록을 사용하는 HOG 기술자를 생성하려면 다음의 생성자를 사용
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1149ee4a-0343-419f-b6d4-80be873eb633/image.png)
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/96e43644-7e39-4dd4-bec5-0e23d8a8df1c/image.png)
    -   뒷부분의 많은 인자는 기본값이 설정되어 있음
    -   \_winSize, \_blockSize, \_blockStride, \_cellSize, \_nbins 인자만 적절하게 지정하여 사용
    -   20x20 영상에서 5x5 셀과 10x10 크기의 블록을 사용함
    -   각 셀마다 아홉 개의 그래디언트 방향 히스토그램을 구하도록 설정하려면 다음과 같이 HOGDescriptor 객체를 생성
        ```cpp
        HOGDescriptor hog(Size(20, 20), Size(10, 10),
        	Size(5, 5), Size(5, 5), 9);
        ```
-   HOGDescriptor 객체를 생성한 후에는
    -   HOGDescriptor::compute() 멤버 함수를 이용하여 HOG 기술자를 계산
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e3402e67-d426-421a-9472-1ce08effde7a/image.png)

```python
oldx, oldy = -1, -1

def on_mouse(event, x, y, flags, _):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        oldx, oldy = -1, -1

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y),
	            (255, 255, 255), 40, cv2.LINE_AA)
            oldx, oldy = x, y
            cv2.imshow('img', img)

digits = cv2.imread('digits.png', cv2.IMREAD_GRAYSCALE)

if digits is None:
    print('Image load failed!')
    sys.exit()

h, w = digits.shape[:2]
hog = cv2.HOGDescriptor((20, 20), (10, 10), (5, 5), (5, 5), 9)

cells = [np.hsplit(row, w//20)
	for row in np.vsplit(digits, h//20)]
cells = np.array(cells)
cells = cells.reshape(-1, 20, 20)

desc = []
for img in cells:
    dd = hog.compute(img)
    desc.append(dd)

train_desc = np.array(desc).squeeze().astype(np.float32)
train_labels = np.repaet(np.arange(10), len(train_desc)/10)

svm = cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_RBF)
svm.setC(2.5)
svm.setGamma(0.50625)
svm.train(train_desc, cv2.ml.ROW_SAMPLE, train_labels)

img = np.zeros((400, 400), np.uint8)

cv2.imshow('img', img)
cv2.setMouseCallback('img', on_mouse)

while True:
    c = cv2.waitKey()

    if c == 27:
        break
    elif c == ord(' '):
        img_resize = cv2.resize(img, (20, 20),
	        interpolation=cv2.INTER_AREA)

        desc = hog.compute(img_resize)
        test_desc = np.array(desc).astype(np.float32)

        _, res = svm.predict(test_desc.T)
        print(int(res[0, 0]))

        img.fill(0)
        cv2.imshow('img', img)

cv2.destroyAllWindows()
```

-   C와 Gamma 파라미터 값
    -   SVM::trainAuto() 함수를 이용하여 구한 값
        -   svm→train() 함수 대신 svm→trainAuto() 함수를 호출하면 상당히 오랜 시간 동안 학습이 진행됨
        -   최적의 파라미터를 알아낸 후에는 svm→train() 함수를 사용하는 것이 효율적

## 프로그램에서 인식에 성공한 영상의 예

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/db8a8753-0589-4ba5-a451-b290d8357e2d/image.png)

## 정상적으로 인식되지 않은 필기체 숫자의 예

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/bd8ec6a3-c545-4fe5-b01c-648d05d54170/image.png)

-   숫자를 중앙이 아닌 한편으로 치우치게 적거나, 다른 숫자와 비슷한 형태로 쓴 경우 → 잘못 인식하는 경우가 많이 발생

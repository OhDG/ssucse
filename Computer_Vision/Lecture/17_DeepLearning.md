# 딥러닝과 OpenCV DNN모듈

## 신경망과 딥러닝

-   딥러닝(deep learning)
    -   2000년대부터 사용되고 있는 심층 신경망(deep neural network)의 또 다른 이름
-   신경망(neural network)
    -   인공 신경망(artificial neural network)이라고도 불림
    -   사람의 뇌 신경 세포(neuron)에서 일어나는 반응을 모델링하여 만들어진 고전적인 머신 러닝 알고리즘
-   딥러닝
    -   신경망을 여러 계층(layer)으로 쌓아서 만든 머신 러닝 알고리즘 일종
-   컴퓨터 비전 분야에서 딥러닝 기술이 크게 주목받고 있는 이유
    -   객체 인식, 얼굴 인식, 객체 검출, 분할 등의 다양한 영역에서 딥러닝이 적용된 기술이 기존의 컴퓨터 비전 기반 기술보다 월등한 성능을 보여주고 있기 때문

## 머신 러닝 vs 딥러닝

-   기존의 머신 러닝 학습
    -   영상으로부터 인식에 적합한 특징을 사람이 추출하여 머신 러닝 알고리즘 입력으로 전달
    -   머신 러닝 알고리즘이 특징 벡터 공간에서 여러 클래스 영상을 상호 구분하기에 적합한 규칙을 찾아냄
    -   사람이 영상에서 추출한 특징이 영상 인식에 적합하지 않다면
        -   어떤 머신 러닝 알고리즘을 사용하더라도 좋은 인식 성능을 나타내기 어려움
-   최근의 딥러닝
    -   특징 추출과 학습을 모두 딥러닝이 알아서 수행
    -   여러 영상을 분류하기 위해 적합한 특징을 찾는 것 + 이 특징을 잘 구분하는 규칙까지 찾는 것

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/303d59c5-53d6-42d1-bc89-aca2c47c0da6/image.png)

## 신경망과 딥러닝

-   퍼셉트론(perceptron) 구조
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/68202625-4542-404a-a8ed-e3ca0355fc1b/image.png)
    -   1950년대에 개발된 신경망의 가장 기초적인 형태
    -   기본적으로 다수의 입력으로부터 가중합을 계산하여 하나의 출력을 만들어 내는 구조
    -   원으로 표현한 것이 노드(node) 또는 정점(vertex)
    -   노드 사이에 연결된 선을 에지(edge) 또는 간선
    -   x1, x2는 입력 노드
    -   y는 출력 노드
    -   입력 노드로 이루어진 계층 : 입력층(input layer)
    -   출력 노드로 이루어진 계층 : 출력층(output layer)
    -   각각의 에지는 가중치(weight)를 가짐
    -   퍼셉트론의 출력 y
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7555e37c-b2a2-44d2-9e91-dc9487ab7491/image.png) - b는 편향(bias) - y 값 결정에 영향을 줄 수 있는 파라미터
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/852523f7-a149-4e94-bc1b-732d1cf71bec/image.png)

## 퍼셉트론에 의한 점들의 분류

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/bf47824c-2fc8-42c9-8964-a2bdb1e18293/image.png)

-   2차원 평면 상에 두 개의 클래스로 나눠진 점들의 분포
-   빨간색 삼각형 점들과 파란색 사각형 점을 분류하기 위해 퍼셉트론을 사용할 경우
    -   가중치는 w1 = w2 = 1로 설정
    -   편향은 b = -0.5로 설정
    -   출력 y
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7f6e8f97-dc3c-413f-a5a5-02252fff9f3b/image.png)
        -   앞 수식에 빨간색 삼각형 점의 좌표를 입력하면 y는 1
        -   파란색 사각형 점의 좌표를 입력하면 y는 -1
        -   두 점들의 분포를 가르는 보라색 직선의 방정식
            -   x1 + x2 - 0.5 = 0

## 다층 퍼셉트론

-   퍼셉트론은 선형 분류기
    -   선형 분리 가능한 데이터만 높은 성능
    -   현실에서는 대부분 비선형(선형 분리 불가능) 데이터
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a233b440-45be-4ca6-a51d-e0e4fceb5cdd/image.png)
-   기본적인 퍼셉트론
    -   입력 데이터를 두 개의 클래스로 선형 분류하는 용도로 사용할 수 있음
-   좀 더 복작합 형태로 분포되어 있는 데이터 집합에 대해서는 노드의 개수를 늘림
-   입력과 출력 사이에 여러 개의 은닉층(hidden layer)을 추가하는 형태로 구조를 발전시켜 해결
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9d0e2702-5f80-4ecb-8d21-9919c0ae0b29/image.png)
-   XOR는 선형 분리 불가능한 데이터
-   다층 퍼셉트론으로 해결 가능
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/97ea3b9b-0aef-4eb7-b53f-b9892ac486de/image.png)
    -   특징 공간 (x1, x2)을 더 유리한 특징 공간 (z1, z2)으로 변환
    -   새로운 특징 공간은 선형 분리 가능 → 은닉 공간(hidden space) 또는 잠복 공간(latent space)이라고 부름
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8092da55-8651-49ea-9b39-2f27c5019821/image.png)
    -   변환된 공간에서 세 번째 퍼셉트론을 사용하여 분류 수행
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c9e441b1-75e8-4180-a5c7-5f252f5f7875/image.png)

## 다층 퍼셉트론의 구조

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8626e71f-12b1-48d4-9b05-52515d241c85/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8ee54f2e-fd84-4954-a08b-565d600b97b4/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/dc3e5b7d-1170-4113-b25f-ff5f0df23df1/image.png)

## 활성 함수

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1b70cb71-8480-4ab3-b4c5-32f3cdf54dc7/image.png)

## 신경망과 딥러닝

-   신경망이 주어진 문제를 제대로 해결하려면
    -   신경망 구조가 문제에 적합해야 함
-   에지에 적절한 가중치가 부여되어야 함
    -   에지의 가중치와 편향 값 → 경사 하강법(gradient descent), 오류 역전파(error backpropagation) 등의 알고리즘에 의해 자동으로 결정할 수 있음
-   신경망에서 학습이란
    -   훈련 데이터셋을 이용하여 적절한 에지 가중치와 편향 값을 구하는 과정
-   신경망은 2000년대 초반까지 크게 발전하지 못함
    -   은닉층이 많아질수록 학습 시간이 너무 오래 걸림
    -   학습도 제대로 되지 않는 문제가 해결되지 않았음
-   2000년대 후반, 2010년 초반부터
    -   신경망은 심층 신경망 또는 딥러닝으로 크게 발전하기 시작

## 깊은 다층 퍼셉트론

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9f16c4bd-43c1-427c-976a-b3c4d8f1cc0d/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/891a81a4-6212-4196-b50d-d76f2b8f03c8/image.png)

## 신경망 학습

-   처음에는 가중치에 대한 실마리가 없기 때문에 난수 설정하고 출발
-   손실 함수 값을 줄이는 방향으로 가중치 갱신을 반복
    -   충분히 높은 정확률을 달성하거나 더 이상 개선이 불가능하다고 여겨질 때 멈춤

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/24ccec92-ffb3-40b8-87e5-272739090523/image.png)

## 역전파(backpropagation)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/f996be16-0ee9-4979-b8fe-406f04e87b89/image.png)

## 신경망과 딥러닝

-   2000년대에 딥러닝이 크게 발전한 이유
    -   딥러닝 알고리즘이 개선 → 은닉층이 많아져도 학습이 제대로 이루어짐
    -   하드웨어의 발전, 특히 GPU(Graphics Processing Unit) 성능 향상과 GPU를 활용한 학습 방법으로 인해 딥러닝 학습 시간이 크게 단축됨
    -   인터넷의 발전에 따른 빅데이터 활용이 용이해짐
-   특히 컴퓨터 비전 분야에서는
    -   Pascal VOC, ImageNet과 같이 잘 다듬어진 영상 데이터를 활용할 수 있음
-   대용량 영상 데이터셋을 이용한 영상 인식 대회 등을 통해 알고리즘 경쟁과 공유가 활발하게 이루어졌음

## 일반적인 CNN 네트워크 구조

-   다양한 딥러닝 구조 중에서 특히 영상을 입력으로 사용하는 영상 인식, 객체 검출 등의 분야에서는
    -   합성곱 신경망(CNN, Convolutional Neural Network) 구조가 널리 사용되고 있음
-   CNN 구조
    -   보통 2차원 영상에서 특징을 추출하는 컨볼루션(convolution) 레이어와 추출된 특징을 분류하는 완전 연결(FC, Fully Connected) 레이어로 구성됨
-   CNN 구조에서 컨볼루션
    -   영상의 지역적인 특징을 추출하는 역할을 담당

## Convolution 연산

-   적합한 kernel을 data로부터 학습
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/f7a6ddb6-a079-40d6-be21-b74a045d4703/image.png)

## Image Classification: Feature Learning

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/05049ce3-44ae-4934-9860-fd16e8e8c3de/image.png)

## Image Classification: Deep Learning

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c1b419d7-57b1-4f07-9014-339c03ad1a03/image.png)

## Convolution 연산

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c06f9e9a-b044-4238-bc37-f24aa628a15c/image.png)

## Pooling 연산

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/924afd30-f11d-4e57-bd65-b71282339faa/image.png)

## 기존 다층 퍼셉트론과의 비교

-   영상을 입력하기 위해 1차원으로 펼칠 때 정보 손실
-   FC(완전 연결)층의 과다한 매개변수
    -   Ex) 256*256*3 영상을 입력하려면 196608개의 입력 노드 필요

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/877d7d49-7aee-4243-9a58-6517eed8c9ee/image.png)

## 일반적인 CNN 네트워크 구조

-   풀링(pooling)
    -   비선형 다운샘플링(down sampling)을 수행하여 데이터양을 줄이고 일부 특징을 강조하는 역할
-   완전 연결 레이어
    -   고전적인 다층 퍼셉트론과 비슷한 구조
    -   추출된 특징을 이용하여 출력 값을 결정
-   보통 컨볼루션 레이어를 여러 개 연결하고
    -   맨 뒤에 완전 연결 레이어를 연결하는 형태로 CNN 네트워크를 구성

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/197b9e81-a774-48ea-9dc7-8d284fec52ce/image.png)

## Convolution Layer

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c5cea605-52dc-4a94-8516-c982af30c608/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/11d39667-325f-4023-8438-43a3a8b8b6dc/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/cb5a91b4-e1a7-40ad-a66b-0ab4581cdd9e/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a962d2c0-63c2-40e3-bf04-e12f9728fa71/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ee3c9bda-666f-4019-9fa4-b98b9731f201/image.png)

## Convolutional Neural Networks (CNN)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/51a96ae5-4a9e-4cde-8109-9d38b7e25baf/image.png)

## 신경망과 딥러닝

-   컴퓨터 비전 분야에서 사용되는 딥러닝 알고리즘
    -   대부분 CNN 구조를 기본으로 사용하면서 인식의 정확도를 높이거나 연산 속도를 빠르게 하는 등의 목적에 맞게 변형된 형태
-   컨볼루션 단계에서 사용하는 커널을 1 x 1, 3 x 3, 5 x 5 등 다양한 크기로 구성하기도 함
    -   기존에는 사람이 직접 필터 설계 (Gaussian, Sobel, …)
    -   이들 필터는 인식에 가장 적합한지? 데이터셋에 맞는 필터는 어떤 것인지?
        -   최적의 필터를 학습으로 알아냄
-   레이어 사이의 연결 방식
    -   새롭게 설계하여 효과적인 성능을 얻기도 함

## OpenCV DNN 모듈

-   OpenCV dnn 모듈
    -   이미 만들어진 네트워크에서 순방향 실행을 위한 용도로 설계됨
    -   딥러닝 학습은 기존의 유명한 카페(Caffe), 텐서플로(TensorFlow) 등의 다른 딥러닝 프레임워크에서 진행함
    -   학습된 모델을 불러와서 실행할 때에는 dnn 모듈을 사용하는 방식
    -   C/C++ 환경에서도 동작할 수 있음 → 프로그램 이식성이 높음
    -   카페, 텐서플로, 토치 등의 프레임워크에서 학습된 모델과 ONNX(Open Neural Network Exchange) 파일 형식으로 저장된 모델을 불러와 실행할 수 있음
    -   이미 널리 사용되고 있는 딥러닝 네트워크 구성을 지원
-   dnn 모듈에서 딥러닝 네트워크
    -   cv::dnn::Net 클래스를 이용하여 표현
    -   Net 클래스
        -   dnn 모듈에 포함됨
        -   cv::dnn 네임스페이스 안에 정의되어 있음
        -   여러 레이어로 구성된 네트워크 구조를 표현
        -   네트워크에서 특정 입력에 대한 순방향 실행을 지원함
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d843507d-1346-496b-9d43-1e99526233fb/image.png)
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/768c6aef-a646-40de-981f-7cd4e62f48da/image.png)
-   Net 클래스 객체는 보통 사용자가 직접 생성하지 않음
    -   readNet() 등의 함수를 이용하여 생성함
    -   readNet() 함수
        -   미리 학습된 딥러닝 모델과 네트워크 구성 파일을 이용하여 Net 객체를 생성함
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/905ef621-60ea-4ff1-beae-0ceec04769bb/image.png)
        -   만약 model 파일에 네트워크 훈련 가중치와 네트워크 구조가 함께 저장되어 있다면
            -   config 인자를 생략할 수 있음
        -   framework 인자
            -   모델 파일 생성 시 사용된 딥러닝 프레임워크 이름을 지정함
        -   만약 model 또는 config 파일 이름 확장자를 통해 프레임워크 구분이 가능한 경우
            -   framework 인자를 생략 가능
        -   model과 config 인자에 지정할 수 있는 파일 이름 확장자와 framework에 지정 가능한 프레임워크 이름
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6dbcb4a9-ec17-4bda-a93d-e65702420797/image.png)
        -   전달된 framework 문자열, 또는 model과 config 파일 이름 확장자를 분석하여 내부에서 해당 프레임워크에 맞는 readNetFromXXX() 형태의 함수를 다시 호출
        -   readNetFromTorch(), readNetFromDarknet(), readNetFromModelOptimizer(), readNetFromONNX() 함수가 OpenCV에서 제공되고 있음
        -   readNetFromXXX() 형태의 함수를 사용자가 직접 호출하여 사용할 수도 있지만
            -   OpenCV 4.0.0 버전부터는 readNet() 대표 함수를 사용하는 것이 좋음
-   readNet() 함수를 이용하여 Net 객체를 생성한 후에는
    -   Net::empty() 멤버 함수를 사용하여 Net 객체가 정상적으로 생성되었는지 확인 - 만약 Net::empty() 함수가 true를 반환하면 - 예외 처리 코드를 추가함
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2632338f-82bc-40f7-a9f5-0478ac6d0919/image.png)
-   Net 객체가 정상적으로 생성되었다면
    -   이제 생성된 네트워크에 새로운 데이터를 입력하여 그 결과를 확인할 수 있음
    -   이때 Net 객체로 표현되는 네트워크 입력으로
        -   Mat 타입의 2차원 영상을 그대로 입력하는 것이 아니라
        -   블롭(blob) 형식으로 변경해야 함

## 블롭(blob)

-   영상 등의 데이터를 포함하는 다차원 데이터 표현 방식
-   OpenCV에서 블롭
    -   Mat 타입의 4차원 행렬로 표현됨
    -   각 차원은 NCHW 정보를 표현
        -   N은 영상 개수, C는 채널 개수, H와 W는 각각 영상의 세로와 가로 크기를 의미
-   OpenCV에서는 blobFromImage() 함수를 이용하여
    -   Mat 영상으로부터 블롭을 생성
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/fe093a34-c464-4fc1-99dc-c2ac8be64e6d/image.png)
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6e8d39ee-7827-4ca1-b384-aa780754410c/image.png)

## OpenCV DNN 모듈

-   blobFromImage() 함수로 생성한 블롭 객체
    -   Net::setInput() 멤버 함수를 이용하여 네트워크 입력으로 설정
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/79015f6b-9701-4501-ad97-15eecbf87a54/image.png)
    -   Net::setInput() 함수 인자에도 blobFromImage() 함수에 있는 scalefactor와 mean 인자가 있음
        -   추가적인 픽셀 값을 조정할 수 있음
    -   결국 네트워크에 입력되는 블롭은 다음과 같은 형태로 설정
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7fce9bbf-40e9-49e6-81f8-a3ae66050b6e/image.png)
-   네트워크 입력을 설정한 후에는
    -   네트워크를 순방향으로 실행하여 결과를 예측할 수 있음
-   네트워크를 실행할 때에는
    -   Net::forward() 멤버 함수를 사용
    -   Net::forward() 함수 - 순방향으로 네트워크를 실행한다는 의미 - 이를 추론(inference)이라고도 함
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/73ddfc21-cfff-416c-a87b-675a0eaddb11/image.png)

# 딥러닝 학습과 OpenCV 실행

## 텐서플로로 필기체 숫자 인식 학습하기

-   필기체 숫자 영상 인식을 딥러닝을 통해 학습
    -   학습에 사용할 딥러닝 구조 → 간단한 형태의 CNN 네트워크
-   딥러닝 학습을 위한 프레임워크 → 텐서플로
-   많은 딥러닝 프레임워크가 파이썬(python) 언어를 주력으로 사용
-   딥러닝 분야에서는 필기체 숫자 인식 훈련을 위해 MNIST 데이터셋을 주로 사용
-   MNIST
    -   뉴욕 대학교 얀 르쿤(Yann LeCun) 교수가 우편번호 등의 필기체 숫자 인식을 위해 사용했던 데이터셋
    -   6만 개의 훈련용 영상과 1만 개의 테스트 영상으로 구성됨
    -   각각의 숫자 영상은 28 x 28 크기로 구성됨
    -   픽셀 값은 0부터 1 사이의 실수 값으로 정규화됨

## MNIST 숫자 영상의 예

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9d141a3d-7a0b-4f67-af3a-c49dcfb1ddd6/image.png)

## Batch size / Epoch / Iteration

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/df306c8f-df90-4192-af07-897a006b471d/image.png)

## 텐서플로로 필기체 숫자 인식 학습하기

```python
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.python.framework import graph_util
from tensorflow.python.platform import gfile

tf.logging.set_verbosity(tf.logging.ERROR)

mnist = input_data.read_data_sets("./MNIST_data/", one_hot=True)

#
# hyper parameters
#
learning_rate = 0.001
training_epochs = 20
batch_size = 100

#
# Model configuration
#
X = tf.placeholder(tf.float32, [None, 28, 28, 1], name='data')
Y = tf.placeholder(tf.float32, [None, 10])

conv1 = tf.layers.conv2d(X, 32, [3, 3], padding="same",
	activation=tf.nn.relu)
pool1 = tf.layers.max_pooling2d(conv1, [2, 2], strides=2,
	padding="same")

conv2 = tf.layers.conv2d(pool1, 64, [3, 3], padding="same",
	activation=tf.nn.relu)
pool2 = tf.layers.max_pooling2d(conv2, [2, 2], strides=2,
	padding="same")

flat3 = tf.contrib.layers.flatten(pool2)
dense3 = tf.layers.dense(flat3, 256, activation=tf.nn.relu)

logits = tf.layers.dense(dense3, 10, activation=None)
final_tensor = tf.nn.softmax(logits, name='prob')

cost = tf.reduce_mean(
	tf.nn.softmax_cross_entropy_with_logits_v2(labels=Y, logits=logits))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

#
# Training
#
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    total_batch = int(mnist.train.num_examples / batch_size)

    print('Start learning!')
    for epoch in range(training_epochs):
        total_cost = 0

        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            batch_xs = batch_xs.reshape(-1, 28, 28, 1)
            _, cost_val = sess.run([optimizer, cost],
	            feed_dict={X: batch_xs, Y: batch_ys})

            total_cost += cost_val

        print('Epoch:', '%04d' % (epoch + 1),
	        'Avg. cost = ', '{:.4f}'.format(total_cost/total_batch))

    print('Learning finished!')

    # Freeze variables and save pb file
    output_graph_def = graph_util.conver_variables_to_constants(sess,
	    sess.graph_def, ['prob'])
    with gfile.FastGFile('./mnist_cnn.pb', 'wb') as f:
        f.write(output_graph_def.SerializeToString())

    print('Save done!')
```

-   단순히 이 네트워크에서 입력 데이터로 MNIST 데이터셋을 사용 → 각각의 필기체 숫자가 28 x 28 크기 행렬로 구성됨
-   각 행렬 원소 값은 0에서 1 사이의 실수 값으로 정규화됨
-   출력은 열 개의 노드로 구성
    -   각 노드의 값은 0부터 9까지의 숫자 값에 대한 확률

## OpenCV에서 학습된 모델 불러와서 실행하기

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

net = cv2.dnn.readNet('mnist_cnn.pb')

if net.empty():
    print('Network load failed!')
    sys.exit()

img = np.zeros((400, 400), np.uint8)

cv2.imshow('img', img)
cv2.setMouseCallback('img', on_mouse)

while True:
    c = cv2.waitKey()

    if c == 27:
        break
    elif c == ord(' '):
        blob = cv2.dnn.blobFromImage(img, 1/255., (28, 28))
        net.setInput(blob)
        prob = net.forward()

        _, maxVal, _, maxLoc = cv2.minMaxLoc(prob)
        digit = maxLoc[0]

        print('%d (%f)' % (digit, maxVal * 100))

        img.fill(0)
        cv2.imshow('img', img)

cv2.destroyAllWindows()
```

-   28 x 28 크기로 축소
-   0과 1 사이로 정규화
-   inputBlob 생성
    -   1 x 1 x 28 x 28

# OpenCV와 딥러닝 활용

## 구글넷 영상 인식

-   딥러닝이 컴퓨터 비전 분야에서 크게 발전할 수 있있던 이유 중에는
    -   ILSVRC(ImageNet Large Scale Visual Recognition Competition) 대회의 영향도 있음
-   ILSVRC
    -   영상 인식과 객체 검출 등의 성능을 겨루는 일종의 알고리즘 경진 대회
    -   2010년부터 매년 개최됨
    -   ImageNet이라는 대규모 영상 데이터베이스를 이용
    -   영상 인식 분야에서는 1000개의 카테고리로 분류된 100만개 이상의 영상을 사용하여 성능을 비교
    -   이 대회에서 2012년에 알렉스넷(AlexNet)이라는 딥러닝 알고리즘이 기존보다 월등히 높은 성능을 나타냄
        -   컴퓨터 비전 분야에 딥러닝 열풍이 시작
-   구글넷(GoogLeNet)
    -   구글(Google)에서 발표한 네트워크 구조
    -   2014년 ILSVRC 영상 인식 분야에서 1위를 차지함
    -   총 22개의 레이어로 구성됨
        -   동시대에 발표되었던 딥러닝 네트워크 구조 중에서 가장 많은 레이어를 사용한 형태
    -   레이러를 매우 깊게 설계하였지만 완전 연결 레이어가 없는 구조 → 기존의 다른 네트워크보다 파라미터 수가 훨씬 적음
    -   다양한 크기의 커널을 한꺼번에 사용 → 영상에서 큰 특징과 작은 특징을 모두 추출할 수 있도록 설계됨

## 구글넷 네트워크 구조

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a830abc0-9e24-4593-bf39-ff70196a7bf9/image.png)

## 구글넷 영상 인식

-   OpenCV에서 구글넷 인식 기능을 사용하려면
    -   다른 딥러닝 프레임워크를 이용하여 미리 훈련된 모델 파일과 구성 파일이 필요함
-   카페는 미리 학습된 딥러닝 모델 파일을 받을 수 있는 모델 주(model zoo)를 운영하고 있음
-   구글넷 인식 기능을 제대로 구현하려면
    -   모델 파일과 구성 파일 외에 인식된 영상 클래스 이름이 적힌 텍스트 파일이 추가로 필요함
-   ILSVRC 대회에서 사용된 1000개의 영상 클래스 이름이 적혀 있는 텍스트 파일이 필요함
    -   이 파일은 OpenCV를 설치할 때 함께 제공됨
        -   classification_classes_LISVRC2012.txt
        -   1000개의 영상 클래스 이름이 한 줄 씩 적혀 있음

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8afc272e-6b7c-459c-8734-fe49681dfa18/image.png)

-   OpenCV에서 이 파일을 이용하여 영상을 인식

    -   먼저 readNet() 함수를 이용하여 Net 객체를 생성
        -   모델 파일 이름과 구성 파일 이름을 순서대로 전달
        ```python
        net = cv2.dnn.readNet('bvlc_googlenet.caffemodel',
        	'deploy.prototxt')
        ```
    -   각 클래스 이름이 적혀 있는 텍스트 파일로부터 각 클래스 이름을 불러와 classNames 변수에 저장
        ```python
        classNames = None
        with open('classification_classes_ILSVRC2012.txt', 'rt') as f:
            classNames = f.read().rstrip('\n').split('\n')
        ```
    -   네트워크에 영상 블롭을 전달하여 추론
        -   입력 영상은 imread() 함수를 이용하여 불러옴
        -   불러온 영상은 blobFromImage() 함수를 이용하여 블롭으로 변환
        -   카페에서 학습된 구글넷은 입력으로 224 x 224 크기의 BGR 컬러 영상을 사용
        -   각 영상에서 평균값 Scalar(104, 117, 123)을 빼서 학습시킴
        ```python
        inputBlob = cv2.dnn.blobFromImage(img, 1,
        	(224, 224), (104, 117, 123))
        net.setInput(inputBlob, 'data')
        prob = net.forward()
        ```
    -   결과 확인 및 출력 - argmax 함수를 사용하여 최대 확률의 classId 도출 - Class 명과 확률을 출력
        ```python
        net = cv2.dnn.readNet('bvlc_googlenet.caffemodel',
        'deploy.prototxt')

            classNames = None
            with open('classification_classes_ILSVRC2012.txt', 'rt') as f:
                classNames = f.read().rstrip('\n').split('\n')

            inputBlob = cv2.dnn.blobFromImage(img, 1,
            	(224, 224), (104, 117, 123))
            net.setInput(inputBlob, 'data')
            prob = net.forward()

            out = prob.flatten()
            classId = np.argmax(out)
            confidence = out[classId]

            str = '%s (%4.2f%%)' % (classNames[classId], confidence * 100)
            cv2.putText(img, str, (10, 30),
            	cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

            cv2.imshow('img', img)
            cv2.waitKey()
            cv2.destroyAllWindows()
            ```

        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2e1c572d-ec65-49ce-988a-0920757aa155/image.png)
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/83d45ef8-9da6-40ee-8de8-8763e7fb79b8/image.png)

## SSD 얼굴 검출

-   얼굴 검출을 위한 용도로 훈련된 딥러닝 학습 모델 준비
    -   res10_300x300_ssd_iter_140000_fp16.caffemodel
        -   Caffe 프레임워크에서 훈련된 파일
    -   opencv_face_detector_uint8.pb
        -   텐서플로에서 훈련된 파일
    -   두 학습 모델은 비슷한 성능으로 동작
    -   2016년에 발표된 SSD(Single Shot Detector) 알고리즘을 이용하여 학습된 파일
-   SSD
    -   입력 영상에서 특정 객체의 클래스와 위치, 크기 정보를 실시간으로 추출할 수 있는 객체 검출 딥러닝 알고리즘
    -   원래 다수의 클래스 객체를 검출할 수 있지만
        -   OpenCV에서 제공하는 얼굴 검출은 오직 얼굴 객체의 위치와 크기만 알아내도록 훈련된 학습 모델을 사용

## SSD 네트워크 구조

-   입력은 300 x 300 크기의 2차원 BGR 컬러 영상을 사용
    -   이 영상은 Scalar(104, 117, 123) 값을 이용하여 정규화한 후 사용함
-   네트워크의 출력
    -   추출된 객체의 ID, 신뢰도, 사각형 위치 등의 정보를 담고 있음

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/cbdaa100-31d0-4906-93af-20f3cb246ad1/image.png)

## SSD 얼굴 검출

-   딥러닝을 이용한 얼굴 검출

```python
model = 'res10_300x300_ssd_iter_140000_fp16.caffemodel'
config = 'deploy.prototxt'
#model = 'opencv_face_detector_uint8.pb'
#config = 'opencv_face_detector_pbtxt'

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed!')
    sys.exit()

net = cv2.dnn.readNet(model, config)

if net.empty():
    print('Net open failed!')
    sys.exit()

while True:
    _, frame = cap.read()
    if frame is None:
        break

    blob = cv2.dnn.blobFromImage(frame, 1, (300, 300),
	    (104, 117, 123))
    net.setInput(blob)
    detect = net.forward()

    (h, w) = frame.shape[:2]
    detect = detect[0, 0, :, :]

    for i in range(detect.shape[0]):
        confidence = detect[i, 2]
        if confidence < 0.5:
            break

        x1 = int(detect[i, 3] * w)
        y1 = int(detect[i, 4] * h)
        x2 = int(detect[i, 5] * w)
        y2 = int(detect[i, 6] * w)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0))

        label = 'Face: %4.3f' % confidence
        cv2.putText(frame, label, (x1, y1 - 1),
	        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
```

-   얼굴 영역을 정확하게 검출하여 녹색 사각형을 그림
    -   녹색 사각형 위에 얼굴 검출 신뢰도가 함께 출력
-   캐스케이드 분류기 기반의 얼굴 검출 방법
    -   정면 얼굴이 아니면 얼굴 검출에 실패하는 경우가 많음
-   SSD 딥러닝 기반의 얼굴 검출
    -   얼굴 일부가 가려지거나 얼굴 옆모습이 입력으로 들어가도 안정적으로 얼굴 영역을 검출
    -   얼굴 검출 속도도 캐스케이드 분류기 기반의 방법보다
        -   SSD 딥러닝 기반의 얼굴 검출이 더 빠르게 동작

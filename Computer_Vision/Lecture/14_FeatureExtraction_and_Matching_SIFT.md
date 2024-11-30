## 특징(feature)

-   영상으로부터 추출할 수 있는 유용한 정보
-   평균 밝기, 히스토그램, 에지, 직선 성분, 코너 등
-   지역 특징(local feature)
    -   영상의 특징 중에서 에지, 직선 성분, 코너처럼 영상 전체가 아닌 일부 영역에서 추출할 수 있는 특징
-   코너(corner)
    -   에지의 방향이 급격하게 변하는 부분
    -   삼각형의 꼭짓점이나 연필 심처럼 뾰족하게 튀어나와 있는 부분
    -   에지나 직선 성분 등의 다른 지역 특징에 비해 분별력이 높고 대체로 영상 전 영역에 골고루 분포
    -   영상을 분석하는 데 유용한 지역 특징으로 사용됨
-   특징점(feature point)
    -   코너처럼 한 점의 형태로 표현할 수 있는 특징
    -   키포인트(keypoint), 관심점(interest point)이라고 부름

## 대응점 문제

-   이웃한 영상에 나타난 같은 물체의 같은 곳을 쌍으로 매칭하는 문제
-   파노라마 영상 제작, 객체 추척, 스테레오 비전, 카메라 캘리브레이션 등에 필수적
-   에지 특징이나 영역 특징은 한계 존재

## 지역 특징점

-   연속된 영상 프레임에서 객체를 추적하는 경우
    -   두 영상에서 특징점(feature point) 추출 후
    -   두 영상의 특징점 매칭을 통해 대응하는 쌍을 찾아야 함
    -   1980년대에 에지 경계선에서 모퉁이(corner) 찾는 연구 진행 → 특징점이 물체의 실제 코너에 해당한다고 생각
-   좁은 지역을 보고 특징점 여부 결정
-   물체의 실제 코너에 특징점이 위치해야 한다는 생각을 버림
    -   반복성을 더 중요하게 고려
-   지역 특징의 표현
    -   (위치, 스케일, 방향, 특징 기술자)로 표현
        -   위치와 스케일은 검출 단계에서 도출
        -   방향과 특징 기술자는 기술 단계에서 도출

## 지역 특징의 조건

-   반복성 (repeatability)
    -   같은 물체가 서로 다른 두 영상에 나타났을 때
    -   특징점이 두 영상의 같은 위치에서 높은 확률로 검출
-   불변성 (invariance)
    -   물체의 이동, 회전, 스케일, 조명 변환에 대해서도 특징 기술자의 값이 비슷해야 함
-   분별력 (discriminative power)
    -   다른 곳에서 추출된 특지오가 두드러지게 달라야 함
-   지역성 (locality)
    -   작은 영역을 중심으로 특징 벡터를 추출
    -   물체가 부분적으로 가려지는 경우(occlusion)가 발생해도 매칭이 안정적으로 동작
-   적당한 양
    -   물체 추적을 위해서는 몇 개의 대응점이 필요하고 오류에 대해 강인한 추적을 위해서 특징점이 많아야 함
    -   그러나 특징점이 너무 많으면 계산 시간 증가
-   계산 효율
    -   계산 시간이 중요한 경우 실시간 처리가 가능해야 함

# 코너 검출

## 모라벡 알고리즘

-   여러 방향에 대해 색상 변화를 측정하는 제곱차의 합 제안
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/057fdfee-c6fa-4283-88f6-64610d3454b3/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/93785fef-9c74-456b-b3d1-853ed162523c/image.png)

-   c : 모든 방향에서 변화가 없어 S 맵의 모든 요소가 0
-   b : 수평 방향만 변화가 있어 S 맵의 좌우 이웃만 큰 값
-   a : 모든 방향으로 변화가 있어 S 맵에서 이웃 모두 큰 값
-   특징 가능성 값 측정
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/77cfc3b6-635d-4c40-99b4-c701b5bf84a8/image.png)
    -   a → C = 2
    -   b, c → C = 0
-   실제로 획득하는 영상은 앞의 예시보다 훨씬 복잡한 형태
-   마스크의 크기가 작음 (3x3)
-   상하좌우의 이웃만 살펴보고 점수를 매기는 방식은 한계가 있음

## 해리스 코너 검출 방법

-   1988년 해리스(C. Harris)가 개발한 코너 검출 방법
    -   코너 점 구분을 위한 아이디어를 수학적으로 잘 정의
-   윈도우(window) 함수 w(x, y)를 추가
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/dc7e63b6-1835-4e01-a982-a3ca86ce64cd/image.png)
    -   Gaussian 혹은 window 안에서만 1이 나오는 함수
-   만약 E(Δx,Δy) 함수가 모든 방향으로 값이 크게 나타난다면 점 (x, y)는 코너라고 간주
    -   모든 방향으로 그 값이 크게 나타나는지를 검사하기 위해
        -   테일러 급수(Taylor series)
        -   고윳값 분석(eigenvalue analysis)
        -   수학적 기법을 적용하여 코너 응답 함수 R을 유도
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9b1a406a-a964-42e0-bee1-3a1357a2f64c/image.png)
-   테일러 급수(Taylor series)를 이용한 전개
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a01f6d13-65cf-4b49-a047-add75e9bbbdd/image.png)
-   테일러 급수
    -   f(x)를 특정 위치 a에서의 도함수 값들의 합으로 근사
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e7b9ff32-d590-4963-8a09-4f41382a0103/image.png)
    -   복잡한 함수를 분석하고 계산하기 쉬운 다항식으로 근사하기 위하여 사용

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4a5d33ea-9d87-4075-b6fb-4266bf04febf/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/063a2def-23f8-4462-b8d2-b110c11964d7/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/38224769-e163-4ca1-b147-573dc22690bd/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/935ccfb3-974b-407b-8e1d-549d727a4c99/image.png)

-   고윳값(eigen value)과 고유 벡터(eigen vector)
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e67c69e3-c54c-47cb-a9b1-acdb02225aca/image.png)
    -   𝜆 : 행렬 A의 eigen value
    -   x : 이에 대응하는 eigen vector
    -   행렬 A를 곱한 결과가 원래의 벡터와 방향은 같고 크기만 𝜆에 비례해서 변함

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2728e889-5767-4fa1-82b0-4f1d5bf9449d/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5891c989-e9d4-4567-8a01-8a3d37bf1170/image.png)

## Window Function w(x, y)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/64e25aad-fdc7-491d-b7a6-ea7570ba8b93/image.png)

## 해리스 코너 검출 방법

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/521e8ac5-4c3d-4610-9e5f-e3e6864da795/image.png)

-   Det()는 행렬식(determinant)
-   Tr()은 대각합(trace)
-   행렬 M
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b1299f01-3f86-4450-bf00-f0d0e8abbd43/image.png)
-   코너 응답 함수 정의에서 상수 k
    -   보통 0.04~0.06 사이의 값을 사용함

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9160ad28-cae9-4b31-8c77-ea09b2c7371c/image.png)

-   해리스에 의해 정의된 코너 응답 함수 R
    -   입력 영상 각각의 픽셀에서 정의되는 실수 값
        -   이 값을 분석하여 코너, 에지, 평탄한 영역을 판별
    -   R이 0보다 충분히 큰 양수
        -   코너 점이라고 간주
    -   R이 0에 가까운 실수
        -   평탄한 영역
    -   R이 0보다 작은 음수
        -   에지라고 판별

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/39bf4e01-9836-4b33-9ae3-0fe86b32f50e/image.png)

## 코너 검출 방법

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/eb8ea393-b8ab-44aa-964a-2eb476b3637c/image.png)

## 해리스 코너 검출 방법

-   OpenCV는 해리스 코너 응답 함수 값을 계산하는 cornerHarris() 함수를 제공
    -   cornerHarris() 함수가 반환하는 해리스 코너 응답 함수 값에 적절한 임계값 연산을 적용 → 영상에서 코너 위치를 모두 찾을 수 있음
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/59bca493-929f-40c2-a00c-d3c2573bf1f6/image.png)
    -   입력 영상 src의 모든 픽셀 위치에서 해리스 코너 응답 함수 값을 계산
        -   그 결과를 dst 행렬로 반환함
    -   dst 행렬의 모든 원소는 float 자료형을 사용
        -   이 값이 사용자가 지정한 임계값보다 크면 코너 점으로 판단
    -   하나의 코너 위치에서 사용자 지정 임계값보다 큰 픽셀이 여러 개 발생할 수 있음
        -   간단한 비최대 억제(non-maximum suppression)를 수행 → 지역 최댓값 위치만 코너로 판별하는 것이 좋음

```python
src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

harris = cv2.cornerHarris(src, 3, 3, 0.04)
harris_norm = cv2.normalize(harris, None, 0, 255,
	cv2.NORM_MINMAX, cv2.CV_8U)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for y in range(harris_norm.shape[0]):
    for x in range(harris_norm.shape[1]):
        if harris_norm[y, x] > 120:
            if (harris[y, x] > harris[y-1, x] and
                harris[y, x] > harris[y+1, x] and
                harris[y, x] > harris[y, x-1] and
                harris[y, x] > harris[y, x+1]):
                cv2.circle(dst, (x, y), 5, (0, 0, 255), 2)

cv2.imshow('src', src)
cv2.imshow('harris_norm', harris_norm)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
```

-   harris_norm
    -   해리스 코너 응답 함수 값을 0부터 255 사이로 정규화한 그레이스케일 영상
    -   밝은 회색 점처럼 표현된 부분이 코너 위치
    -   픽셀 값이 120보다 큰 곳을 코너로 검출
    -   이 중에서 지역 최대인 지점을 선별
-   다수의 건물 모서리 부분과 나뭇가지 끝부분이 코너로 검출
-   임계값 120을 낮추면 더 많은 건물 모서리를 코너로 검출
    -   나뭇잎 또는 풀밭에서 코너로 검출되는 부분도 함께 늘어날 수 있으니 주의

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/bf723db7-d48f-45e3-a433-4ae8de1e05c6/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6e5bc31f-1c1c-44f6-a89a-3c37e33076b6/image.png)

## FAST 코너 검출 방법

-   해리스 코너 검출 방법
    -   영상의 코너 특성을 수학적으로 잘 정의
    -   복잡한 수식을 잘 전개하여 수치적으로 코너를 검출하였다는 데 의미
-   비슷한 컵셉을 발전시켜 추적에 적합한 특징(Good Features to Track)이라는 이름의 코너 검출 방법도 제안됨
    -   Shi-Tomasi corner detection
    -   cv.goodFeaturesToTrack()

## 코너 검출 방법

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0925f28b-1a91-4e19-a333-c1cd0bd098eb/image.png)

## FAST 코너 검출 방법

-   이러한 코너 검출 방법들
    -   복잡한 연산을 필요로 함 → 연산 속도가 느리다는 단점
-   2006년에 발표된 FAST 코너 검출 방법
    -   단순한 픽셀 값 비교 방법을 통해 코너를 검출
-   FAST : Featuers from Accelerated Segment Test
    -   매우 빠르게 동작하는 코너 검출 방법
-   FAST 방법
    -   영상의 모든 픽셀에서 픽셀을 둘러싸고 있는 16개의 주변 픽셀과 밝기를 비교하여 코너 여부를 판별
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ee16239b-6a4f-4b96-8b8e-fdb5ae8e62ed/image.png)
    -   점 p가 코너인지를 판별하기 위해 p점 주변 1번부터 16번 픽셀과의 밝기를 비교
    -   주변 16개의 픽셀 중에서 점 p보다 충분히 밝거나 또는 충분히 어두운 픽셀이 아홉 개 이상 연속으로 존재하면 코너로 정의
    -   점 p에서의 밝기는 I_p, 충분히 밝거나 어두운 정도를 조절하기 위한 임계값은 t
        -   만약 주변 16개의 픽셀 중에서 그 값이 I_p + t 보다 큰 픽셀이 아홉 개 이상 연속으로 나타나면
            -   점 p는 어두운 영역이 뾰족하게 돌출되어 있는 코너
        -   반면에 주변 16개의 픽셀 중에서 그 값이 I_p - t 보다 작은 픽셀이 아홉 개 이상 연속으로 나타나면
            -   점 p는 밝은 영역이 돌출되어 있는 코너
    -   특정 코너 점 주변 픽셀들도 함께 코너로 검출하는 경우가 많음
        -   주변 코너 픽셀 중에서 가장 코너에 적잡한 픽셀을 선택하는 비최대 억제 작업을 추가적으로 수행
    -   코너 점과 주변 16개 점과의 픽셀 값 차이 합을 코너 점수로 정의
        -   인접한 코너 중에서 코너 점수가 가장 큰 코너만 최종 코너로 선택
-   OpenCV는 FAST 코너 검출 방법을 구현한 FAST() 함수를 제공
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1c39da2d-2881-4cf2-bb0f-5abb1adb68d5/image.png)

```python
src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

fast = cv2.FastFeatureDetector_create(60)
keypoints = fast.detect(src)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for kp in keypoints:
    pt = (int(kp.pt[0], int(kp.pt[1])))
    cv2.circle(dst, pt, 5, (0, 0, 255), 2)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9df733bc-acea-4d84-a605-57303c6e8c92/image.png)

# 크기 불변 특징점 검출과 기술

## 크기 불변 특징점 알고리즘

-   코너는 회전 불변 특징점
-   영상의 크기가 변경될 경우 코너는 더 이상 코너로 검출되지 않을 수 있음
-   크기가 다른 두 객체 영상에서 단순한 코너 점을 이용하여 서로 같은 위치를 찾는 것에는 한계가 있음
-   SIFT는 크기 불변 특징 변환(Scale Invariant Feature Transform)
    -   2004년 캐나다의 브리티시 컬럼비아 대학교 로우(D. Lowe) 교수가 발표한 논문에 소개된 방법
-   SIFT 알고리즘
    -   영상의 크기 변화에 무관하게 특징점을 추출하기 위하여 입력 영상으로부터 스케일 스페이스(scale space)를 구성함
-   스케일 스페이스
    -   영상에 다양한 표준 편차를 이용한 가우시안 블러링을 적용하여 구성한 영상 집합
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4c8612d9-cc69-4277-858c-21a95f177a99/image.png)
    -   맨 윗줄에 나타난 여섯 개의 블러링된 영상이 스케일 스페이스를 구성한 결과
        -   이렇게 구성한 영상 집합을 옥타브(octave)라고 부름
    -   이후 입력 영상의 크기를 가로, 세로 반으로 줄여 가면서 여러 옥타브를 구성

## Scale Invariant Detection

-   Scale detection을 위한 좋은 함수의 조건
    -   하나의 안정적이고 뚜렷한 peak
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e30c6d14-6409-42c3-8354-f4c4629fbf77/image.png)
-   일반적인 영상의 경우
    -   밝기 대비에 대응하는 함수 (뚜렷한 지역적인 밝기 변화를 나타낼 수 있는 함수)

## Laplacian of Gaussian

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/bce8c8f5-d552-4210-a152-4632be059ebe/image.png)

## 크기 불변 특징점 알고리즘

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/cb30d927-1594-4884-adfd-353ebea09045/image.png)

## Scale Invariant Detection

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b2a95cef-b1d1-4305-8cfa-e594debfddec/image.png)

## 크기 불변 특징점 알고리즘

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ea12c14c-62c6-4dd6-afe8-9f07ba05fc21/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e9605b1d-3904-4905-b166-00f4254ef023/image.png)

## Difference-of-Gaussians

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4d65b261-5099-43f7-a65d-5dad7c1293e2/image.png)

## Scale-Space Extrema

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ba6cab0b-2493-4b49-93be-89c4414f0676/image.png)

## Multiple scales

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/f315030d-4942-4946-a1be-ffde170da1b4/image.png)

## SIFT 특징점 검출

-   SIFT 알고리즘에서 크기에 불변한 특징점 때
    -   인접한 가우시안 블러링 영상끼리의 차영상을 사용
    -   이를 DoG(Difference of Gaussian) 영상이라고 함
    -   DoG 영상 집합에서 인접한 DoG 영상을 고려한 지역 극값 위치를 특징점으로 사용함
    -   이후 에지 성분이 강하거나 명암비가 낮은 지점은 특징점에서 제외함

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c811224e-9753-427b-824d-d5cb4c40bc42/image.png)

-   SIFT 알고리즘
    -   특징점을 검출하는 기능
    -   특징점 주변의 픽셀 값을 이용한 기술자(descriptor) 계산 방법도 포함
-   특징점 기술자
    -   특징점 주변 영상의 특성을 여러 개의 실수 값으로 표현한 것
    -   특징 벡터(feature vector)라고도 함
    -   서로 같은 특징점에서 추출된 기술자는 실수 값 구성이 서로 일치해야 함
-   SIFT는 기본적으로 특징점 부근의 부분 영상으로부터 그래디언트 방향 히스토그램을 추출하여 기술자로 사용
    -   특징점 근방으로부터 특징점의 주된 방향 성분을 계산
        -   이 방향만큼 회전한 부분 영상으로부터 128개의 빈으로 구성된 그래디언트 방향 히스토그램을 계산
        -   각각의 빈 값은 float 자료형을 사용
        -   하나의 SIFT 특징점은 512바이트 크기의 기술자로 표현됨

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6da769d0-4431-415a-a68d-cfe761edeb10/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/dd1f5748-2e50-4b15-9a5a-bdfbbc88443c/image.png)

-   SIFT 알고리즘
    -   영상의 크기, 회전 등의 변환뿐만 아니라 촬영 시점 변황에도 충분히 강인하게 동작
    -   잡음의 영향과 조명 변화가 있어도 특징점을 반복적으로 잘 찾아냄
    -   다양한 컴퓨터 비전 분야에서 적용
        -   객체 인식, 파노라마 영상 이어 붙이기, 3차원 장면 인식 등의 분야에서 효과적

## 크기 불변 특징점 알고리즘

-   SIFT의 속도와 성능을 개선한 알고리즘
-   2008년에 발표된 SURF(Speed-Up Robust Features) 알고리즘
    -   SIFT에서 사용한 DoG 영상을 단순한 이진 패턴으로 근사화하여 속도를 향상
-   2012년에 발표된 KAZE 알고리즘
    -   가우시안 함수 대신 비등방성 확산 필터(nonlinear diffusion filter)를 이용하여 비선형 스케일 스페이스를 구축하여 특징점을 검출
    -   객체의 윤곽을 잘 보전 → 블러링, 크기 및 회전 변환, 잡음 등의 영향으로 변형된 영상에서 같은 특징점을 반복적으로 찾아내는 성능이 뛰어남
-   SIFT, SURF, KAZE 방법
    -   스케일 스페이스를 구성하는 등의 복잡한 연산을 수행 → 실시간 응용에서 사용하기 어려운 단점
    -   이들 특징점 알고리즘에 의해 만들어지는 기술자는 128개 또는 64개의 실수 값으로 구성됨
        -   메모리 사용량이 많고 특징점 사이의 거리 계산도 오래 걸리는 단점
-   2010년 전후로는 특징점 검출이 매우 빠르고 이진수로 구성된 기술자를 사용하는 알고리즘이 발표
-   당시 OpenCV를 관리하던 연구소에서 2011년에 발표한 ORB(Oriented FAST and Rotated BRIEF) 알고리즘
    -   SIFT와 SURF를 대체하기에 좋은 알고리즘
    -   FAST 코너 검출 방법을 이용하여 특징점을 추출
    -   기본적인 FAST 알고리즘은 영상의 크기 변화에 취약
        -   ORB 알고리즘은 입력 영상의 크기를 점진적으로 축소한 피라미드 영상을 구축하여 특징점을 추출
    -   각 특징점에서 주된 방향 성분을 계산하고, 방향을 고려한 BRIEF 알고리즘으로 이진 기술자를 계산
        -   BRIEF(Binary Robust Independent Elementary Features)는 순수하게 특징점 기술자만을 생성하는 알고리즘
        -   특징점 주변의 픽셀 쌍을 미리 정하고, 해당 픽셀 값 크기를 비교하여 0 또는 1로 특징을 기술
        -   두 점 x와 y에서의 픽셀 값 비교 테스트 T
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9dd700f6-e7dc-45d0-bf8c-03fc42ab7725/image.png)
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8791a110-b0ce-4255-b40c-3f080779d86b/image.png)
        -   특징점 p 주변에 a, b, c 점을 미리 정의
        -   T(a, b), T(b, c), T(c, a) → 이진수 110(2)
            -   b 점이 a보다 밝음
            -   c 점이 b보다 밝음
            -   a 점은 c보다 어두움
            -   특징점 주변 정보를 이진수 형태로 표현하는 기술자 → 이진 기술자(binary descriptor)
    -   FAST 기반의 방법으로 특징점을 구함
        -   각 특징점에서 픽셀 밝기 값 분포를 고려한 코너 방향 성분을 계산
            -   이 방향 성분을 이용하여 BRIEF 계산에 필요한 점들의 위치를 보정 → 회전에 불변한 BRIEF 기술자를 계산
    -   기본적으로 256개의 크기 비교 픽셀 쌍을 사용하여 이진 기술자를 구성
        -   하나의 특징점은 256비트로 표현할 수 있음
    -   SIFT와 SURF 기술자가 각각 512바이트, 256바이트를 사용
        -   ORB는 32바이트의 크기로 특징점을 기술 → 효율적
    -   이진 기술자로 표현된 특징점 사이의 거리 계산 → 해밍 거리(Hamming distance) 방법을 사용
        -   해밍 거리는 이진수로 표현된 두 기술자에서 서로 값이 다른 비트의 개수를 세는 방식으로 계산
            -   두 기술자의 비트 단위 배타적 논리합(XOR) 연산
            -   비트 값이 1인 개수를 세는 방식으로 빠르게 계산
-   ORB 외에도 BRISK, AKAZE, FREAK 등의 이진 기술자를 사용하는 특징점 알고리즘이 있음

## OpenCV 특징점 검출과 기술

-   KeyPoint 클래스
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6e12b54a-9449-4244-9044-02b12fced814/image.png)
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0b5024f7-b8d5-433a-8f51-a602584eb058/image.png)
    -   pt : 특징점 좌표
    -   size : 특징점 크기(지름)
    -   angle : 특징점의 주된 방향(각도)
    -   response : 반응성 (좋은 특징점을 선별하는 용도)
-   KeyPoint 클래스
    -   특징점 좌표, 특징점 검출 시 고려한 주변 영역의 크기, 주된 방향, 옥타브 정보 등을 멤버 변수로 가짐
        -   이러한 정보는 특징점 주변 영역의 특징을 표현하는 기술자 계산 시에도 사용됨
-   일반적으로 KeyPoint 객체는 사용자가 직접 생성하지 않음
    -   특징점 검출 클래스 내부에서 생성하여 사용자에게 반환함
-   OpenCV에서 특징점 관련 클래스는 모두 Feature2D 클래스를 상속받아 만들어짐
-   Feature2D 클래스
    -   detect(), compute(), detectAndCompute()라는 이름의 가상 멤버 함수를 가짐
    -   Feature2D 클래스를 상속받은 각각의 특징점 알고리즘 구현 클래스는 이들 멤버 함수 기능을 실제로 구현하도록 설계됨
    -   detect() 멤버 함수
        -   영상에서 키포인트를 검출함
    -   compute() 멤버 함수
        -   검출된 키포인트를 표현하는 기술자를 생성함
    -   detectAndCompute() 멤버 함수
        -   키포인트 검출과 기술자 생성을 동시에 수행함

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a7b7ad5f-a0d0-4479-b513-fbdc7be07b77/image.png)

-   Feature2D 클래스를 상속받아 만들어진 SIFT, SURF, FastFeatureDetector, BriefDescriptorExtractor, KAZE, ORB 등의 클래스
    -   실제 특징점 검출 및 기술 알고리즘을 구현한 클래스
-   가장 유명한 특징점 검출 알고리즘 : SIFT와 SURF
    -   각각 알고리즘과 동일한 이름의 클래스로 구현되어 있음
    -   소스 코드는 공개
    -   알고리즘 자체에 특허가 걸려 있음 → 상업적인 사용 시 제약
-   BriefDescriptorExtractor 클래스
    -   BRIEF 기술자 계산 방법이 구현된 클래스
-   SIFT, SURF, BriefDescriptorExtractor 클래스
    -   xfeatures2d 추가 모듈에 포함됨
    -   cv::xfeatures2d 네임스페이스를 사용
    -   OpenCV 소스 코드를 직접 빌드해야 사용할 수 있음
-   FastFeatureDetector, KAZE, ORB 등의 클래스
    -   cv 네임스페이스 사용
    -   OpenCV 기본 소스에 포함 → 쉽게 사용
-   FastFeatureDetector 클래스
    -   FAST 코너 검출 방법을 클래스로 구현
    -   특징점을 검출하는 기능만 있음
    -   FastFeatureDetector 객체에서 compute() 또는 detectAndCompute() 함수를 호출 → 에러 발생
-   BriefDescriptorExtractor 클래스
    -   다른 방법으로 구한 특징점 위치에서 BRIEF 이진 기술자를 구하는 기능만 제공
    -   BriefDescriptorExtractor 객체에서 detect() 또는 detectAndCompute() 함수를 호출하면 안됨
-   SIFT, SURF, KAZE, ORB
    -   특징점 검출과 기술을 함께 지원하는 알고리즘 클래스
    -   detect(), compute(), detectAndCompute() 함수를 모두 사용할 수 있음
-   특징점 구현 알고맂므 클래스를 이용하려면 먼저 각 특징점 클래스 객체를 생성해야 함
-   Feature2D를 상속받아 만들어진 특징점 클래스들은 모두 create()라는 이름의 정적 멤버 함수를 가짐
    -   특징점 클래스마다 정의된 create() 정적 멤버 함수의 인자 구성을 각기 다름
    -   모든 인자에 기본값이 지정 → 인자를 지정하지 않고도 사용할 수 있음
    -   각 특징점 클래스의 create() 멤버 함수는 해당 클래스 객체를 참조하는 스마트 포인터를 반환함
-   Feature2D::compute() 가상 멤버 함수
    -   이미 검출된 특징점에서 각 특징점 주변의 부분 영상을 표현하는 기술자를 추출
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/3288f215-fd8d-4005-aeed-512bedb0bb13/image.png)
-   Feature2D::detectAndCompute() 멤버 함수
    -   특징점 검출과 기술자 계산을 한꺼번에 수행
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/11722c44-1ee1-4d22-ace8-995b0ce63413/image.png)
-   drawKeypoints() 함수
    -   특징점을 검출한 후에는 입력 영상 어느 위치에서 특징점이 검출되었는지를 영상 위에 직접 표시하여 확인
    -   단순히 특징점 좌표만 보이도록 표현할 수도 있음
    -   특징점 검출 시 고려한 크기 성분과 주된 방향 성분을 함께 표현할 수도 있음
    -   OpenCV는 Feature2D::detect() 또는 Feature2D::detectAndCompute() 함수에 의해 검출된 특징점을 직접 영상 위에 그림
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a546dfe3-dfb6-41fb-95ee-44a896a7e00b/image.png)
    -   DrawMatchesFlags 열거형 상수
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7b3b5cd9-479f-4d46-8dbe-94e4084f827b/image.png)

```python
def detect_keypoint():
    src = cv2.imread('box_in_scene.png',
	    cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        sys.exit()

    orb = cv2.ORB_create()

    keypoints = orb.detect(src)
    keypoints, desc = orb.compute(src, keypoints)

    print('len(keypoints):', len(keypoints))
    print('desc.shape:', desc.shape)

    dst = cv2.drawKeypoints(src, keypoints,
	    None, (-1, -1, -1),
		    cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()
```

-   dst : ORB 알고리즘으로 검출된 특징점을 표시한 결과 영상
    -   각 특징점 위치를 중심으로 하는 다수의 원이 그려짐
    -   원 크기는 특징점 검출 시 고려한 이웃 영역 크기를 나타냄
    -   각 원의 중심에서 뻗어 나간 직선 → 특징점 근방에서 추출된 주된 방향을 표시함

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/172f5397-efcd-48a7-8693-c97ac318514e/image.png)

-   detect_keypoints() 함수 실행하면 콘솔 창
    ```
    keypoints.size(): 500
    desc.size(): [32 x 500]
    ```
    -   ORB 알고리즘으로 영상에서 500개의 특징점이 검출
    -   기술자 행렬이 500행, 32열로 구성됨
    -   ORB 알고리즘에 의해 구해지는 기술자 행렬
        -   CV_8UC1 타입 → 각 기술자의 크기는 32바이트
-   특징점에서 기술자를 계산
    -   detectAndCompute() 함수로 축약 가능

# 특징점 매칭

## OpenCV 특징점 매칭

-   특징점 매칭(matching)
    -   두 영상에서 추출한 특징점 기술자를 비교하여 서로 비슷한 특징점을 찾는 작업
    -   크기 불변 특징점으로부터 구한 기술자를 매칭 → 크기와 회전에 강인한 영상 매칭을 수행할 수 있음
-   DMatch 클래스
    -   한 장의 영상에서 추출한 특징점과 다른 한 장의 영상, 또는 여러 영상에서 추출한 특징점 사이의 매칭 정보를 표현할 수 있음
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/3429c345-3908-4a91-a337-a83f48ef1be0/image.png)
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/3fafa82a-2661-4c27-9077-eaf15d7a87a7/image.png)
    -   queryIdx : 질의 기술자 번호
    -   trainIdx : 훈련 기술자 번호
    -   imgIdx : 훈련 영상 번호
    -   distance : 두 기술자 사이의 거리
-   DMatch 클래스에서 distance 멤버 변수
    -   두 키포인트 기술자가 얼마나 차이가 나는지를 나타내는 매칭 척도의 역할
    -   두 특징점이 서로 유사 → distance 값이 0에 가까움
    -   서로 다른 특징점 → distance 값이 크게 나타남
    -   distance 계산 방식 → 다차원 벡터의 유클리드 거리(Euclidean distance)로 주로 계산
    -   이진 기술자끼리 비교하는 경우
        -   해밍 거리를 사용
    -   DMatch 클래스 객체는 보통 사용자가 직접 생성하지 않음
        -   특징점 매칭 알고리즘 내부에서 생성하여 사용자에게 반환
-   OpenCV의 특징점 매칭 클래스
    -   DescriptorMatcher 클래스를 상속받아 만들어짐
-   DescriptorMatcher 클래스
    -   match(), knnMatch(), radiusMatch() 등의 가상 멤버 함수를 가지고 있는 추상 클래스
    -   DescriptorMatcher 클래스를 상속받은 BFMatcher 클래스와 FlannBasedMatcher 클래스
        -   이들 멤버 함수 기능을 실제로 구현하도록 설계됨
    -   match() 함수 : 가장 비슷한 기술자 쌍을 하나 찾음
    -   knnMatch() 함수 : 비슷한 기술자 쌍 k개를 찾음
    -   radiusMatch() 함수 : 지정한 거리 반경 안에 있는 기술자 쌍을 모두 찾아 반환

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/df82d4ce-79f3-4eac-ab71-40bf6dd87c4e/image.png)

-   BFMatcher 클래스
    -   전수 조사(Brute-Force) 매칭을 수행
    -   질의 기술자 집합에 있는 모든 기술자와 훈련 기술자 집합에 있는 모든 기술자 사이의 거리를 계산
        -   이 중 가장 거리가 작은 기술자를 찾아 매칭하는 방식
    -   매우 직관적이지만 특징점 개수가 늘어날수록 거리 계산 횟수가 급격하게 늘어나는 단점
        -   첫 번째 영상에 1000개, 두 번째 영상에 2000개의 특징점이 있음
        -   BFMatcher 방법은 총 2000000번의 비교 연산을 수행
    -   특징점 개수가 늘어날수록 BFMatcher 방법에 의한 매칭 연산량을 크게 늘어나게 됨
        -   이러한 경우에는 FlannBasedMatcher 클래스를 사용하는 것이 효율적
-   Flann(Fast Library approximate nearest neighbors)
    -   근사화된 최근방 이웃(ANN, Approximate Nearest Neighbors) 알고리즘을 빠르게 구현한 라이브러리
-   FlannBasedMatcher 클래스
    -   Flann 라이브러리를 이용하여 빠르게 매칭을 수행하는 클래스
    -   근사화된 거리 계산 방법을 사용
    -   가장 거리가 작은 특징점을 찾지 못할 수 있지만, 매우 빠르게 동작
    -   기본적으로 L2 노름 거리 측정 방식을 사용
    -   해밍 거리를 사용하는 이진 기술자에 대해서는 사용할 수 없음
-   일단 BFMatcher 또는 FlannBasedMatcher 객체를 생성한 후에는
    -   두 입력 영상에서 추출한 기술자 행렬 사이의 매칭을 수행할 수 있음

```python
orb = cv2.ORB_create()

src1 = cv2.imread('box.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('box_in_scene.png', cv2.IMREAD_GRAYSCALE)

keypoints1, desc1 = orb.detectAndCompute(src1, None)
keypoints2, desc2 = orb.detectAndCompute(src2, None)

matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING)
matches = matcher.match(desc1, desc2)
```

-   drawMatches() 함수
    -   두 영상에서 추출한 특징점의 매칭 결과를 한눈에 확인할 수 있도록 매칭 결과 영상 생성 기능을 제공
    -   매칭 입력 영상을 가로로 이어 붙임
    -   각 영상에서 추출한 특징점과 매칭 결과를 다양한 색상으로 표시한 결과 영상을 생성함
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/98993083-78cd-420b-af6b-44440c43c272/image.png)
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4273c955-19d0-46c4-9ea3-9c13ff4ac875/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2bf6cd9e-b6bd-4c63-935f-30ab61fedb1f/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/845df4be-0759-4ac5-bf63-6640dfad8b37/image.png)

-   box.png 영상에서 추출한 모든 특징점 기술자에 대해 가장 유사한 box_in_scence.png 영상의 특징점 기술자를 찾아 직선을 그렸기 때문에 매칭 결과가 매우 복잡
-   box_in_scene.png 영상에서 추출된 일부 특징점 → 매칭이 되지 않아 직선이 연결되어 있지 않음
-   box.png 스낵 상자 글자 부분에서 추출된 많은 특징점이 box_in_scene.png 영상으로 제대로 매칭됨
-   여전히 몇몇 특징점은 box_in_scene.png 영상에서 스낵 박스 위치가 아닌 다른 지점으로 매칭됨

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ff646718-aad6-4e67-9eea-d277df2588a6/image.png)

-   키포인트 매칭 후 Distance 기반으로 상위 50개 선택

## 호모그래피와 영상 매칭

-   호모그래피
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/f4034ab0-3827-4e84-9c7d-47585cc7aa07/image.png)
-   실제적인 연산 관점에서
    -   호모그래피는 투시 변환과 같음 → 호모그래피는 3x3 실수 행렬로 표현할 수 있음
-   네 개의 대응되는 점의 좌표 이동 정보가 있으면 호모그래피 행렬을 구할 수 있음
-   특징점 매칭 정보로부터 호모그래피를 구하는 경우에는 서로 대응되는 점 개수가 네 개보다 훨씬 많음
    -   이러한 경우에는 투시 변환 시 에러가 최소가 되는 형태의 호모그래피 행렬을 구해야 함
-   findHomography() 함수
    -   두 영상 평면에서 추출된 특징점 매칭 정보로부터 호모그래피를 계산할 때 사용
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4e7ab024-1528-40ff-a54b-6ec244881251/image.png)
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9150c2b7-57e0-4c58-a441-1b216d7f46a7/image.png)
    -   RANSAC 알고리즘을 이용하여 호모그래피 행렬을 계산
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b292aa5b-4eb6-42f0-8df6-04f3bd2d226f/image.png)

# 영상 이어 붙이기

## 영상 이어 붙이기

-   영상 이어 붙이기(image stitching)
    -   여러 장의 영상을 서로 이어 붙여서 하나의 큰 영사을 만드는 기법
    -   영상 이어 붙이기로 만들어진 영상 → 파노라마 영상(panorama image)
-   영상 이어 붙이기에서 입력으로 사용할 영상
    -   서로 일정 비율 이상으로 겹치는 영역이 존재해야 함
    -   서로 같은 위치를 분간할 수 있도록 유효한 특징점이 많이 있어야 함
-   영상 이어 붙이기를 수행하려면
    -   입력 영상에서 특징점을 검출하고, 서로 매칭을 수행하여 호모그래피를 구해야 함
    -   구해진 호모그래피 행렬을 기반으로 입력 영상을 변형하여 서로 이어 붙이는 작업을 수행
    -   이때 영상을 이어 붙인 결과가 자연스럽게 보이도록 이어 붙인 영상의 밝기를 적절하게 보정하는 블렌딩(blending) 처리도 해야 함
-   OpenCV는 이러한 일련의 영상 이어 붙이기 작업을 수행하는 Stitcher 클래스를 제공
-   Stitcher 클래스를 이용하여 여러 장의 영상을 이어 붙이려면 먼저 Stitcher 객체를 생성해야 함
    -   Stitcher::create() 정적 멤버 함수를 사용
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e38b4edc-bc6a-4e5e-91ec-d57c60d50ea7/image.png)
    -   Stitcher::PANORAMA 모드 : 입력 영상들이 서로 투시 변환(또는 호모그래피) 관계에 있다고 가정
    -   Stitcher::SCANS 모드 : 입력 영상들이 서로 어파인 변환 관계라고 간주

```
argc = len(sys.argv)
if argc < 3:
    print('Usage: stitching.exe
	    <image_file1> <image_file2> [<image_file3> ...]')
    sys.exit()

imgs = []
for i in range(1, argc):
    img = cv2.imread(sys.argv[i])

    if img is None:
        print('Image load failed!')
        sys.exit()

    imgs.append(img)

    stitcher = cv2.Stitcher_create()
    status, dst = stitcher.stitch(imgs)

    if status != cv2.Stitcher_OK:
        print('Error on stitching!')
        sys.exit()

    cv2.imwrite('result.png', dst)

    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1b40e20d-9148-4e32-a777-b03c049ead52/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/56c31c22-95df-4b1c-a9cf-1f37f5642ce7/image.png)

-   영상을 이어 붙이는 과정에서 입력 영상이 변형되면서 결과 영상 주변부에 검은색으로 채워지는 영역이 발생할 수 있음

# 10.1 : Entity and Relationship

## Entitiy-Relationship Data Model

-   ER 데이터 모델
    -   데이터베이스를 개체와 관계로 모델링을 함
-   ER 데이터 모델의 모델링 원소는 개체와 관계
    -   개체와 관계 모두 특성으로 속성만을 가짐
-   객체 관계형 데이터 모델
    -   modeling primitive로는 객체(object)만 존재함
    -   객체가 가질 수 있는 특성으로서
        -   속성(attribute), 관계성(relationship), 메소드(method)를 가짐
-   클래스(class)
    -   동일한 특성을 가지는 객체 모임

## Entity, Entity Set

-   개체
    -   구별이 가능한 객체
    -   어떤 객체도 개체가 될 수 있음
        -   구체적인 사물, 개념적인 사물, 눈에 보이는 사물, 눈에 안보이는 사물 등 데이터베이스에 저장/관리하고자 하는 어떤 것(객체)도 개체가 될 수 있음
-   개체가 결정되면 개체는 속성을 가짐
    -   속성은 개체의 특성을 나타냄
-   개체 타입(또는 개체 집합)
    -   개체 중에서 같은 속성을 가지는 개체의 모임
-   개체와 객체의 차이점
    -   용어가 처음으로 도입된 개념에 차이가 있음
    -   개체
        -   ER 데이터 모델에서 사용한 용어
    -   객체
        -   객체지향 패러다임(또는 모델)에서 사용한 용어
    -   역사적으로는 개체 용어가 객체 용어 이전부터 사용됨

## Entity Sets

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a97d10e4-0127-497a-a555-9e7951b54a6d/image.png)

-   student 개체 집합
    -   속성이 동일한 다수 개의 student 개체가 있음
    -   속성은 동일하지만 속성 값은 다름
-   course 개체 집합
    -   다수 개의 course 개체가 있음

## Relationship, Relationship Set

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a01e4113-5654-4129-8d8a-914e1b2336a1/image.png)

-   개체 집합 내의 개체
    -   다른 개체 집합의 개체와 연관성이 있을 수 있음
-   연관성
    -   서로 관련이 있는 것
    -   그 의미는 무수함
    -   학생과 과목 개체 간에는 “수강하다” 의미가 있음
-   관계성은 수학적으로 표현
    -   각 개체 집합에 속하는 개체의 나열
-   관계성 집합(또는 관계성 타입)
    -   관계성 중에서 같은 속성을 가지는 관계성

## Relationship Set “takes”

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/70618ef8-a9a7-4d2a-9969-b6007be256ad/image.png)

-   관계성 집합 takes
    -   Student 개체 집합에 속한 개체가 Course 개체 집합에 속한 개체와 연관이 있음
    -   <10, Yoon> Student 개체
        -   Course 개체 <H-102, History>, <CS-101, Introduction to CS>, <CS-311, System Programming>과 연관이 있음
        -   의미는 ”수강하다“
-   동일 개체 집합 간에 한 개 이상의 관계성 집합이 존재할 수 있음
    -   Student 개체 집합과 Course 개체 집합 간에 “수강하다” 관계성 집합 외에도 다른 의미를 가지는 관계성 집합이 존재할 수 있음
        -   Ex) “과목 조교를 하다”

## Attributes of Relationship Set (1/2)

-   관계성 집합은 속성을 가질 수 있음
-   takes 관계성 집합
    -   수강 학기 및 연도를 속성으로 가질 수 있음

## Attributes of Relationship Set (2/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6a39a876-d219-46f5-81f9-034a1de786f9/image.png)

-   관계성 집합이 속성을 가짐

## Degree of a Relationship Set

-   관계성 집합 차수
    -   관련되는 개체의 개수
        -   이진(binary) 관계성 집합이 가장 흔함
        -   3진(ternary) 관계성 집합도 존재함
        -   이론적으로 4진(quaternary), 5진(quinary) 등의 차수도 가능

## Attributes

-   속성
    -   개체 또는 관계성이 가지는 특성
    -   서술적인 사항
-   속성의 구분
    -   단순 속성(simple attribute)과 복합 속성(composite attribute)
    -   단일 값 속성과 다수 값 속성
-   유도된 속성
    -   다른 속성을 이용하여 속성 값을 구할 수 있는 속성
    -   나이는 유도된 속성
        -   주어진 생년월일 속성을 이용하여 나이를 구할 수 있음

## Composite Attribute Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5b5c982e-9c7d-426d-8e3d-309c5bddfb3b/image.png)

-   복합 속성 이름
    -   이름, 중간이름, 성으로 구성됨
-   복합 속성 주소
    -   거리, 도시, 도, 우편번호로 구성됨
        -   거리는 다시 거리번호, 거리명, 아파트번호로 구성됨

## Cardinality Constraints (1/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6ec7279d-ee86-4d75-857a-ae3492cbb464/image.png)

-   카디날리티 제약
    -   이진 관계성 집합에서 유용함

## Cardinality Constraints (2/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/bcf0aacc-26cb-4d04-9aea-5ae7c096a820/image.png)

-   이진 관계성 집합에서 적용 가능한 4가지 카디날리티 제약

## Keys

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ba050062-13f3-4968-afd8-98532700775f/image.png)

-   ER 모델 개체에 대한 키 정의
-   개체에 대한 슈퍼 키, 후보 키, 주 키에 대한 개념
    -   테이블에 대한 슈퍼 키, 후보 키, 주 키 개념과 완전히 동일함

## Keys for Relationship Sets

-   관계성 집합의 슈퍼 키
    -   관련되는 개체 집합의 주 키를 합성하면 됨
    -   개체 간의 관계는 반드시 하나임
-   student 개체 집합과 course 개체 집합 간의 takes 관계성 집합
    -   student 개체 s_i는 course 개체 c_j와 연관이 될 수 있음
        -   이 경우 개체 s_i와 개체 c_j 사이에는 관계성이 하나만 존재함
        -   다수 개의 관계성은 존재하지 않음
-   슈퍼 키에서 후보 키 및 주 키를 선정할 때에는
    -   카디날리티 제약 및 참여 제약을 고려함

# 10.2 : ER Diagram

## ER Diagrams

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/91a6d445-6957-4925-9d66-1857d6ffd4b3/image.png)

-   ER 다이어그램
    -   ER 모델의 결과물
-   데이터베이스 설계자는 사용자 요구 사항을 분석하여 데이터 모델리을 함
    -   그 결과로 ER 다이어그램을 생산함
-   ER 다이어그램은 표기법이 다수 존재
    -   동일한 다이어그램도 다른 모습으로 보이기도 함
-   사각형 → 개체 집합
-   마름모형 → 관계성 집합
-   밑줄 → 주 키 속성
-   속성 → 사각형 안에 나열

## An Entity with Complex Attributes

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4b9e60f0-7007-4541-bf97-d0755abbed0a/image.png)

-   복합 속성을 가진 Employee 개체
    -   name
        -   firstName, middleInitial, lastName을 가진 복합 속성
    -   phoneNumber
        -   하나 이상의 값을 가진 다수 값 속성
    -   age
        -   유도된 속성(dateOfBirth 속성으로부터)
    -   address
        -   street, city, state, zipCode를 가진 복합 속성
        -   street는 streetNumber, streetName, aptNumber를 가진 복합 속성
        -   복합 속성 내에 복합 속성이 있는 경우

## Relationship Sets with Attributes

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d7e72a02-ba06-4db0-8c3b-72f62e12210b/image.png)

-   date 속성을 가진 관계성 집합 takes

## Cardinality Constraints

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/eb0ecf68-2604-46a8-beba-650974391a1f/image.png)

-   카디날리티 제약
    -   화살표가 “일(one)”을 의미
    -   화살표가 없으면 “다(many)”를 의미

## M:1/M:N Relationship Set

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a6973369-6475-45fd-9af5-aa5b1f55f6ab/image.png)

-   통상 대학교에서는
    -   교수 1인이 다수명의 학생을 상담
    -   학생 1인은 교수 1인에게만 상담을 받음
        -   advise 관계성 집합 → 1:N (student 개체가 N) 제약을 가짐

## Participation Constraints

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a35a85ae-f741-492e-a497-efbf90b53fe6/image.png)

-   참여 제약
    -   관계성 집합에 대한 제약
    -   부분(partial) 참여
        -   단일선
    -   전체(total) 참여
        -   이중선

## Constraint Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/06702c3c-9492-42b7-9fc3-c734d95e7eea/image.png)

-   takes 관계성 집합
    -   학생 1명은 다수 개의 과목을 수강
    -   과목 하나에는 다수 명의 학생이 수강
    -   다대다 카디날리티 제약
-   student 개체는 부분 참여 → 학생 중에는 수업을 수강하지 않는 학생도 있음
-   course는 전체 참여 → 모든 괌고은 학생이 수강하고 있음
    -   학생이 수강하지 않는 과목은 없음

## ER Diagram with a Ternary Relationship

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ffcf1ac7-d045-4a04-ba60-21223c36fcf2/image.png)

-   3진 관계성 ER 다이어그램
-   학생, 교수, 과제 개체가 함께 연관됨 → 3진 관계성 집합이 사용
-   만약 학생과 교수 간의 관계가 과제와 관련이 없고, 교수와 과제 간의 관계가 학생과 관련이 없고, 과제와 학생 간의 관계가 교수와 관련이 없으면
    -   세 개의 이진 관계성 집합으로 표현이 됨

## Cardinality Constraints on Ternary Relationship

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d56b4770-6b66-430b-aac0-81a8f194701d/image.png)

-   projAdvise 관계성 집합에 오직 professor 개체에만 일(one)에 대응된다고 하면
    -   이 경우 professor 한 명이
        -   다수의 student를 지도하고 또한 다수의 project를 지도하고 있음
    -   project 개체 하나에 대응되는 student 개체는 다수 명
    -   또한 student 개체 한 명에 대응되는 project 개체 또한 다수 개
        -   그러나 project 하나에 관련되는 professor도 한 명
        -   student 한 명에 관련되는 professor도 한 명

## Roles

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/28296b77-7a25-4f1d-9ad2-f0a984ab904b/image.png)

-   개체 집합이 관계성 집합에 참여를 할 때
    -   반드시 한 번만 참여하지 않아도 됨
    -   동일 개체 집합이 두 번 이상 관계성 집합에 참여를 하는 경우에는
        -   참여에 대한 의미(meaning)를 구분하기 위하여 롤 표시를 하여야 함
-   과목 개체 집합은 prerequisiteOf 관계성 집합에 2회 참여함
    -   한 번은 과목으로, 다른 한 번은 선수 과목으로 참여함
    -   과목 참여는 일(one)에 대응, 선수 과목 참여는 다(many)에 대응
        -   한 과목에 선수 과목이 다수가 있음
    -   모든 참여가 부분 참여
        -   모든 과목에 선수 과목이 있지 않음
        -   모든 과목이 선수 과목으로 참여하지도 않음

## Role Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/f8dac4b6-06cb-44cf-b034-eba3763abfd0/image.png)

-   people 개체는 spouse 관계성에 1:1 제약으로 부분 참여를 하고 있음
    -   people 개체 중에는 배우자가 없는 사람도 있음
    -   배우자가 있으면 배우자는 한 명(일부일처제)

## Weak Entity Sets

-   강한(strong) 개체
    -   자체적으로 주 키를 가지고 있음
-   약한 개체 집합
    -   주 키가 없는 개체 집합
    -   약한 개체를 구분하는 강한 개체(구분하는 개체(identifying entity))에 의존적 → 약한 개체는 강한 개체 존재 없이 존재할 수 없음
    -   약한 개체와 강한 개체 간에 존재하는 관계성(구분하는 관계성(identifying relationship)) 구성
        -   반드시 약한 개체는 전체 참여
        -   구분하는 개체가 일(one)에 대응
        -   약한 개체가 다(many)에 대응

## Keys of Weak Entity Sets

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/267ee7ac-fc71-4cd3-8e04-e0ce924e9e86/image.png)

-   약한 개체 집합 내에서는 부분 키가 존재할 수 있음
-   약한 개체 집합의 주 키
    -   구분하는 개체의 주 키와 부분 키의 결합(concatenation)

## Weak Entity Sets Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e6d02109-7d9f-4c88-9f65-7efb14dbab72/image.png)

-   대학교에서 과목(course) 개체
    -   과목명, 학점 등의 속성을 가짐
-   분반(section) 개체
    -   학생들이 수강하고 교수들이 강의하는 것
-   과목에 대한 분반
    -   동일 학년과 동일 학기에 대하여 다수 개가 개설
    -   분반 번호, 연도, 학기
        -   과목 하나 안에서는 유일
        -   분반 전체에서는 유일하지 않음
            -   이 경우 분반은 주 키를 가지지 못하는 약한 개체
-   분반 개체
    -   과목 개체 존재에 의존적 → 과목 개체에 연관이 없는 분반 개체는 존재할 수 없음
        -   참여 제약 관점에서는 전체 참여 제약
        -   카디날리티 제약은 과목 개체 하나에 분반 개체 다수가 존재 → 1:N
-   만약 과목 cID를 분반의 속성으로 설정하게 되면
    -   분반 개체가 강한 개체가 됨
    -   과목과 분반 간의 관계성은 불필요하게 됨

## E-R Diagram for a University

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/19cf800f-c63e-4a6f-837e-4e1d4760dadc/image.png)

-   대학교 데이터베이스를 구축하기 위하여 작성한 ER 다이어그램
    -   과목은 반드시 한 학과에서 개설되어야 함
        -   두 개 학과 이상이 공통으로 과목 개설을 할 수 없음
    -   분반(section)은 다수 명의 강사가 강의할 수 있음
    -   time_slot 개체
        -   요일, 시작시간, 종료시간 속성을 가짐
        -   하나의 시간대에 다수 개의 분반이 배정됨
        -   모든 시간대에 분반이 배정되지 않을 수도 있음
    -   학생 중에서는 상담(advise)을 받지 않은 학생도 있음

## Exercise (1/3)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5008d462-a235-47e2-8540-f0beca66c55b/image.png)

## Exercise (2/3)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/bbf3af81-5c4a-4f15-9164-e99a5d957b94/image.png)

-   Dependents 속성
    -   이름, 성별, 생년월일, 관계(부, 모, 배우자, 아들 딸 등등)가 있음
        -   주 키를 할 수 있는 속성이 없음 → weak entity type
    -   만약 주 키가 될 수 있는 주민번호(SSN) 속성을 가지면 strong entity type

## Exercise (3/3)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/bfd670e3-93f5-4edb-8360-55a6c9453cab/image.png)

-   타원은 속성을 의미
-   Name 속성
    -   Fname, Minit, Lname으로 구성되는 composite attribute
-   Location 속성
    -   두 개의 타원으로 표현된 multi-valued attribute
-   DEPENDENT weak entity type의 Name 속성
    -   점선 밑줄이 있음
    -   partial key를 표현

# 10.3 : Reduction to Relational Schema

## Entity Sets, Relationship Sets

-   설계자가 사용자 요구 사항을 반영하는 ER 다이어그램을 작성하면
    -   다음 단계는 이를 관계형 스키마로 변환하는 것
-   데이터베이스 설계의 목적
    -   좋은 관계형 스키마를 구하는 것
-   개체 집합과 관계성 집합
    -   각각 테이블로 속성과 함께 변환됨
    -   기본 원칙은 테이블 한 개씩으로 변환됨
-   기본적으로 개체 속성은 테이블 속성으로 변환됨
    -   개체 속성 타입에 따라 변환이 상이할 수 있음

## Strong/Weak Entity Sets

-   강한 개체는 관계로 변환이 됨
-   약한 개체도 관계로 변환이 됨
    -   약한 개체를 구분하는(identifying) 관계성은 테이블로 변환이 되지 않음
        -   약한 개체를 변환할 때 강한 개체의 주 키를 이미 포함하기 때문에 구분하는 관계성을 관계로 변환하면 중복이 됨

## Weak Entity Set Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4734e4ef-e6e8-47c7-a310-902c674d50d4/image.png)

-   강한 개체와 약한 개체 변환
-   변환된 테이블의 주 키도 결정해야 함

## M:N Relationship Sets

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4caf0c98-8418-4504-b2ed-ed0226c0ed9b/image.png)

-   다대다 관계성
    -   반드시 독립적인 테이블로 변환됨
    -   속성은 관여하는 개체 집합의 주 키를 포함

## N:1/1:1 Relationship Sets

-   다대일 관계성
    -   독립적인 테이블로 변환도 가능
    -   다(many)측 개체로 병합되어 테이블로 변환이 가능

## N:1 Relationship Set Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/18d73cc6-c2a4-48ad-8d88-e8ceb4a868cd/image.png)

-   첫 번째 방식
    -   own 테이블의 주 키는 vehicleID
    -   people 개체에 다수 개의 car 개체가 연관이 됨 → car 개체의 주 키만으로도 own 테이블의 주 키가 됨
-   두 번째 방식
    -   car 개체는 pID를 포함해야 함
    -   car 개체의 주 키는 vehicleID
    -   관계성에 참여하지 않는 car 터플의 pID 값은 널 값이 됨

## 1:1 Relationship Set Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ea1df90b-e95b-49cf-9f06-8c90e7ba66fa/image.png)

-   일대일 관계성 집합
-   첫 번째 방식
    -   own 테이블의 주 키는 pID 또는 vehicleID

## Composite Attributes

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0f0c2f7f-efea-48f9-a3a8-6ba1bbcb4998/image.png)

-   복합 속성
    -   flatten out되어 테이블 속성으로 변환됨
    -   복합 속성의 각 구성(component) 속성이 테이블 속성으로 변환됨
-   복합 속성 address
    -   street, city, state, zipCode로 구성
    -   street 속성
        -   streetNumber, streetName, aptNumber로 구성이 되는 복합 속성
    -   이 경우 streetNumber, streetName, aptNumber, city, state, zipCode 속성으로 변환됨
-   다수 값을 가지는 phoneNumber
    -   결과 테이블 스키마에 포함되지 않음
    -   독립 테이블로 변환됨
-   유도된 속성 age()
    -   관계형 스키마에는 명시적으로 포함됨
    -   객체지향 데이터 모델 또는 객체 관계형 데이터 모델에서는
        -   메소드(method)로 변환될 수 있음

## Multivalued Attributes

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1e29076d-ba58-482d-83c2-2579aeeb82ad/image.png)

-   다수 값 속성
    -   단일 테이블로 변환됨
    -   관련 개체의 주 키 속성을 포함
-   관계형 데이터 모델의 기본적인 가정
    -   모든 값이 원자 값이어야 함
-   만약 데이터 모델이 속성 값으로 집합 값을 허용하면
    -   다수 값 속성이 독립적인 테이블로 변환되지 않음
    -   다른 단순 값 속성과 유사하게 변환됨
-   객체 관계형 데이터 모델에서는
    -   속성 값으로 집합을 허용

# 10.4 : Design Issues

## E-R Design Decisions

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/f62d4e7b-edcc-4e5c-a46c-16f0f20810bc/image.png)

-   소세상(mini world)에 대해 데이터 모델을 하는 경우
    -   위처럼 결정하여야 하는 사항은 많음
-   동일한 정보를 표현하는 방식에 따라 데이터베이스 시스템의 성능이 좌우되기도 함

## Entity Sets vs. Attributes

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b426a0a6-e389-4a26-9174-057279a7d42a/image.png)

-   데이터베이스에서 표현하고자 하는 사항
    -   개체로 표현할 것인지
    -   개체 속성으로 표현할 것인지 결정해야 함
-   전화번호를 독립 개체로 모델링하는 것
-   전화번호 정보를 사람 개체의 속성으로 모델링
-   오른쪽 ER 다이어그램
    -   전화번호만을 가지는 테이블이 존재
    -   바람직한 모델이 아님
    -   전화번호에 대한 다양한 정보가 함께 저장이 된다면
        -   해당 번호 허가일, 해당 번호 누적 사용 시간 등등
        -   전화번호에 대한 독립적인 관계 생성을 고려할 수 있음

## Entity vs. Relationship

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2c6b8d70-93e2-4096-9273-a47397ddc3cd/image.png)

-   정보를 표현하기 위하여
    -   개체화 또는 관계성화를 결정해야 함
-   일반적으로 명사(noun)는 개체로 표현됨
-   명사 간의 동사는 관계성으로 표현됨
-   “학생이 분반을 수강하다”를 ER 모델링
    -   첫 번째 ER 다이어그램이 적합

## Where to Put Attributes (1/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e7b8694e-1c05-415e-9e94-239da4228258/image.png)

-   단일 아이디어는 단일 개체 또는 단일 관계성으로 표현해야 함
-   관계성의 속성 위치
    -   다대다 카디날리티 제약에서는 관계성에 반드시 위치해야 함

## Where to Put Attributes (2/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2c210a7d-8f15-4cc6-8793-58e85200e148/image.png)

-   카디날리티 제약이 일대일 경우에는
    -   관계성 속성은 임의의 관련 개체에 위치할 수 있음
-   카디날리티 제약이 일대다인 경우에는
    -   관계성 속성은 다(many)쪽 개체에 위치할 수 있음

```
people(ID, name, address, age)
car(vehicleID, make, model, year, color,
	registrationDate, pID)
```

## Redundant Attributes

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/dcbea7f3-bf95-480c-b742-b2f1157e4cb1/image.png)

-   professor 개체의 deptName
    -   중복되는 속성으로 제거되어야 함
-   Professor가 속하는 학과 정보
    -   deptName 속성과 belongs 관계성 집합으로 중복적으로 표현되어 있음
-   관계형 스키마로 변환을 하면 중복성이 더욱 명확해짐

## Binary vs. Non-binary Relationships

-   다진 관계성이 다수 개체 간의 관계를 명확히 표현함
-   다진 관계성을 다수 개의 이진 관계성으로 변환이 가능함
    -   변환 시에 다진 관계성의 모든 정보가 완전히 변환되지 않고 일부 정보가 유실되는 경향이 있음

## Binary vs. Ternary Relationship Set

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c91ded1b-a685-47b7-b092-c67c0fc71a5b/image.png)

-   회귀적(recursive) 관계성을 사용하여 이진 관계성과 삼진 관계성을 비교
-   parenthood 관계성
    -   아버지/어머니/자식에 대한 정보가 정확히 기록되어야 함
-   fatherhood 관계성과 motherhood 관계성
    -   서로 관련이 없는 관계성
-   데이터베이스에 아버지/어머니/자식 정보를 반드시 함께 기록하려면
    -   삼진 관계성 parenthood를 사용해야 함
    -   부분 정보만이라도 표현을 하려면 두 개의 이진 관계성을 사용
-   parenthood 삼진 관계성은 fatherhood 관계성과 motherhood 관계성을 동시에 표현하지만
    -   fatherhood 관계성과 motherhood 관계성이 반드시 parenthood 삼진 관계성을 표현하지는 않음

## Converting Non-Binary Relationships (1/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7007d1ad-1bd4-4e95-8eaf-8ac6b7fe56d3/image.png)

-   일반적으로 다진 관계형은 다수 개의 이진 관계성으로 변환이 가능
-   새로운 객체 집합을 생성한 후
    -   다진 관계성 집합에 속하는 관계성에 대응하는 개체 및 관계성을 생성

## Converting Non-Binary Relationships (2/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e8d94254-841a-464b-85f6-3c80d0a1b150/image.png)

-   이러한 변환의 문제점
    -   다진 관계성에 존재하는 제약 사항을 새로운 다이어그램에서 정확하게 표현하지 못하는 것

# 10.5 : Extended ER Model

## Specialization/Generalization

-   ER 데이터 모델
    -   객체지향 모델의 일반화/특수화/상속 기능을 지원
-   하향식 설계과정에서는 특수화가 가능
-   상향식 설계과정에서는 일반화가 가능
-   특수화와 일반화
    -   동일한 현상을 의미 → 두 개 용어는 호환적으로 사용됨

## Specialization/Generalization Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4a83d8bb-2174-4ccf-880d-6cd6433230ab/image.png)

-   people 개체
    -   3개 속성을 가지고 있음
-   하위 개체인 employee
    -   salary 속성만 가지고 있음
    -   속성 상속으로 인하여 총 4개 속성을 가짐
-   people의 하위 개체 employee, student
    -   overlapping specialization을 의미
-   employee의 하위 개체 professor, secretary
    -   disjoint specialization을 의미

## Multiple Specialization

-   상위 개체와 하위 개체 간에 반드시 하나만의 특수화/일반화가 존재하는 것은 아님
    -   다수 개의 특수화가 가능

## Constraints on Specialization/Generalization (1/2)

-   상위 개체에 속하는 개체가 하위 개체에 속하는 기준에 대하여 조건을 정의할 수도 있으며 또는 사용자가 지정할 수도 있음
-   상위 개체가 하위 개체에 속하는 방식에서 제약은
    -   disjoint
        -   상위 개체가 하위 개체 하나에만 속하게 됨
    -   overlapping
        -   상위 개체가 다수 개의 하위 개체에 속할 수 있음

## Constraints on Specialization/Generalization (2/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1e9c6daf-29c8-4faa-b7ba-68f00bb3cf5d/image.png)

-   완전 제약 조건
    -   전체(total)와 부분(partial)이 있음

## Representing Specialization as Schemas (1/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ec02b096-d0c6-4010-8b93-b692d1b1b4a3/image.png)

-   스키마로 변환
-   첫 번째 방법
    -   하위 개체는 하위 개체에만 속하는 속성과 상위 개체의 주 키만으로 스키마를 변환하는 것
        -   이 경우, 하위 관계에 대한 모든 속성을 검색하기 위해서는 하위 관계와 상위 관계 모두를 접근해야 함

## Representing Specialization as Schemas (2/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e5ac4003-fe99-45bd-9a5b-fa51e85415b7/image.png)

-   스키마로 변환
-   두 번째 변환
    -   하위 개체는 상속받은 모든 속성과 해당 개체에만 적용되는 속성만으로 스키마를 구성하는 것
    -   특수화가 total 제약을 가지면 상위 개체는 반드시 하위 개체에 속하게 됨 → 상위 개체만을 위한 테이블 생성이 필요하지 않을 수도 있음
    -   하위 개체를 이용하는 뷰로 상위 개체를 대신할 수 있음
        -   뷰 테이블에는 참조 무결성을 설정하지 못함 → 상위 개체에 대한 데이터 제약 사항을 설정할 수 없음

# 10.6 : Notations

## Symbols in E-R Diagram (1/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/180e742b-6ce6-4171-918c-907559d706b9/image.png)

-   ER 다이어그램에 대한 기호

## Symbols in E-R Diagram (2/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/bf78f881-3754-4079-8b82-b329352e5a28/image.png)

-   오른쪽 위에서 두 번째 그림
    -   카디날리티 제약과 참여 제약을 동시에 표현할 수 있는 표기법
-   오른쪽 위에서 세 번째 그림
    -   특수화의 overlapping 조건
-   오른쪽 위에서 네 번재 그림
    -   특수화의 disjoint 조건
-   왼쪽 가장 밑 그림
    -   특수화의 total 참여 조건은 명시해야 함

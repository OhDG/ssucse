# 2.1 : Relational Data Model

---

## Relation Example

---

-   관계형 데이터 모델에서 의미하는 관계
    -   테이블 형식
-   각 속성(attribute)은 속성 헤드(attribute head)를 가짐
-   student 관계는 7개의 속성(attribute)와 5개의 터플(tuple)을 가지고 있음

## Equivalent Terms

---

-   관계형 모델 ↔ 기존 데이터 모델
-   관계(relation) ↔ 테이블(table)
-   터플(tuple) ↔ 레코드(record), row
-   속성(attribute) ↔ 칼럼(column)

## Attributes

---

-   도메인
    -   각 속성은 속성 값으로 허용할 수 있는 값의 집합을 가짐
-   속성 값은 해당 도메인의 원소임
-   현실적으로 사용자가 도메인을 명확하게 정의하여야 DBMS를 사용할 수 있는 것은 아님
    -   속성에 대한 데이터 타입 정의로 부터 통상 도메인을 유추할 수 있음
-   속성 도메인에 속하는 값은 원자(atomic) 값을 가져야 함
-   각 도메인은 값이 없는 것을 의미하는 널(null) 값을 디폴트(default)로 가짐

## All attributes are atomic in relational model

---

-   관계형 모델에서
    -   모든 속성 값은 원자 값이어야 함
        -   원자 값은 더 이상 분해할 수 없는 값
        -   일반적으로 정수, 실수, 문자, 문자열, 시간, 날짜, 타임스탬프(timestamp) 등
            -   문자열은 각 문자로 분해가 가능하나, 관계형 모델에서 문자열은 원자 값
        -   원자 값이 아닌
            -   집합, 리스트, 복합값(composite values) 등
-   군집 데이터를 정의하는 집합(set), 백(bag), 리스트(list)값은 원자 값이 아님
    -   집합, 백, 리스트는 서로 상이한 대상을 표시함
-   집합
    -   집합에 속하는 원소간에 중복이 없고
    -   원소간에 순서가 없음
-   백
    -   원소간에 순서가 없음
    -   원소의 중복을 허용함
-   리스트
    -   원소의 중복을 허용함
    -   원소간에 순서가 존재함
-   집합 {a,b}와 집합 {b,a}는 동일한 집합이다.
-   {a,b,a}는 집합은 아니나, 백은 될 수 있다.
-   백 {a,b,a}와 백 {a,a,b}는 동일한 백이다. (원소 순서에 무관하므로)
-   리스트 [a,b,a,c]와 리스트 [a,a,b,c]는 상이한 리스트이다.

## Relation Schema and Instance

---

-   관계 스키마
    -   관계 이름과 속성명 나열을 의미함
-   관계 스키마가 정의되면 우리는 관계 스키마에 적합한 값의 조합을 가질 수 있음
    -   이를 관계 인스턴스라고 함
-   관계 스키마는 관계형 및 속성명 외에도 각 속성의 데이터 타입, 관계에 관련되는 무결성제약도 함께 표현함
-   관계 인스턴스
    -   각 속성 도메인 값의 모든 조합에서 일부분(부분 집합)을 가짐
    -   도메인의 카타시안곱(Cartesian product)의 부분 집합
        -   이러한 집합을 관계(relation)이라고 명명함

## Relational Databases

---

-   관계형 데이터베이스 시스템에서
    -   데이터베이스는 관계와 제약 조건으로 구성됨
-   무결성 제약(integrity constraints)은 다양한 형태가 존재
    -   키 제약 : 주 키는 중복된 값을 가지지 못하는 제약
    -   엔티티 제약 : 주 키는 널 값을 가지지 못하는 제약
    -   참조 무결성 제약 등

## Sample University Database

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e429274f-d28e-4430-92a0-c8c0b4be467f/image.png)

-   속성 밑줄은 주 키(primary key) 속성을 표시
    -   course 관계에서 cID 값은 항상 유일함
-   teaches 관계의 주 키는 4개 속성의 연결(concatenation) (pID, cID, semester, year)
    -   속성 하나 하나는 주 키가 아님
    -   pID만으로는 주키가 아니므로 pID는 중복되어 터플에 나타날 수 있음
    -   각 pID, cID, semester, year값을 연결한 전체 값은 주 키이므로 항상 유일
-   화살 표시는 참조 무결성 제약임
    -   teaches 관계의 cID 속성은 course 관계의 주 키 속성인 cID 속성을 참조하는 외래 키(foreign key)임

## Order is immaterial

---

-   관계형 데이터베이스에서 관계 간에는 순서가 없음
-   관계 내에서의 터플도 순서가 없음
-   관계형 모델에서는 관계간의 순서 또는 상하관계가 없음

## Keys

---

-   키는 속성의 집합으로 구성됨
-   슈퍼 키
    -   관계에서 터플을 유일하게 식별할 수 있는 속성의 집합
-   후보 키
    -   슈퍼 키의 유일성을 유지하면서 가장 적은(minimal) 수의 속성으로 구성된 키
-   minimal 개수의 속성이 가장 적은 개수의 속성을 의미하지는 않음
-   minimal 속성
    -   유일성을 유지하면서 가장 적은 속성을 의미
-   관계에 하나 이상의 후보 키가 존재하면
    -   데이터베이스 설계자가 그 중의 하나의 주 키(primary key)로 저장하게 됨

## Key Example

---

-   MyStudent(student-id, name, national-id, address, phone)
-   student-id와 national-id 속성은 유일 식별자
-   Superkey
    -   (student-id), (student-id, name), (student-id, name, address),
    -   (national-id), (national-id, name), (national-id, address, phone)
    -   (student-id, national-id) (student-id, national-id, name) (student-id, national-id, address, phone), …
    -   슈퍼 키는 그 수가 매우 많으며 그 중 일부분이 나열
    -   슈퍼 키 (student-id, name)은 student-id만으로도 각 학생을 유일하게 식별할 수 있음
    -   학생을 유일하게 식별하기 위하여 굳이 (student-id, name)와 같이 두 개 속성을 가질 필요가 없지만 그래도 슈퍼 키임
-   후보 키(Candidate key)
    -   슈퍼 키에서 키 속성을 유지하면서 가장 적은 수(minimal)의 속성을 가지는 키
    -   student-id은 가장 적은 수의 속성을 가지는 후보 키가 되는 것
    -   같은 방식대로 national-id도 후보 키
-   주 키(Primary key)
    -   후보 키 중에 하나
    -   (student-id) or (national-id)
-   후보 키는 minimal 속성을 가지는 수퍼 키이지, minimum 속성을 가지는 수퍼 키는 아님
    -   특정 테이블에 대한 후보키가 두 개 존재할 수 있고, 하나는 단일 속성, 다른 하나는 2개 속성을 가질 수 있음

## Referential Integrity Constraint

---

-   참조 무결성 제약(referential integrity constraint, 또는 referential constraint)
    -   관계형 데이터 모델에만 존재하는 제약
        -   관계형 데이터 모델은 데이터 간의 관계를 값으로 표현하기 때문
    -   관계형 데이터 모델을 기반으로 하는 객체-관계형 데이터 모델에서도 존재
    -   특정 속성에 나타나는 모든 값은 반드시 다른 속성에도 나타나야 한다는 것
        -   특성 속성에 나오는 모든 값은 다른 속성 값의 일부분이어야 함
-   기존 계층/네트워크 데이터 모델에서는 데이터 간의 관계를 포인터로 표현했음

## Why Referential Integrity Constraint?

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/95187c70-21f9-44fd-ad6c-46d401471c28/image.png)

-   Sohn 학생은 major 속성값 4에 대응이 되는 학과가 없어 문제가 있음
-   Park 학생은 major 값이 없는 null 값인데, 문제가 있는 것은 아님
-   major 속성 값
    -   아무런 제약 없이 임의의 값을 가질 수 없음
    -   department의 dID 속성값에서 중에서 나와야 의미가 있음
-   major 속성을 department(dID) 참조하는 외래 키(foreign key)라고 함
-   student 테이블을 참조하는 테이블(referencing relation)
-   department 테이블을 참조 받는 테이블(referenced relation)
    -   참조 받는 속성은 반드시 그 테이블의 주 키이어야 함
    -   student 관계의 특정 터플과 department 관계의 특정 터플이 관련이 있을 때, department 관계의 주 키를 참조하여야 하기 때문
    -   department 주 키를 참조하여야만, 반드시 department 관계의 하나 터플이 특정됨
-   department 테이블의 <3, media> 터플을 참조하는 터플이 student 테이블에 없음
    -   참조 무결성 제약과 관련 없이 허용되는 현상

## Data Dictionary

---

-   데이터 사전은 데이터베이스 시스템이 내부적으로 관리하는 데이터 장소이며, 데이터에 대한 데이터 즉 메타 데이터를 관리함
    -   관계 이름
    -   각 관계의 이름, 유형 및 속성 길이
    -   보기의 이름 및 정의
    -   무결성 제약
    -   비밀번호를 포함한 사용자 및 계정 정보
    -   통계 및 설명 데이터
        -   각 관계의 튜플 수
    -   실제 파일 구성 정보
        -   관계 저장 방식(순차/해시/...)
        -   관계의 물리적 위치
    -   지수에 대한 정보

## Metadata Example

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7e2f2ab3-2919-43eb-93d3-703c955d6432/image.png)

-   일반 테이블 형식으로 저장 관리됨

# 2.2 : Sample University Database

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c1bf323a-305e-4337-819e-ac94fae6714f/image.png)

# 2.3 : Relational Algebra

---

## Relational Algebra

---

-   관계 대수는 관계형 데이터 모델의 일부임
    -   제약 사항에 대한 연산을 제공함
    -   관계에 대한 다수 개의 연산을 제공함
    -   사용자는 관계 대수를 이용하여 데이터베이스로부터 구하고자 하는 정보를 데이터베이스 시스템에 요청(또는 표현)할 수 있음
    -   입력으로 하나 또는 두 개의 관계를 가지고 결과물로 새로운 관계를 생성함
    -   관계 대수 연산의 중첩(composition)을 허용함
-   상용 데이터베이스 시스템은 관계 대수를 직접적으로 사용자에게 지원하지는 않음
    -   SQL 언어를 사용자에게 지원함
-   관계 대수는 데이터베이스 시스템 내부에서 사용되는 언어
    -   사용자에게 직접 보이지 않음

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8b2e2ff5-c025-40cd-bfb0-217a0478ce3e/image.png)

## Select Operation Example

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/feef90ce-8f43-418d-a02a-7263e6ebd227/image.png)

-   선택 연산은 입력 관계에서 주어진 조건을 만족하는 터플을 생성함
-   선택 연산의 결과물은 새로운 관계임

## Select Operation

---

-   선택 연산의 기호
    -   σ(sigma)
-   p는 선택 조건(selection predicate)
    -   선택 조건 p는 명제 논리(propositional logic) 표현
    -   각 항(term)은 ⋀(and), ⋁(or), ﹁(not)으로 연결이 가능
    -   각 항은 “<attribute> op <attribute>” 또는 “<attribute> op <constant>” 형태
    -   op는 6개의 비교 연산자
-   σdeptName=“CS” (professor)
    -   교수 중에서 CS 과에 속한 교수를 검색

## Project Operation Example

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0f2d020c-e704-4246-8114-ababd63a03f9/image.png)

-   투영 연산
    -   관계에서 임의의 속성을 선택하는 연산
    -   투영 후에 중복된 터플은 제거됨
    -   결과 관계에서 동일한 터플이 두 번 이상 나타나지 않음

## Project Operation

---

-   투영 연산의 기호는 Π(pi)
-   보고자 하는 속성을 아래첨자(subscript)로 표시
-   중복 터플은 결과 관계에서 제거
    -   set로 결과 관계가 다뤄짐
-   결과 관계는 항상 터플의 집합
-   선택 연산이 터플 단위로 원하는 결과를 구함 ↔ 투영 연산은 속성 단위로 결과를 구함
-   데이터 모델
    -   사용자에게 데이터를 추상화하여 보이게 하고 동시에 추상화된 데이터에 대한 연산을 제공

## Union Operation Example

---

-   관계 대수의 집합 연산 관점
    -   관계를 터플을 원소로 가지는 집합으로 봄

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0949d399-a80e-41f1-8e7d-5cb4a81efd0d/image.png)

## Union Operation

---

-   일반적인 합집합 정의와 동일함
-   터플을 원소로 취급함
-   관계 대수 집합 연산이 유효하려면
    -   터플의 속성 개수가 동일하여야 함
    -   대응되는 속성의 도메인이 상호 호환적이어야 함
        -   이러한 제약은 교집합, 차집합 연산에도 동일
-   ΠcID(σsemester=”Fall” ⋀ year=2014 (teaches)) U ΠcID(σsemester=”Spring” ⋀ year=2015 (teaches))
    -   2014년 가을과 2015년 봄에 개설된 모든 과목의 과목번호(cID)를 검색함

## Set Difference Operation Example

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a1d29b7f-cb7d-4c65-ab7b-f5a0abf10fe8/image.png)

-   차집합 연산은 commutative 하지 않음
    -   제시된 수의 순서에 상관없이 결과가 동일하지 않음

## Set Difference Operation

---

-   ΠcID(σsemester=”Fall” ⋀ year=2014 (teaches)) - ΠcID(σsemester=”Spring” ⋀ year=2015 (teaches))
    -   2014년 가을 학기에 개설되었으나 2015년 봄 학기에는 개설되지 않은 과목 번호를 검색하는 질의

## Cartesian Product Operation Example

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1774bb10-af7b-47af-98c6-3f4a808b5755/image.png)

-   카타시안곱의 결과물은 입력 관계에 속하는 터플의 모든 가능한 조합을 결과 관계로 산출함

## Cartesian Product Operation

---

-   카타시안곱 연산
    -   입력 관계의 각 터플을 취하여 이를 연결(concatenation)하여 결과 관계를 만듦
    -   두 개의 입력 테이블에 동일 속성이 존재하면
        -   재명명(rename) 연산을 이용하여 동일한 속성 이름이 없도록 함
        -   존재하면 자연 조인(natural join) 연산이 되기 때문

## Rename Operation

---

-   재명명 연산은 단순히 테이블 이름이나 속성 이름을 변경하는 연산
-   수학 기호는 ρ(rho)
-   입력 관계가 E이면
    -   이를 아래 첨자에 표시된 바와 같이 재명명하여 결과 관계를 도출함
-   아래 첨자로 표현되는 명시부에서 X는 관계명
-   A1, …, An는 속성명
-   관계명만 또는 속성명만 재명명이 가능함
-   관계명만 변경하고자 할 때에는
    -   아래 첨자 명시부에서 속성명을 생략
-   속성명만 변경하고자 할 때에는
    -   아래 첨자 명시부에서 관계(속성명)을 모두 명시해야함

## Relational Algebra Expressions

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a15db14c-6cee-4e5a-b3cd-a0c066a83db3/image.png)

-   관계 대수식의 결과는 관계
    -   관계 대수식의 합성이 가능
    -   입력 관계 대신에 유효한 관계 대수식을 사용할 수 있음

## Exercise 1

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c1bf323a-305e-4337-819e-ac94fae6714f/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7a70b0ce-0dc4-485a-a0fe-e74798a81030/image.png)

## Exercise 2

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a4818d63-5b64-4ecd-ad5b-94b4a65e83b2/image.png)

-   마지막 관계 대수식이 잘못된 이유
    -   선택 조건이 and 조건인데 양쪽 조건을 모두 만족하는 deptName이 조잰할 수 없기 때문
    -   올바른 질의
        -   Πtitle(σdeptName="CS"(course)) ⋂ Πtitle(σdeptName="EE"(course))

## Exercise 3

---

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4c84e92b-3cab-4764-8325-6de04954cd84/image.png)

-   department 관계를 재명명하며 department 관계와 카타시안곱을 함
    -   결과 테이블은 8(=4+4)개의 속성을 가짐
    -   터플은 9(=3\*3)개
-   카타시안곱 결과 관계의 속성명은
    -   (deptName, chairman, building, budget, new-deptName, new-chairman, new-building, new-budget)
-   카타시안곱 결과 관계에 선택 연산을 적용
    -   조건을 만족하는 터플은 총 3개
-   3개 터플에 대하여 투영 연산을 수행하면, 결과는 {<EE, CS>, <EE, Media>, <CS, Media>}
-   왜 재명명을 하나?
    -   기존의 department와 구별하기 위해서(budget ↔ new-budget)

# 2.4 : Additional Relational Algebra

---

## Additional Operations

-   추가되는 관계 대수는 이미 살펴본 기본 확장 대수를 이용하여 표현이 가능
    -   관계 대수의 표현력(expressive power)을 확장시키지는 않음
    -   사용 편리성을 제공
-   할당 연산
-   교집합 연산
-   자연 조인
-   외부 조인
-   나눔 연산

## Assignment Operation

-   할당 연산자 (←)
    -   복잡한 질의문을 작성할 때 중간 결과 표현을 임시로 저장할 수 있음
-   할당 연산을 하면서 재명명 연산자를 함께 사용
    -   중간 결과의 관계 및 속성 이름을 원하는 것으로 변경하면서 할당할 수 있음

## Set Intersection Operation

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1941681f-a26c-4ed1-b44b-feb60ca70c45/image.png)

-   교집합 연산자
    -   2회 차집합 연산 적용으로 표현이 가능 → 확장 관계 연산자
-   관계 대수 집합 연산자의 경우
    -   입력 관계에 대한 속성 개수가 같음
    -   대응되는 속성의 데이터 타입이 상호 호환되어야 함
-   터플을 하나의 원소로 취급하여 연산을 함

## Natural Join Operation

-   타 관계 대수 연산에 비하여 시간이 많이 소요됨
-   조인 연산 중에 가장 흔하게 사용되는 조인은 자연 조인
-   자연 조인은 입력 테이블에 대하여
    -   카타시안 곱을 수행
    -   조인 조건을 이용하여 선택 연산을 수행
    -   조인 조건에 언급된 속성을 이용하여 투영 연산을 수행
-   조인은 기본적으로 카타시안곱, 선택 연산, 투영 연산을 수행
    -   선택 연산과 투영 영산 방법 차이에 의해 세 가지 내부 조인(inner join)으로 구분

## Natural Join Example 1

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8ad50d96-e76f-489a-835a-5a903b953017/image.png)

-   입력 테이블 R과 S 속성 중에서 같은 이름의 속성이 조인 속성이 됨
-   자연 조인의 경우
    -   조인 속성이 결과 관계에 한 번만 나오게 됨
-   자연 조인 시에 조인 조건을 명시하지 않으면
    -   두 개 테이블에서 동일 이름을 가지고 속성 간에 자연 조인을 수행
-   만약 동일을 가지는 속성 중에서 일부 속성만으로 조인 조건을 사용하려면
    -   속성 이름을 rename하거나 조인 조건을 명시적으로 표시
-   동일한 속성명을 구분하기 위해 ‘테이블명.속성명’ 형식을 사용

## Natural Join Example 2

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6b65d436-0dc8-43e5-85fd-5347d82f31ba/image.png)

-   2020년 가을 학기에 강의한 교수명과 교수가 강의한 과목명을 검색
    -   2020년 가을에 대한 정보 → teaches 관계에만 있음 → teaches 관계에 선택 연산을 하면 됨
    -   teaches 관계에는 교수번호와 과목번호만 있음
        -   교수번호를 가지고 교수명을 검색 → professor 관계와 자연 조인
        -   과목번호를 가지고 과목명을 검색 → course 관계와 자연 조인
    -   course 테이블을 myCourse 테이블로 재명명하는 이유
        -   deptName 속성 이름을 변경하기 위함
        -   course의 deptName과 professor의 deptName 속성 간에 조인이 발생하기 때문

## Natural join is associative and commutative

-   자연 조인 연산은 결합성과 교환성이 있음
    -   이러한 특성은 질의어 최적화 과정에서 사용

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/27bad2de-0752-429e-81e6-bdaae0b3f7b4/image.png)

## Theta-join, Equi-join, Natural Join

-   조인
    -   내부 조인(inner join)
        -   세타 조인(theta join)
            -   가장 일반적인 조인
        -   동등 조인(equi-join)
            -   세타 조인 중에서 조인 조건이 동등 조건만으로 구성이 되는 경우
        -   자연 조인
            -   동등 조인 중에서 조인 조건 속성이 조인 결과에 한 번만 나오는 경우
    -   외부 조인(outer join)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/81cffa8a-4af8-4716-a028-57d616831687/image.png)

## Theta Join/Equijoin Example (1/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c9d1a13c-c2fd-49bf-9a43-b3e6a9a2d319/image.png)

## Theta Join/Equijoin Example (2/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c450b519-1c0f-49c2-8654-27af04d7f517/image.png)

-   세타 조인은 pID의 산술 비교 “myProfessor.pID > myTeaches.pID”가 조인 조건
-   pID는 두 입력 관계에 모두 나옴 → 모호성을 해결하기 위하여 관계명을 속성명 앞에 명기
-   동등 조인은 조인 조건 모두가 동등 조건을 가지는 경우
    -   입력 관계의 모든 속성이 결과 테이블에 속하게 됨
    -   동등 조인에서는 반드시 동일한 내용을 가지는 속성이 2번 결과 테이블에 나옴 → 중복되는 정보가 존재
-   중복되는 정보를 제거한 것이 자연 조인임

## Outer Join

-   내부 조인 연산에서는 조인 조건을 만족시키지 않는 터플은 조인 결과에서 배제
    -   외부 조인은 이러한 터플도 결과 관계에 포함시킴
    -   null 사용해서

## Natural Left Outer Join Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/eac956d9-3917-4fb0-a90b-b3f3a78ceeea/image.png)

-   왼쪽 외부 조인
    -   조인 수식에서 왼쪽에 오는 입력 관계의 모든 터플은 결과 관계에 나와야 함
    -   조인되는 값이 없으면 null 값을 사용

## Natural Right/Full Outer Join Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5a6a7436-133f-44b0-a0a6-afa4db8c5c5e/image.png)

-   완전 외부 조인 연산
    -   오른쪽 외부 조인 연산과 왼쪽 외부 조인 연산을 합친 연산
    -   두 입력 관계의 모든 터플이 결과 관계에 존재함

## Division Operation

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/177d575b-b235-4b45-a1e8-71f4521bc953/image.png)

-   나눔 연산
    -   입력 관계가 두 개 있음
        -   두 관계에는 공통 이름을 가지는 속성이 있어야 함
-   나눔 연산의 결과 관계
    -   공통 속성이 제거된 속성을 가짐
-   결과 관계에 속하는 터플
    -   S 관계의 공통 속성에 속하는 모든 터플을 가지는 R 관계 터플임

## Division Operation Example 1

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6d036a42-fd2f-4d96-90f7-b498f4318dbd/image.png)

-   s1 관계는 속성이 하나, r 관계는 속성을 두 개 가짐
    -   결과 관계의 속성은 하나
-   결과 관계의 터플은 s1 관계의 모든 터플을 가지는 r 관계 터플임

## Division Operation Example 2

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2ec8243b-f564-4bb4-9fcb-19c5e89f10cf/image.png)

-   분자 관계의 속성 개수는 5
-   분모 관계의 속성 개수는 2
-   결과 관계 속성 개수는 3 = ( 5 - 2 )

## Division Operation Semantic

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0ee8eff0-7c15-4185-95bc-3b5255ca6a76/image.png)

-   나눔 연산의 의미
    -   모든 조건을 포함하는 질의, 즉 전체정량자(universal quantifier)에 대응되는 질의를 구현함
-   자연어로 표현된 질의어를 수학 논리식으로 표현
    -   전체정량자는 나눔 연산에 대응
    -   존재정량자(existential quantifier)는 조인 연산에 대응
-   SQL은 나눔 연산을 직접적으로 지원하지 않음
    -   차집합 연산을 활용하는 간접적으로 나눔 연산 의미를 지원

## Why division operation is not fundamental?

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6d7715b2-6bb5-407e-a163-d1bd9f890ac7/image.png)

-   나눔 연산은 카타시안곱, 투영, 차집합을 사용하여 표현이 가능

## Relational Algebra Recap

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0cd25d2f-9ab4-4843-8606-62e3548b349e/image.png)

-   왼쪽 군에 속하는 관계 대수
    -   기본 대수
-   오른쪽 군에 속하는 관계 대수
    -   기본 대수를 이용하여 대치가 가능한 확장 관계 대수

## Bank Schema

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/12aeb4d0-6f05-4c3b-95c1-a6082dc89f43/image.png)

-   6개 참조 무결성
    -   depositor.customerName ---> customer.customerName
    -   depositor.accountNumber ---> account.accountNumber
    -   borrower.customerName ---> customer.customerName
    -   borrower.loanNumber ---> loan.loanNumber
    -   account.branchName ---> branch.branchName
    -   loan.branchName ---> branch.branchName
-   첫 번째와 세 번째 참조 무결성은 customer 테이블에 나오는 고객 중에서 일부가 depositor 테이블 또는 borrower 테이블에 나온다는 제약
    -   depositor 테이블에 고객명이 나오려면 우선은 customer 테이블에 등록이 되어야 함

## Exercise 1

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5ff6b8ff-7831-4733-aecf-c3d14c3044fc/image.png)

## Exercise 2

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/39ff3474-38b7-479e-870a-4bc29ac4f6b2/image.png)

-   customer 테이블에서 customerName을 그냥 project
    -   아직 account 또는 loan을 가지지 않은 customer도 구하기 때문에 바람직한 방법은 아님

## Exercise 3

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/45bfb565-98ac-4e4f-934c-0984bfaa395b/image.png)

```sql
ΠcustomerName(σbranchName=‘Seoul'(loan) ⋈ borrower)
```

-   자연 조인을 사용하는 것이 자연스러움

## Exercise 4

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/50353261-18bf-45ea-8065-c368c8f83999/image.png)

-   할당(assignment) 연산은 관계대수식이 복잡한 경우 중간 표현을 저장하는 기능을 제공

## Exercise 5

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7f9905c1-bd0e-409f-8c49-12a1b0a48cb4/image.png)

-   account(accountNumber, branchName, balance)
    -   a1 Seoul 10
    -   a2 Pusan 40
    -   a3 Inchoen 20
-   account x ρd(account) 표현식은 총 6개의 속성을 가짐
    -   account.balance, d.balance를 포함
    -   2개 속성에 대한 값은
    -   <10, 10>, <10, 40>, <10, 20>
        <40, 10>, <40, 40>, <20, 20>
        <20, 10>, <20, 40>, <20, 20>
    -   account.balance<d.balance 조건으로 선택
        -   <10, 40>, <10, 20>, <20, 40> 터플이 선택됨
            -   이에 대하여 account.balance 속성으로 투영을 하면, {<10>, <20>}이 나옴
                -   이를 전체 잔고 값에서 차집합 연산을 하면, 연산 결과는 {<40>}

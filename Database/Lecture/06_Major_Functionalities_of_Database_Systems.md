# 6.1 : Views

## Views

-   뷰
    -   특정 사용자로부터 특정 사용자로부터 특정 속성을 숨기는 기능
    -   데이터베이스 스키마 일부를 특정 사용자에게 숨김 → 특정 사용자는 데이터 존재 여부를 인지하지 못함
-   뷰의 사용 목적
    -   데이터 보호
    -   사용자 편리성 제공
    -   질의 간소화 등

## View Definition

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/dfdc39d9-2696-4fb0-8f57-e3263ebfbfd3/image.png)

-   뷰는 “create view” 문장으로 정의
-   정의가 된 뷰는 질의문에서 일반 테이블처럼 사용할 수 있음

## Views are always up to date!

-   뷰는 한 개 이상의 테이블로부터 정의할 수 있음
-   뷰 테이블은 터플을 실제 뷰 내부에 저장하지 않음 → 가상 관계(virtual relation 또는 virtual table)
-   터플을 가지는 테이블 → 베이스 관계(base relation)
-   뷰는 항상 가장 최신의 데이터를 가지고 있음
    -   정확하게 표현하면 뷰는 터프을 내부적으로 가지고 있지 않음
    -   데이터베이스 시스템이 뷰 정의를 활용하여 질의문을 처리 → 뷰가 가장 최신 데이터를 가지고 있는 것처럼 사용자에게 보임

## Views Using Other Views

-   뷰를 정의할 때 베이스 테이블이나 또는 다른 뷰를 사용할 수 있음
-   순환 뷰(recursive view)
    -   새로운 뷰를 정의할 때 자신 뷰를 이용

## View Expansion

-   뷰에 대한 질의가 들어오면
    -   해당 뷰를 기존에 저장되어 있는 뷰 정의로 치환하여 뷰가 아닌 베이스 테이블에 대한 질의문이 되도록 함
        -   변환 과정은 뷰 정의가 베이스 관계만으로 구성될 때까지 진행
        -   치환되는 뷰가 순환 뷰가 아니면 치환은 종료
    -   변환된 질의문
        -   뷰가 존재하지 않고 베이스 테이블로만 구성이 됨

## View Expansion Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5b7b581e-82a8-45d7-8dc3-412fa6520576/image.png)

## View Modifications

-   뷰에 대한 검색 연산
-   뷰에 대한 변경 연산
    -   입력, 삭제, 갱신
    -   뷰를 정의하고 있는 베이스 테이블에 대한 변경 연산으로 변환

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c27656fb-6544-4807-8835-51e45c29173b/image.png)

## Some modifications cannot be supported !!!

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b0285550-1bea-4a14-9cc2-521f00d5a1df/image.png)

-   professorInfo에 터플이 입력되면
    -   베이스 테이블을 수정하는 데에 모호함(ambiguous)
    -   professorInfo 테이블에 대한 입력 연산을 지원할 수 없음
-   salary 합을 가지는 집계 함수
    -   집계 함수에 대한 경신을 베이스 테이블에 반영하기에 명확한 방법이 없음
    -   이러한 변경 연산도 지원할 수 없음

## Updatable View

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a18ab4f2-0650-4b33-9d9f-0ac52d1d1426/image.png)

-   변경가능 뷰는 뷰 생성 정의 시에 다양한 제약이 존재
    -   “group by”, having, distinct, 집합 연산, 집계함수, “order by” 등이 뷰 정의에 들어가 있으면 그 뷰는 변경 가능하지 않음

## “With check option” Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2bfa5344-21bb-44b5-987f-0e43e81f25c4/image.png)

-   입력된 <255, Brown, EE, 100000> 터플
    -   CSProfessor 뷰를 통하여 입력이 확인되지 않음
    -   터플의 deptName 속성이 EE
    -   사용자 관점에서 입력된 터플이 테이블에 존재하지 않는다는 잘못된 인식을 할 수 있음
-   “with check option”
    -   갱신된 뷰를 통하여 갱신 효과를 사용자가 볼 수 있을 경우에만 뷰 갱신을 허용

## Restrictions on Views

-   뷰에 대한 색인은 불가능
    -   뷰는 터플을 가지고 있지 않음 → 색인은 의미가 없음
-   뷰에 대한 키 속성 또는 무결성 제약을 정의할 수 없음

# 6.2 : Integrity Constraints

## Integrity Constraints (ICs)

-   사람의 나이 속성 값이 음수 → 정확하지 않은 데이터(not accuracy)
-   사람의 나이가 테이블마다 다름 → 서로 일치하지 않은 데이터(consistency)
-   무결성 제약
    -   은행 계좌의 최소 잔고는 $1000 이상이어야 함
    -   시간 당 근로소득은 $6 이상이어야 함
-   무결성 제약은 데이터베이스의 일치성 및 정확도를 유지하기 위해 사용됨

## Constraints on a Single Relation

-   not null
-   primary key
-   unique
-   check (P), where P is a predicate

## Not Null/Primary Key/Unique Constraints

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e9681006-f2ba-4e3b-a767-7fef345626d7/image.png)

-   not null 제약
    -   개별 속성에 적용이 가능
-   primary key, unique 제약
    -   한 개 이상의 속성에 적용이 가능
-   primary key 선언 → 널 값을 가질 수 없음
-   unique 선언 → 널 값은 가질 수 있음

## “check” Clause

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/9e52abe9-0fea-445d-88c0-ad2b21df5cc1/image.png)

-   check절
    -   관련 테이블이 항상 만족하여야 하는 조건을 명시함
-   semester 속성이 주어진 4개 값(”Spring”, “Summer”, “Fall”, “Winter”)만 가지게 함
    -   주어진 4개 외의 값으로 변경을 하려는 데이터 변경 및 입력 연산은 실행되지 않음

## Referential Integrity Constraint

-   참조 무결성 제약의 정의
    -   외래 키에 나오는 모든 값은 외래 키가 참조하는 테이블의 주 키 값으로 나와야 함
    -   외래 키는 널 값을 가질 수 있음
    -   외래 키가 참조하는 주 키는 해당 테이블의 주 키이므로 널 값이 나올 수 없음
-   참조 무결성 제약은 상이한 두 관계 사이에 존재
    -   동일 관계 내에서도 존재할 수 있음
-   참조 무결성 제약은 연관되는 데이터(터플) 연결을 값(value)을 이용하기 때문에 발생하는 현상
    -   터플 간의 관계를 값이 아닌 포인터로 연결을 하면 참조 무결성이 존재하지 않음

## Referential Integrity Declaration

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/257317e4-a350-440e-96d1-42ce02a23243/image.png)

-   참조 무결성을 선언
    -   구체적인 행동(action) 명시 없이 선언할 수 있음
        -   이 경우 참조 무결성이 위반되는 연산은 허용하지 않음
    -   참조 무결성을 선언하면서 참조 무결성이 위반되는 경우 이를 해결하는 구체적인 행동까지 명시
        -   명시할 수 있는 행동
            -   “cascade”
            -   “set null”
            -   “set default”
-   참조 무결성은 외래키를 가지는 테이블에서 선언됨
    -   참조되는 테이블에서는 선언하는 부분이 없음
-   외래키를 선언하면서 함께 명시하는 행동 부분
    -   delete/update 연산
        -   참조되는 테이블에 대한 삭제 및 갱신 연산을 의미
        -   professor 테이블에 대한 delete/update 연산

## “on delete” Operation

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a7152740-05f6-4a83-b318-370fe4a26bdb/image.png)

-   teaches의 pID는 professor 주 키 pID를 참조하는 외래 키
-   professor 테이블의 첫 번째 터플이 삭제되면
    -   teaches 테이블에서 참조하는 터플로 인하여 참조 무결성이 위배됨
    -   이 경우 행동이 명시되지 않았으면 삭제 연산이 허용되지 않음
    -   cascade인 경우
        -   삭제 연산이 teaches 테이블에 파급 → 삭제된 터플을 참조하는 두 터플이 모두 삭제됨
    -   set null인 경우
        -   해당 테이블 속성 값을 널 값으로 하는 것
        -   teaches 테이블 주 키의 일부부인 pID이므로 허용되지 않음
-   teaches 테이블의 터플을 삭제
    -   참조 무결성 제약을 위배할 가능성이 전혀 없음 → 해당 터플만 삭제됨

## “on update” Operation

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/894081f4-1564-4d4e-9948-8d59ece1f88f/image.png)

-   professor 테이블의 첫 번째 터플의 값이 100에서 400으로 변경
    -   참조 무결성 제약에 위반됨
    -   행동이 명시되지 않는 경우에는 변경 연산 자체가 수행되지 않음
    -   cascade인 경우
        -   teaches 테이블의 첫 번째와 두 번째 터플의 값이 함께 변경됨
    -   set null인 경우
        -   pID 속성이 professor 테이블의 주 키 → 널 값이 허용되지 않음
        -   갱신 연산이 허용되지 않음
-   teaches 테이블의 <100,CS101, ...> 터플이 <400,CS101, ...>으로 변경되는 경우
    -   참조 무결성을 위반
    -   갱신 연산이 수행되지 않음
    -   행동 명시와는 관련이 없음

## How to Insert Tuples?

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e85161a5-9ec7-49b8-acd3-0854b9a75abb/image.png)

-   mother와 father 속성이 외래 키로 선언이 되어 있음 → person 데이터를 입력하려면 그 사람에 대한 mother, father 정보가 있어야 함
-   첫 번째 방법은 대규모 데이터 입력이 이론적으로 가능하나 현실적으로 아주 불편
-   두 번째 방법은 추가적인 갱신 연산이 필요함
-   데이터베이스 시스템은 무결성 제약을 연기하여 점검하는 기능을 제공함

## Deferrable ICs

-   무결성 제약은 기본적으로 즉시 실행됨
-   무결성 제약을 명시할 때 “initially deferred” 표현
    -   무결성 제약 검사 및 행동을 연기할 수 있음
-   트랜잭션 정의 시에 무결성 제약 점검을 연기할 수 있음

## Complex Integrity Constraints

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0f85bee0-319b-4ad8-901f-d55963b0e3f9/image.png)

-   사용자가 임의로 정의하는 복잡한 무결성 제약
    -   check절 조건을 활용
    -   주장(assertion) 기능을 활용
-   SQL 표준은 check 조건에 임의의 조건을 허용 → 서브질의를 조건으로 할 수 있음
-   teaches pID 값은 professor pID 값 중에 하나를 가지는 참조 무결성
    -   이 경우에는 무결성 제약 만족 여부를 teaches 테이블에 변화가 있을 때만 한정 ⇒ professor 테이블에 변화가 있어도 무결성 제약을 점검하지 않는 문제
-   주장(assertion)은 표준 SQL2에 명시되어 있는 사양
    -   사용자 임의의 무결성 제약을 유지하는 방법
-   일반적으로 상용 데이터베이스 시스템은
    -   check 절에 서브질의를 허용하지 않음
    -   주장(assertion) 기능을 지원하지 않음
        -   많은 비용이 들어감, 시스템 성능 저하의 이유로

## Assertion Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/3db9d2b9-7541-4275-80cf-40ac82df0a4a/image.png)

-   student 테이블의 totalCredit 속성 값을 점검하는 assertion
-   언급되는 테이블에 대한 변화(데이터 입력, 삭제, 변경)가 있으면 데이터베이스 시스템은 묵결성 제약 만족 여부를 매번 점검해야 함 (not exists)
    -   자원이 많이 소모되는 연산
-   assertion 기능은 자원 낭비가 많아, 무결성 제약 관리를 위하여 트리거(trigger)를 제공함

# 6.3 : Triggers

## Triggers

-   트리거
    -   상용 데이터베이스 시스템이 무결성제약 관리를 위하여 지원하는 기능
    -   기본적으로 ECA 규칙으로서 사건(event) / 조건(condition) / 행동(action) 부문으로 구성됨
        -   데이터베이스 시스템에 어떤 사건이 발생하면, 주어진 조건을 평가하여 조건이 만족되면 주어진 행동을 하는 규칙
        -   사건이란 데이터베이스에 대한 변경 연산(insert/delete/update 연산)

## Events and Actions in Triggers

-   트리거에서 의미하는 사건
    -   터플 인스턴스 변화
    -   터플 입력, 터플 삭제, 터플 갱신 연산을 의미
-   트리거 갱신(update) 연산에서 속성을 지정할 수 있음
    -   “Update of 속성명 on 테이블명”
-   터플에 변화가 있으면 변화하기 전 터플과 변화 후의 터플을 지칭하는 문장
    -   “referencing old row as”
        -   for deletes and updates
    -   “referencing new row as”
        -   for inserts and update

## Trigger Example 1 (1/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/596f67f6-48a1-491d-bd1a-1fd50b302b49/image.png)

-   사건
    -   takes 테이블의 grade 속성에 변경이 있을 때
-   조건
    -   grade 속성의 값이 변경 전에는 F이거나 또는 널 값
    -   변경 후의 속성 값은 F가 아니면서 널 값도 아니어야 함
-   행동
    -   student 테이블의 totalCredit 속성 값을 조정
    -   추가하는 학점은 course 테이블에서 찾음

## Trigger Example 1 (2/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7ceb6aaa-c427-46d2-ac26-94f5b108ffd6/image.png)

-   트리거를 구현하는 SQL 문장
-   첫 문장에서 트리거 이름과 사건 명시
-   두, 세 번째 문장은 update가 발생하는 경우 update 전과 후의 테이블의 터플을 참조하는 문장
-   when절은 조건을 명시
    -   변경 후 터플의 grade 값은 ‘F’가 아니면서 널 값도 아님
    -   변경 전 터플의 grade 값은 ‘F’이거나 널 값이어야 함
-   begin 블록은 트리거의 행동을 명시
    -   when절의 조건을 만족하면 begin 블록을 수행
    -   student 테이블의 totalCredit 속성 갱신
    -   새로운 터플의 cID 값을 가지고 course 테이블에서 해당 과목의 credit 값을 구하여 기존 totalCredit 속성 값에 합산하는 연산을 함
-   네 번째 문장(for each row)은 조건과 행동을 값이 변경된 각 터플을 기준으로 수행하는 것을 의미
    -   takes 테이블의 update된 각 터플에 대하여 조건을 검사하고 조건이 만족하면 행동(Update 문장)을 수행함

## Trigger Example 2 (1/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5211ea4d-1b35-465f-9470-14d55e512cd2/image.png)

-   잔고보다 더 많은 금액의 수표가 발생되는 경우(overdraft)
    -   대출 계좌를 사용자 명의로 개설하고 대출금을 overdraft된 금액으로 하는 작업을 함
-   이벤트
    -   account 관계 갱신 연산
-   조건
    -   balance 속성 값이 음수(negative)로 되는 것

## Trigger Example 2 (2/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/88f7f81f-d88b-440c-a69b-e810c2ba61f1/image.png)

-   트리거가 수행되는 조건
    -   account의 balance가 음(negative)이 되는 것
-   첫 번째 입력 연산
    -   borrower 관계에 새로운 터플을 생성
    -   depositor 관계에 있는 account 번호를 loan number로 사용함
-   두 번째 입력 연산
    -   loan 관계에 새로운 터플을 입력
    -   주어진 balance의 값에 음수를 붙여 양수 값이 됨
    -   이 값을 loan amount로 입력
-   마지막 갱신 연산
    -   account 관계의 balance 속성 값을 zero로 갱신
-   행동에 해당되는 insert/insert/update 문장을 트랜잭션으로 수행하기 위하여 “begin atomic … end”를 사용함
    -   행동 SQL 문장이 하나이면 “begin atomic … end”를 사용하지 않아도 됨
-   트랜잭션
    -   ACID(atomicity, consistency, isolation, durability) 성질을 가지는 데이터베이스 연산의 sequence

## Trigger Example 3

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b1ab8b25-c18b-4276-93fb-4e6dcaa5897f/image.png)

-   employee 관계의 salary 속성에 변경이 발생하는 경우, department 관계의 totalSalary 속성을 변경하는 터플 수준 트리거
-   트리거 조건
    -   nrow.dNumber의 값이 널이 아닌 경우

## Triggers can be activated before an event!

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/975c89be-11f0-4212-9cbf-caeb1229ee74/image.png)

-   트리거를 정의할 때, before 키워드를 사용하면
    -   이벤트가 수행되기 전에 트리거가 수행됨
-   takes 테이블을 갱신하기 전에 터플의 grade 속성 값이 ‘ ‘이면 널 값으로 갱신하는 트리거

## Statement Level Triggers

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/056e216f-9e79-4454-a1e1-ca2a1ce6f7fe/image.png)

-   터플 수준 트리거
    -   터플 단위로 트리거 행동을 수행
-   문장 수준 트리거
    -   SQL 문장 단위로 트리거 행동을 수행
    -   사건 전후 테이블을 테이블 단위로 참조함
    -   트리거 행동으로 인하여 많은 터플에 변화가 있는 경우에 유용

## Statement Level Trigger Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/bbcc310b-b81f-4e5d-858f-7b92af518fe6/image.png)

-   employee 관계의 salary 속성에 변경이 발생하는 경우
    -   department 관계의 totalSalary 속성을 변경하는 문장 수준 트리거
-   when절의 조건
    -   구 테이블이나 신 테이블의 dNumber 속성이 널 값이 아닌 터플이 존재하면 만족
    -   널 값이 아닌 dNumber 터플이 존재하면 해당 department의 totalSalary 속성 값을 변경하여야 하기 때문
-   트리거의 실행 부문
    -   전체 테이블에 대하여 일괄적으로 totalSalary 속성 값을 변경

## Comments on Triggers (1/2)

-   트리거는 속성의 통계 정보를 유지하거나 또는 임의 테이블의 복사본을 유지할 때 많이 사용
-   현대 데이터베이스
    -   통계 데이터를 관리하기에 편리한 실체화된(materialized) 뷰 기능을 제공
    -   테이블 복제를 지원하는 replication 기능을 제공

## Comments on Triggers (2/2)

-   객체 관계형 또는 객체지향 데이터베이스 시스템
    -   데이터에 대한 연산을 메소드 방식으로 지원
    -   데이터에 대한 연산을 꼭 트리거를 사용하여 구현하지 않아도 됨
-   데이터 변화가 발생되면 원하지 않은 트리거를 수행하는 경우가 많음

# 6.4 : Authorization

## Overview on Authorization

-   사용자는 데이터베이스 연산을 하려면 연산에 필요한 권한을 가지고 있어야 함
    -   권한이 없는 연산 → 시스템에 의하여 수행이 거부됨
-   DBA는 모든 권한을 가짐
    -   특정 사용자에게 특정 권한을 부여할 수 있음

## Authorization

-   데이터베이스 인스턴스에 대한 권한
    -   읽기 권한
    -   입력 권한
    -   갱신 권한
    -   삭제 권한
-   데이터베이스 스키마에 대한 권한
    -   색인 생성/삭제 권한
    -   테이블 생성 권한
    -   테이블 속성 변경 권한
    -   테이블 삭제 권한

## Privileges in SQL

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/3a47928c-48ea-4463-a746-c5718d9b36c4/image.png)

-   References 권한
    -   테이블 생성시에 외래 키를 선언할 수 있는 권한
        -   외래 키 선언 → 단순히 해당 테이블에만 영향을 미치지 않음
            -   참조되는 테이블(referenced table)의 주 키(primary key) 값의 생성/삭제/변경에 영향을 미침
            -   외래 키가 참조하는 테이블의 주 키 값은 입력/삭제/변경시에 참조 무결성에 의한 여러 제약이 존재함

## Grant Statements

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ca10b897-e853-4b35-8ab7-314c5124a87a/image.png)

-   Grant 문장
    -   권한을 부여하는 기능
    -   <user list>
          - 사용자 아이디의 나열이나 role을 사용하여도 됨
          - public은 키워드로서 모든 사용자를 의미함
-   Grant 문장에 “with grant option”을 사용
    -   권한을 받는 사용자가 부여 받은 권한을 다른 사용자에게 부여할 수 있음

## Grant Statement Examples

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/7f409e35-c2f5-4f48-8684-5aa89fb0afbb/image.png)

-   첫 번째 문장
    -   사용자 U1, U2, U3에게 professor 테이블에 대한 select 문장을 사용할 수 있는 권한을 부여함
-   두 번째 문장
    -   사용자 U4에게 professor 테이블에 대한 select 문장을 사용할 수 있는 권한을 부여
    -   U4에게 받은 권한을 다른 사용자에게 부여할 수 있는 권한을 함께 부여
-   세 번째 문장
    -   Lee 사용자에게 department 테이블의 deptName 속성을 참조하는 외래 키를 생성하는 권한을 부여함
        -   즉, Lee 사용자는 본인 소유의 테이블에서 department(deptName)을 참조할 수 있음
        -   이러한 권한이 필요한 이유
            -   참조 무결성 제약이 형성 → department(deptName) 속성값 변경에 제한을 받기 때문

## Revoke Statements (1/3)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d95247fe-4a9b-40cb-b942-7410f854e70c/image.png)

-   Revoke 문장
    -   부여한 권한을 철회하는 기능
-   사용자 U1, U2가 동일 권한을 사용자 U3에게 각각 부여할 수 있음
    -   이 경우 사용자 U1이 권한 취소를 해도 U3는 권한을 계속 가지고 있음

## Revoke Statements (2/3)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8b79e3e6-c3fd-4dc2-a4df-f821abf16be3/image.png)

-   cascade 옵션
    -   권한 취소 시에 취소되는 권한으로 인하여 함께 취소가 되어야 하는 권한이 있으면 그 권한도 함께 취소하는 것
-   restrict 옵션
    -   취소하려는 권한으로 인하여 다른 권한이 함께 취소되어야 하는 경우에는 권한 취소 연산 자체가 수행되지 않음
    -   사용자가 본의 아니게 취소하는 권한을 방지하는 기능을 함

## Revoke Statements (3/3)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b4b4543a-67ac-4053-824e-6b062b45a767/image.png)

-   권한 취소를 받는 사용자가 public이면
    -   모든 사용자에게서 권한을 취소하는 것
    -   만약 다른 사용자로부터 동일 권한을 이미 받았으면
        -   그 권한까지 취소되지 않음
-   “grant option” 권한만으로도 취소가 가능

## Authorization Graph

-   노드는 사용자를 나타냄
-   그래프의 뿌리는 DBA(DataBase Administrator)
-   에지는 권한 부여를 나타냄
-   모든 권한은 DBA로부터 나오게 됨 → 그래프의 모든 에지는 DBA 모드로부터 접근이 가능해야 함
    -   길(path)이 있어야 함

## Authorization Graph Example 1

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d037ffc6-ac50-4a25-9842-fdbe9cf02204/image.png)

-   만약 DBA가 U2의 권한을 취소하면
    -   U2가 U3, U4에게 부여한 권한이 함께 취소되어야 함
-   권한 그래프 관점에서는
    -   U2에서 U3로 가는 에지, U2에서 U4로 가는 에지
        -   DBA 노드에서 접근이 불가능 → 두 개 에지는 제거되어야 함

## Authorization Graph Example 2

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/cfc9faaf-0d1f-46d0-8c39-d7a6ca6db51b/image.png)

-   “DBA → U7” 에지가 취소되면
    -   “U7 → U8” 및 “U8 → U7” 에지도 함께 취소되어야 함
-   DBA > Revoke select on professor from U7 restricted;
    -   restricted 옵션으로 권한 취소 연산 → 실행 오류 발생

## Authorization on Views (1/2)

-   뷰는 일반 테이블과 마찬가지로 권한 부여 대상임 → 뷰에 대한 검색/삭제/삽입/갱신 권한 등이 존재함
    -   그러나 뷰에 대한 권한은 일반 테이블 권한가 다르게 적용됨
-   뷰는 베이스 테이블의 조합으로 생성되지만
    -   기본적으로 베이스 테이블에 대한 권한과 뷰에 대한 권한은 상관이 없음
    -   예를 들어
        -   베이스 테이블에 대한 최소한 읽기 권한이 있어야 뷰 생성이 가능
        -   생성된 뷰에 대해서도 베이스 테이블에 대한 권한을 능가하는 권한을 가질 수 없음

## Authorization on Views (2/2)

-   뷰 생성자는 resource 권한이 필요 없음
    -   일반 테이블을 생성하는 것이 아니기 때문
-   일반 테이블 생성자는 그 테이블에 대한 모든 권한을 가짐
    -   뷰 생성자는 뷰에 대한 모든 권한을 가지지 못함
-   베이스 테이블에 대한 select 권한이 있어야 뷰 생성이 가능함 → 뷰 생성자는 뷰에 대한 select 권한을 가지게 됨
    -   그러나 그 이상의 권한은 베이스 테이블에 대한 권한에 의존적임
-   본인이 생성한 뷰에 대해서도 갱신 권한을 가지지 못할 수 있음
    -   뷰를 통한 갱신은 실제로는 베이스 테이블 갱신이기 때문
    -   사용자가 베이스 테이블에 갱신 권한을 이미 가지고 있으면 뷰에 대한 갱신 권한도 당연히 가짐

## View Authorization Example 1 (1/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e061e16c-8765-434a-b211-2e1ed6687f8d/image.png)

-   교수가 2015년 가을 학기에 강의하는 과목은 접근을 하고 교수 봉급을 접근하지 못하게 하려면
    -   myTeach 뷰를 생성하여 읽기 권한을 부여해주면 됨
    -   professor 테이블에 대한 권한은 부여하지 않음

## View Authorization Example 1 (2/2)

-   생성된 뷰 myTeach를 사용자에게 접근하게 함 → 교수 salary 속성을 숨기는 효과가 있음
-   데이터베이스 시스템
    -   뷰에 대한 질의가 들어오면 뷰 정의를 이용하여 뷰를 확장하게 됨
        -   이 경우 확장된 뷰는 베이스 테이블 professor, course, teaches를 가짐
-   사용자는 베이스 테이블에 대한 권한이 전혀 없음 → 뷰에 대한 접근 권한 검사는 뷰가 확장되기 전에 뷰에 대하여 수행하여야 함

## View Authorization Example 2

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/04a3bc30-a210-4f02-9c54-2460ce44b530/image.png)

-   staff가 professor 테이블에 대한 읽기 권한이 없어도 뷰에 대한 읽기 권한만 가지고 CSProfessor 뷰를 접근할 수 있음
    -   그 결과 professor 테이블을 접근하지만
-   뷰 생성자 user1이 professor 테이블에 대한 다른 권한을 가지고 있지 않아도
    -   읽기 권한만 있으면 뷰는 생성할 수 있음

## Roles

-   롤
    -   사용자의 집합
-   사용자 다수에게 동일한 권한을 부여하는 경우에
    -   다수 사용자를 동일한 롤로 정의한 후에, 롤에 권한을 부여하면,
        -   롤에 속하는 모든 사용자에게 권한이 부여됨
-   롤을 다른 롤에게 부여할 수 있음
    -   사용자를 계층적으로 관리하는 것이 가능

## Role Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ed26ae8e-a3a8-45bc-8cac-5e8e07fc20a3/image.png)

-   teller 롤을 manager 롤에게 부여하는 것
    -   teller가 가진 모든 권한을 manager에게 부여하는 것
-   teller와 manager에게 궁극적으로 사용자를 부여함 → 사용자를 계층적으로 관리하는 효과

## Limitations of SQL Authorization

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/d3dbdeee-5c30-463d-ab52-09e388fb4c71/image.png)

-   SQL 데이터베이스 시스템에서 터플 수준에서의 권한 관리는 불가능
    -   다만 갱신 연산인 경우 속성에 대한 권한 관리는 가능
-   이름, 성적 등이 기록되어 있는 학생 테이블에 대하여 특정 학생이 본인 성적만을 접근하게 하는 기능을 DBMS가 제공하지 않음
-   데이터베이스 응용은 웹 환경에서 개발이 주로 이루어짐
    -   이 경우, 데이터베이스 시스템을 접근하는 응용 프로그램이 가지는 데이터베이스 시스템 총 사용자 아이디가 하나일 수도 있음
        -   이 경우에는 데이터베이스 시스템 권한 관리를 사용하지 않고 응용 프로그램에서 사용자 관리 및 권한 관리를 수행함
-   응용 프로그램에서는 여러 형태의 데이터 접근 제어가 가능

# 6.5 : Recursive Queries

## Recursion in SQL

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/06551a47-565a-404e-b9c0-1e0fdb37d07c/image.png)

-   SQL:1999 표준은 순환 뷰를 지원함
-   prereq(x, y)
    -   과목 x를 수강하기 위하여 미리 수강하여야 하는 선수 과목이 y임을 의미
    -   prereq 테이블을 활용 → x를 수강하기 위한 선수과목을 모두 구할 수 있는 recPrereq 순환 뷰를 정의할 수 있음
-   두 번째 논리식
    -   몸통 식에 변수 z가 두 테이브를 매개함
        -   조인 연산을 의미
    -   recPrereq 테이블과 prereq 테이블을 조인하여 recPrereq 테이블을 구함
-   첫 번째 논리식
    -   recPrereq 테이블의 초기값을 주는 효과를 가짐

## Iterative Program

-   순환 뷰가 지원되지 않으면
    -   사용자는 순환 뷰의 의미를 구현하는 SQL 프로그램을 개발해야 함
-   프로그램은 기본적으로 iterative loop을 사용하여 특정 연산을 반복적으로 수행
    -   반복이 종료되는 조건을 매번 점검함

## Computation Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e12dc86c-2101-4388-9817-81dbfe50b581/image.png)

-   CS-401 과목의 선수과목을 구함
    -   점차적으로 선수과목을 구함 → 더 이상 새로운 선수과목이 생성되지 않으면 반복 연산을 종료함
-   iterative loop은 새로운 터플이 발견되지 않으면 종료할 수 있음
    -   종료 시점에는 모든 값을 구한다는 것
        -   즉, 순환 질의는 특정한 조건이 만족하면 반복 문장을 유한번 반복하여 원하는 답을 구할 수 있음

## Transitive Closure

-   transitive closure를 계산하는 방식
    -   순환을 사용하여 recPrereq 뷰에 새로운 터플을 첨가하는 것
        -   순환은 더 이상 새로운 터플이 첨가되지 않은 시점까지 계속됨
-   이러한 성질이 성립하려면
    -   순환 뷰가 단순증가 성질을 가지고 있어야 함
    -   단순증가 성질을 가지고 있지 않는 순환 뷰 - 종료 시점을 설정할 수 없음 → 순환 뷰의 fixed point를 구할 수 없음
        (∀x)(∀y) (RR(x,y) ← R(x,y))
        (∀x)(∀y)(∀z) (RR(x,y) ← ¬RR(x,z) ∧ R(z,y))

## Recursive View Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/b5d178dc-aeeb-4366-b51e-33e873b2ade0/image.png)

-   recPrereq 순환 뷰
    -   2개 속성을 가짐
    -   두 select 문장의 합(union)으로 정의
-   순환 뷰 recPrereq를 prereq 테이블의 transitive closure라고 함

## Recursive Views

-   순환 뷰 정의는 사용자에게 순환 뷰를 구하기 위하여 프로그램 개발을 하지 않게 함

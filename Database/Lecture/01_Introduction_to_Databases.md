# 1.1 : Databases

---

## DB, DBMS, DBS

---

-   DB
    -   데이터의 컬렉션
-   DBMS(Database Management System)
    -   사용자에게 데이터 관리에 필요한 기능을 제공
    -   데이터를 정의, 생성, 변경, 삭제, 접근, 조작하는 기본적인 연산 제공
    -   데이터 추상화, 데이터 독립성, 데이터 보호 기능 제공
-   DBS(Database system)
    -   DB + DBMS

## Database applications are ubiquitous!

---

-   데이터베이스 응용은 주위에 많이 있다!

## Advantages of DBMSs

---

-   데이터 추상화 제공
-   데이터 접근의 용이성 제공
    -   데이터 접근을 위한 언어를 제공
    -   편리한 사용자 인터페이스를 제공
-   데이터 중복 및 불일치성에 대한 제어 용이
    -   데이터 간에 값이 서로 일치하지 않은 현상
-   데이터 무결성 제약조건(integrity constraint) 유지 용이
    -   데이터가 만족하여야 하는 조건
    -   ex) “학생의 학점 데이터는 최소값 0.0 최대값 4.5 내의 실수 값이어야 한다”
-   갱신 원자성 제공
    -   데이터베이스 시스템에서는 데이터 갱신이 원자적으로 이루어져야 함
        -   데이터 갱신 시에 갱신 연산이 부분적으로 데이터베이스에 반영되지 않음
        -   갱신이 부분적으로 이루어지면 데이터베이스 상태가 불일치 되거나 데이터베이스 제약 조건이 만족하지 않게 될 가능성
-   다수 사용자의 동시성 제어
-   데이터 보호
-   데이터 백업 및 회복

## File Systems

---

-   운영체제의 기능 중 하나로
    -   화일 시스템(file system) 제공
        -   Unix의 “filesystem”
-   사용자에게 화일을 생성, 제거, 열고, 닫음, 읽고, 쓸 수 있는 기능을 제공
-   상세한 사용 방법은 화일 시스템마다 다름
-   데이터베이스 관리 시스템
    -   운영체제가 제공하는 화일 시스템을 활용하여 구현되는 경우가 보통
    -   운영체제가 관리하는 사용자 프로세스(process) 중 하나
-   실질적으로 사용자는 여러 가지 제약 사항으로 인하여 화일 시스템만으로는 효율적인 데이터 베이스 관리가 불가능함

# 1.2 : Data Abstraction and Data Model

---

## Instances and Schemas

---

-   스키마
    -   변수의 타입(type)
    -   데이터베이스의 논리적 또는 물리적 구조
    -   구체적으로 구조를 기술(description)하는 방법은 데이터베이스 모델에 따라서 또한 데이터베이스를 보는 높이(level)에 따라서 상이함
    -   데이터가 저장되는 공간에 대한 구조를 기술하는 면에서는 동일함
    -   시간의 흐름에 따른 변경이 적음
-   인스턴스
    -   변수의 값
    -   데이터베이스 스키마가 결정이 되면
        -   실제 데이터 값이 스키마 형태로 저장되는데
            -   데이터의 실제 값을 인스턴스라고 함
    -   시간의 흐름에 따른 변경이 잦음

## Abstraction in Computer Science

---

-   추상화
    -   어떤 사물에 대한 세세한 개체(instance)로부터 중요한 개념을 분리하는 프로세스
    -   구현상에서만 관련 있는 사항이나 문제 해결에 중요하지 않은 사항을 제거
    -   추상화 레벨에 따라 사용자에게 보이는 상세한 정도가 달라짐

## Levels of Data Abstraction

---

-   데이터베이스 시스템은 데이터베이스에 대한 추상화를 제공
-   추상화를 위한 관점(또는 높이, 레벨)
    -   물리적 레벨, 논리적 레벨, 뷰 레벨로 구성됨
-   논리적 레벨에서의 추상화
    -   데이터베이스에 저장되어 있는 데이터와 데이터간의 관계를 논리적 관점에서 추상화하는 것

## Three Level Abstraction

---

-   뷰 레벨 추상화는 사용자에게 오직 관심 있는 데이터만을 추상화함
-   동일 논리적 레벨에서의 추상화에 대하여 다수 개의 서로 다른 뷰 레벨 추상화가 가능함
-   물리적 레벨에서의 추상화
    -   실제 데이터 레코드가 어떻게 저장되는지 기술
    -   데이터 필드 길이, 필드간의 간격 길이, 레코드의 전체 길이 등을 포함함
-   동일 데이터베이스를 다른 관점에서 3가지 형태로 추상화를 하고 있으나
    -   실은 한 장소에 저장되어 있는 데이터베이스를 추상화하고 있음

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/c3a9bd91-ee13-4721-b2da-ac2d75e37545/image.png)

## Three-schema Architecture

---

-   데이터베이스에 대한 3단계에서의 추상화가 성립되면
    -   추상화에 따른 데이터베이스 스키마가 생성됨
        -   3단계 스키마 구조 만들어짐
-   각 레벨에 따른 스키마는 뷰 스키마, 논리적 스키마, 물리적 스키마
    -   각 스키마는 스키마간의 변환을 이용하여 레벨에 따른 데이터 뷰를 제공

## Data Independence

---

-   물리적 데이터 독립성
    -   논리적 스키마 변화 없이 물리적 스키마를 변화할 수 있는 기능
-   논리적 데이터 독립성
    -   뷰 스키마 변화 없이 논리적 스키마를 변화할 수 있는 기능
-   뷰 스키마
    -   최종 사용자가 보는 데이터베이스 스키마
    -   사용자는 이를 기반으로 데이터베이스 프로그램 및 응용을 개발하게 됨

## Data Model

---

-   데이터 모델
    -   데이터, 데이터 관계성, 데이터 의미, 데이터 제약 조건 등을 기술하는 명세(specification) 또는 개념적인 도구(conceptual tool)
    -   데이터 추상화를 지원하는 도구
    -   데이터 모델을 이용하여 데이터를 기술하거나 조작할 수 있음
-   데이터 모델의 종류
    -   관계형 데이터 모델, 객체지향 데이터 모델, 객체관계형 데이터 모델, 네트워크 데이터 모델, 계층 데이터 모델, 개체-관계 데이터 모델, XML 데이터 모델 등
    -   네트워크 데이터 모델 및 계층 데이터 모델은 더 이상 사용 안해서 래가시(legacy) 시스템이라고 함
-   상용 데이터베이스 관리 시스템은 상기 데이터 모델 중의 하나를 지원함
-   관계 데이터 모델
    -   관계형 데이터 모델의 기본 요소인 관계(relation)
-   객체 관계형 데이터 모델
    -   관계형 데이터 모델을 기반으로 객체지향 요소를 부분적으로 도입
    -   튜플의 속성에 중첩 관계와 같은 비원자 값을 포함한 복잡한 유형을 허용
    -   모델링 능력을 확장하면서 관계적 기반, 특히 데이터에 대한 선언적 액세스를 보존
    -   기존 관계형 언어와의 상향 호환성 제공
-   XML (Extensible Markup Language)
    -   WWW Consortium (W3C)에서 정의
    -   SGML(표준 일반화 마크업 언어)에서 파생되었지만 SGML보다 사용이 간단
    -   새로운 태그를 지정하고 중첩된 태그 구조를 생성할 수 있는 기능
        -   데이터를 교환하기 좋음
    -   데이터(document) 교환의 기술적 문제를 해결

## Database Design

---

-   데이터베이스 설계
    -   데이터베이스 구조를 설계하는 작업
    -   사용자 요구사항을 분석하여 요구사항을 충족하는 좋은 스키마를 생성하는 것
-   논리적 설계
    -   데이터베이스 스키마를 결정하는 것
        -   논리적 스키마, 뷰 스키마
-   물리적 설계
    -   데이터베이스의 레이아웃을 결정하는 것
        -   물리적 스키마
-   데이터베이스 설계는 데이터베이스 시스템 성능에 많은 영향을 줌

## Database Design Approaches

-   Entity Relationship Model
    -   enterprise의 실체와 관계의 집합으로 모델링

# 1.3 : Database Systems

---

## Database Languages

---

-   데이터베이스 관리 시스템
    -   데이터베이스에 대하여 원하는 바를 표현하기 위하여 데이터베이스 언어를 제공
-   SQL, QUEL, 관계 대수, 예제 질의(query by example) 등

## DMBS Components

---

-   데이터베이스 관리 시스템은 복잡하고 방대한 소프트웨어
-   개념적 관점에서 크게 두 가지 구성요소
    -   질의어 처리기
        -   질의어 처리, 권한 부여 및 철회, 인증 등의 기능
    -   저장 관리자
        -   데이터베이스 서버의 하단 부분을 의미
        -   데이터 저장, 검색
        -   화일 구조, 색인, 트랜잭션 관리 등의 업무를 담당

## Simplifed Database Systems

---

-   데이터베이스 관리 시스템
    -   질의어 처리기
    -   저장 관리기
        -   디스크에 존재하는 데이터베이스
        -   데이터 사전(meta data)
-   데이터베이스 시스템을 사용하는 사용자는 동시에 다수 명
-   데이터베이스 응용을 통하여 데이터베이스 관리 시스템을 접근함

## Data dictionary

---

-   데이터베이스 시스템은 사용자가 저장하여 관리하고자 하는 데이터베이스 외에도
    -   데이터베이스에 대한 데이터를 관리해야 함
-   메타 데이터(데이터에 대한 데이터)를 저장하는 장소를 데이터 사전이라고 함
-   데이터 사전에는
    -   데이터베이스 스키마에 대한 데이터
    -   제약 조건에 대한 데이터
    -   접근 권한에 대한 데이터 등

## Transaction Management

---

-   트랜잭션
    -   데이터베이스 애플리케이션에서 단일 논리적 기능을 수행하는 일련의 데이터베이스 작업
    -   동시성 제어
        -   데이터베이스의 일관성을 보장하기 위해 동시 트랜잭션 간의 상호 작용을 제어함
    -   복구 기능
        -   장애에도 불구하고 데이터베이스가 일관된(올바른) 상태를 유지하도록 보장

## Database Users

---

-   일반 사용자
    -   데이터베이스 응용을 이용하여 데이터베이스 접근/관리
    -   주어진 화면 형식에 의거하여 주어진 절차대로 데이터베이스 시스템을 사용함
-   응용 프로그래머
    -   데이터베이스 시스템에 접근하는 응용 프로그램을 개발하는 사용자
    -   이들이 개발한 데이터베이스 응용을 일반 사용자가 사용
-   데이터베이스 분석가
    -   다양한 데이터 분석 도구를 가지고 데이터베이스를 분석하는 업무를 담당함

## Database Administrator (DBA)

---

-   데이터베이스 관리자(DBA)
    -   데이터베이스에 대한 모든 권한을 가지고 있는 데이터베이스 시스템의 슈퍼 유저(superuser)
    -   데이터베이스 시스템의 모든 활동을 주관
        -   스키마 정의
        -   저장 구조 및 접근 방법 정의
        -   스키마 및 물리 구조 변경
        -   데이터베이스 접근 권한 관리
        -   제약 조건 관리
        -   시스템 성능 관리 등

## Database System Architecture

---

-   데이터베이스 시스템 구조는 데이터 위치에 의거하여
    -   중앙집중식 데이터베이스
    -   분산 데이터베이스
    -   중간 형태를 보이는 고객/서버 데이터베이스
    -   컴퓨터 병렬 처리(multi-processor) 기술을 적용한 병렬 데이터베이스

## History of Database Systems

---

-   1950s and 1960s
    -   화일 시스템을 이용하여 자료 처리
-   1970s
    -   네트워크(network) 데이터 모델과 계층 데이터 모델을 주로 사용
        -   이러한 모델을 사용하는 시스템을 legacy systems라고 함
    -   E. Codd가 관계형 데이터 모델을 제안
-   1980s
    -   80년대 초에 관계형 모델을 지원하는 상용 데이터베이스 시스템이 처음으로 출시
    -   데이터베이스 기술, 설계 기술, 트랜잭션 처리, 분산 데이터베이스에 대한 연구 및 개발이 많이 진행
    -   80년대 중후반에 객체지향 데이터베이스 시스템에 대한 개념이 정립, 이후에 관련 연구 및 개발 활발히 진행됨
-   1990s
    -   90년대 중후반에는 데이터 웨어하우스 및 데이터 마이닝 연구 개발이 활발하게 이루어짐
        -   객체 관계형 데이터 모델 정립
-   2000s
    -   XML 기술이 출현
    -   튜닝 및 자동 데이터베이스 관리 기술이 발전
        -   이를 지원하는 상용 데이터베이스 시스템이 출현함
-   2010s
    -   빅 데이터 시대
        -   이를 지원하기 위해 BigTable, Pnuts(또는 Sherpa), Hadoop(Apache)와 같은 대용량 저장 시스템 또는 대용량 분산 처리 플랫폼이 개발되어 사용
    -   NOSQL은 (No SQL 보다는) Not Only SQL을 의미
        -   전통적인 DBMS보다는 다른 형태의 데이터 관리를 요구하는 응용 분야에서 적합
        -   통상 분산 데이터 관리 및 운영, semi-structured 데이터 저장 및 관리, 고성능, 유용성(availability), 확장성(scalability)를 강조

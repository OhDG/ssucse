# 8.1 : Embedded SQL

## We need to program database applications!

-   데이터베이스 시스템 접근 방법
    -   direct SQL 방식
        -   사용자가 화면상에서 SQL 문장을 입력하면 그 결과를 화면에 보이게 하는 단순한 형태
        -   상용 데이터베이스 시스템은 direct SQL 인터페이스를 제공
    -   일반 프로그램 내에서 데이터베이스 시스템을 접근하는 형식
        -   데이터베이스 응용 환경
        -   응용 프로그램은 SQL 문장을 데이터베이스 시스템에게 보냄
        -   데이터베이스 시스템은 SQL 문장을 받아 처리함, 필요하면 그 결과를 사용자 프로그램에게 반환하는 형식

## Embedded SQL (1/2)

-   내장 SQL 프로그램
    -   호스트 언어 중간 중간에 SQL 문장을 직접 삽입하는 형식
        -   이러한 방식은 전처리(pre-processing) 과정을 꼭 거쳐야 함
        -   IBM에서 1970년대에 개발한 관계형 데이터베이스 시스템의 시제품 System R에서부터 지원하는 방식
-   전처리기
    -   내장 SQL 문장을 해당 언어 구문에 맞추어 함수 호출 형식으로 변환
        -   이 과정에서 SQL 문장에 대한 구문 검사 권한 검사, 질의 최적화 등의 작업도 진행
        -   전처리 과정이 끝나면 해당 프로그램 언어 컴파일러가 이해할 수 있는 형태로 변환됨

## Embedded SQL (2/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5bbc7d02-0f02-41e2-99bd-b2b6dd3eb003/image.png)

-   EXEC SQL BEGIN DECLARE SECTION … EXEC SQL END DECLARE SECTION
    -   호스트 프로그램과 데이터베이스 시스템 간에 데이터 할당을 위한 변수를 선언하는 곳
    -   선언된 변수는 프로그램에서 사용할 때 반드시 클론(:)을 접두사 형식으로 선행해야 함

## Cursors (1/2)

-   데이터베이스 시스템 접근 시
    -   두 언어 간에 발생하는 불일치를 해결해야 함
        -   SQL 언어는 관계를 입력으로 받아 관계를 결과물로 반환
        -   일반 프로그램 언어의 변수 및 상수에는 집합(또는 멀티셋) 타입을 지원하지 않음
            -   select 문장의 결과로 나온 관계를 일반 프로그래밍 언어 변수가 직접 받을 수 없음
-   두 언어 간에 자료 처리 방식 차이로 인한 불일치(impedance mismatch)를 해결해야 함
    -   데이터베이스 시스템은 이러한 불일치 해소를 위하여 cursor 기능을 제공
-   C++ STL(standard template library)
    -   C++에서 제공하는 표준 라이브러리
    -   container 타입으로 set, multiset 타입을 제공

## Cursors (2/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1bb4b4e8-3994-4c12-ac52-88f1890806d5/image.png)

-   커서가 선언(declare)되고, 커서 open 시에 데이터베이스 시스템이 해당 질의를 실행하여 그 결과를 임시 테이블에 저장함
-   fetch는 임시 테이블에서 터플을 하나씩 검색하여 호스트 프로그램 변수에 터플 단위로 값을 전달함
-   SQL 문장을 실행하면 SQLCA 영역에 있는 SQLSTATE 변수에 실행 성공 여부가 저장됨
    -   ‘00000’ : 성공적인 실행
    -   ‘02000’ : 더 이상 검색되는 터플이 없음
-   커서는 declare → open → fetch → close 과정을 거침
-   실제 질의문이 수행되는 시점은 커서 open 때임
-   커서 open 시에 질의문의 결과가 결정됨
-   fetch는 이 결과를 터플 단위로 접근함

## Cursor Example 1

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a16fab98-8e47-4d29-b986-894c327439e9/image.png)

-   customer 테이블에서 firstName, lastName 속성을 검색
    -   지역 변수 fname, lname에 값을 저장함
-   SQLSTATE 값이 ‘00000’이 아니면 for 루프 종료
-   지역변수 fname, lname을 사용할 때 변수 명에 콜론(colon)을 접두(prefix)하고 있음
-   int strncmp(char *string1, char *string2, int n)
    -   compares first n characters of string1 and string2
    -   returns a value
        -   0 (if string1=string2)
        -   positive (if string1 > string2)
        -   negative (if string1 < string2)

## Cursor Example 2

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5cd46656-8877-4a7f-9dae-cf0a84bc175d/image.png)

-   eInfo 커서 선언 시에 공유 변수(shared variable) c_minRating을 사용
    -   c_minRating 변수
        -   placeholder 역할
        -   커서 선언 시에 값이 결정됨
    -   placeholder는 동일 질의문을 변수 값을 변화시키면서 반복적으로 수행할 때 편리성을 제공
-   c_minRating 변수 값을 random() 함수를 호출하여 설정
-   myEmployee 테이블에서 rating 조건을 만족하는 eName, age를 출력

## Updates Through Cursors

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1ca25329-6ed9-49b9-8d03-2a2049539f01/image.png)

-   커서를 이용하여 데이터 갱신이 가능함
-   갱신을 위한 커서
    -   커서 선언 시에 갱신 커서임을 명시해야 함

## Dynamic SQL

-   SQL 문장
    -   정적 SQL
    -   동적 SQL
-   동적 SQL
    -   프로그램 실행 시간에 SQL 문장이 생성되는 SQL
    -   SQL 문장이 프로그램에 명시적으로 저장되어 있지 않음
    -   사용자가 동적으로 SQL 문장을 생성하며 입력함
    -   동적 SQL은 질의어 수행 성능
        -   정적 SQL보다 다소 뒤처짐
    -   사용자에게 질의문 작성에 대한 융통성(flexibility)을 제공
-   정적 SQL
    -   프로그램 실행 시간 이전에 SQL 문장이 명시됨
    -   데이터베이스 시스템이 전처리 단계(또는 컴파일 단계)에서 SQL 문장에 대한 구문 검사, 권한 검사, 질의 실행 코드 생성 등의 작업이 가능
        -   동적 SQL에 대해서는 이러한 작업이 원천적으로 불가능
-   동적 SQL 수행
    -   prepare과 execute 단계가 있음
    -   execute immediate 문장은 prepare과 execute를 동시에 수행

## Dynamic SQL Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6a07bc77-827e-450d-954a-503f40a33e62/image.png)

-   stcopy를 이용하여 동적 SQL을 생성
-   prepare
    -   SQL 문장에 대한 compile 단계임
    -   변수(placeholder) 이용이 가능함
-   my1 동적 SQL에서
    -   select 문장의 물음표 기호(?)
        -   my1 prepare 단계에서 실제 값으로 대치되는 placeholder를 의미
-   execute immediate 문장
    -   prepare와 execute 단계를 일괄적으로 수행
    -   변수 사용은 불가능
-   void stcopy(*from, *to)
    -   copies a null-terminated string from one location to another location.

# 8.2 : ODBC, JDBC

## ODBC, JDBC

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/4b3c57b2-467e-4065-a174-3075d09d71cb/image.png)

-   동적 방식의 ODBC, JDBC
    -   응용 프로그램에서 데이터베이스 시스템에 연결하여 데이터베이스 연산을 요청하고 이에 대한 결과를 받는 방식을 제공하는 API

## ODBC

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a302d816-1e1d-4857-be61-de7f241391d3/image.png)

-   ODBC
    -   90년대에 Microsoft가 발표한 이후에 지속적으로 사용되고 있는 데이터베이스 시스템을 위한 표준 API
    -   1992년에 ODBC 1.0 발표
    -   1995년에 ODBC 3.0 발표
    -   가장 최신 버전 2009년에 3.8
-   응용 프로그램은 ODBC 라이브러리와 링크하여 함께 컴파일해야 함

## ODBC 2.0 Connect Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6c2fdf24-6ca2-42f3-893b-537f429b3a2b/image.png)

-   RETCODE, HENV, HDBC 타입을 이용하여 서버 연결
-   environment handle을 할당하고, 이를 이용하여 connection handle을 할당 받은 후에, 데이터베이스 서버와 연결
-   함수 수행 결과 여부를 알려주는 return status를 저장하기 위하여 error code를 선언
-   SQLConnect 함수의 주요 매개 변수
    -   connection handle
    -   the server to which to connect
    -   user identifier
    -   password
-   SQL_NTS
    -   선행 매개 변수가 null로 끝나는 스트링(null-terminated string)임을 의미함

## ODBC 3.0 Connect Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/dff55ec7-4e18-4be9-b390-5b005fee0660/image.png)

-   ODBC 3.0 version
    -   응용 프로그램이 데이터베이스 서버에 연결하려면 세 가지 변수 영역을 할당해야 함
        -   environment handle
        -   connection handle
        -   statement handle

## ODBC Data Access

-   ODBC는 기본적으로 동적 SQL 접근 방식을 제공함
-   SQLExecDirect() 함수를 이용하여 SQL 문장을 수행한 후에
-   SQLBindCol() 함수를 이용하여 결과 속성 값을 로컬 변수와 연결한 후에
-   SQLFetch() 함수를 이용하여 터플 단위로 데이터를 받아옴

## Data Access Example

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/5195b115-b62f-47c0-896a-4dc34fc04cea/image.png)

-   ODBC를 이용하여 데이터베이스를 검색
-   SQLBindCol() 함수의 매개 변수
    -   ODBC 명령문 변수
    -   쿼리 결과에서 속성의 위치
    -   SQL에서 C로의 데이터 타입 변환
    -   변수의 주소
    -   가변 길이 데이터 타입(Character Array 등)의 최대 길이
        -   고정 길이 데이터 타입(Integer, Float 등)의 경우 최대 길이 필드는 무시됨
    -   튜플이 가져와질 때 실제 길이를 저장할 위치

## ODBC Dynamic SQL

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ec4d214c-19d3-47de-99ba-241d27d920f6/image.png)

-   SQL injection

    -   데이터 침입 및 해킹을 목적으로 SQL 코드를 악의적으로 삽입하는 기술
    -   사용자로부터 SQL 문장 일부를 동적으로 입력받아 수행하는 응용에서 발생할 수 있음

        ```sql
        	SQLstatement = "SELECT * FROM users WHERE name = '"
        		+ userName + "';";

        ```

        -   사용자가 `userName`에 `' or '1'='1`을 입력하면

            ```sql
            SELECT * FROM users WHERE name = '' or '1'='1';

            ```

            -   결과적으로 조건이 항상 참(`1=1`)이 되어 모든 사용자 정보가 노출됨

        ```sql
        SQLstatement = "SELECT * FROM userinfo WHERE id = "
        	+ a_variable + ";";
        ```

        -   사용자가 `a_variable`에 `1; DROP TABLE users`를 입력하면

            ```sql
            SELECT * FROM userinfo WHERE id = 1; DROP TABLE users;

            ```

            -   이로 인해 `users` 테이블이 삭제될 수 있음
            -   이를 방지하기 위하여 SQL 문장 끝에 semicolon 기호를 지원하지 않는 데이터베이스 시스템이 등장함

-   SQL injection은 데이터베이스 시스템의 데이터 보호 기능을 공격하는 방식 중의 하나
    -   이 경우 prepare 기능을 사용하여 SQL 문장을 미리 컴파일 작업을 하면 SQL injection 공격을 일정 수준 피할 수 있음
        -   데이터 타입 및 값 유효성 검사 등이 가능해지므로

## ODBC Metadata

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/2ee980e7-4e15-4a6c-b188-6c2d90e99fc9/image.png)

-   ODBC는 메타 데이터에 대한 접근 기능을 제공
    -   데이터베이스에 저장되어 있는 관계 및 속성 등에 대한 질의가 가능함
-   SQLTables() 함수
    -   데이터베이스에 대한 메타 데이터를 조회함
-   데이터베이스에 존재하는 테이블은 특정 schema에 속하게 됨
-   schema는 특정 catalog에 속하게 됨
-   데이터베이스에 존재하는 개체(테이블, 뷰, 무결성 제약 등등)들이 모여서 schema가 됨
-   몇 개의 schema가 모여서 catalog를 구성함

## ODBC Transactions

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/e3564d26-d8f3-417b-9f83-f774e58e8920/image.png)

-   트랜잭션의 기본 값
    -   각 SQL 문장을 트랜잭션으로 취급 → 각 SQL 문장 수행이 완료되면 트랜잭션이 commit된 것으로 처리함
    -   이러한 방식을 AutoCommit이라고 함
-   AutoCommit이 off된 상태에서는
    -   여러 개의 SQL 문장으로 트랜잭션을 구성할 수 있음
    -   이 경우에는 SQLTransact() 함수로 트랜잭션을 종료해야 함

## ODBC Conformance Levels

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a5e98de6-fa53-4484-8c20-aee6182c0f06/image.png)

-   ISO 표준안으로 제정된 Standard CLI(1995) 및 SQL/CLI(1999)
    -   ODBC를 기반으로 개발됨
    -   de facto 표준이 de jure 표준에 영향을 미치는 사례

## JDBC

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/bc533389-bc33-4b0e-a558-8cf737ea5c1d/image.png)

-   JDBC
    -   자바 언어에서 데이터베이스 서버를 연결하게 하는 API
    -   1997년 Sun Microsystems(후에 Oracle로 합병됨)가 발표함
    -   가장 최신 버전은 JDBC 4.2

## SQLJ

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/a880581e-2897-4c94-9e54-ef6c0c065668/image.png)

-   The Java embedding of SQL(SQLJ)
    -   자바 언어에서 내장 SQL 기능을 제공
-   “EXEC SQL” 대신에 #SQL 표현을 사용
-   JDBC는 데이터베이스 연결을 위한 API를 제공하지만
    -   SQLJ는 언어 확장 방식 → SQLJ 프로그램 컴파일 이전에 반드시 전처리 과정을 거쳐야 함
-   SQLJ는 90년대 후반에 IBM, Oracle, Compaq, Informix, Sybase, Sun Microsystems 등의 공동 노력으로 개발 및 표준화가 진행되었음
    -   현재 기준으로는 대부분의 상용 시스템이 지원하지 않는 사장된(fade out) 기술임

## ADO.NET

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/00acae55-c249-47af-8470-03c51441eae3/image.png)

-   ADO.NET
    -   Microsoft .NET Framework의 기본 라이브러리로 제공됨
    -   관계형 데이터베이스 시스템뿐만 아니라, SQL 언어를 지원하지 않는 비관계형 시스템에 대한 접근도 가능
-   OLE-DB(Object Linking and Embedding Database)
    -   MS가 개발함
    -   단일 방식으로 여러 가지 데이터 소스를 접근하게 하는 API
-   Entitiy Framework
    -   Microsoft .NET Framework의 구성요소
    -   ADO.NET을 위한 객체-관계 사상(object-relational mapping)을 제공

## Static vs. Dynamic Approaches

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/6523388b-a04a-44c4-83bc-38d46ef7ed17/image.png)

-   내장 SQL
    -   전처리 과정이 필요함
    -   전처리 과정에서 구문 검사, 권한 검사, 실행 계획 수립 등이 가능함 → 데이터베이스 연산이 신속하게 수행할 수 있음
    -   실행 코드 작성 시에 두 단계를 거쳐야 하는 번거로움
-   Mainframe 시대에는 내장 SQL 방식이 유행함
-   ODBC/JDBC가 발표된 이후에는 SQL API 방식이 널리 사용됨

# 8.3 : Application Architecture

## Application Programs

-   대부분의 데이터베이스 사용자는 SQL 언어를 직접 사용하여 데이터베이스를 접근하지 않음
    -   데이터베이스 응용 프로그램을 이용하여 데이터베이스 시스템을 접근함
-   데이터베이스 응용 프로그램
    -   front-end
        -   사용자 인터페이스를 담당
    -   back-end
        -   데이터베이스 시스템과의 연동을 담당
    -   middle layer
        -   비즈니스 로직(business logic)을 구현

## Application Architecture Evolution

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/1894189e-aa1b-44de-b83a-1adb85d9cc3e/image.png)

-   80년대 이전
    -   대용량(mainframe) 컴퓨터에 다량의 터미널이 동시에 접속하는 형식
    -   터미널은 자체적으로 컴퓨팅 능력(computing power)을 가지지 못함
        -   단순히 문자 데이터를 입력받고 출력하는 더미 터미널(dummy terminal)
            -   thin client
    -   모든 데이터 처리는 중앙 서버에서 이루어짐
-   80년대 중반
    -   개인용 컴퓨터 기술이 발전되고 보급됨
    -   단말기가 일정 수순의 컴퓨팅 능력을 가짐 → 클라이언트가 응용 프로그램의 일부 기능을 담당
    -   중앙집중식으로 관리되는 서버 데이터를 접근하는 클라이언트/서버 구조가 널리 사용됨
    -   클라이언트 단말기에서도 응용 프로그램 일부 기능을 담당
        -   fat client
    -   클라리언트에 특정 프로그램이 장착되어야 함
        -   이를 정기적으로 관리 및 업그레이드(upgrade)해 주어야 함
-   90년대 중반
    -   웹 기술이 탄생
    -   웹 브라우저
        -   데이터베이스 응용의 가장 대표적인 사용자 인터페이스

## Client/Server Application Deployment

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/8125c36c-ecd3-4592-9556-751c4afbab3e/image.png)

-   클라이언트/서버 모델에서 응용 프로그램을 배치하는 전략
    -   two-tier 구조 및 three-tier 구조
-   Two-tier 구조
    -   응용 프로그램이 클라이언트에 존재함 → 응용 프로그램이 변경되는 경우 많은 클라이언트에 존재하는 응용 프로그램을 변경해야 함
    -   서버는 데이터베이스만 관리함
    -   클라이언트는 ODBC/JDBC 등을 이용하여 데이터베이스에 접근함
-   Three-tier 구조
    -   응용 프로그램이 클라이언트와 서버에 분배되어 존재함
    -   서버에 존재하는 응용 프로그램은 응용에 고유한 비지니스 로직(business logic)을 담당함
    -   비지니스 로직에 변경이 있는 경우 서버에 존재하는 응용 프로그램만 수정 보완하면 됨 → 자원 배치 및 관리 측면, 보안 측면에서 우수함
    -   대규모 응용 환경이나 웹 환경에서 적합함

## The Web appeared mid 90s !!!

-   웹(world wide web)
    -   브라우저(browser)가 발표된 1990년 중반부터 널리 사용되기 시작함
    -   세상을 변화시킨 기술
-   웹의 구성 요소
    -   HTML
        -   웹 문서를 작성하는 언어
    -   HTTP
        -   웹 환경에서 사용되는 통신 규약
    -   URL
        -   자원 위치를 명시함
-   웹 브라우저
    -   데이터베이스를 접근하는 기본적인 도구
    -   클라이언트 프로그램의 분배 및 관리가 용이함
    -   최종 사용자의 인지 없이 개인 브라우저에서 실행되는 프로그램을 용이하게 관리할 수 있음

## Web Servers

-   HTML 언어의 한계성을 극복하기 위하여
    -   대부분의 브라우저는 JavaScript, Flash(Adobe)와 같은 스크립트 언어를 지원함
-   필요한 소프트웨어는 사용자 인지없이(transparently) 다운로드되고 실행할 수 있음
-   웹 브라우저
    -   사용자 인터페이스를 담당
-   웹 서버
    -   데이터베이스 로직을 구현하는 응용 프로그램을 구현 또는 구동해야 함
-   서버 사이트에서 응용을 개발하게 하는 다양한 기술
    -   Java servlet, Java Server Page(JSP), Active Server Page(ASP), 스크립트 언어(PHP, Perl, Python 등) 등
-   웹 서버와 응용 프로그램 간의 통신은 CGI 표준을 사용함

## Three-Layer Web Architecture

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/f8f22ac9-565b-433e-8ba9-42b605bca0d2/image.png)

-   웹 서버, 응용 서버, 데이터베이스 서버로 구성되는 3층 구조
-   2층 구조와 비교하여
    -   프로세스 구동 및 연동 간의 오버헤드가 다소 존재
    -   좀 더 유연한 시스템 구조가 가능함

## Two-Layer Web Architecture

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/124cf134-81e8-490d-b33c-22e1e30b05d1/image.png)

-   2층 웹 구조
    -   데이터베이스 서버는 독립적으로 운영됨
    -   웹 서버와 응용 서버가 결합된 서버 형태
    -   웹 서버가 비즈니스 로직을 담당하는 응용 프로그램 기능을 함께 수행하는 형태
    -   여러 응용 분야에서 널리 사용됨

## Cookies (1/2)

-   HTTP 프로토콜
    -   통신 연결이 유지되지 않는 connectionless 통신
-   데이터베이스 환경에서 클라이언트가 서버와 연결을 하는 경우
    -   서버와의 연결이 일정시간 동안 유지되기를 원함
        -   클라이언트는 서버에 보낸 SQL 문장에 대한 결과도 손쉽게 받을 수 있음
        -   받은 결과를 사용자에게 보이고 이에 대한 사용자의 응답에 따라 다른 SQL 문장을 서버로 손쉽게 보낼 수 있음
    -   웹 환경에서 이러한 데이터베이스 요구사항을 해결한 것이 쿠키임

## Cookies (2/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0f4ac80a-b5d8-40fc-a4a1-ce3781cda43d/image.png)

-   쿠키
    -   사용자 브라우저에 저장이 됨
    -   서버에 HTML 문서를 요청할 때 쿠키도 함께 서버에 전달됨

## Inputs in HTML

-   HTML provides formatting, hypertext link, and image display features including tables, stylesheets, etc.
-   HTML provides input features
    -   Select from a set of options
        -   Pop-up menus, radio buttons, check lists
    -   Enter values: text boxes
    -   Filled-in-inputs are sent back to the server, which do something with inputs

## Table/Form Example (1/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/ddfb16dd-69e7-401b-8c92-99d1a7090aa1/image.png)

-   table을 구성하는 태그 중에서
    -   <tr> 태그
          - table row
    -   <th> 태그
          - table header
    -   <td> 태그
          - table data
-   table 속성 border
    -   테이블을 구성하는 셀(cell) 경계 표시 여부를 결정함
-   form HTML 명세에서
    -   action 속성
        -   form 데이터를 받았을 때 데이터를 보낼 URL을 지정함
    -   method 속성
        -   입력 데이터를 서버로 보낼 방식을 지정함
            -   get method
                -   입력 받은 데이터를 URL에 첨부하여 데이터를 보냄
            -   post method
                -   HTTP 프로토콜 데이터 교환 방식을 사용 → URL에 입력 데이터가 보이지 않음

## Table/Form Example (2/2)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/80651bdc-a740-4857-9255-39299a6f9b10/0ef3d258-c3b2-4dfe-8ad7-83968f2154b2/image.png)

# Week6 - RESTful API

### REST Architecture

**REST(Representational State Transfer)**

- HTTP를 이용해 통신하는 네트워크상에서 정한 약속
- 분산 하이퍼미디어 시스템(인터넷 등)을 위한 소프트웨어 설계 형식
- 자원을 대표하는 단어 또는 식별자(Representational)로 자원의 상태(State)를 전송(Transfer)하는 방법
    
    > 자원
    > 
    > - 인터넷에서 제공하고 얻을 수 있는 모든 것
- 자원을 이름으로 구분하여 상태를 전송하는 방법


**REST 설계 조건**

1. Server - Client
    - 서버와 클라이언트가 존재해야 함
        
        > 클라이언트(Client)
        > 
        > - 서비스를 요청(request)
        > 
        > 서버(Server)
        > 
        > - 요청(request)에 응답(response)
2. Stateless
    - 클라이언트의 이전 상태를 기록하지 않음
        
        > All REST interactions are stateless.
        That is, each request contains all of the information necessary for a connector to understand the request, **independent of any requests that may have preceded it**.
        > 
        > 
        > This restriction accomplishes four functions:
        > 
        > 1) it removes any need for the connectors to retain application state between requests, thus reducing consumption of physical resources and improving scalability;
        > 
        > 2) it allows interactions to be processed in parallel without requiring that the processing mechanism understand the interaction semantics;
        > 
        > 3) it allows an intermediary to view and understand a request in isolation, which may be necessary when services are dynamically rearranged;
        > 
        > 4) it forces all of the information that might factor into the reusability of a cached response to be present in each request.
        >
        > \- Fielding, R. T. (2000). Architectural styles and the design of network-based software architectures. University of California, Irvine.
        > 
3. Cache
    - 응답을 저장하여 나중에 요청되는 상호 작용에 재사용할 수 있도록 함
4. **Uniform Interface: 일관된 인터페이스**
    1. Identification of resources
        - 리소스가 URI에 의해 식별되어야 함
            
            > URI(Uniform Resource Identifiers)
            > 
            > - 자원을 식별하는 유일한 식별자
    2. Manipulation of resources through representations
        - CRUD를 HTTP 메시지로 수행할 수 있어야 함
    3. **Self-descriptive messages**
        - **메시지 자체만으로 모든 것이 설명이 되어야 함**
        - JSON에 모든 태그가 만들어져 있지 않고, 만든 이가 정의하기 나름이라는 특성 때문에 만족하기 쉽지 않음
            
            ```json
            {
            	"title": "제목입니다",
            	"body": "내용입니다"
            }
            ```
            
    4. **Hypermedia as the engine of application state (HATEOAS)**
        - **애플리케이션의 상태는 하이퍼링크를 이용해 전이되어야 함**
        - JSON은 자원을 넘겨주고, 다음 상태를 고려하지 않다는 특성 때문에 만족하기 쉽지 않음
    5. Layered System
    6. Code-On-Demand
        - 서버가 보낸 코드를 클라이언트가 실행할 수 있어야 함
        ex) Javascript

**API(Application Program Interface)**

- 요청(request), 응답(response)로 오가는 구조화된 데이터
- 서버와 클라이언트 사이의 메신저 역할

### 5. JSON 직렬화 - Serializer

Django: form/modelform → HTML Form 생성

Django Rest Framework: Serializer / ModelSerializer → JSON 문자열 생성

Model로부터 Field 읽어옴

유효성 검사

![스크린샷 2022-06-01 오후 1.51.28.png](Week6%20-%20RESTful%20API%20efeb7b982c1549ba97f293a5825f842a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-06-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.51.28.png)
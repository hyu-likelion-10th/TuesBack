# restful api 요약

* REST : HTTP를 이용해 통신하는 네트워크상에서 정한 약속. 분산 하이퍼미디어 시스템을 위한 소프트웨어 설계 방식
  * REpresentational : 자원을 대표하는 단어 or 식별자로 
  * State Transfer : 자원의 상태를 전송하는 방법
  * -> 자원을 이름으로 구분하여 상태를 전송하는 방법

  * REST 설계 조건
    * Server-Client
    * STATELESS
    * Cache
    * Uniform Interface
    * Layered System
    * Code-On-Demand

* API
  * Application Program Interface : Request, Response로 오가는 구조화된 데이터
  * Client(식당손님) -> API(웨이터) -> Server(요리사)
  * 특정 형식에 맞게 전달

* REST API : REST 아키텍처 스타일을 따르는 API (REST 설계조건 잘 지키는 API)
  * -> HTTP(GET,POST 등)로 CRUD를 구현할 수 있는 API
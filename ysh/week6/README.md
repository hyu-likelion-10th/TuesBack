# REST, RESTful
## REST (Representational State Transfer)
- 웹(www)과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 개발 아키텍처의 한 형식
  - 자원을  이름(표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것
- **웹 사이트에 존재하는 모든 자원(사진, 영상, DB 자원 등)에 고유한 URI를 부여하고,  HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD Operation을 수행.**
- REST는 기본적으로 웹의 기존 기술과 HTTP 프로토콜을 그대로 활용하기 때문에 웹의 장점을 최대한 활용할 수 있는 아키텍처 스타일이다.

### REST 구성 요소
- 자원(Resource) - URI
  - 모든 자원(사진, 영상, DB 자원 등)은 서버에 위치하며, 고유한 URI를 갖는다.

  - Client는 URI를 이용해 자원의 상태(정보)에 대한 조작을 Server에 요청한다.

- 행위(Verb) - HTTP Method
  -  자원을 조작하기 위해 Method를 사용하는데, HTTP 프로토콜은 POST, GET, PUT, DELETE, HEAD와 같은 메소드를 제공한다.

- 표현(Representation)
  - 클라이언트가 서버로 요청을 보냈을 때 응답 자원의 상태를 의미.
  - REST에서 하나의 자원은 JSON, XML, RSS등 여러 형태의 Representaion으로 나타낼 수 있다.
  - 주로 JSON, XML 을 이용


## HTTP 대표적인 메서드
- GET : GET를 통해 해당 리소스를 조회


- POST : POST를 통해 리소스를 추가


- DELETE : DELETE를 통해 리소스를 삭제


- PUT : PUT를 통해 해당 리소스를 수정 


- PATCH : PATCH를 통해 해당 리소스의 데이터를 부분적으로 수정.
  - PATCH의 경우 모든 브라우저, 서버, 앱 어플리케이션 프레임워크에서 사용할 수 있는 것은 아님.

## REST 특징
- Server-Client(서버-클라이언트 구조)
- Stateless(무상태)
- Cacheable(캐시 처리 가능)
- Layered System(계층화)
- Code-On-Demand(optional)
- Uniform Interface(인터페이스 일관성)


## RESTful
- RESTful :  REST 아키텍처를 구현한 웹 서비스, REST 원리를 따르는 시스템을 의미

RESTful의 목적 (성능 향상 X)
- 이해하기 쉽고 사용하기 쉬운 REST API를 만드는 것
- 일관적인 컨벤션을 통한 API의 이해도 및 호환성을 높이는 것


출처
- https://velog.io/@ellyheetov/REST-API
- https://qazyj.tistory.com/303?category=923921
- https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html

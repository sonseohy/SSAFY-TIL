# 08-pjt
## 버전2 영화

### CDN 작성
- Ajax를 적용하기 위해 base template에 axios CDN 작성
```
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```

### script영역을 위한 base.html 수정
- script를 작성할 영역 지정해서 각각 상속받는 html의 script를 {% block script %}에 작성
```
<body>
  
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

  {% block script %}
  {% endblock script %}

</body>

```

### request.GET
- request.GET은 클라이언트(사용자)로부터 전달된 GET 요청의 쿼리 매개변수를 서버에서 접근할 수 있도록 해주는 객체
- 장르 필터링 기능에서 사용자가 특정 장르를 선택했을 때, 해당 장르 ID를 서버로 보내야 필터링을 할 수 있다. AJAX를 통해 장르 선택 시 genre_id를 쿼리 매개변수로 전달하고, 서버에서는 request.GET['genre_id'] 또는 request.GET.get('genre_id')로 이를 받아 필터링에 사용할 수 있다.

### genres__id
- genres__id에서 밑줄(__) 두 개는 Django ORM에서 "필드 탐색"을 위한 문법
- 이를 통해 다대다(Many-to-Many)나 외래 키(Foreign Key) 관계를 통해 연결된 모델의 특정 필드에 접근할 수 있다.
- Django ORM에서 (밑줄 두 개)는 필터링이나 필드 접근 시 관계 모델로 "연결"해주는 기능
- Movie와 Genre 모델이 ManyToManyField 관계로 연결되어 있을 때, Movie 모델에서 Genre 모델의 특정 필드에 접근할 수 있다.
# 07-pjt

### pip install
- django
- djangorestframework
- requests

### 초기 데이터
- fixtures파일 내부의 폴더에 있는 json 파일 여러개를 load할 때
```
$ python manage.py loaddata movies/actors.json movies/movies.json movies/reviews.json
```
- 각각의 파일이 위치한 경로 작성해서 load

### 모델별 기능 구현
1. actor : 단일 배우 정보 제공
- 배우 정보를 제공할 때 출연한 영화의 제목도 포함하기 위해 단일 배우를 제공하는 ActorSerializers 안에 MovieTitleserializers를 만들어 fields를 'title'만 제공하는 serializer를 movies에 담아 제공
```python
class ActorSerializers(serializers.ModelSerializer):
    class MovieTitleSerializers(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movies = MovieTitleSerializers(read_only=True, many=True)

    class Meta:
        model = Actor
        fields = '__all__'
```

2. movie : 단일 영화 정보 제공
- 단일 영화 정보 제공시 출연 배우 이름과 리뷰 목록을 포함해야 함
- 출연 배우 이름을 제공하기 위해 MovieSerializers 안에 출연 배우의 이름을 제공하는 ActorNameSerializers를 만들어 기존의 actors 데이터를 override
- 리뷰 목록을 제공하기 위해 기존에 리뷰 조회를 위해 만들었던 ReviewListSerializers를 사용해 review_set 역참조 데이터를 override
```python
class MovieSerializers(serializers.ModelSerializer):
    class ActorNameSerializers(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name', )

    actors = ActorNameSerializers(read_only=True, many=True)

    review_set = ReviewListSerializers(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'
```

3. review : 단일 리뷰 조회
- 단일 리뷰 조회시 출연 영화 제목도 포함해야 하므로 ReviewSerializers 안에 영화 제목만 제공하는 MovieTitleSerializers를 만들어 movie에 담아 조회시 제공
```python
class ReviewSerializers(serializers.ModelSerializer):
    class MovieTitleSerializers(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    
    movie = MovieTitleSerializers(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
```

### 도전 과제 : 영화 검색
- urls.py
```python
  path('movies/search/', views.movie_search),
```
- views.py
```python
@api_view(['GET'])
def movie_search(request):
    title = request.query_params.get('title', None)
    if title:
        movies = Movie.objects.filter(title__icontains=title)
    else:
        return Response({"message": "영화 제목을 입력해 주세요."}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = MovieSearchSerializers(movies, many=True)

    if not movies:  # 영화가 없을 경우
        return Response({"message": "영화가 없습니다."}, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data, status=status.HTTP_200_OK)
```
- 영화를 검색하는 get 요청이 들어왔을 때 요청의 쿼리 파라미터에서 title값을 가져온다.
  - 쿼리 파라미터는 URL의 끝에 ? 기호 뒤에 추가되는 키-값 쌍
  - query_params.get은 Django REST Framework에서 HTTP 요청의 쿼리 파라미터를 가져오는 방법 중 하나로, 이를 통해 클라이언트가 URL에 포함시킨 데이터를 쉽게 추출할 수 있다.
- title 변수가 None이 아닌 경우, 즉 사용자가 제목을 입력한 경우 filter를 통해 입력된 제목을 포함하는 영화를 데이터베이스에서 검색한다.
  - icontains는 대소문자를 구분하지 않고 특정 문자열이 필드에 포함되어 있는지를 확인한다.
- 사용자가 title을 입력하지 않은 경우, 클라이언트에게 '영화 제목을 입력해 주세요.' 메시지를 포함한 400 Bad Request 상태 코드를 반환한다.
- movies 쿼리셋을 직렬화하기 위해 MovieSearchSerializers를 사용하고, many=True로 여러 개의 영화 객체를 직렬화
- if not movies에서 영화가 없는 경우 "영화가 없습니다."라는 메시지를 포함한 404 Not Found 상태 코드를 반환한다.
- 모든 처리가 정상적으로 완료되었을 경우, 직렬화된 영화 데이터를 반환하며, 상태 코드는 200 OK로, 요청이 성공적으로 처리되었음을 나타낸다.
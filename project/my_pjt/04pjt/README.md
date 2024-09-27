# 04-pjt
# 버전2_영화

### 1. pip install : 외부 라이브러리 설치
1. django
  - Django 설치
2. ipython, django-extensions
  - QuerySetAPI를 위해 설치
  - django-extensions는 settings.py의 INSTALLED_APPS에 작성 필요함
3. pillow
  - ImageField 사용을 위해 설치
  
- 라이브러리 설치가 끝나면 패키지 목록 파일 requirements.txt 생성

### 2. 모델 생성 및 setting 수정
- 모델에 title, content, image 필드 지정
- 사용자가 업로드하는 이미지 파일 관리를 위해 setting에 MEDIA_ROOT, MEDIA_URL 설정

### 3. movies views 작성
- update의 view에서 키워드 인자 instance로 수정할지 결정
- create, update의 view에서 이미지를 받기 위해 request.FILES 작성
- delete의 view에서 POST일때 삭제 하는 것 분리
```python
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)
```

### 4. html 작성
- base.html 작성 : settings BASE_DIR / 'templates' 설정
- create.html에서 이미지도 같이 보내줘야 하므로 enctype='multipart/form-data'
- detail.html에서 이미지를 불러올 때 .url 써주기
```python
<img src="{{ movie.Movie_image.url }}" alt="moive-image" style="max-width: 300px;">
```
- if문 써줘야 이미지 없는 경우도 상세페이지 들어가기 가능
```python
{% if article.Movie_image %}
  img src="{{ movie.Movie_image.url }}" alt="moive-image">
{% endif %}
```

#### MEDIA_ROOT와 MEDIA_URL에 대한 URL 지정을 해줘야 함
- project.urls
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```


## 도전과제
### 이미지 리사이징
- Django에서 이미지를 업로드할 때 원본 이미지 대신 변경된 사이즈의 이미지를 업로드하는 방법은 주로 PIL(Pillow) 라이브러리를 사용하여 이미지를 리사이즈한 후, 그 이미지를 저장하는 방식
- 이미지를 업로드하는 뷰에서 이미지를 리사이즈하고 저장
- vews.py의 create와 update를 수정
```python
  # create
  # Pillow를 사용하여 이미지 리사이즈
  img = PilImage.open(image_file)
  img = img.resize((300, 400))  # 원하는 크기로 변경
  
  # BytesIO를 사용하여 이미지를 메모리에 저장
  img_io = io.BytesIO()
  img.save(img_io, format='JPEG')  # 원하는 포맷으로 저장
  img_file = ContentFile(img_io.getvalue(), name=image_file.name)

  # Movie 인스턴스 생성
  movie = form.save(commit=False)
  movie.image = img_file  # 리사이즈된 이미지 할당
  movie.save()  # 저장
```
```python
  # update
  # Pillow를 사용하여 이미지 리사이즈
  img = PilImage.open(image_file)
  img = img.resize((300, 300))  # 원하는 크기로 변경
  
  # BytesIO를 사용하여 이미지를 메모리에 저장
  img_io = io.BytesIO()
  img.save(img_io, format='JPEG')
  img_file = ContentFile(img_io.getvalue(), name=image_file.name)

  movie.image = img_file  # 리사이즈된 이미지 할당
```
- create와 update 함수에서 이미지 파일이 폼에 포함된 경우를 체크하고, pillow를 사용해 리사이즈 한다.
- 리사이즈된 이미지를 BytesIO 객체에 저장하고, ContentFile로 변환해 movie.image에 할당한다.
- create 함수에서는 새로운 Movie 인스턴스를 생성한 후 리사이즈된 이미지를 할당하여 저장하고, update 함수에서는 이미지가 포함된 경우에만 리사이즈된 이미지를 할당한다.

#### 이미지 리사이징 시 화질이 깨지는 문제 발생
- 화질 저하를 최소화하기 위해 리사이징 시 필터를 사용한다.
1. Pillow에서 이미지를 리사이즈할 때 사용되는 필터를 설정할 수 있는데, 기본적으로는 Image.NEAREST가 사용되며, 이 경우 화질이 떨어질 수 있다. 따라서 Image.LANCZOS를 사용하여 품질을 개선할 수 있다.
```python
img = img.resize((300, 300), PilImage.LANCZOS)  # LANCZOS 필터 사용
```
2. 이미지 저장 시 포맷을 변경하는 것도 영향을 미칠 수 있는데, JPEG 포맷으로 저장하는 경우 품질 조정이 가능하다.
```python
img.save(img_io, format='JPEG', quality=85)  # quality 값 조정
```
3. 이미지 비율을 유지하면서 크기를 조정할 수도 있다. 함수를 사용해서 이미지를 리사이즈 하는 방법도 있다.
```python
def resize_image(image, max_size=(300, 300)):
    img.thumbnail(max_size, PilImage.LANCZOS)  # 비율 유지
    return img
```
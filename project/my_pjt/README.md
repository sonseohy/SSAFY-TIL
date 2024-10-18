# 06-pjt

# 버전2_영화

### model 생성
- UserFollowings : 중개 테이블
- MovieLikeUsers : 중개 테이블

### index : 전체 영화 데이터 조회
```python
# movies.views.py
movies = Movie.objects.all().order_by('-created_at')
```
- .order_by('-created_at') : created_at 필드를 기준으로 정렬, '-'는 내림차순 정렬을 의미
- 가장 최근 생성된 영화가 먼저 나오게 된다.

### Admin site에 모델 등록
```python
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
```

###
```python
from django.shortcuts import get_object_or_404

get_object_or_404(Movie, pk=movie_pk)
```
```python
from django.views.decorators.http import require_http_methods
```

### detail : 영화 상세정보 페이지
```python
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment_form = CommentForm()
    context = {
        'movie': movie,
        'comment_form': comment_form,
    }
    return render(request, 'movies/detail.html', context)
```
- comment_form은 detail 함수에 context로 전달

### 댓글 삭제 경로
- path('<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
- movie_pk와 comment_pk 둘 다 받아오기

### 영화 좋아요 기능
1. 경로
```python
path('<int:movie_pk>/likes/', views.likes, name='likes')
```
2. views.py
- 유저가 좋아요를 누른 상태인지 아닌지 확인이 필요하다.
```python
@require_http_methods(["POST"])    
def likes(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.user in movie.like_user.all():
        # 이미 좋아요를 누른 상태이므로 좋아요 취소
        movie.like_user.remove(request.user)
    else:
        # 아직 좋아요 누르지 않은 상태
        movie.like_user.add(request.user)
    return redirect('movies:index')
```

### 로그인
1. form
- UserCreationForm을 상속받는 CustomUserCreationForm을 생성해야 한다.
```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model
```
2. views.py
- 로그인 form : from django.contrib.auth.forms import AuthenticationForm
- 로그인 진행 : from django.contrib.auth import login as auth_login
- next 경로가 있는 경우
```python
# next가 있는 경우
next_url = request.GET.get('next')
if next_url:
    return redirect(next_url)
```
3. login.html
- 현재 경로에 그대로 POST 요청을 보내면 되므로 로그인 form의 action을 비워두는것 가능

### 회원가입
- 회원가입 후 바로 로그인 되도록 설정하는 방법
```python 
if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        auth_login(request, user)
        return redirect('movies:index')
```
- 회원정보 수정 CustomUserChangeForm()의 인자 : request.POST와 instance=request.user
- 비밀번호 수정은 프로젝트 폴더의 urls에 작성
- 비밀번호 수정 form은 from django.contrib.auth.forms import  PasswordChangeForm
- 비밀번호 수정 views.py
```python
from django.contrib.auth import update_session_auth_hash

def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```
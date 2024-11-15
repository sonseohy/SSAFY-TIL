from django.shortcuts import render
from django.views.decorators.http import require_safe
from django.http.response import JsonResponse
from .models import Genre, Movie

# Create your views here.
# 전체 리뷰 목록 페이지 조회
@require_safe
def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movies/index.html', context)

# 필터링 된 영화 데이터 제공
def filter_genre(request):
    genre_id = request.GET.get('genre_id')
    if genre_id and genre_id != 'all':
        movies = list(Movie.objects.filter(genres__id=genre_id).values('title'))
    else:
        movies = list(Movie.objects.all().values('title'))
    context = {
        'movies': movies,
    }
    return JsonResponse(context)


# 영화 추천 페이지 조회
@require_safe
def recommended(request):
    pass

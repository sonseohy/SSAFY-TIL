from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.actor_list),  # 전체 배우 목록
    path('actors/<int:actor_pk>/', views.actor_detail),  # 단일 배우 정보
    path('movies/', views.movie_list),   # 전체 영화 목록
    path('movies/<int:movie_pk>/', views.movie_detail), # 단일 영화 목록
    path('reviews/', views.review_list),    # 전체 리뷰 목록
    path('reviews/<int:review_pk>/', views.review_detail),   # 단일 리뷰 조회, 수정, 삭제
    path('movies/<int:movie_pk>/reviews/', views.create_review),    # 리뷰 생성
    path('movies/search/', views.movie_search), # 영화 검색
]

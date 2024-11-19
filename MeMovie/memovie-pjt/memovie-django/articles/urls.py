from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list),                      # 전체 게시글
    path('articles/<int:article_pk>/', views.article_detail),   # 상세 게시글
]

from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    # <username>으로 앞에 자료형을 생략해서 작성하면 기본으로 str로 설정됨
    # path('<str:username>/', views.profile, name='profile') 와 같이 작성하면 밑에 다른 경로를 작성했을때 올바른 작동을 하지 못함
    # why? 밑에 있는 모든 주소 이름을 <str:username>으로 생각함
    # 따라서 앞에 profile을 붙인 것 같이 앞에 주소를 작성하거나 경로 가장 밑에 작성 
    path('profile/<str:username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]

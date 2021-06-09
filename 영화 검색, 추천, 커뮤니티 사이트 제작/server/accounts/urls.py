from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('like-movie/', views.like_movie),
    path('api-token-auth/', obtain_jwt_token),
    path('manager/', views.manager),
    path('cf/<int:movie_id>/', views.cf_algo),
    path('dummy-user/', views.dummy_user),
    path('dummy/', views.dummy), # 이 주소로 요청을 보내면 더미 데이터가 생성됩니다!

]




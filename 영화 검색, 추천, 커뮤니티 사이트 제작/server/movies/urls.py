from django.urls import path
from . import views

urlpatterns = [
    path('get_movie/', views.get_movie),
    path('print_movie/', views.print_movie),
    path('print_now_playing_movie/', views.print_now_playing_movie)
]

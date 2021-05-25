from django.urls import path 
from . import views 

app_name = 'movies'

urlpatterns = [
    path('articles/', views.article_list),
    path('<int:article_pk>/', views.article_delete),
    path('seeding/', views.seeding),
    path('movieList/', views.movie_list),
]
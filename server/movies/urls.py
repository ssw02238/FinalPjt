from django.urls import path 
from . import views 

app_name = 'movies'

urlpatterns = [
    path('<int:article_pk>/comments/', views.comments_create),
    path('comments/<int:comment_pk>/delete/', views.comments_delete),
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),

]
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.conf import settings 
# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=10)
    content = models.TextField()
    movietitle = models.CharField(max_length=50)
    movieId = models.IntegerField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MovieComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="movieComments")
    # article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # shell plus 로 몇 번째 댓글인지 보기 위해 
    def __str__(self):
        return self.content 


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True)
    release_date = models.DateField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    
        
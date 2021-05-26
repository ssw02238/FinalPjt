from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.conf import settings 
# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    # title -> weather
    weather = models.CharField(max_length=10)
    # 한줄평에 100자 제한 
    content = models.CharField(max_length=100)
    movietitle = models.CharField(max_length=50)
    movieId = models.IntegerField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True)
    release_date = models.DateField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    
        
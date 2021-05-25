from django.db import models
from rest_framework import serializers
from .models import Article, Movie


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id','title','content','rating', 'movietitle', 'movieId')


# class MovieCommentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = MovieComment
#         fields = ('id', 'content','rating',)


class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
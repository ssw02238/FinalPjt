from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('title', 'content','rating', )

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content',)


class ArticleSerializer(serializers.ModelSerializer):
    # 기존 필드 override
    # 첫번째 방법
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # # 두번째 방법

    class Meta:
        model = Article
        fields = '__all__'


from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import requests
from .serializers import ArticleListSerializer, ArticleSerializer, MovieCommentSerializer, MovieSerializer
from .models import Article, Movie

@api_view(['GET'])
def seeding(request):
    API_KEY = '80ced8591ed61ab4a22df20840478047'
    for pageNum in range(1, 10): 
        URL = f'https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=ko-KR&page={pageNum}'
        res = requests.get(URL).json()

        for movie_info in res['results']:
            if not Movie.objects.filter(id=movie_info['id']).exists():
                serializer = MovieSerializer(data=movie_info)
                if serializer.is_valid(raise_exception=True):
                    movie = serializer.save(id=movie_info['id'])
    return Response('성공적으로 가져왔습니다.')


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
def movie_list(request):
    movies = get_list_or_404(Movie)
    if request.method == 'GET':
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comments_create(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            serializer = MovieCommentSerializer(request.user.movieComments, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = MovieCommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['DELETE'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def comments_delete(request, comment_pk):
#     comment = get_object_or_404(Comment, pk=comment_pk)

#     if not request.user.comments.filter(pk=comment_pk).exists():
#         return Response({'#':'댓글 삭제 권한이 없습니다!'}, status=status.HTTP_403_FORBIDDEN)
#     if request.method == 'DELETE':
#         comment.delete()
#         return Response({'id':'삭제되었습니다'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
def article_list(request):
    articles = get_list_or_404(Article)
    if request.method == 'GET':
        # articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번 글이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
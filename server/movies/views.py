from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import CommentSerializer, ArticleListSerializer, ArticleSerializer
from .models import Comment, Article


# @api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def comments_create(request, article_pk):
#     if request.user.is_authenticated:
#         article = get_object_or_404(Article, pk=article_pk)

#         if request.method == 'GET':
#             serializer = CommentSerializer(request.article.comments, many=True)
#             return Response(serializer.data)
#         elif request.method == 'POST':
#             serializer = CommentSerializer(data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 comment = serializer.save(commit=False)
#                 comment.article = article 
#                 comment.save()
#                 return Response(comment.data, status=status.HTTP_201_CREATED)


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
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        serializer = ArticleListSerializer(request.user.todos, many=True)
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


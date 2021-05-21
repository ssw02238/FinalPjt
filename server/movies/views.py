# from django.http import response
from server.movies.serializers import CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import CommentSerializer
from .models import Comment


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comments_create(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)

        if request.method == 'GET':
            serializer = CommentSerializer(request.article.comments, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                comment = serializer.save(commit=False)
                comment.article = article 
                comment.save()
                return Response(comment.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comments_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if not request.user.comments.filter(pk=comment_pk).exists():
        return Response({'#':'댓글 삭제 권한이 없습니다!'}, status=status.HTTP_403_FORBIDDEN)
    if request.method == 'DELETE':
        comment.delete()
        return Response({'id':'삭제되었습니다'}, status=status.HTTP_204_NO_CONTENT)


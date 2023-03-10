from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Comment, Izoh
from .serializers import CommentSerializer, IzohSerializer, CommentUpdateSerializer, CommentListSerializer
from blog.models import BlogVideo


@api_view(('POST', ))
@permission_classes([IsAuthenticated])
def post_comment(request, pk):
    user = request.user

    try:
        blog = BlogVideo.objects.get(id=pk)
    except BlogVideo.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    comment = Comment(author=user, blog=blog)

    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET', ))
def comment_list(request, pk):
    blog = BlogVideo.objects.get(id=pk)
    comments = Comment.objects.filter(blog=blog)
    serializer = CommentListSerializer(comments, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('GET', ))
@permission_classes([IsAuthenticated])
def comment_list_author(request):
    account = request.user
    comment = Comment.objects.filter(author=account)
    serializer = CommentSerializer(comment, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('PUT', ))
@permission_classes([IsAuthenticated])
def comment_update(request, pk):
    account = request.user
    try:
        comment = Comment.objects.get(id=pk)
    except Comment.DoesNotExist:
        return Response({"message":"Kechirasiz bu comment mavjud emas!"}, status=status.HTTP_404_NOT_FOUND)

    if account != comment.author:
        return Response({"message":"Siz comment egasi emassiz"}, status=status.HTTP_403_FORBIDDEN)

    serializer = CommentUpdateSerializer(instance=comment, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



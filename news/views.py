from django.shortcuts import render
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from .models import News
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from .serializers import NewsSerializer, NewsListSerializer, NewsUpdateSerializer


@api_view(('GET', ))
def news_list_view(request):
    news_posts = News.objects.all()
    serializer = NewsListSerializer(news_posts, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('GET', ))
def news_detail_view(request, slug):
    try:
        news = News.objects.get(slug=slug)
    except News.DoesNotExist:
        return Response({'message': 'This News does not exist'}, status=status.HTTP_404_NOT_FOUND)

    serializer = NewsListSerializer(news)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('POST', ))
@permission_classes([IsAdminUser])
def news_post(request):
    account = request.user

    news_post = News(author=account)

    serializer = NewsSerializer(news_post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('PUT', 'DELETE'))
@permission_classes([IsAdminUser])
def news_update_delete(request, slug):
    user = request.user
    try:
        news = News.objects.get(slug=slug)
    except News.DoesNotExist:
        return Response({'message':'Bu yangilik mavjud emas'}, status=status.HTTP_404_NOT_FOUND)

    if user != news.author:
        return Response({'message':'Bu yangilikni tahrirlash uchun sizga ruxsat yoq'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = NewsUpdateSerializer(instance=news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        news.delete()
        return Response({'message':"yangilik muvaffaqiyatli o'chirildi"}, status=status.HTTP_202_ACCEPTED)

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)






from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import BlogVideo
from .serializers import BlogVideoSerializer, BlogVideoListSerializer,\
    BlogVideoDetailSerializer, BlogVideoUpdateSerializer


@api_view(('GET',))
def blog_video_list_view(request):
    blog_list = BlogVideo.objects.all()
    serializer = BlogVideoListSerializer(blog_list, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('GET',))
def blog_video_detail_view(request, slug):
    try:
        blog = BlogVideo.objects.get(slug=slug)
    except BlogVideo.DoesNotExist:
        return Response({"message":"This blog does not exist!"}, status=status.HTTP_404_NOT_FOUND)

    serializer = BlogVideoDetailSerializer(blog)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('POST',))
@permission_classes([IsAuthenticated])
def blog_video_post(request):
    account = request.user

    blog_post = BlogVideo(author=account)

    serializer = BlogVideoSerializer(blog_post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('PUT', 'DELETE'))
@permission_classes([IsAuthenticated])
def blog_update_delete_view(request, slug):
    account = request.user

    try:
        blog = BlogVideo.objects.get(slug=slug)
    except BlogVideo.DoesNotExist:
        return Response({"message":"Kechirasiz bu blog mavjud emas"}, status=status.HTTP_404_NOT_FOUND)

    if account != blog.author:
        return Response({"message":"Siz bu blog egasi emassiz"}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = BlogVideoUpdateSerializer(instance=blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        blog.delete()
        return Response({"message":"Hisob muvaffaqiyatli o'chirildi"}, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(('GET', ))
@permission_classes([IsAuthenticated])
def myblog_list(request):
    user = request.user
    myblog_list = BlogVideo.objects.filter(author=user)

    serializer = BlogVideoSerializer(myblog_list, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

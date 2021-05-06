from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer
from posts.models import Post


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/post-list/',
        'Detail View': '/post-detail/<int:pk>/',
        'Create': '/post-create/',
        'Update': '/post-update/<int:pk>/',
        'Delete': '/post-delete/<int:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def postList(request):
    posts = Post.objects.all().order_by('-id')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def postDetail(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def postCreate(request):
    request.data['author'] = request.user
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def postUpdate(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def postDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()

    return Response('Item deleted successfully!')

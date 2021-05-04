from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer
from posts.models import Post


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
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



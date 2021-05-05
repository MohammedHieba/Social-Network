from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView , DeleteView, FormView
from django.urls import reverse_lazy
from django import forms
# the model
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def PostList(request):
	return render(request, 'posts/list.html')
# class PostList(ListView):
#     model = Post
#     context_object_name = 'posts'
#     template_name = 'posts/list.html'

# class PostCreate(CreateView):
#     model = Post
#     fields = ['content']
#     success_url = reverse_lazy('posts')

class PostUpdate(LoginRequiredMixin,UpdateView):
	model = Post
	fields = ['content']
	success_url = reverse_lazy('posts')



class PostDelete(LoginRequiredMixin,DeleteView):
	model = Post
	context_object_name = 'deleted_post'
	success_url = reverse_lazy('posts')
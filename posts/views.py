from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView , DeleteView, FormView
from django.urls import reverse_lazy

<<<<<<< HEAD
# the model
from .models import Post

class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/list.html'

class PostCreate(CreateView):
    model = Post
    fields = ['content']
    success_url = reverse_lazy('posts')

class PostUpdate(UpdateView):
    model = Post
    fields = ['content']
    success_url = reverse_lazy('posts')

class PostDelete(DeleteView):
    model = Post
    context_object_name = 'deleted_post'
    success_url = reverse_lazy('posts')
=======

def index(request):
    return render(request, "posts/base.html")
>>>>>>> ea6f6491797de5cb7cc18668499ceeffab633ed6

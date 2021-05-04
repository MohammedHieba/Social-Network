from django.urls import path

from .views import PostList, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', PostList.as_view() , name = 'posts'),
    path('post/create' , PostCreate.as_view() , name = 'post-create'),
    path('post/update/<int:pk>/', PostUpdate.as_view() , name = 'post-edit'),
    path('post/delete/<int:pk>/', PostDelete.as_view() , name = 'post-delete')
]
from django.urls import path
from . import views
from .views import PostUpdate,PostDelete

urlpatterns = [
    path('', views.PostList , name = 'posts'),
    # path('post/create' , PostCreate.as_view() , name = 'post-create'),
    path('post/update/<int:pk>/', PostUpdate.as_view() , name = 'post-edit'),
    path('post/delete/<int:pk>/', PostDelete.as_view() , name = 'post-delete')
]
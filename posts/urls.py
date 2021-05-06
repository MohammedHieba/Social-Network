from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, \
    CommentDeleteView, AddLike, AddDislike, AddDislikeToComment, AddLikeToComment, delete_post
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('delete/<post_id>/', views.delete_post, name='post_delete'),
    path('<post_id>/comment/delete/<comment_id>/', views.delete_comment, name='comment_delete'),
    path('<int:pk>/like', AddLike.as_view(), name='like'),
    path('<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('<int:post_pk>/comment/<int:pk>/like', AddLikeToComment.as_view(), name='likeComment'),
    path('<int:post_pk>/comment/<int:pk>/dislike', AddDislikeToComment.as_view(), name='dislikeComment'),
]
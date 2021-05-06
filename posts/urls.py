from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView, AddLike, AddDislike, AddDislikeToComment, AddLikeToComment

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('<int:pk>/like', AddLike.as_view(), name='like'),
    path('<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('<int:post_pk>/comment/<int:pk>/like', AddLikeToComment.as_view(), name='likeComment'),
    path('<int:post_pk>/comment/<int:pk>/dislike', AddDislikeToComment.as_view(), name='dislikeComment'),
]
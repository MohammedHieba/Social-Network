from django.urls import path
from . import views

urlpatterns = [
    path("friends", views.index, name="get_friends"),
    path("add_friend/<receiver_id>", views.friend_request, name="send_friend_request"),
    path("friend_requests", views.friend_requests, name="friend_requests"),
    path("accept_friend/<request_id>", views.accept_friend, name="accept_friend"),
]

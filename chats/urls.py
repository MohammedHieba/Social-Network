from django.urls import path

from chats.views import ChatsView, ChatView, chat

app_name = "Chats"
urlpatterns = [
    path('', ChatsView.as_view(), name="index"),
    path('<int:id>', ChatView.as_view(), name="show"),
    path('new', chat, name='new_chat'),
]

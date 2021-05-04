from django.urls import path, include

app_name = 'API'

urlpatterns = [
    path('posts/', include('posts.api.urls') , name = "posts"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("friends", views.index, name="accounts_index"),
    path("friendship/<receiver_id>", views.friendship, name="accounts_friendship"),
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="groups_index"),
    path('create', views.create, name="groups_create"),

]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="groups_index"),
    path('create', views.create, name="groups_create"),
    path('my_groups', views.my_groups, name="groups_my_groups"),
    path('my_members/<int:group_id>', views.my_members, name="groups_my_members"),
    path('join/<int:group_id>', views.join, name="groups_join"),

]

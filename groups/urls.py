from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="groups_index"),
    path('create', views.create, name="groups_create"),
    path('delete/<group_id>', views.delete_group, name="groups_delete"),
    path('my_groups', views.get_my_groups, name="groups_my_groups"),
    path('get_requests/<group_id>', views.get_my_requests, name="groups_get_requests"),
    path('get_members/<group_id>', views.get_my_members, name="groups_get_members"),
    path('remove_members/<int:user_id>/<int:group_id>', views.remove_members, name="groups_remove_members"),
    path('accept_request/<int:user_id>/<int:group_id>', views.accept_request, name="groups_accept_request"),
    path('join/<int:group_id>', views.join, name="groups_join"),

]

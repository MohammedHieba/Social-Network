from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="groups_index"),
    path('create', views.create, name="groups_create"),
    path('edit/<group_id>', views.edit, name="groups_edit"),
    path('show_group/<group_id>', views.show_group, name="groups_show"),
    path('delete/<group_id>', views.delete_group, name="groups_delete"),
    path('my_groups', views.get_my_groups, name="groups_my_groups"),
    path('get_requests/<group_id>', views.get_my_requests, name="groups_get_requests"),
    path('get_members/<group_id>', views.get_my_members, name="groups_get_members"),
    path('remove_members/<int:user_id>/<int:group_id>', views.remove_members, name="groups_remove_members"),
    path('cancel_request/<int:user_id>/<int:group_id>', views.cancel_request, name="groups_cancel_request"),
    path('accept_request/<int:user_id>/<int:group_id>', views.accept_request, name="groups_accept_request"),
    path('decline_request/<user_id>/<group_id>', views.decline_request, name="groups_decline_request"),
    path('join/<int:group_id>', views.join, name="groups_join"),

]

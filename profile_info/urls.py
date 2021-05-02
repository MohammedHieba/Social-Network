from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="profile_index"),
    path('edit/<int:user_id>', views.edit, name="edit"),
    path('edit/password/<int:user_id>', views.edit_pass, name="edit_pass"),
]

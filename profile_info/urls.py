from django.urls import path, include
from . import views

urlpatterns = [
    path('<user_id>', views.index, name="profile_index"),
    path('add_friend/<user_id>', views.index, name="add_friend"),
    path('edit/<int:user_id>', views.edit, name="edit"),
    path('edit/password/<int:user_id>', views.edit_pass, name="edit_pass"),
]

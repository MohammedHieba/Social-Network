from django.shortcuts import redirect

from .models import *


def create_group_request(request, form):
    user = request.user
    if form.is_valid():
        form.save()
        return redirect('groups_index')

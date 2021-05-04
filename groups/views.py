from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateGroupForm
from .utils import *


@login_required
def index(request):
    return render(request, 'groups_views/index.html')


@login_required
def create(request):
    group_form = CreateGroupForm(request.POST or None, initial={'owner': request.user})

    # create_group_request(request, group_from)
    if group_form.is_valid():
        group_form.save()
        return redirect('groups_index')
    else:
        print(group_form)
    context = {'group_from': group_form}
    return render(request, 'groups_views/create.html', {'group_from': group_form})

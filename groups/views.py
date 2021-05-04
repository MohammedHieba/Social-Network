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
    memberships = [group[0] for group in request.user.group_set.all().values_list('id')]
    groups = Group.objects.all()
    context = {'groups': groups, 'memberships': memberships, }
    return render(request, 'groups_views/index.html', context)


@login_required
def create(request):
    group_form = CreateGroupForm(request.POST or None, initial={'owner': request.user})
    if request.method == 'POST':
        group_form = CreateGroupForm(request.POST or None, files=request.FILES, initial={'owner': request.user})
        if group_form.is_valid():
            group_form.save()
            return redirect('groups_index')
        else:
            print(group_form.errors)
    context = {'group_from': group_form, }
    return render(request, 'groups_views/create.html', context)


@login_required
def join(request, group_id):
    group = Group.objects.get(id=group_id)
    user = request.user
    member = Membership(user=user, group=group)
    member.save()
    return redirect('groups_index')


@login_required
def my_groups(request):
    user = request.user
    groups = Group.objects.filter(owner=user.username)
    context = {'groups': groups, }
    return render(request, 'groups_views/my_groups.html', context)


@login_required
def my_members(request, group_id):
    pass
    user = request.user
    # my_group_id = [id[0] for id in Group.objects.filter(owner=user.username).values_list('id')]
    # my_group_id = Group.objects.filter(owner=user.username)
    # print(group_id)
    members = Membership.objects.filter(group_id=group_id)
    my_members_id = [id[0] for id in members.values_list('id')]
    print("members", members)
    type(members)
    users = User.objects.filter(pk__in=my_members_id)
    print("members", users)
    context = {'members': members, 'users': users, }
    return render(request, 'groups_views/my_members.html', context)

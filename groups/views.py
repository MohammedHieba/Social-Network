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
def get_my_groups(request):
    user = request.user
    groups = Group.objects.filter(owner=user.username)
    context = {'groups': groups, }
    return render(request, 'groups_views/my_groups.html', context)


@login_required
def get_my_requests(request, group_id):
    members = get_group_members(group_id, is_approved=0)
    context = {'members': members, 'group_id': group_id, }
    return render(request, 'groups_views/my_requests.html', context)


@login_required
def get_my_members(request, group_id):
    members = get_group_members(group_id, is_approved=1)
    context = {'members': members, 'group_id': group_id, }
    return render(request, 'groups_views/my_members.html', context)


@login_required
def accept_request(request, user_id, group_id):
    membership = Membership.objects.get(group_id=group_id, user_id=user_id)
    membership.approved = True
    membership.save()
    members = get_group_members(group_id, is_approved=0)
    return redirect('/groups/get_requests/' + str(group_id), {"members": members})


@login_required
def remove_members(request, user_id, group_id):
    membership = Membership.objects.get(group_id=group_id, user_id=user_id)
    membership.delete()
    members = get_group_members(group_id, is_approved=1)
    return redirect('/groups/get_members/' + str(group_id), {"members": members})


@login_required
def delete_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group.delete()
    return redirect('groups_index')

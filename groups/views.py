from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateGroupForm, EditGroupForm, EditGroupImageForm
from .utils import *


@login_required
def index(request):
    context = get_index_context(request)
    return render(request, 'groups_views/index.html', context)


@login_required
def show_group(request, group_id):
    group = Group.objects.get(id=group_id)
    context = {'group': group}
    return render(request, 'groups_views/show_group.html', context)


@login_required
def edit(request, group_id):
    group = Group.objects.get(id=group_id)
    group_form = EditGroupForm(request.POST or None, instance=group)
    group_image_form = EditGroupImageForm(request.POST or None, request.FILES, instance=group)
    if request.method == 'POST':
        if group_form.is_valid() and group_image_form.is_valid():
            print(group_form.cleaned_data)
            group_form.save()
            group_image_form.save()
            return redirect('groups_my_groups')
    context = {'form': group_form, 'image_form': group_image_form, 'group': group, }
    return render(request, 'groups_views/edit.html', context)


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


def decline_request(request, user_id, group_id):
    print(user_id, group_id)
    membership = Membership.objects.get(user_id=user_id, group_id=group_id)
    membership.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_members(request, user_id, group_id):
    membership = Membership.objects.get(group_id=group_id, user_id=user_id)
    membership.delete()
    members = get_group_members(group_id, is_approved=1)
    return redirect('/groups/get_members/' + str(group_id), {"members": members})


@login_required
def cancel_request(request, user_id, group_id):
    membership = Membership.objects.get(group_id=group_id, user_id=user_id)
    membership.delete()
    members = get_group_members(group_id, is_approved=1)
    return redirect('groups_index')


@login_required
def delete_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group.delete()
    return redirect('groups_index')

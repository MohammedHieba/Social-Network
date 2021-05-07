from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from posts.models import Post
from .forms import CreateGroupForm, EditGroupForm, EditGroupImageForm, PostGroupForm
from .utils import *


# return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def index(request):
    context = get_index_context(request)
    return render(request, 'groups_views/index.html', context)


@login_required
def show_group(request, group_id):
    group_post_form = PostGroupForm(request.POST or None)
    if group_post_form.is_valid():
        group_post_form.add_initial_prefix({'group': group_id})
        data = group_post_form.cleaned_data
        data['author'] = request.user
        data['group_id'] = group_id
        Post.objects.create(**data)
        return redirect('groups_show', group_id)
    group = Group.objects.get(id=group_id)
    posts = Post.objects.get_group_posts(group=group)
    context = {'group': group, 'group_post_form': group_post_form, "posts": posts}
    return render(request, 'groups_views/show_group.html', context)


@login_required
def joined_groups(request):
    context = get_joined_groups_context(request, joined_groups)
    return render(request, 'groups_views/joined_groups.html', context)


@login_required
def edit(request, group_id):
    group = Group.objects.get(id=group_id)
    group_form = EditGroupForm(request.POST or None, instance=group)
    group_image_form = EditGroupImageForm(request.POST or None, request.FILES, instance=group)
    if request.method == 'POST':
        http_referer = request.POST.get('refer')
        if group_form.is_valid() and group_image_form.is_valid():
            group_form.save()
            group_image_form.save()
            return redirect(http_referer)
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
    groups = Group.objects.filter(owner=user)
    context = {'groups': groups, 'user': user, }
    return render(request, 'groups_views/my_groups.html', context)


@login_required
def get_my_requests(request, group_id):
    members = get_group_members(group_id, is_approved=0)
    context = {'members': members, 'group_id': group_id, }
    return render(request, 'groups_views/my_requests.html', context)


@login_required
def get_my_members(request, group_id):
    members = get_group_members(group_id, is_approved=1)
    group = Group.objects.get(id=group_id)
    context = {'members': members, 'group_id': group_id, 'group': group}
    return render(request, 'groups_views/my_members.html', context)


@login_required
def accept_request(request, user_id, group_id):
    membership = Membership.objects.get(group_id=group_id, user_id=user_id)
    membership.approved = True
    membership.save()
    members = get_group_members(group_id, is_approved=0)
    return redirect('/groups/get_requests/' + str(group_id), {"members": members})


def decline_request(request, user_id, group_id):
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

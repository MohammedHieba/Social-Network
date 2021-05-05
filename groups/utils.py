from django.shortcuts import redirect

from .models import *


def create_group_request(request, form):
    user = request.user
    if form.is_valid():
        form.save()
        return redirect('groups_index')


def get_group_members(group_id, is_approved):
    members = Group.objects.get(id=group_id).members.filter(membership__approved=is_approved)
    my_members_id = [ids[0] for ids in members.values_list('id')]
    users = User.objects.filter(pk__in=my_members_id)
    return users

from django.shortcuts import redirect

from .filter import GroupsFilter
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


def get_joined_groups(user_id):
    joined_groups = Membership.objects.filter(user_id=user_id, approved=1)
    joined_groups_id = [group[0] for group in joined_groups.values_list('group_id')]
    return joined_groups_id


def get_joined_groups_context(request, joined_groups):
    user = request.user
    joined_groups_id = get_joined_groups(user.id)
    joined_groups = Group.objects.filter(id__in=joined_groups_id)
    groups = Group.objects.all()
    user_query = request.GET.get('search_name')
    my_filter = GroupsFilter(request.GET, queryset=joined_groups)
    if request.GET and user_query:
        groups = my_filter.qs
        context = {'groups': groups, "filter": my_filter, }
    else:
        context = {'groups': joined_groups,  "filter": my_filter, }
    return context


def get_index_context(request):
    user = request.user
    memberships = [group[0] for group in request.user.group_set.all().values_list('id')]
    groups = Group.objects.all().exclude(owner=user.id)
    user_query = request.GET.get('search_name')
    my_filter = GroupsFilter(request.GET, queryset=groups)
    joined_groups = Membership.objects.filter(user_id=user.id, approved=1)
    joined_groups_id = [group[0] for group in joined_groups.values_list('group_id')]
    if request.GET and user_query:
        groups = my_filter.qs
        context = {'groups': groups, 'memberships': memberships, "filter": my_filter,
                   'joined_groups_id': joined_groups_id, }
    else:
        context = {'groups': groups, 'memberships': memberships, "filter": my_filter,
                   'joined_groups_id': joined_groups_id, }
    return context

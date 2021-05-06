from accounts.models import User

from profile_info.filter import UserFilter


def get_index_context(request, user_id):
    user = User.objects.get(id=user_id)
    users = User.objects.all()
    user_query = request.GET.get('username')
    my_filter = UserFilter(request.GET, queryset=users)
    if request.GET and user_query:
        users = my_filter.qs
        context = {"user": user, "users": users, "filter": my_filter}
    else:
        context = {"user": user, "filter": my_filter}
    return context

from accounts.models import User, Friendship
from posts.models import Post

from profile_info.filter import UserFilter


def get_index_context(request, user_id):
    user = User.objects.get(id=user_id)
    friend = Friendship.objects.filter(from_user=request.user, to_user=user_id).first()
    exists = Friendship.objects.filter(from_user=request.user, to_user=user).exists()
    print("exists: ", exists)
    users = User.objects.all()
    user_query = request.GET.get('username')
    my_filter = UserFilter(request.GET, queryset=users)
    if request.GET and user_query:
        users = my_filter.qs
        context = {"user": user, "users": users, "filter": my_filter, 'friend': friend, 'exists': exists,
                   'post_list': Post.objects.get_user_posts(user)}
    else:
        context = {"user": user, "filter": my_filter, 'friend': friend, 'exists': exists,
                   'post_list': Post.objects.get_user_posts(user)}
    return context

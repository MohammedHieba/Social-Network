from django.http import HttpResponseRedirect

from .models import User, Friendship
from django.shortcuts import render, redirect


def index(request):
    friends = Friendship.objects.filter(to_user=request.user, approved=True)
    context = {'friends': friends}
    return render(request, 'accounts/index.html', context)


def friend_request(request, receiver_id):
    receiver = User.objects.get(id=receiver_id)
    if not Friendship.objects.filter(from_user=request.user, to_user=receiver).exists():
        # doesnt exists
        friendship = Friendship(from_user=request.user, to_user=receiver)
        friendship.save()
    else:
        # exists
        print("exists")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def friend_requests(request):
    requests = Friendship.objects.filter(to_user=request.user, approved=False)
    context = {'requests': requests}
    return render(request, 'accounts/requests.html', context)


def accept_friend(request, request_id):
    if Friendship.objects.filter(id=request_id).exists():
        request_to = Friendship.objects.filter(id=request_id).first()
        friendship = Friendship(from_user=request.user, to_user=request_to.from_user)
        friendship.save()
        request1 = Friendship.objects.filter(id=request_id).first()
        friendship = Friendship.objects.filter(id=friendship.id).first()
        request1.approved = True
        friendship.approved = True
        request1.save()
        friendship.save()
    return redirect('friend_requests')


def cancel_request(request, request_id, user_id):
    friendship = Friendship.objects.filter(id=request_id).first()
    friendship.delete()
    print(user_id)
    return redirect('profile_index', user_id)
    # context = {'friends': friends}
    # return render(request, 'accounts/index.html', context)

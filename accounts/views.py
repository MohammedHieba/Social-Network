from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import User, Friendship
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


# return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def index(request):
    print(request.user)
    friends = Friendship.objects.filter(to_user=request.user, approved=True)
    context = {'friends': friends}
    return render(request, 'accounts/index.html', context)


def friend_request(request, receiver_id):
    print(receiver_id)
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
        request = Friendship.objects.filter(id=request_id).first()
        request.approved = True
        request.save()
    return redirect('friend_requests')


def get_friends(request):
    user = request.user.id
    print(user)

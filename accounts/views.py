from django.contrib import messages
from django.http import HttpResponseRedirect

from accounts.models import User, Friendship
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


# return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def index(request):
    print(request.user)
    context = {}
    return render(request, 'accounts/index.html', context)


def friendship(request, receiver_id):
    print(receiver_id)
    # friendship = Friendship()
    pass


def friend_request(request):
    print(request.user.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

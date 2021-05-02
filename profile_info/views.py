from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .models import Profile


def signup(request):
    form = UserCreationForm(request.POST or None)
    profile = ProfileForm(request.POST or None)
    if form.is_valid() and profile.is_valid():
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        Profile.objects.filter(user=user).update(**profile.cleaned_data)
        if user:
            login(request, user)
            # return redirect("index")
    else:
        print(profile.errors)
        print(form.errors)
    return render(request, "registration/signup.html", {
        "form": form,
        "profile": profile,
    })

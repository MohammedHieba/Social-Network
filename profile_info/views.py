from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm, SignUpForm, EditProfileForm, EditPassForm
from .models import Profile


def signup(request):
    print("IN REGISTER")
    form = SignUpForm(request.POST or None)
    profile = ProfileForm(request.POST or None)
    if form.is_valid() and profile.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        Profile.objects.filter(user=user).update(**profile.cleaned_data)
        if user:
            login(request, user)
            return redirect("profile_index")
        else:
            print(form.errors)
    return render(request, "registration/register.html", {
        "form": form,
        "profile": profile,
    })



@login_required
def index(request):
    return render(request, 'profile_info_views/index.html', {
        "user": request.user
    })


@login_required
def edit(request, user_id):
    user = request.user
    user_form = EditProfileForm(request.POST or None, instance=user)
    if user_form.is_valid():
        user_form.save()
        login(request, user)
        return redirect('profile_index')

    return render(request, 'profile_info_views/edit.html', {
        "user_form": user_form,
        "user": user
    })


@login_required
def edit_pass(request, user_id):
    user = request.user
    pass_form = EditPassForm(request.POST or None, instance=user)
    if pass_form.is_valid():
        pass_form.save()
        login(request, user)
        return redirect('profile_index')
    return render(request, 'profile_info_views/editPass.html', {
        "form": pass_form,
        "user": user
    })

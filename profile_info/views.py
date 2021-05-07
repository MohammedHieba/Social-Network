from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ProfileForm, SignUpForm, EditProfileForm, EditPassForm, ProfileImage
from .utils import get_index_context


def signup(request):
    form = SignUpForm(request.POST or None)
    profile = ProfileForm(request.POST or None)
    if request.method == "POST":

        if form.is_valid() and profile.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile = ProfileForm(request.POST, request.FILES, instance=user.profile)
            profile.save()
            if user:
                login(request, user)
                return redirect("profile_index", user.id)
            else:
                print(form.errors)
    return render(request, "registration/signup.html", {
        "form": form,
        "profile": profile,
    })


@login_required
def index(request, user_id):
    context = get_index_context(request, user_id)
    return render(request, 'profile_info_views/index.html', context)


@login_required
def edit(request, user_id):
    user = request.user
    profile = user.profile
    user_form = EditProfileForm(request.POST or None, instance=user)
    image_form = ProfileImage(request.POST or None, files=request.FILES, instance=profile)
    if user_form.is_valid() and image_form.is_valid():
        image_form.save()
        user_form.save()
        return redirect('profile_index', user_id)
    context = {"form": user_form, "profile": image_form, "user": user}
    return render(request, 'profile_info_views/edit.html', context)


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


@login_required
def add_friend(request, user_id):
    print(user_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

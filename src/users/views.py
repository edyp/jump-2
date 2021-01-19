from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect

from .forms import SignUpForm, ProfileForm, UserForm


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    args = {'form': form}
    return render(request, '../templates/registration/signup.html', args)


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        args = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'profile.html', args)

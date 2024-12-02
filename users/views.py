# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm
from .models import Profile
from django.contrib import messages

def register(request):# view to register users using the User RegisterForm
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # Profile is created via signals
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
    return render(request, 'users/register.html', {'user_form': user_form, 'profile_form': profile_form})



@login_required# login required to access profile
def profile(request):
    # Get the logged-in user's profile
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    # Pass user and profile information to the template
    return render(request, 'profile.html', {'user': user, 'profile': profile})

@login_required
def edit_profile(request):# edit profile view
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('edit_profile')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/edit_profile.html', {'profile_form': profile_form})

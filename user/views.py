from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import Newregistration, UpdateProfile, UpdateAvatar
from django.contrib.auth.decorators import login_required

def registration(request):
    if request.method == 'POST':
        form = Newregistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Регистрация прошла успешно. Пользователь {username} зарегистрирован')
            return redirect('http://127.0.0.1:8000/login')
    else:  
        form = Newregistration()
    return render(request, 'user/regist.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')

def update_profile(request):
    if request.method == 'POST':
        update_avatar = UpdateAvatar(request.POST, request.FILES, instance=request.user.userprofile)
        update_user = UpdateProfile(request.POST, instance=request.user)
        if update_user.is_valid() and update_avatar.is_valid():
            update_user.save()
            update_avatar.save()
            
            return redirect('profile')
    else:
        update_avatar = UpdateAvatar(instance=request.user.userprofile)
        update_user = UpdateProfile(instance=request.user)

    return render(request, 'user/updateprofile.html', {'update_avatar': update_avatar, 'update_user': update_user})
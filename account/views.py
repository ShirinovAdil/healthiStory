from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def user_register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/register.html', {'form': form})
    else:
        return render(request, 'account/register.html', {'form': form})


def user_login(request):
    # Log user in
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserLoginForm(request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                messages.info(request, "Welcome!")
                return redirect('home')
            else:
                return render(request, 'account/login.html', {'form': form})
        else:
            form = UserLoginForm()
            return render(request, 'account/login.html', {'form': form})
    return redirect('home')


def user_logout(request):
    # Logout user
    if request.user.is_authenticated:
        if request.method == "POST":
            logout(request)
            return redirect('home')
    else:
        return redirect('home')
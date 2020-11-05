from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import City, District
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
            print(form.errors)
            return render(request, 'account/register.html', {'form': form})
    else:
        return render(request, 'account/register.html', {'form': form})


def user_login(request):
    # Log user in
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserLoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                print(f'{username} - {password}')
                user = authenticate(request, username=username, password=password)
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


def load_cities(request):
    cities = City.objects.filter(country=1)
    return render(request, 'account/city_dropdown_list_options.html', {'cities': cities})


def load_districts(request):
    city = request.GET.get('city')
    districts = District.objects.filter(city=city)
    return render(request, 'account/city_dropdown_list_options.html', {'districts': districts})
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserLoginForm, UserRegistrationForm
from accounts.models import User


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            c_data = form.cleaned_data
            user = authenticate(request, email=c_data['email'], password=c_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You Logged In Successfully!', 'success')
                return redirect('shop:home')
            else:
                messages.error(request, 'Email Or password Is Incorrect', 'danger')

    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'You Logged Out Successfully', 'success')
    return redirect('shop:home')


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            c_data = form.cleaned_data
            user = User.objects.create_user(c_data['email'], c_data['full_name'], c_data['password'])
            user.save()
            messages.success(request, 'Registered Successfully', 'success')
            return redirect('shop:home')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

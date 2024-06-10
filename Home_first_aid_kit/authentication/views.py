from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import AuthenticationForm, RegisterUserForm


# Create your views here.


def login_user(request):
    message = 'Введите имя пользователя и пароль для входа'
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = authenticate(request, username=name, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('main'))
            else:
                message = 'Пользователя с такими данными не существует. Попробуйте еще раз!'
                return render(request, 'authentication/login.html', {'message': message, 'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'message': message, 'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_user'))


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            form = AuthenticationForm()
            # return HttpResponseRedirect(reverse('login_user'))
            return render(request, 'authentication/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'authentication/register.html', {'form': form})

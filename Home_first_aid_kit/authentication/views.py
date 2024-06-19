from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from authentication.forms import ResetPasswordForm
from .forms import AuthenticationForm, RegisterUserForm
from django.contrib.auth.models import User


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
                message = (f'Пользователя с такими данными не существует.' 
                           f'Попробуйте еще раз!')
                return render(request, 'authentication/login.html',
                              {'message': message, 'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html',
                  {'message': message, 'form': form})


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
            return render(request, 'authentication/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request,
                  'authentication/register.html',
                  {'form': form})


def password_reset(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            user = User.objects.filter(username=username).first()
            if (User.objects.filter(username=username).exists() and
                    user.first_name == first_name and
                    user.last_name == last_name and
                    user.email == email):
                user.set_password(password)
                user.save()
                return HttpResponseRedirect(reverse('login_user'))
            else:
                return render(request,
                              'authentication/password_reset.html',
                              {'form': form, 'message': 'Такой пользователь не зарегистрирован'})
    else:
        form = ResetPasswordForm()
    return render(request, 'authentication/password_reset.html', {'form': form})

from django.http import HttpResponseRedirect
from django.shortcuts import render
from authentication.models import User
from authentication.forms import AuthenticationForm


# Create your views here.


def authentication(request):
    message = 'Введите имя пользователя и пароль для входа'
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = User.objects.filter(name=name).first()
            if user is not None and user.password == password:
                return HttpResponseRedirect('medicaments/')
            else:
                message = 'Пользователя с такими данными не существует. Попробуйте еще раз!'
                return render(request, 'authentication/login.html', {'message': message, 'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'message': message, 'form': form})

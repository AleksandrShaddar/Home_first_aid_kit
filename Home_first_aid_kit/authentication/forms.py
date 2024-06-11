from django import forms
from django.contrib.auth import get_user_model


class AuthenticationForm(forms.Form):
    name = forms.CharField(max_length=50, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Такой E-mail уже существует!')
        return email


class ResetPasswordForm(forms.Form):
    username = forms.CharField(max_length=50, label='Логин')
    first_name = forms.CharField(max_length=50, label='Имя')
    last_name = forms.CharField(max_length=50, label='Фамилия')
    email = forms.CharField(max_length=50, label='Эл. почта')
    password = forms.CharField(widget=forms.PasswordInput(), label='Новый пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password']

from django import forms


class AuthenticationForm(forms.Form):
    name = forms.CharField(max_length=50, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')

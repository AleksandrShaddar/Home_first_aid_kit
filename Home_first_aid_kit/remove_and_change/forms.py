from django import forms
import datetime


class ChangeMedicamentForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    quantity = forms.IntegerField(required=False)
    expiration_date = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}
        ), required=False
    )
    instruction = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={'class': "form-control", 'placeholder': 'Инструкция'}
        ), required=False
    )
    type_medicament = forms.CharField(max_length=100, required=False)
    category = forms.CharField(max_length=100, required=False)
    image = forms.ImageField(required=False)

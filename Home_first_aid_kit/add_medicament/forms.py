from django import forms
import datetime


class AddMedicamentForm(forms.Form):
    name = forms.CharField(max_length=100)
    quantity = forms.IntegerField()
    expiration_date = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}
        ),
    )
    instruction = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={'class': "form-control", 'placeholder': 'Инструкция'}
        ),
    )
    type_medicament = forms.CharField(max_length=100)
    category = forms.CharField(max_length=100)
    image = forms.ImageField(required=False)

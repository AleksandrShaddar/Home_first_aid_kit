from django import forms
import datetime


class AddMedicamentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Наименование')
    quantity = forms.IntegerField(label='Количество')
    expiration_date = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}
        ), label='Срок годности'
    )
    instruction = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={'class': "form-control", 'placeholder': 'Инструкция'}
        ), label='Инструкция'
    )
    type_medicament = forms.CharField(max_length=100, label='Тип')
    category = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={'class': "form-control",
                   'placeholder': 'Укажите подходящие категории'}
        ), label='Категория'
    )
    image = forms.ImageField(required=False, label='Изображение')

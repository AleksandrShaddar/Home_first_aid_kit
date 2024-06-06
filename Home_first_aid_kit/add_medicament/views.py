from django.shortcuts import render
from medicaments.models import Medicament
from add_medicament.forms import AddMedicamentForm

# Create your views here.


def add_medicament(request):
    message = 'Укажите сведения о медикаменте:'
    if request.method == 'POST':
        form = AddMedicamentForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            expiration_date = form.cleaned_data['expiration_date']
            instruction = form.cleaned_data['instruction']
            type_medicament = form.cleaned_data['type_medicament']
            category = form.cleaned_data['category']
            image = form.cleaned_data['image']
            if not Medicament.objects.filter(name=name).exists():
                medicament = Medicament(
                    name=name,
                    quantity=quantity,
                    expiration_date=expiration_date,
                    instruction=instruction,
                    type_medicament=type_medicament,
                    category=category,
                    image=image
                )
                medicament.save()
                message = 'Медикамент успешно добавлен'
                return render(request, 'add_medicament/add_medicament.html', {'message': message})
            else:
                message = 'Медикамент с таким названием уже существует'
                return render(request, 'add_medicament/add_medicament.html', {'message': message})
    else:
        form = AddMedicamentForm()
    return render(request, 'add_medicament/add_medicament.html', {'form': form, 'message': message})
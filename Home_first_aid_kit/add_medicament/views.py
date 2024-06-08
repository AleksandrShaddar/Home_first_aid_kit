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
                message = f'Медикамент "{medicament.name}" успешно добавлен!'
                return render(request, 'add_medicament/success_add.html', {'message': message})
            else:
                medicament = Medicament.objects.get(name=name)
                message = f'Медикамент "{medicament.name}" уже существует!'
                return render(request, 'add_medicament/fail_add.html', {'message': message, 'medicament': medicament})
    else:
        form = AddMedicamentForm()
    return render(request, 'add_medicament/add_medicament.html', {'form': form, 'message': message})

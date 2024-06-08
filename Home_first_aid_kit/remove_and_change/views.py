from django.shortcuts import render
from medicaments.models import Medicament
from add_medicament.forms import AddMedicamentForm


# Create your views here.


def apply_remove(request, medicament_id):
    medicament = Medicament.objects.get(id=medicament_id)
    context = {'medicament': medicament}
    return render(request, 'remove_and_change/apply_remove.html', context)


def remove_medicament(request, medicament_id):
    medicament = Medicament.objects.get(id=medicament_id)
    medicament.delete()
    context = {'message': f' {medicament.name.capitalize()} успешно удален!'}
    return render(request, 'remove_and_change/remove.html', context)


def change_medicament(request, medicament_id):
    medicament = Medicament.objects.get(id=medicament_id)
    message = 'Измените требуемые данные о медикаменте:'
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
            medicament.name = name.lower()
            medicament.quantity = quantity
            medicament.expiration_date = expiration_date
            medicament.instruction = instruction
            medicament.type_medicament = type_medicament.lower()
            medicament.category = category.lower()
            if image is not None:
                medicament.image = image
            medicament.save()
            message = f'Медикамент "{medicament.name.capitalize()}" успешно изменен!'
            return render(request,
                          'remove_and_change/success_change.html',
                          {'message': message, 'medicament': medicament})
    else:
        form = AddMedicamentForm(initial={'name': medicament.name.capitalize(),
                                          'quantity': medicament.quantity,
                                          'expiration_date': medicament.expiration_date,
                                          'instruction': medicament.instruction,
                                          'type_medicament': medicament.type_medicament.capitalize(),
                                          'category': medicament.category.capitalize()
                                          }
                                 )
    return render(request,
                  'remove_and_change/change_medicament.html',
                  {'message': message, 'medicament': medicament, 'form': form})

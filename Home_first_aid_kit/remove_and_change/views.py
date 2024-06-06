from django.shortcuts import render
from medicaments.models import Medicament

# Create your views here.


def apply_remove(request, medicament_id):
    medicament = Medicament.objects.get(id=medicament_id)
    context = {'medicament': medicament}
    return render(request, 'remove_and_change/apply_remove.html', context)


def remove_medicament(request, medicament_id):
    medicament = Medicament.objects.get(id=medicament_id)
    medicament.delete()
    context = {'message': f' {medicament.name} успешно удален!'}
    return render(request, 'remove_and_change/remove.html', context)

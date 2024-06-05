from django.shortcuts import render
from medicaments.models import Medicament

# Create your views here.


def main(request):
    medicaments = Medicament.objects.all()
    quantity = len(medicaments)
    context = {'medicaments': medicaments, 'quantity': quantity}
    return render(request, 'medicaments/index.html', context)


def detail(request, medicament_id):
    medicament = Medicament.objects.get(pk=medicament_id)
    context = {'medicament': medicament}
    return render(request, 'medicaments/detail.html', context)


def search_results(request):
    search = request.GET.get('search')
    if search is not '':
        medicaments = Medicament.objects.filter(name__icontains=search)
        context = {'medicaments': medicaments, 'search': search}
        return render(request, 'medicaments/search_results.html', context)
    return main(request)
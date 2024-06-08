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
    name = request.GET.get('name')
    type_med = request.GET.get('type')
    category = request.GET.get('category')
    if name is not None:
        medicaments = Medicament.objects.filter(name__icontains=name.lower())
        context = {'medicaments': medicaments, 'search': name, 'message': 'названию'}
        return render(request, 'medicaments/search_results.html', context)
    elif type_med is not None:
        medicaments = Medicament.objects.filter(type_medicament__icontains=type_med.lower())
        context = {'medicaments': medicaments, 'search': type_med, 'message': 'типу'}
        return render(request, 'medicaments/search_results.html', context)
    elif category is not None:
        medicaments = Medicament.objects.filter(category__icontains=category.lower())
        context = {'medicaments': medicaments, 'search': category, 'message': 'категории'}
        return render(request, 'medicaments/search_results.html', context)
    return main(request)

from django.shortcuts import render
from medicaments.models import Medicament

# Create your views here.


def main(request):
    medicaments = Medicament.objects.all()
    context = {'medicaments': medicaments}
    return render(request, 'medicaments/index.html', context)

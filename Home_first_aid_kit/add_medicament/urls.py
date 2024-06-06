from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_medicament, name='add_medicament'),
]

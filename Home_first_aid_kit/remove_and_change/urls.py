from django.urls import path
from . import views

urlpatterns = [
    path('apply_remove/<int:medicament_id>', views.apply_remove,
         name='apply_remove'),
    path('remove/<int:medicament_id>', views.remove_medicament,
         name='remove_medicament'),
    path('change/<int:medicament_id>', views.change_medicament,
         name='change_medicament'),
]

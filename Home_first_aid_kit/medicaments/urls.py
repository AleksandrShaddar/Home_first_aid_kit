from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('detail/<int:medicament_id>', views.detail, name='detail'),
    path('search_results/', views.search_results, name='search_results'),
]

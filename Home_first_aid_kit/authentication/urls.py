from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('register/', views.register, name='register'),
    path('password_reset/', views.password_reset, name='password_reset'),
]

from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home, name='home' ),
    path('privacy-policy/', views.PrivayPolicy, name='privacy-policy'), 
    path('t&c.py/', views.TandC, name='t&c'),
    path('steam_kits/', views.Steam_Kits, name='steam_kits')
] 
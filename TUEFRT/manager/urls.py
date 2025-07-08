from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('landing/', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('dashboard/<str:pk>/', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),
]


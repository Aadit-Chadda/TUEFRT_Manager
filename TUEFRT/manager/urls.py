from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('landing/', views.landing),
    path('home/', views.home),
    path('dashboard/', views.dashboard),
    path('inventory/', views.inventory),
]


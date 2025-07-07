from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def landing(request):
    return render(request, 'manager/landing.html')

def home(request):
    return render(request, 'manager/home.html')

def dashboard(request):
    return render(request, 'manager/dashboard.html')

def inventory(request):
    return render(request, 'manager/inventory.html')


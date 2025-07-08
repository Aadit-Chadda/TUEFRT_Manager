from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def landing(request):
    return render(request, 'manager/landing.html')


def home(request):
    responders = Responder.objects.all()
    total_responders = responders.count()
    context = {
        'responders': responders,
        'total_responders': total_responders
    }

    return render(request, 'manager/home.html', context)


def dashboard(request, pk):
    agent = Responder.objects.get(id=pk)
    context = {'responder': agent}

    return render(request, 'manager/dashboard.html', context)


def inventory(request):

    return render(request, 'manager/inventory.html')


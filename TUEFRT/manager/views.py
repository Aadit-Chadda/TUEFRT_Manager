from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'manager/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or Password is incorrect")

        context = {}
        return render(request, 'manager/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def landing(request):
    return render(request, 'manager/landing.html')


@login_required(login_url='login')
def home(request):
    responders = Responder.objects.all()
    total_responders = responders.count()
    context = {
        'responders': responders,
        'total_responders': total_responders
    }

    return render(request, 'manager/home.html', context)


@login_required(login_url='login')
def dashboard(request, pk):
    agent = Responder.objects.get(id=pk) # responder class

    orders = agent.order_set.all()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'responder': agent, 'orders': orders, 'myFilter': myFilter}

    return render(request, 'manager/dashboard.html', context)


@login_required(login_url='login')
def inventory(request):
    items = Inventory.objects.all()

    context = {'Item' : items}   
    return render(request, 'manager/inventory.html', context)


@login_required(login_url='login')
def createOrder(request):
    form = OrderForm()
    context = {'form': form}

    if request.method == 'POST':
        print("\nPrinting Post: ")
        print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'manager/order_form.html', context)

@login_required(login_url='login')
def editOrder(request, product_id):
    form = EditForm() # Calls EditForm in form.py
    item = Inventory.objects.get(product_id=product_id)
    context = {'form': form, 'item': item}

    # just some logic for request type.
    if request.method == 'POST':
        print("\nPrinting Post: ")
        print(request.POST)
        form = EditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'manager/edit_order.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'manager/order_form.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'manager/delete.html', context)

# Bcos this is the views this is where my business logic
# of requesting information goes??

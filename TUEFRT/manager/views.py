from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.forms import *
from .filters import *
from .decorators import unauthenticated_user, allowed_users, admin_only, authenticated_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.

@unauthenticated_user
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='responder')
                user.groups.add(group)

                Responder.objects.create(
                    user=user,
                    name=user.first_name + " " + user.last_name,
                )

                messages.success(request, 'Account was created for ' + username)

                return redirect('login')

        context = {'form': form}
        return render(request, 'manager/register.html', context)


@unauthenticated_user
def loginPage(request):
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
@allowed_users(allowed_roles=['admin', 'responder'])
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
    agent = Responder.objects.get(id=pk)  # responder class

    orders = agent.order_set.all()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'responder': agent, 'orders': orders, 'myFilter': myFilter}

    return render(request, 'manager/dashboard.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['responder'])
def userPage(request):
    orders = request.user.responder.order_set.all()

    context = {'orders': orders}
    return render(request, 'manager/user.html', context)


@login_required(login_url='login')
def accountSettings(request):
    responder = request.user.responder
    form = CustomerForm(instance=responder)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=responder)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'manager/account_settings.html', context)


@login_required(login_url='login')
def inventory(request):
    items = Inventory.objects.all()

    context = {'Item': items}
    return render(request, 'manager/inventory.html', context)


@authenticated_user
@allowed_users(['admin'])
@login_required(login_url='login')
def createOrder(request, pk):
    OrderFromSet = inlineformset_factory(Responder, Order, fields=('supplier', 'product', 'cost', 'quantity', 'status', 'note'), extra=1)
    responder = Responder.objects.get(id=pk)
    formset = OrderFromSet(queryset=Order.objects.none(), instance=responder)
    # form = OrderForm()

    if request.method == 'POST':
        # print("\nPrinting Post: ")
        # print(request.POST)
        # form = OrderForm(request.POST)
        formset = OrderFromSet(request.POST, instance=responder)
        if formset.is_valid():

            formset.save()
            return redirect('/')

    context = {'formset': formset}

    return render(request, 'manager/order_form.html', context)

@login_required(login_url='login')
def editOrder(request, product_id):
    item = Inventory.objects.get(product_id=product_id)

    # just some logic for request type.
    if request.method == 'POST':
        # request.POST is the data submitted by user.
        form = EditForm(request.POST, originalQuantity=item.quantity)
        if form.is_valid():
            # valid data dictionary. All validation handled in forms.py
            # If the user is teamlead, they should be able to also add items.
            reduce_by = form.cleaned_data['reduce_by']
            item.quantity -= reduce_by

            # create instance of UpdateHistory. Need product, responder, quantity, note.
            optional_note = form.cleaned_data['opt_note']
            #history = UpdatedInventory(product=product_id, responder=)

            item.save()

            return redirect('/inventory')
    else:
        form = EditForm()

    context = {'form': form, 'item': item}
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

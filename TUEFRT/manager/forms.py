from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"  # Include all of the Order fields in the form
        exclude = ['responder']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class CustomerForm(ModelForm):
    class Meta:
        model = Responder
        fields = "__all__"
        exclude = ['user']

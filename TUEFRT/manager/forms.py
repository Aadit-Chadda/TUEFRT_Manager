from django import forms
from django.forms import ModelForm
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'  # Include all of the Order fields in the form


import django_filters
from django import forms
from django_filters import DateFilter, CharFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(
        field_name="datetime",
        lookup_expr="gt",
        widget=forms.DateInput(
            attrs={
                'type': 'date',
            }
        )
    )
    end_date = DateFilter(
        field_name="datetime",
        lookup_expr="lt",
        widget=forms.DateInput(
            attrs={
                'type': 'date',
            }
        )
    )
    note = CharFilter(field_name="note", lookup_expr="icontains")

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['responder', "datetime"]


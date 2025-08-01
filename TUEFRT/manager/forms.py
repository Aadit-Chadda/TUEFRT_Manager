from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'  # Include all of the Order fields in the form

# NOTE: Teamlead should see history of inventory edits along with notes.
# Can't really add notes until later tho.

class EditForm(forms.Form):
    reduce_by = forms.IntegerField(min_value=1, label='Amount used')
    # opt_note will be saved within UpdatedInventory table.
    opt_note = forms.CharField(
        required=False,
        max_length=255,
        label='Optional notes',
        widget=forms.TextInput(attrs={
            'placeholder': 'Type of incident, reason, etc...',
            'class' : 'edit-inventory-note'
        })
    )
    # forms init method needs to be overrided for it to 
    # know how to handle the second argument "originalQuantity"
    # *args are just og positional arguments like request.POST and 
    # **kwargs are extra keyword arguments like originalQuantity.
    
    def __init__(self, *args, originalQuantity=None, **kwargs):
        super().__init__(*args, **kwargs) # django does normal form setup.
        self.originalQuantity = originalQuantity # saves custom value for validation.

    # clean_variable is a django naming convention for validation.
    def clean_reduce_by(self):
        reduce_by = self.cleaned_data.get('reduce_by')

        # Better python practice to use 'is not None'.
        if self.originalQuantity is not None and reduce_by > self.originalQuantity:
            raise forms.ValidationError(
                f"You can't reduce by more than the current stock ({self.originalQuantity})."
            )
        return reduce_by

    '''
    ditching ModelForm approach bcos it's too convoluted trying to reduce an item.
    It would be fine for directly changing the item instead of doing subtraction tho
    keeping here as a reference..
    class Meta:
        model = Inventory
        fields = ['quantity']

        widgets = {
            'quantity': forms.NumberInput(attrs={
                'min': 0,
                'class': 'edit-inventory-form',
                'placeholder': 'Enter quantity'
        })}

        # HELP_TEXTS: Small text that appears below the field to help users
        #help_texts = {
        #    'quantity': 'Enter the number of items in stock'
        #}

        def clean_quantity(self):
            # cleaned_data dictionary of valid data.
            quantity = self.cleaned_data['quantity']

            # making sure data isn't less than 0.
            if quantity < 0:
                raise forms.ValidationError("Quantity cannot be negative")
            return quantity
        '''
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Responder)
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(UpdatedInventory)

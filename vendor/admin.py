from django.contrib import admin

# Register your models here.
from .models import Vendors, PurchaseOrder, Historical

admin.site.register(Vendors)
admin.site.register(PurchaseOrder)
admin.site.register(Historical)
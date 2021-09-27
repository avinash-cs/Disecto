from django.contrib import admin
from .models import Invoice,LineItem,Products,Orders
# Register your models here.
admin.site.register(Invoice)
admin.site.register(LineItem)
admin.site.register(Products)
admin.site.register(Orders)

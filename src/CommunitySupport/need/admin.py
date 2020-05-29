from django.contrib import admin

from .models import Order, Donation
# Register your models here.

admin.site.register(Order)

admin.site.register(Donation)
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (
    Customer
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']
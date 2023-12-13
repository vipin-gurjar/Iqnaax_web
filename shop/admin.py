from django.contrib import admin
from .models import Steam_Product,Cart,Lab_Setup

# Register your models here.
@admin.register(Steam_Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price',
                    'product_image']
    
@admin.register(Lab_Setup)
class LabModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price',
                    'lab_image']
    
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']
    

    
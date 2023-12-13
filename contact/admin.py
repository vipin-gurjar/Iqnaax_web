from django.contrib import admin
from .models import ContactInfo,Address_Info

# Register your models here.
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'phone', 'message']
 
@admin.register(Address_Info)   
class AddressModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    
    

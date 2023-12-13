from django.contrib import admin
from .models import Gallery_Images

# Register your models here.
@admin.register(Gallery_Images)
class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'images']



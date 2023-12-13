from django.contrib import admin
from .models import We_Different,About_image_gallery,Point,Reason_to_shop,Counterup_content

    
@admin.register(We_Different)
class WeDifferentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'different_Img']
    
@admin.register(Point)
class PointModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']
    
@admin.register(About_image_gallery)
class AboutImageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'about_img_gallery']
    
@admin.register(Reason_to_shop)
class ReasonModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'medalImg']
    
@admin.register(Counterup_content)
class CounterupModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']


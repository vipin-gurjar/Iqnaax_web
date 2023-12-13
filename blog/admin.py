from django.contrib import admin
from .models import Blog_Content,Blog1_Details_conent,Blog1_Details_desc,Blog2_Details_conent,Blog2_Details_desc,Blog3_Details_conent,Latest_Post

# Register your models here.
@admin.register(Blog_Content)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'date', 'blogImg']
    
@admin.register(Blog1_Details_conent)
class BlogDetails1ModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'heading', 'blog_Detail_Img']
    
    
@admin.register(Blog1_Details_desc)
class BlogDetails1DescModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']
    
    
@admin.register(Blog2_Details_conent)
class Blog2Details1ModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'heading', 'blog2_Detail_Img']
    
    
@admin.register(Blog2_Details_desc)
class Blog2Details1DescModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'desc']
    
@admin.register(Blog3_Details_conent)
class Blog3Details1ModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'desc', 'blog3_Detail_Img']

@admin.register(Latest_Post)
class LatestPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'latest_img']
    
    

    
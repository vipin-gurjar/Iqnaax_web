from django.urls import path
from .import views

urlpatterns = [
    path('', views.Blog, name='blog' ),
    path('blog-detail/<int:blog_id>/', views.Blog_detail, name='blog-detail'),
   
] 
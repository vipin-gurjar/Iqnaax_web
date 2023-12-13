from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.shop, name='shop' ),
    path('steam/', views.filter_products, name='steam'),
    path('lab/', views.lab_product, name='lab'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('lab-product-detail/<int:pk>/', views.LabProductDetailView.as_view(), name='lab-product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('empty/', views.empty, name='empty'),
    path('cart/',views.show_cart, name='cart'),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),
    path('checkout/', views.checkout, name='checkout'),
]
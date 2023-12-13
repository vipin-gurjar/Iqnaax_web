from django.urls import path
from .import views

urlpatterns = [
    path('', views.ContactInfoView.as_view(), name='contact'),
]
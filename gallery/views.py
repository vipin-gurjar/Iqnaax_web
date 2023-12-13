from django.shortcuts import render
from .models import Gallery_Images

# Create your views here.

def Gallery(request):
    images = Gallery_Images.objects.all()
    return render(request, 'myapp/gallery.html', {'images': images})

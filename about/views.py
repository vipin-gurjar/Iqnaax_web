from django.shortcuts import render
from .models import We_Different,Point,About_image_gallery,Reason_to_shop,Counterup_content

# Create your views here.

def About(request):
    we_different = We_Different.objects.all()
    point = Point.objects.all()
    about_Img = About_image_gallery.objects.all()
    reason_shop = Reason_to_shop.objects.all()
    counterup = Counterup_content.objects.first()
    context = {'wediff': we_different, 'points':point, 'about_Imgs':about_Img, 'reason_shops':reason_shop, 'counterup':counterup}
    return render(request, 'myapp/about.html', context)

    
    



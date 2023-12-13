from django.shortcuts import render
from .models import Banner,About_Section,Vision_and_Mission,Gallery_Section,Feature,Gallery_Images,About_Content,Why_Choose_Box,Testimonial,Blog,About_Section_Images,Campus_Image,Home_about_Image

# Create your views here.
def Home(request):
    banner = Banner.objects.all()
    about_section =About_Section.objects.first()
    vision_mission = Vision_and_Mission.objects.all()
    gallery_section = Gallery_Section.objects.first()
    gallery_images = Gallery_Images.objects.all()
    campusImg = Campus_Image.objects.first()
    feature = Feature.objects.all()
    about_content = About_Content.objects.first()
    about_section_image = About_Section_Images.objects.all()
    why_choose = Why_Choose_Box.objects.all()
    testimonial = Testimonial.objects.all()
    blog = Blog.objects.all()
    images = Home_about_Image.objects.all()
 
    context = {
        'banners':banner,
        'about_section':about_section,
        'about_section_images':about_section_image,
        'vision_missions': vision_mission,
        'gallery_section': gallery_section,
        'gallery_images': gallery_images,
        'campusImgs': campusImg,
        'features':feature,
        'about_content':about_content,
        'why_choose':why_choose,
        'testimonials':testimonial,
        'blogs':blog,
        'images':images,
        
        
    }
    return render(request, 'myapp/index.html', context)


def PrivayPolicy(request):
    return render(request, 'myapp/privacyPolicy.html')

def TandC(request):
    return render(request, 'myapp/termandcond.html')

def Steam_Kits(request):
    return render(request, 'myapp/shop_steam_kits.html')











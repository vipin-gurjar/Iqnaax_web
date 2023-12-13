from django.contrib import admin
from . models import Banner,About_Section,Vision_and_Mission,Gallery_Section,Gallery_Images,Feature,About_Content,Why_Choose_Box,Testimonial,Blog,About_Section_Images,Campus_Image,Home_about_Image

# Register your models here.
@admin.register(Banner)
class HomeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'bannerImg']
    
@admin.register(About_Section)
class AboutSectionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']
    
@admin.register(Vision_and_Mission)
class Vision_and_MissionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']
    
@admin.register(Gallery_Section)
class GallerySectionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']
    
@admin.register(Gallery_Images)
class GalleryImagesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'galleryImg']

@admin.register(Campus_Image)
class CampusImagesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'campusImg']
    
    
@admin.register(Feature)
class FeatureModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'icon']
    
@admin.register(About_Content)
class AboutContentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']
    
@admin.register(Why_Choose_Box)
class WhyChooseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'count', 'title', 'desc', 'icon_img']
    
@admin.register(Testimonial)
class TestimonialModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subtitle','desc', 'testimonialImg']
    
@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'blogImg']
    
@admin.register(About_Section_Images)
class AboutImgModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'aboutImg']
    
@admin.register(Home_about_Image)
class HomeAbtImgModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'home_about_img']
    
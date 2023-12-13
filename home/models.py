from django.db import models

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    bannerImg = models.ImageField(upload_to='Banner Images')
    
    def __str__(self):
        return str(self.id)
    
class About_Section(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
class About_Section_Images(models.Model):
    aboutImg = models.ImageField(upload_to='AboutSec Images')
    
    def __str__(self):
        return str(self.id)    

    
class Vision_and_Mission(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
class Gallery_Section(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
class Gallery_Images(models.Model):
    galleryImg = models.ImageField(upload_to='Gallery_Section Images')
    
    def __str__(self):
        return str(self.id)
    
class Campus_Image(models.Model):
    campusImg = models.ImageField(upload_to='Campus_Images') 
    
class Feature(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    icon = models.ImageField(upload_to='Feature Icon')
    
    def __str__(self):
        return str(self.id)
    
class About_Content(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    
    def __str__(self):
        return str(self.id)
    
class Why_Choose_Box(models.Model):
    count = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    icon_img = models.ImageField(upload_to='Why Choose img')
 
    
    def __str__(self):
        return str(self.id)
    
class Testimonial(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    desc = models.TextField()
    testimonialImg = models.ImageField(upload_to='Testimonial Images')
    
    def __str__(self):
        return str(self.id)
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    blogImg = models.ImageField(upload_to='Blog Images')
    
    def __str__(self):
        return str(self.id)
    
class Home_about_Image(models.Model):
    home_about_img = models.ImageField(upload_to='Home_about_images')
    alt_text = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.id)
    
    
    

    

    
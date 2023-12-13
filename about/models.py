from django.db import models

# Create your models here.    
class We_Different(models.Model):
    title = models.CharField(max_length=200)
    different_Img = models.ImageField(upload_to='Different_Images')
    
    def __str__(self):
        return str(self.id)
    
    
class Point(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
    
class About_image_gallery(models.Model):
    about_img_gallery = models.ImageField(upload_to='About_image_gallery')
    
    def __str__(self):
        return str(self.id)
    
class Reason_to_shop(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    medalImg = models.ImageField(upload_to='Medal Images')
    
    def __str__(self):
        return str(self.id)
    
class Counterup_content(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
    

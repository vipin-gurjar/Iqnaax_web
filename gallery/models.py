from django.db import models

# Create your models here.
class Gallery_Images(models.Model):
    images = models.ImageField(upload_to='Gallery Images')

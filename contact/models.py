from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    message = models.TextField(max_length=250)
    
    def __str__(self):
        return str(self.id)
    
class Address_Info(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    
    def __str__(self):
        return str(self.id)
    
    
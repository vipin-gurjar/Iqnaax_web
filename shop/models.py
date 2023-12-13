from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Steam_Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    product_image = models.ImageField(upload_to='Steam Product images')

    def __str__(self):
        return str(self.title)
    
class Lab_Setup(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    lab_image = models.ImageField(upload_to='Lab images')

    def __str__(self):
        return str(self.title)    

    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Steam_Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    

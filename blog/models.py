from django.db import models

class Blog_Content(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    date = models.DateField()
    blogImg = models.ImageField(upload_to='Blog Images')
    
    def __str__(self):
        return str(self.id)
    
    
class Blog1_Details_conent(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    heading = models.TextField()
    blog_Detail_Img = models.ImageField(upload_to='Blog Detail Img')
    
    def __str__(self):
        return str(self.id)
    
class Blog1_Details_desc(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
    
class Blog2_Details_conent(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    heading = models.TextField()
    blog2_Detail_Img = models.ImageField(upload_to='Blog Detail2 Img')
    
    def __str__(self):
        return str(self.id)
    
class Blog2_Details_desc(models.Model):
    desc = models.TextField()
    
    def __str__(self):
        return str(self.id)
    

class Blog3_Details_conent(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    desc = models.TextField()
    blog3_Detail_Img = models.ImageField(upload_to='Blog Detail3 Img')

class Latest_Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    latest_img = models.ImageField(upload_to='Latest Post Images')
    
    
    


   
    
    

    

    

    

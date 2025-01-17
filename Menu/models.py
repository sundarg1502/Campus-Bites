from django.db import models
import os
import datetime 

def getFileName(instance, filename):
    if isinstance(instance,Catagory):
        folder = 'Catagory'
    elif isinstance(instance,Product):
        folder =  'Product'
    else :
        folder = 'Others'
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = "%s%s"%(date,filename)
    return os.path.join(f'images/{folder}/',new_filename)

class Catagory(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    trending = models.BooleanField(default=False)
    img = models.ImageField(upload_to=getFileName,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    quantity = models.IntegerField()
    label = models.CharField(max_length=25,null=True,blank=True)
    trending = models.BooleanField(default=False)
    img = models.ImageField(upload_to=getFileName,null=True)
    actuall_price = models.IntegerField()
    discount_price = models.DecimalField(max_digits=4,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    

class NutritionalInfo(models.Model):
    calories = models.CharField(max_length=15,null=True,blank=True)
    carbs = models.CharField(max_length=15,null=True,blank=True)
    proteins = models.CharField(max_length=15,null=True,blank=True)
    fats = models.CharField(max_length=15,null=True,blank=True)
    cholesterol = models.CharField(max_length=15,null=True,blank=True)
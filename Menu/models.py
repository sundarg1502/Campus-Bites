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
    return os.path.join(f'static/images/{folder}/',new_filename)

class Catagory(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    trending = models.BooleanField(default=False)
    img = models.ImageField(upload_to=getFileName,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class NutritionalInfo(models.Model):
    name = models.CharField(max_length=35)
    calories = models.CharField(max_length=15,null=True,blank=True)
    carbs = models.CharField(max_length=15,null=True,blank=True)
    proteins = models.CharField(max_length=15,null=True,blank=True)
    fats = models.CharField(max_length=15,null=True,blank=True)
    cholesterol = models.CharField(max_length=15,null=True,blank=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    quantity = models.IntegerField()
    label = models.CharField(max_length=25,null=True,blank=True)
    trending = models.BooleanField(default=False)
    img = models.ImageField(upload_to=getFileName,null=True)
    actuall_price = models.IntegerField()
    discount_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    nutritionalinfo = models.ForeignKey(NutritionalInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    name = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()
    status = models.BooleanField(default=False)
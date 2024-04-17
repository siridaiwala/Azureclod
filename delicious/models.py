from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.





CATEGORY_CHOICES=(
    ('V','Veg'),
    ('N','Nonveg'),
    ('D','Dessert'),
    
)

class Order(models.Model):
    food_image=models.ImageField(upload_to='delicious/')
    price = models.CharField(max_length=100,blank=True)
    offer_price = models.CharField(max_length=100,blank=True)
    des=models.TextField(max_length=2000,blank=True)
    title = models.CharField(max_length=100,blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    type = models.CharField(max_length=100,blank=True)
    
    

class Cart(models.Model):
    product = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
   

class UserDetails(models.Model):
    username=models.CharField(max_length=50)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    password1=models.CharField(max_length=100,blank=True)
    password2 = models.CharField(max_length=100,blank=True)


class FoodVlogs(models.Model):
    name = models.TextField(max_length=2000,blank=True)
    founder_image = models.ImageField(upload_to='delicious/',blank=True)
    founder_des = models.TextField(max_length=2000,blank=True)

class ExecutiveDetails(models.Model):
    ex_image = models.ImageField(upload_to='delicious/')
    ex_name = models.CharField(max_length=200,blank=True)
    ex_des = models.TextField(max_length=2000,blank=True)
    ex_designation = models.CharField(max_length=200,blank=True)

class Advertisements(models.Model):
    ad_image = models.ImageField(upload_to='delicious/')
    ad_name = models.TextField(max_length=1000,blank=True)
    ad_des = models.TextField(max_length=2000,blank=True)
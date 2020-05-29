from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length = 150)
    alias = models.CharField(max_length = 150, default="Anonymous")
    town = models.TextField(default='blank')
    address = models.TextField(default='blank')
    email = models.TextField(default='blank')
    number = models.TextField(default='blank')
    urgency = models.TextField(default='blank')
    Non_Perishable = models.TextField(default='blank')
    Perishable = models.TextField(default='Placeholder')
    terms = models.BooleanField(default=False)
    time = models.CharField(max_length=500,default='blank')
    featured = models.BooleanField(default=False)
    score = models.DecimalField(max_digits=10,decimal_places=5,default=0)
    
class Donation(models.Model):
    name = models.CharField(max_length = 150)
    town = models.TextField(default='blank')
    address = models.TextField(default='blank')
    email = models.TextField(default='blank')
    number = models.TextField(default='blank')
    donation = models.TextField(default='blank')
    terms = models.BooleanField(default=False)
    time = models.CharField(max_length=500,default='blank')
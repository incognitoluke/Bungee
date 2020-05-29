from django.db import models

# Create your models here.
class Volunteer(models.Model):
    name = models.CharField(max_length = 150)
    town = models.TextField()
    email = models.EmailField()
    number = models.TextField()
    age = models.TextField()
    terms = models.BooleanField(default=False)
    time = models.TextField(default=1)
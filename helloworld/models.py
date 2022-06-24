from django.db import models

# Create your models here.
class User_details(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

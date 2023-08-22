from django.db import models

# Create your models here.

class User(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=60)
    PhoneNumber = models.CharField(max_length=20)

class UserLogin(User):
    Password = models.CharField(max_length=100)


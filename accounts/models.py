from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserLogin(AbstractUser):
    choice = (('MALE', 'male'), ('FEMALE', 'female'))
    dob = models.DateField()
    gender = models.CharField(max_length=6, choices=choice, default='None')
    address = models.CharField(max_length=250)
    phone = models.IntegerField(default=0)
    usertype = models.CharField(max_length=10)

class ShopDetails(models.Model):
    shopname = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    contact = models.CharField(verbose_name="contact person",max_length=20)
    login = models.ForeignKey(to=UserLogin,on_delete=models.CASCADE)

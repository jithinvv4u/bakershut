from django.db import models
from accounts.models import UserLogin
# Create your models here.

class StaffDetails(models.Model):
    designation = models.CharField(max_length=20)
    salary = models.IntegerField()
    incentives = models.IntegerField(default=0)
    login = models.ForeignKey(to=UserLogin,on_delete=models.CASCADE)

class Products(models.Model):
    name = models.CharField(max_length=50)
    cost = models.FloatField()
    stock = models.IntegerField()
    description = models.CharField(max_length=100)
    mfg = models.DateField(verbose_name='manufactured date')
    image = models.FileField(upload_to='images',max_length=300)
    status = models.BooleanField(default=True)

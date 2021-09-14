from django.db import models
# Create your models here.

class OrderItems(models.Model):
    userid = models.ForeignKey(to='accounts.UserLogin',on_delete=models.CASCADE)
    productid = models.ForeignKey(to='owner.Products',on_delete=models.CASCADE)
    cost = models.FloatField()
    qty = models.IntegerField(verbose_name='quantity')
    discount = models.IntegerField(default=0)
    orderdate = models.DateField(auto_now_add=True)
    ordertype = models.CharField(max_length=10)
    status = models.BooleanField(default=0)

class Cart(models.Model):
    userid = models.ForeignKey(to='accounts.UserLogin',on_delete=models.CASCADE)
    productid = models.ForeignKey(to='owner.Products',on_delete=models.CASCADE)
    

from django.db import models
from django.urls import reverse
# Create your models here.
class Item(models.Model):
    iname=models.CharField(max_length=40)
    price=models.FloatField()
    OPTION=(('rte','Ready to Eat'),('rtd','Ready to Drink'))
    category=models.CharField(max_length=30,choices=OPTION,default='rte')
    description=models.TextField()
    pic=models.FileField(upload_to='images/')
    def get_absolute_url(self):
        return reverse('home')
class Cart(models.Model):
    pid=models.IntegerField()
    name=models.CharField(max_length=30)
    quantity=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()
    user=models.CharField(max_length=30)
    pic=models.CharField(max_length=30)


class Ordernow(models.Model):
    name=models.CharField(max_length=40)
    price=models.FloatField()
    Quantity=models.IntegerField()
    Total=models.FloatField()

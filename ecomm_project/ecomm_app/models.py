from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    mobile=models.CharField(max_length=15)
    appartment=models.CharField(max_length=50,blank=True, null=True)
    street=models.CharField(max_length=50, blank=True, null=True)
    area_choices=(('Dongareshwar Nagar','Dongareshwar Nagar'),('Palase Punarvasan','Palase Punarvasan'),('Mhasake Wasti','Mhasake Wasti'),('Datta Nagar','Datta Nagar'),('MoteWada','MoteWada'))
    area=models.CharField(max_length=50, blank=True, null=True ,choices=area_choices)
    pincode=models.CharField(max_length=10,default='412219')
    confirm_password = models.CharField(max_length=10, default="confirm")
    def __str__(self):
        return self.username
class Products(models.Model):
    product_name=models.CharField(max_length=50,verbose_name="Product Name")
    price=models.IntegerField()
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='products/')
    stock=models.IntegerField(default=0)
    cat=(('Electronics','Electronics'),('Clothes','Clothes'),('Books','Books'),('Kitchen Appliances','Kitchen Appliances'),('Home Decoration','Home Decoration'),('Makeup','Makeup'),('Mobile','Mobile'),('Hair care','Hair care'),)
    category=models.CharField(max_length=50,choices=cat)
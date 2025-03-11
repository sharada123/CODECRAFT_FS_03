from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
# Create your models here.
USEFUL_FOR_CHOICES = [
    ('Kids', 'Kids'),
    ('Women', 'Women'),
    ('Men', 'Men'),
    ('Night ware', 'Night ware'),
    ('Party ware', 'Party ware'),
    ('Novels', 'Novels'),
    ('Worksheets', 'Worksheets'),
    ('General', 'General'),
    ('Living room decoration', 'Living room decoration'),
    ('Home decor', 'Home decor'),
    ('Bathroom', 'Bathroom'),
    ('Bedroom', 'Bedroom'),
    ('Dining room', 'Dining room'),
    ('Study', 'Study'),
    ('Office', 'Office'),
    ('Garden', 'Garden'),
    ('Kitchen', 'Kitchen'),
    ('Lipstick', 'Lipstick'),
    ('Foundation', 'Foundation'),
    ('Skincare', 'Skincare'),
    ('Hair care', 'Hair care'),
    ('Fragrance', 'Fragrance'),
    ('Travel', 'Travel'),
    ('Personal care', 'Personal care'),
    ('Home care', 'Home care'),
    ('Nutrition', 'Nutrition'),
    ('Sports', 'Sports'),
    ('Pet care', 'Pet care'),
]
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
    useful_for_who = MultiSelectField(choices=USEFUL_FOR_CHOICES, blank=True,null=True)
    category=models.CharField(max_length=50,choices=cat)

class CoverImage(models.Model):
    image=models.ImageField(upload_to='cover_images/')
    def __str__(self):
        return self.image.name

class Cart(models.Model):
    uid=models.ForeignKey(CustomUser,on_delete=models.CASCADE,db_column="User")
    pid=models.ForeignKey(Products, on_delete=models.CASCADE,db_column="Product")
    quantity=models.IntegerField(default=1)
    def __str__(self):
        return f"{self.uid.username} - {self.pid.product_name}"
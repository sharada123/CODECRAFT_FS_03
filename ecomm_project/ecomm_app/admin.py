from django.contrib import admin
from .models import CustomUser,Products,CoverImage
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    class Meta:
        model = CustomUser
        list_display=['username', 'email', 'first_name', 'last_name','mobile','area']
        
class ProductsAdmin(admin.ModelAdmin):
    class Meta:
        model = Products
        list_display=['id','product_name', 'price', 'stock', 'category','image']
class CoverImageAdmin(admin.ModelAdmin):
    class Meta:
        model = CoverImage
        list_display=['id','image']
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(CoverImage,CoverImageAdmin)
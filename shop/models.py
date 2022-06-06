from datetime import datetime
from itertools import product

from django.db import models
from django.contrib.auth.models import User
import os
import datetime


def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename )
    return os.path.join('uploads/.', filename)



class Category(models.Model):
    slug = models.CharField(max_length= 100, null=False, blank=True)
    name = models.CharField(max_length=100, null=False, blank=True)
    image =models.ImageField(upload_to = get_file_path  , null=True, blank=False)
    status =models.BooleanField(default=False, help_text="0 = default ,  1= Trending ")
    description = models.TextField(max_length=400, null=False , blank=False)
    trending =models.BooleanField(default=False, help_text="0 = default ,  1= Trending ")
    meta_title = models.CharField(max_length=100, blank=False , null=False)
    meta_keywords = models.CharField(max_length=100, blank=False , null=False)
    meta_description = models.TextField(max_length=500, null= True)
    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length= 100, null=False, blank=True)
    name = models.CharField(max_length=100, null=False, blank=True)
    product_image =models.ImageField(upload_to = get_file_path  , null=True, blank=False)
    status =models.BooleanField(default=False, help_text="0 = default ,  1= Trending ")
    description = models.CharField(max_length=400, null=False , blank=False)
    quantity = models.IntegerField(null=False)
    price = models.FloatField(null=False , blank= False)
    discount = models.FloatField(null=False , blank= False)


    trending =models.BooleanField(default=False, help_text="0 = default ,  1= Trending ")
    meta_title = models.CharField(max_length=100, blank=False , null=False)
    meta_keywords = models.CharField(max_length=100, blank=False , null=False)
    meta_description = models.TextField(max_length=500, null= True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty= models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=False)




""" from rest_framework.response import Response
from rest_framework.decorators import api_view
from shop.models import *
from .serializer import  *
from django.contrib import messages
from django.shortcuts import redirect, render




@api_view(['GET'])
def homeData(request):

    category = Category.objects.filter(status=0)
    serializer = CategorySerializer(category, many = True)
   
    return Response(serializer.data)




@api_view(['GET'])
def productData(request, slug):
  if(Category.objects.filter(slug=slug, status=0)):
    products = Product.objects.filter(category__slug=slug)
    serializer = ProductSerializer(products, many = True)
    category_name = Category.objects.filter(slug=slug).first
    context= {
      'products':products, 
      'category_name':category_name
    }

    return Response(serializer.data)

    # return render(request, 'product.html' , context)
  else:
    messages.warning(request, "Sorry, The link was broken :(")
    return redirect('/')




@api_view(['GET'])
def productDetailData(request ,  cate_slug , prod_slug):
   if (Category.objects.filter(slug=cate_slug, status = 0)):
     if (Product.objects.filter(slug=prod_slug, status = 0)):
       products = Product.objects.filter(slug=prod_slug, status = 0)
       serializer = ProductSerializer(products, many = True)
       
      
       return Response(serializer.data)
     else:
        messages.error(request , "Sorry, You have encounter and error!")
        return redirect('home')
   
   else:
     messages.error(request , "Sorry, You have encounter and error!")
     return redirect('home')
   
 """
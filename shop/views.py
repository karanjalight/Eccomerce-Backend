from multiprocessing import context
from unicodedata import category
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages

def home(request):
  category = Category.objects.filter(status=0)
  context = {
    'category': category
  }

  return render(request, 'home.html' , context)


def collectionsview(request, slug):
  if(Category.objects.filter(slug=slug, status=0)):
    products = Product.objects.filter(category__slug=slug)
    category_name = Category.objects.filter(slug=slug).first
    context= {
      'products':products, 
      'category_name':category_name
    }

    return render(request, 'product.html' , context)
  else:
    messages.warning(request, "Sorry, The link was broken :(")
    return redirect('home')

def productview(request ,  cate_slug , prod_slug):
  if (Category.objects.filter(slug=cate_slug, status = 0)):
    if (Product.objects.filter(slug=prod_slug, status = 0)):
      products = Product.objects.filter(slug=prod_slug, status = 0).first()
      context ={
        'products':products
      }
    
    else:
       messages.error(request , "Sorry, You have encounter and error!")
       return redirect('home')
   
  else:
    messages.error(request , "Sorry, You have encounter and error!")
    return redirect('home')
  return render(request, "view.html", context)   
    




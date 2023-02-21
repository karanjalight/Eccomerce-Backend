from cgi import print_environ
from multiprocessing import context
from re import X
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *


def addtocart(request):
  
  if request.method =='POST':

     print('======================----Post Form------========')
     
     if request.user.is_authenticated:
      
       print('================---------User Auth------========')

       prod_id = request.POST.get('product_id')
       print( "Product id = ", prod_id )
     
       product_check = Product.objects.get( id = prod_id)
       print( "Product name = ",product_check.quantity)      

       if (product_check):
        if (Cart.objects.filter(user=request.user.id, product_id =prod_id)):
          return JsonResponse({'status':"Item added already!"})

        else:
          prod_qty = int(request.POST.get('product_qty'))

          
          if product_check.quantity >= prod_qty:
            Cart.objects.create(user=request.user, product_id = prod_id, product_qty=prod_qty)
            print("Product Added Sucessfully")
            product_check = Product.objects.get( id = prod_id)
            print( "Product quantity = ",product_check.quantity) 
            


            return JsonResponse({'status':"Product Added Sucessfully  ;"})

        
            

     else:
        return JsonResponse({'status':"login to continue"})


  return redirect('/')



def viewcart(request):
  print('===================--------View cart---------======================')
  cart = Cart.objects.filter(user=request.user)
  context={ 'cart':cart }

  return render(request, "cart.html", context)


def updatecart(request):
  if request.method == "POST":
    prod_id = int(request.POST.get('product_id')) 
    print(prod_id)

    if (Cart.objects.filter(user=request.user, product_id=prod_id)):
      prod_qty = request.POST.get('product_qty')
      cart = Cart.objects.get(product_id=prod_id, user= request.user)
      cart.product_qty = prod_qty
      cart.save()
      for i in range(10):
        print("bitches! and nyash")
        
      return JsonResponse({'status':"UPDATED SUCCESSFULLY!"}) 

  
  

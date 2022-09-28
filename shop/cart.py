from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *

def addtocart(request):
  print("hello world")
  if request.method =='POST':

     if request.user.is_authenticated:
      prod_id =  request.POST.get('product_id')
      print(prod_id)
     
      product_check = Product.objects.get( id = prod_id)
      print(product_check)

      if (product_check):
        if (Cart.objects.filter(user=request.user.id, product_id =prod_id)):
          return JsonResponse({'status':"Item added already!"})

        else:
          prod_qty = int(request.POST.get('product_qty'))

          print(prod_qty )

          if product_check.quantity >= prod_qty:
            Cart.objects.create(user=request.user, product_id = prod_id, product_qty=prod_qty)
            return JsonResponse({'status':"Product Added Sucessfully"})
          else :
            return JsonResponse({'status':"AVAILABLE"})
      
      else: 
        return JsonResponse({'status':"Sorry! Product does not exist"})


     else:
        return JsonResponse({'status':"login to continue"})


  return redirect('/')

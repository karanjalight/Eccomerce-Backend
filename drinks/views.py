from itertools import product
from django.shortcuts import render
from .models import Cartitems, Product , Cart


#"d:/2022PROJECTS/Eccomerce Backend/venv/Scripts/activate.bat" this line is to activate the virtual


 
def home(request):
    category = request.GET.get('category')
    if category:
        ls = Product.objects.filter(category=category)
    else:
        ls = Product.objects.all()
    
    return render(request, 'home.html' , {'ls': ls})

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer , completed = False)
        cartitems = cart.cartitems_set.all()
         

        return render(request, 'cart.html', {'cartitems' : cartitems} )
from django.db import models
from django.contrib.auth.models import User
import uuid



CATEGORY = (
    ('Juice', 'Juice'),
    ('Alcohol', 'Alcohol'),
    ('Soda', 'Soda'),
    ('Cocktail', 'Cocktail'),
    ('Fresh', 'Fresh Juices'),
    ('Energy', 'Energy Drinks'),
    
    
)



class Customer(models.Model):
  user = models.OneToOneField(User , on_delete=models.CASCADE)
  name = models.CharField(max_length= 20)
  email = models.EmailField()

  def __str__(self) :
      return self.name


class Product(models.Model):
  name= models.CharField(max_length=15)
  price = models.IntegerField()
  image = models.ImageField()
  category = models.CharField(choices=CATEGORY, max_length=20)

  def __str__(self) :
    return self.name

class Cart(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  cart_id = models.UUIDField(default=uuid.uuid4 , unique=True , editable=False)
  completed = models.BooleanField(default=False)

  def __str__(self) :
    return str(self.id)


class Cartitems(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=0)

  def __str__(self) :
    return self.product.name

class ShippingAddress(models.Model):
  customer = models.ForeignKey(Customer ,  on_delete=models.CASCADE)
  
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  address = models.CharField(max_length=10)     #this is the city 
  phone_number = models.CharField(max_length=10)

  def __str__(self) :
    return self.address





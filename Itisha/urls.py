from django.contrib import admin
from django.urls import path , include

#for the registration app
from oauth import views 


from drinks import views as drink

#for the shop app best to rem=name it as the app name
from shop import views as shop
from shop import cart as cart


#importing  inbuilt user authentication
from django.contrib.auth import views as auth_views

from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #shops url to map the pages in the app
    #the name value is used in html to connect the webpages e.g {% url 'home' %}
    #"products" this string value is used in the page url to display where you are on the site
    #shop.collection is used to refer to the object in views.py, shop=(name of app), collectionsview=object name

    path('' , shop.home, name='home'),

    path('add-to-cart' , shop.cart, name='home'),


    path('products/<str:slug>', shop.collectionsview, name='collectionsview'),
    path('products/<str:cate_slug>/<str:prod_slug>',shop.productview, name='productview'),
   # path("add-to-cart", cart.addtocart, name='addtocart'),


    
  
    
   #Django auth
    path('login/', auth_views.LoginView.as_view(), name='login'),  #<--to login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), #<--to logout
    path('register/', views.register, name='register'), #<--to register new users

    # for facebook auth
    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
    

]


urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


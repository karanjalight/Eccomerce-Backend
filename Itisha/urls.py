


from django.contrib import admin
from django.urls import path , include
from oauth import views 
from drinks import views as drink
from shop import views as shop


from django.contrib.auth import views as auth_views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , shop.home, name='home'),
    path('products/<str:slug>', shop.collectionsview, name='collectionsview'),
    path('products/<str:cate_slug>/<str:prod_slug>',shop.productview, name='productview'),





    path('' , drink.home, name='home'),
    path('cart' , drink.cart, name='cartitem'),
    

    
   
    path('login/', auth_views.LoginView.as_view(), name='login'),  #<--to login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), #<--to logout
    path('register/', views.register, name='register'), #<--to register new users

    # for facebook auth
    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
    

]


urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


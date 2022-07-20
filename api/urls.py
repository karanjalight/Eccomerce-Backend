from django.urls import path
from . import views

urlpatterns = [
    path('yep', views.getFata),

]

from rest_framework.routers import DefaultRouter 
from django.urls import path, include 
from . import views

urlpatterns = [  
   path('', views.hello, name="hello")
]

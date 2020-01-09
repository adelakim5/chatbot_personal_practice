from django.contrib import admin
from django.urls import path, include
import hello_uuri.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello_uuri.urls')),
]

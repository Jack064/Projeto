from django.contrib import admin
from django.urls import path, include
from .views import home, about, gallery

urlpatterns = [
    path('index.html', home),
    path('about.html', about),
    path('gallery.html', gallery),
    
]

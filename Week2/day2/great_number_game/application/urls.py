from django.contrib import admin
from django.urls import path
from . import views

print("In urls file!")

urlpatterns = [
    path('', views.index),
    path('process_guess', views.process_guess),
]
from django.urls import path
from django.views import generic
from . import views
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')



urlpatterns = [
    path('', index),
]
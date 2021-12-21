from django.http import request
from django.shortcuts import render

from .models import *

# Create your views here.
top_menu = ["home", "about", "cars"]

def index(request):
    return render(request, 'homepage/index.html', {'top_menu': top_menu, 'title': 'Главная'})


def about(request):
    return render(request, 'about/index.html', {'title': 'about'})


def cars(request):
  cars= Car.objects.all()  
  return render(request, 'cars/index.html', {'cars':cars})

def show_car(request, carid):
  car= Car.objects.get(pk=carid)   
  return render(request, 'show_car/index.html', {'car': car})

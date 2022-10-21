from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'shop/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def shops(request):   #из urls название будет обращаться сюда 
    return render(request, 'shop/shops.html' )
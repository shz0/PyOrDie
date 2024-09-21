from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import JsonResponse
from . models import Artikel

def index(request):
    artikel = Artikel.objects.get(id=1)
    return render(request, 'hallo.html', {'artikel': artikel})

def start(request):
    artikels = Artikel.objects.all()
    return render(request, 'start.html', {'artikels': artikels})

def navbar(request):
    return render(request, 'navbar.html')
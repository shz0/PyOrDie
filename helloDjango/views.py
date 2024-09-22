from django.shortcuts import render
from . models import Artikel


def index(request):
    artikels = Artikel.objects.all()
    return render(request, 'index.html', {'artikels': artikels})
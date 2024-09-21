from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import JsonResponse

def index(request):
    return render(request, 'hallo.html')

def start(request):
    return render(request, 'start.html')

def navbar(request):
    return render(request, 'navbar.html')
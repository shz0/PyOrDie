from django.urls import path
from . import views

urlpatterns = [
    path('',views.start, name='index'),
    path('hallo/', views.index, name='hallo'),
    path('navbar/', views.navbar, name='navbar')
]
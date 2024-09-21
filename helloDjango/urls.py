from django.urls import path
from . import views

urlpatterns = [
    path('hallo/', views.index, name='hallo'),
    path('',views.start, name='index')
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('warenkorb/', views.warenkorb, name='warenkorb'),
    path('kasse/', views.kasse, name='kasse'),
]


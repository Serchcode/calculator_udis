from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('converter/', views.ConverterView.as_view(), name='converter'),
    path('tiie/', views.TiieView.as_view(), name='tiee'),
]

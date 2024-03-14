
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teste/', views.teste, name='teste'),
    path('teste2/<int:valor>/', views.teste2, name='teste2'),
    path('teste3/', views.teste3, name='teste3'),
    path('teste4/', views.teste4, name='teste4'),
]


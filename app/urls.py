
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teste/', views.teste, name='teste'),
    path('teste/<int:valor>/', views.teste, name='teste_com_parametro'),
]


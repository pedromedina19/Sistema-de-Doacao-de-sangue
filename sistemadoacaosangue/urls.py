from django.contrib import admin
from django.urls import path
from app_doador import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('formulario/cadastro/', views.cadastrar, name='cadastrar'),
    path('formulario/buscar/', views.buscar, name='buscar'),
    path('formulario/', views.cadastrar_doador, name='cadastrar_doador')
]



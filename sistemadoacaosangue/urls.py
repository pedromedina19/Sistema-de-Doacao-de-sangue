from django.contrib import admin
from django.urls import path
from app_doador import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('formulario/cadastro/', views.cadastrar, name='cadastrar'),
    path('formulario/buscar/', views.buscar, name='buscar'),
    path('formulario/', views.cadastrar_doador, name='cadastrar_doador'),
    path('formulario/buscar/mostrar_formularios/', views.mostrar_formularios, name='mostrar_formularios'),    
    path('formulario/buscar/mostrar_formularios/confirmar_remocao/<int:valor>/', views.confirmar_remocao, name='confirmar_remocao'),
    path('formulario/buscar/mostrar_formularios/confirmar_remocao/remover_doador/<int:valor>/', views.remover_doador, name='remover_doador'),
    path('formulario/buscar/mostrar_formularios/busca_anterior', views.recuperar_busca_anterior, name='recuperar_busca_anterior'),        
    path('formulario/buscar/mostrar_formularios/atualizar_cadastro/<int:valor>/', views.atualizar_cadastro, name='atualizar_cadastro'),    
    path('formulario/buscar/mostrar_formularios/atualizar_cadastro/atualizar/<int:valor>/', views.atualizar, name='atualizar'),    

    path('formulario/buscar/mostrar_formularios/doar/<int:valor>/', views.doar, name='doar'),    
    path('formulario/buscar/mostrar_formularios/doar/cadastrar_doacao/<int:valor>/', views.cadastrar_doacao, name='cadastrar_doacao'),    
    path('formulario/buscar/mostrar_formularios/mostrar_doacoes/<int:valor>/', views.mostrar_doacoes, name='mostrar_doacoes'),    
    path('formulario/buscar_doacoes/', views.buscar_doacoes, name='buscar_doacoes'),
    path('formulario/buscar_doacoes/doacoes_por_intervalo_de_datas/', views.buscar_doacoes_por_intervalo_de_datas, name='buscar_doacoes_por_intervalo_de_datas'),        
]




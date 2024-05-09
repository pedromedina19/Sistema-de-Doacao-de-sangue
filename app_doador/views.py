from audioop import reverse
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DoadorForm
from .models import Doador


def home(request):
    return render(request, 'formularios/home.html')


def cadastrar(request):
    return render(request, 'formularios/cadastro.html')


def cadastrar_doador(request):
    if request.method == 'POST':
        doador = DoadorForm(request.POST)
        if doador.is_valid():                                                               
            doador.save()
            messages.success(request, 'Formulário salvo com sucesso!')
            return redirect('home') 
        else:
            for field, errors in doador.errors.items():
                for error in errors:                        
                    messages.error(request, f'Erro no campo {field}: - {error}')
        
    return redirect('cadastrar')
 

def buscar(request):
    return render(request, 'formularios/buscar.html')


def mostrar_formularios(request):
    if request.method == 'GET':
        nome = request.GET.get("nome")
        cpf = request.GET.get("cpf")
        contato = request.GET.get("contato")
        tipo_sanguineo = request.GET.get("tipo_sanguineo")
        rh = request.GET.get("rh")         
        
        filtro = {}
        if nome:
            filtro['nome'] = nome
        if cpf:
            filtro['cpf'] = cpf
        if contato:
            filtro['contato'] = contato
        if tipo_sanguineo and tipo_sanguineo != 'todos':
            filtro['tipo_sanguineo'] = tipo_sanguineo
        if rh and rh != 'todos':
            filtro['rh'] = rh

        request.session['filtro'] = filtro
        
        if filtro or (tipo_sanguineo == 'todos' or rh == 'todos'):
            doadores = Doador.objects.filter(**filtro)        
            return render(request, 'formularios/mostrar_formularios.html', {'doadores': doadores})
        else:
            return render(request, 'formularios/buscar.html')
    

def confirmar_remocao(request, valor=None):    
    if valor is not None:        
        doador = Doador.objects.filter(codigo=valor).first()
        if doador and doador.situacao == 'ativo': 
            return render(request, 'formularios/confirmar_remocao.html', {'codigo': valor})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/') )


def remover_doador(request, valor=None):
    if valor is not None:        
        doador = Doador.objects.filter(codigo=valor).first()
        if doador and doador.situacao == 'ativo':            
            doador.situacao = 'inativo'
            doador.save()
        return redirect('recuperar_busca_anterior')
    
    return redirect('home')


def atualizar_cadastro(request, valor=None):    
    if valor is not None:
        doador = Doador.objects.filter(codigo=valor)
        return render(request, 'formularios/atualizar_cadastro.html', {'doador': doador})
    
    return redirect('home')


def atualizar(request, valor=None):
    if request.method == 'POST':
        if valor is not None:
            doador = Doador.objects.get(codigo=valor)
            cadastro = DoadorForm(request.POST, instance=doador)            
            if cadastro.is_valid():   
                if all([cadastro.cleaned_data[field] for field in cadastro.fields if cadastro.fields[field].required]):
                    cadastro.save()
                    return redirect('recuperar_busca_anterior')
            else:
                for field, errors in cadastro.errors.items():
                    for error in errors:                        
                        messages.error(request, f'Erro no campo {field}: - {error}')
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/') )


def recuperar_busca_anterior(request):
    busca_anterior = request.session.get('filtro', {})
    doadores = Doador.objects.filter(**busca_anterior)        
    return render(request, 'formularios/mostrar_formularios.html', {'doadores': doadores})

def confirmar_remocao(request, valor=None):    
    if valor is not None:        
        doador = Doador.objects.filter(codigo=valor).first()
        if doador and doador.situacao == 'ativo': 
            return render(request, 'formularios/confirmar_remocao.html', {'codigo': valor})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/') )


def remover_doador(request, valor=None):
    if valor is not None:        
        doador = Doador.objects.filter(codigo=valor).first()
        if doador and doador.situacao == 'ativo':            
            doador.situacao = 'inativo'
            doador.save()
        return redirect('recuperar_busca_anterior')
    
    return redirect('home')


def atualizar_cadastro(request, valor=None):    
    if valor is not None:
        doador = Doador.objects.filter(codigo=valor)
        return render(request, 'formularios/atualizar_cadastro.html', {'doador': doador})
    
    return redirect('home')


def atualizar(request, valor=None):
    if request.method == 'POST':
        if valor is not None:
            doador = Doador.objects.get(codigo=valor)
            cadastro = DoadorForm(request.POST, instance=doador)            
            if cadastro.is_valid():   
                if all([cadastro.cleaned_data[field] for field in cadastro.fields if cadastro.fields[field].required]):
                    cadastro.save()
                    return redirect('recuperar_busca_anterior')
            else:
                for field, errors in cadastro.errors.items():
                    for error in errors:                        
                        messages.error(request, f'Erro no campo {field}: - {error}')
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/') )


def recuperar_busca_anterior(request):
    busca_anterior = request.session.get('filtro', {})
    doadores = Doador.objects.filter(**busca_anterior)        
    return render(request, 'formularios/mostrar_formularios.html', {'doadores': doadores})
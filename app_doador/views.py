from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Doador
from .forms import DoadorForm

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
        
    return redirect('home')
 

def buscar(request):
    return render(request, 'formularios/buscar.html')

def buscar_doador(request):
    return redirect('home')
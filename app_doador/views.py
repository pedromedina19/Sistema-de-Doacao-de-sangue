
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DoacaoForm, DoadorForm
from .models import Doacao, Doador


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
    boolean_param = request.GET.get('doar', 'false').lower() in ('true', '1')           
    return render(request, 'formularios/buscar.html', {'boolean_param': boolean_param})   


def mostrar_formularios(request):
    if request.method == 'GET':
        boolean_param = request.GET.get('doar', 'false').lower() in ('true', '1')
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
        request.session['boolean_param'] = boolean_param        
        
        if filtro or (tipo_sanguineo == 'todos' or rh == 'todos'):
            doadores = Doador.objects.filter(**filtro)       
            context = {
                'doadores': doadores,
                'boolean_param': boolean_param
            }  
            return render(request, 'formularios/mostrar_formularios.html', context)
        else:
            return render(request, 'formularios/buscar.html', {'boolean_param': boolean_param})    
    

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


def recuperar_busca_anterior(request):
    busca_anterior = request.session.get('filtro', {})    
    boolean_param = request.session.get('boolean_param', False)
    doadores = Doador.objects.filter(**busca_anterior)       
    context = {
        'doadores': doadores,
        'boolean_param': boolean_param
    }         
    return render(request, 'formularios/mostrar_formularios.html', context)


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

# =====================

def doar(request, valor=None):
    if valor is not None:
        doador = Doador.objects.filter(codigo=valor).first()
        return render(request, 'formularios/doar.html', {'doador': doador})
    return redirect('home')

def cadastrar_doacao(request, valor=None):
    if request.method == 'POST' and valor is not None:
        volume = request.POST.get("volume")
        data = request.POST.get("data")
        hora = request.POST.get("hora")
                 
        doacao = DoacaoForm({
            'volume': volume,
            'data': data,
            'hora': hora,
            'codigo_doador': valor 
        })

        if not doacao.is_valid(): 
            for field, errors in doacao.errors.items():
                for error in errors:                        
                    messages.error(request, f'Erro no campo {field}: - {error}') 

        else:              
            doacao.save() 
            messages.success(request, 'Doação cadastrada.')
            return redirect('home') 
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/') )

#================
def mostrar_doacoes(request, valor=None):
    if valor is not None:
        doacoes = Doacao.objects.filter(codigo_doador=valor) 
        doadores = Doador.objects.filter(codigo=valor)
        context = {
            'doacoes':doacoes,
            'doadores':doadores
        }       
        return render(request, 'formularios/mostrar_doacoes.html', context)
    redirect('home')


def buscar_doacoes(request):
    return render(request, 'formularios/buscar_doacoes.html')


def buscar_doacoes_por_intervalo_de_datas(request):
    if request.method == 'GET':
        data_inicial = request.GET.get("data_inicial")
        data_final = request.GET.get("data_final")            
        doacoes = Doacao.objects.filter(data__range=(data_inicial, data_final))
        return render(request, 'formularios/mostrar_doacoes.html', {'doacoes':doacoes})
    redirect('home')
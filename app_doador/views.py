# from django.forms import ValidationError
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import Formulario
# from .forms import Form

# def home(request):
#     return render(request, 'formularios/home.html')


# def salvarFormularios(request):
#     if request.method == 'POST':  # Verifica se a requisição é do tipo POST
#         try:
#             novo_valor = Form(request.POST) 
#             if novo_valor.is_valid():                           
#                 novo_valor.texto = request.POST.get('texto')
#                 novo_valor.inteiro = int(request.POST.get('inteiro'))
#                 novo_valor.booleano = bool(request.POST.get('booleano'))
#                 novo_valor.opcaoSelect = request.POST.get('opcaoSelect')
#                 novo_valor.opcaoRadio = request.POST.get('opcaoRadio')            
#                 novo_valor.save()
#                 messages.success(request, 'Formulário salvo com sucesso!')
                
#             else:
#                 for field, errors in novo_valor.errors.items():
#                     for error in errors:                        
#                         messages.error(request, f'Erro no campo {field}: - {error}')
        
            
#         except Exception as e:
#             messages.error(request, f'Erro ao salvar formulário: {e}')
#         return redirect('home')  # Redireciona de volta para a página inicial
#     else:
#         return redirect('home')  # Se a requisição não for do tipo POST, apenas redireciona de volta para a página inicial


# def mostrar(request):
#     mostrar_formularios = {
#         'formularios': Formulario.objects.all()
#     }
#     return render(request, 'formularios/mostrar_formularios.html', mostrar_formularios)

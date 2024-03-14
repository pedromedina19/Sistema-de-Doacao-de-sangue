from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def home(request):
  return render(request, "app/index.html")  
  

def teste(request):
  # return render(request, "app/teste.html")
  return HttpResponse("Rota executou com sucesso!")

def teste2(request, valor):
  return HttpResponse(f'Rota executou com sucesso recebendo o valor {valor}!')
  # return JsonResponse({'message': response_message})
  

def teste3(request):
  if request.method == 'POST':
    valor = request.POST.get('valor') 
    return HttpResponse(f'Rota executou com sucesso recebendo o valor {valor}!')

def teste4(request):  
  valor = request.GET.get('valor')  
  quantidade = request.GET.get('quantidade')
  return HttpResponse(f'Rota executou com sucesso recebendo o valor {valor} e quantidade {quantidade}!')

  

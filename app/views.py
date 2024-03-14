from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def home(request):
  return render(request, "app/index.html")  
  

def teste(request, valor=None):    
  if valor is not None:
    return HttpResponse(f'Rota executou com sucesso recebendo o valor {valor}!')  

  valor_query = request.GET.get('valor')  
  quantidade = request.GET.get('quantidade')
  
  if valor_query and quantidade:
    return HttpResponse(f'Rota executou com sucesso recebendo o valor {valor_query} e quantidade {quantidade}!')

  return HttpResponse("Rota executou com sucesso!")
  

from django import forms
from django.core.exceptions import ValidationError
from .models import Doacao, Doador

class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = ['nome', 'cpf', 'contato', 'tipo_sanguineo', 'rh', 'tipo_rh_corretos']   
  
class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = ['volume','data', 'hora', 'codigo_doador'] 
    
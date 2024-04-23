from django import forms
from django.core.exceptions import ValidationError
from .models import Doador

class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = ['nome', 'cpf', 'contato', 'tipo_sanguineo', 'rh']   
  

    
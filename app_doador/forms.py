from django import forms
from django.core.exceptions import ValidationError
from .models import Formulario

class Form(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'


    def clean_booleano(self):        
        booleano = self.cleaned_data.get("booleano")

        if booleano == False:
            raise ValidationError('Checkbox deve ser marcado.')
        
        return booleano
        

    def clean_opcaoSelect(self):
        opcaoSelect = self.cleaned_data.get("opcaoSelect")

        if opcaoSelect == 'empty':
            raise ValidationError('Selecione uma opção.')

        return opcaoSelect
  

    
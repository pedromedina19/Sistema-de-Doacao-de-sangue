from django import forms
from django.core.exceptions import ValidationError
from .models import Formulario

class Form(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'


  
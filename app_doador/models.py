from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

class Formulario(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(
        max_length = 255, 
        validators=[        
            MinLengthValidator(2, "Texto deve ter pelo menos 2 caracteres."),
            MaxLengthValidator(255, "Texto deve ter no máximo 255 caracteres.")
        ]
    )
    inteiro = models.IntegerField(
        validators=[        
            MinValueValidator(1, "Valor deve ser maior que 0."),
            MaxValueValidator(1000, "Valor deve ser menor que 1000.")
        ]
    )
    booleano = models.BooleanField()
    opcaoSelect = models.CharField(max_length=100)
    opcaoRadio = models.CharField(max_length=100)

    
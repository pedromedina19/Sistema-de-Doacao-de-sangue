from django.db import models

class Formulario(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=100)
    inteiro = models.IntegerField()
    booleano = models.BooleanField()
    opcaoSelect = models.CharField(max_length=100)
    opcaoRadio = models.CharField(max_length=100)
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

class Doador(models.Model):
    RH_CHOICES = [
        ('Positivo', 'Positivo'),
        ('Negativo', 'Negativo'),
    ]

    TIPO_SANGUINEO_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ]
    codigo = models.BigAutoField(primary_key=True)
    nome = models.TextField()
    cpf = models.TextField()
    contato = models.TextField()
    tipo_sanguineo = models.CharField(max_length=2, choices=TIPO_SANGUINEO_CHOICES)
    rh = models.CharField(max_length=8, choices=RH_CHOICES)
    tipo_rh_corretos = models.BooleanField(default=False)
    situacao = models.TextField(default='ativo')
    
    class Meta:
        db_table = 'doador'

class Doacao(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    data = models.DateField()
    hora = models.TimeField()
    volume = models.DecimalField(max_digits=10, decimal_places=3)
    situacao = models.TextField(default='disponível')
    codigo_doador = models.ForeignKey(Doador, on_delete=models.CASCADE)

    class Meta:
        db_table = 'doacao'
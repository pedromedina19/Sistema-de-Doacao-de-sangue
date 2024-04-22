# Generated by Django 5.0.4 on 2024-04-18 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_doador', '0003_doacao_doador_delete_formulario_doacao_doador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doacao',
            name='situacao',
        ),
        migrations.RemoveField(
            model_name='doador',
            name='situacao',
        ),
        migrations.AddField(
            model_name='doacao',
            name='inativo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='doador',
            name='inativo',
            field=models.BooleanField(default=False),
        ),
    ]
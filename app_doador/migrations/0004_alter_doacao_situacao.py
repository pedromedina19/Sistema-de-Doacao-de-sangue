# Generated by Django 5.0.6 on 2024-06-12 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_doador', '0003_alter_doador_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doacao',
            name='situacao',
            field=models.TextField(default='disponível'),
        ),
    ]
# Generated by Django 4.2.13 on 2024-05-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_doador', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doacao',
            old_name='doador',
            new_name='codigo_doador',
        ),
        migrations.AlterField(
            model_name='doacao',
            name='situacao',
            field=models.TextField(),
        ),
    ]
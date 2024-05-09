# Generated by Django 4.2.13 on 2024-05-09 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doador',
            fields=[
                ('codigo', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('cpf', models.TextField()),
                ('contato', models.TextField()),
                ('tipo_sanguineo', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=2)),
                ('rh', models.CharField(choices=[('Positivo', 'Positivo'), ('Negativo', 'Negativo')], max_length=8)),
                ('tipo_rh_corretos', models.BooleanField(default=False)),
                ('situacao', models.BooleanField(default='ativo')),
            ],
            options={
                'db_table': 'doador',
            },
        ),
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('codigo', models.BigAutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('volume', models.DecimalField(decimal_places=3, max_digits=10)),
                ('situacao', models.BooleanField(default='ativo')),
                ('doador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_doador.doador')),
            ],
            options={
                'db_table': 'doacao',
            },
        ),
    ]

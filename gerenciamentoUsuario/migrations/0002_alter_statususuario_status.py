# Generated by Django 5.1.6 on 2025-03-11 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamentoUsuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statususuario',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo'), ('Bloqueado', 'Bloqueado'), ('Suspenso', 'Suspenso')], default='Ativo', max_length=100),
        ),
    ]

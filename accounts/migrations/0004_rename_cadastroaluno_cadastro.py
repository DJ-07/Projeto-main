# Generated by Django 4.0.4 on 2022-06-16 18:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_rename_cadastro_cadastroaluno'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CadastroAluno',
            new_name='Cadastro',
        ),
    ]
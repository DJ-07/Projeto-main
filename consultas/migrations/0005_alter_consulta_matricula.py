# Generated by Django 4.0.4 on 2022-06-30 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0004_alter_consulta_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='matricula',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
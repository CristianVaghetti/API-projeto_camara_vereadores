# Generated by Django 4.1.3 on 2022-11-20 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='fornecedor_cadastro_data',
            field=models.DateField(auto_now_add=True),
        ),
    ]

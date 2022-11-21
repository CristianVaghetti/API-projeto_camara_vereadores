# Generated by Django 4.1.3 on 2022-11-21 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0002_alter_fornecedor_fornecedor_cadastro_data'),
        ('material', '0002_alter_material_material_data_cadastro'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='material_fornecedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='material_fornecedor', to='fornecedor.fornecedor'),
        ),
    ]
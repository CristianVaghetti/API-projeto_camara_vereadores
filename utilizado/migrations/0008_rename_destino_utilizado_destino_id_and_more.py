# Generated by Django 4.1.3 on 2022-12-26 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilizado', '0007_rename_destino_id_utilizado_destino_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilizado',
            old_name='destino',
            new_name='destino_id',
        ),
        migrations.RenameField(
            model_name='utilizado',
            old_name='material',
            new_name='material_id',
        ),
        migrations.RenameField(
            model_name='utilizado',
            old_name='utilizador',
            new_name='utilizador_id',
        ),
    ]

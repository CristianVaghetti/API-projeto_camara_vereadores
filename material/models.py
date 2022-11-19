from django.db import models

class TipoMaterial(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    tipo_descricao = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'tipos_materiais'

class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    tipo_material = models.ForeignKey(TipoMaterial, on_delete=models.SET_NULL, related_name='tipo_material', null=True)
    material_descricao = models.CharField(max_length=50)
    material_valor = models.CharField(max_length=50)
    material_quantidade = models.IntegerField()
    material_data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'materiais'

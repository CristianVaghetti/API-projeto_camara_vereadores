from django.db import models
from material.models import Material

class Destino(models.Model):
    destino_id = models.AutoField(primary_key=True)
    destino_descricao = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'destinos'

class Utilizado(models.Model):
    utilizado_id = models.AutoField(primary_key=True)
    utilizado_quantidade = models.IntegerField()
    material_id = models.ForeignKey(Material, on_delete=models.SET_NULL, related_name='materialDetalhes', null=True)
    destino_id = models.ForeignKey(Destino, on_delete=models.SET_NULL, related_name='destinoDetalhes', null=True)
    utilizado_data = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'utilizados'
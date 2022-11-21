from django.db import models
from uuid import uuid4

class Vereador(models.Model):
    vereador_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    vereador_matricula = models.CharField(max_length=15, blank=False, null=False)
    Vereador_nome = models.CharField(max_length=50, blank=False, null=False)
    vereador_cadastro_data = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'vereadores'
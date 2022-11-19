from django.db import models
from uuid import uuid4

class Fornecedor(models.Model):
    fornecedor_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    fornecedor_cnpj = models.CharField(max_length=18, blank=False, null=False)
    fornecedor_nome = models.CharField(max_length=50, blank=False, null=False)
    fornecedor_cadastro_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'fornecedores'

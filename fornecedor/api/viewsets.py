from rest_framework import viewsets
from fornecedor.api.serializers import FornecedorSerializer
from fornecedor.models import Fornecedor

class FornecedorViewSet(viewsets.ModelViewSet):
    serializer_class = FornecedorSerializer
    queryset = Fornecedor.objects.all()
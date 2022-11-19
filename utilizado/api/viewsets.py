from rest_framework import viewsets
from utilizado.models import Utilizado
from utilizado.api.serializers import UtilizadoSerializer

class UtilizadoViewSet(viewsets.ModelViewSet):
    serializer_class = UtilizadoSerializer
    queryset = Utilizado.objects.all()

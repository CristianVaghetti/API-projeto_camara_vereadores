from rest_framework import viewsets
from utilizado.models import Utilizado, Destino
from utilizado.api.serializers import UtilizadoSerializer, DestinoSerializer

class UtilizadoViewSet(viewsets.ModelViewSet):
    serializer_class = UtilizadoSerializer
    queryset = Utilizado.objects.all()

class DestinoViewSet(viewsets.ModelViewSet):
    serializer_class = DestinoSerializer
    queryset = Destino.objects.all()
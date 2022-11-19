from rest_framework import viewsets
from vereador.api.serializers import VereadorSerializer
from vereador.models import Vereador

class VereadorViewSet(viewsets.ModelViewSet):
    serializer_class = VereadorSerializer
    queryset = Vereador.objects.all()
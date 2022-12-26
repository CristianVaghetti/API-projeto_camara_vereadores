from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from vereador.api.serializers import VereadorSerializer
from vereador.models import Vereador
from vereador.api.serializers import DetalhesUtilizadoSerializer 

class VereadorViewSet(viewsets.ModelViewSet):
    serializer_class = VereadorSerializer
    queryset = Vereador.objects.all()
    
    @action(detail=True, methods=['get'])
    def detalhes(self, request, pk=None, *args, **kwargs):
        queryset = Vereador.objects.filter(pk=pk)
        self.serializer_class = DetalhesUtilizadoSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
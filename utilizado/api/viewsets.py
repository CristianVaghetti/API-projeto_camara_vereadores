from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from utilizado.models import Utilizado, Destino
from utilizado.api.serializers import UtilizadoSerializer, DestinoSerializer, DestinoDetalhesSerializer
from material.models import Material

class UtilizadoViewSet(viewsets.ModelViewSet):
    serializer_class = UtilizadoSerializer
    queryset = Utilizado.objects.all()

    def create(self, request, *args, **kwargs):

        material_queryset = Material.objects.filter(pk=request.data['material_id'])
        quantidade_utilizada = int(request.data['utilizado_quantidade'])
        quantidade_antiga = int(material_queryset[0].material_quantidade)
        quantidade_nova = quantidade_antiga - quantidade_utilizada
        material = Material.objects.get(pk=request.data['material_id'])
        material.material_quantidade = quantidade_nova
        material.save()
        
        utilizado_serializer = self.get_serializer(data=request.data)
        utilizado_serializer.is_valid(raise_exception=True)
        self.perform_create(utilizado_serializer)
        return Response(utilizado_serializer.data)
    
class DestinoViewSet(viewsets.ModelViewSet):
    serializer_class = DestinoSerializer
    queryset = Destino.objects.all()

    @action(detail=True, methods=['get'])
    def detalhes(self, request, pk=None, *args, **kwargs):
        queryset = Destino.objects.filter(pk=pk)
        self.serializer_class = DestinoDetalhesSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
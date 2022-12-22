from rest_framework import viewsets
from material.api.serializers import MaterialSerializer
from material.api.serializers import TipoMaterialSerializer
from rest_framework.response import Response
from material.models import Material
from material.models import TipoMaterial

class MaterialViewSet(viewsets.ModelViewSet):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()

    def update(self, request, *args, **kwargs):
        material_queryset = Material.objects.filter(pk=request.data['material_id'])
        quantidadeAdd = int(request.data['material_quantidadeAdd'])
        quantidade_antiga = int(material_queryset[0].material_quantidade)
        quantidade_nova = quantidade_antiga + quantidadeAdd

        material = Material.objects.get(pk=request.data['material_id'])
        material.material_quantidade = quantidade_nova
        material.save()

        material_serializer = self.get_serializer(data=request.data)
        material_serializer.is_valid(raise_exception=True)
        return Response(material_serializer.data)

class TipoMaterialViewSet(viewsets.ModelViewSet):
    serializer_class = TipoMaterialSerializer
    queryset = TipoMaterial.objects.all()
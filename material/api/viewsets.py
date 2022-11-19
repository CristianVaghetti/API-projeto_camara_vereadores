from rest_framework import viewsets
from material.api.serializers import MaterialSerializer
from material.models import Material

class MaterialViewSet(viewsets.ModelViewSet):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
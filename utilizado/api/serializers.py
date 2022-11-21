from rest_framework import serializers
from utilizado.models import Utilizado, Destino

class UtilizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilizado
        fields = "__all__"

class DestinoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Destino
        fields = "__all__"

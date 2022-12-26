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

class DestinoDetalhesSerializer(serializers.ModelSerializer):
    destinoDetalhes = UtilizadoSerializer(many=True, read_only=True)
    class Meta: 
        model = Destino
        fields = [
            'destino_id',
            'destino_descricao',
            'destinoDetalhes',
        ]

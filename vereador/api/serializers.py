from rest_framework import serializers
from vereador.models import Vereador
from utilizado.api.serializers import UtilizadoSerializer

class VereadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vereador
        fields = "__all__"

class DetalhesUtilizadoSerializer(serializers.ModelSerializer):
    vereadorGastos = UtilizadoSerializer(many=True, read_only=True)
    class Meta:
        model = Vereador
        fields = [
            'vereador_id',
            'vereador_matricula',
            'vereador_nome',
            'vereador_cadastro_data',
            'vereadorGastos',
            ]
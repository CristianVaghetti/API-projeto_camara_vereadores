from rest_framework import serializers
from vereador.models import Vereador

class VereadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vereador
        fields = "__all__"
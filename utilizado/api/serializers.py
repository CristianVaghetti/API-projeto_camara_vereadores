from rest_framework import serializers
from utilizado.models import Utilizado

class UtilizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilizado
        fields = "__all__"

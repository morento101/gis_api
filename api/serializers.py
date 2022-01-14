from rest_framework import serializers
from .models import MapModel


class MapListSerializer(serializers.ModelSerializer):
    """Serializer for all maps"""

    class Meta:
        model = MapModel
        fields = '__all__'

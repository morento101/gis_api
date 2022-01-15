from pyexpat import model
from rest_framework import serializers
from .models import MapModel, ChainModel, LineModel, PointModel


class MapListSerializer(serializers.ModelSerializer):
    """Serializer for all maps"""

    class Meta:
        model = MapModel
        fields = '__all__'

    
class ChainListSerializer(serializers.ModelSerializer):
    """Displays list of chains"""

    class Meta:
        model = ChainModel
        fields = '__all__'


class LineListSerializer(serializers.ModelSerializer):
    """Displays list of lines"""

    class Meta:
        model = LineModel
        fields = '__all__'


class PointListSerializer(serializers.ModelSerializer):
    """Displays list of points"""

    class Meta:
        model = PointModel
        fields = '__all__'

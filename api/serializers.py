from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import MapModel, ChainModel, LineModel, PointModel


class MapListSerializer(serializers.ModelSerializer):
    """Serializer for all maps"""

    class Meta:
        model = MapModel
        fields = '__all__'


class MapDetailSerializer(serializers.ModelSerializer):
    """Detail map Serializer"""

    class Meta:
        model = MapModel
        fields = "__all__"


    def to_representation(self, instance):
        response = super().to_representation(instance)
        print(dir(instance))
        response["chains"] = ChainListSerializer(instance.chainmodel_set, many=True).data
        return response

    
class ChainListSerializer(serializers.ModelSerializer):
    """Displays list of chains"""

    class Meta:
        model = ChainModel
        exclude = ("map",)

class ChainDetailSerializer(serializers.ModelSerializer):
    """Displays chain"""

    map = serializers.SlugRelatedField(slug_field='name_of_territory', read_only=True)

    class Meta:
        model = ChainModel
        fields = '__all__'


class LineListSerializer(serializers.ModelSerializer):
    """Displays list of lines"""

    class Meta:
        model = LineModel
        exclude = ('point', )


class LineDetailSerializer(serializers.ModelSerializer):
    """Displays line"""

    class Meta:
        model = LineModel
        fields = '__all__'


class PointListSerializer(serializers.ModelSerializer):
    """Displays list of points"""

    class Meta:
        model = PointModel
        exclude = ("name",)


class PointDetailSerializer(serializers.ModelSerializer):
    """Displays point"""

    class Meta:
        model = PointModel
        fields = '__all__'

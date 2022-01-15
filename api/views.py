from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    MapListSerializer, ChainListSerializer, LineListSerializer, PointListSerializer
)
from .models import MapModel, ChainModel, LineModel, PointModel


class MapListView(APIView):
    """Returns all maps"""

    def get(self, request):
        maps = MapModel.objects.all()
        serializer = MapListSerializer(maps, many=True)
        return Response(serializer.data)


class ChainListView(APIView):
    """Returns list of chains"""


    def get(self, request):
        chains = ChainModel.objects.all()
        serializer = ChainListSerializer(chains, many=True)
        return Response(serializer.data)


class LineListView(APIView):
    """Returns all lines"""

    def get(self, request):
        lines = LineModel.objects.all()
        serializer = LineListSerializer(lines, many=True)
        return Response(serializer.data)


class PointListView(APIView):
    """Returns list of points"""


    def get(self, request):
        points = PointModel.objects.all()
        serializer = PointListSerializer(points, many=True)
        return Response(serializer.data)

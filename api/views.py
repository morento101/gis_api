from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    MapListSerializer, MapDetailSerializer, 
    ChainListSerializer, ChainDetailSerializer,
    LineListSerializer, LineDetailSerializer,
    PointListSerializer, PointDetailSerializer, PointCreateSerializer
)
from .models import MapModel, ChainModel, LineModel, PointModel


class MapListView(APIView):
    """Returns all maps"""

    def get(self, request):
        maps = MapModel.objects.all()
        serializer = MapListSerializer(maps, many=True)
        return Response(serializer.data)


class MapDetailView(APIView):
    """View for detail map"""

    def get(self, request, pk):
        map = MapModel.objects.get(id=pk)
        serializer = MapDetailSerializer(map)
        return Response(serializer.data)


class ChainListView(APIView):
    """Returns list of chains"""


    def get(self, request):
        chains = ChainModel.objects.all()
        serializer = ChainListSerializer(chains, many=True)
        return Response(serializer.data)


class ChainDetailView(APIView):
    """Returns specific chain"""


    def get(self, request, pk):
        chain = ChainModel.objects.get(id=pk)
        serializer = ChainDetailSerializer(chain)
        return Response(serializer.data)


class LineListView(APIView):
    """Returns all lines"""

    def get(self, request):
        lines = LineModel.objects.all()
        serializer = LineListSerializer(lines, many=True)
        return Response(serializer.data)


class LineDetailView(APIView):
    """Returns line"""

    def get(self, request, pk):
        line = LineModel.objects.get(id=pk)
        serializer = LineDetailSerializer(line)
        return Response(serializer.data)


class PointListView(APIView):
    """Returns list of points"""


    def get(self, request):
        points = PointModel.objects.all()
        serializer = PointListSerializer(points, many=True)
        return Response(serializer.data)


class PointDetailView(APIView):
    """Returns specific point"""


    def get(self, request, pk):
        point = PointModel.objects.get(id=pk)
        serializer = PointDetailSerializer(point)
        return Response(serializer.data)


class PointCreateView(APIView):
    """View for creating point"""

    def post(self, request):
        point = PointCreateSerializer(data=request.data)
        if point.is_valid():
            point.save()
            return Response(status=201)
        return Response(status=400)

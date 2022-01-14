from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MapListSerializer
from .models import MapModel


class MapListView(APIView):
    """Returns all maps"""

    def get(self, request):
        maps = MapModel.objects.all()
        serializer = MapListSerializer(maps, many=True)
        return Response(serializer.data)

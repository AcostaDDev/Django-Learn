
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import  ModelViewSet

from .serializers import SerieSerializer, DetailSerieSerializer
from series.models import Serie


class SeriesViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = SerieSerializer
    queryset = Serie.objects.all()

    def get_serializer_class(self):
        serializer = self.serializer_class

        if self.action in 'retrieve':
            serializer = DetailSerieSerializer

        return serializer

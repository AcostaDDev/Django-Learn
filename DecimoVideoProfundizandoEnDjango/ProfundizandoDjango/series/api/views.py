
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import  ModelViewSet

from .serializers import SerieSerializer, DetailSerieSerializer
from .permissions import IsMeOrReadOnly
from series.models import Serie


class SeriesViewset(ModelViewSet):
    permission_classes = [IsMeOrReadOnly]

    serializer_class = SerieSerializer
    queryset = Serie.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailSerieSerializer
        else:
            return self.serializer_class

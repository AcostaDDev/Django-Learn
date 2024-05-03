from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet

from .serializers import ModelSeriesSerializers
from series.models import Series


class SerieApiView(ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = ModelSeriesSerializers

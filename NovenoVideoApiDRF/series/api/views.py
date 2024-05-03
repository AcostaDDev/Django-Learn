from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet

from .serializers import ModelSeriesSerializers
from series.models import Series


class SerieApiView(ViewSet):

    # def get(self, request):
    #     series = ModelSeriesSerializers(Series.objects.all(), many=True)
    #     return Response(data=series.data, status=status.HTTP_200_OK)
    def list(self, request):
        series = ModelSeriesSerializers(Series.objects.all(), many=True)
        return Response(data=series.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk: int):
        series = ModelSeriesSerializers(Series.objects.get(pk=pk))
        return Response(data=series.data, status=status.HTTP_200_OK)

    def create(self, request):
        serie = ModelSeriesSerializers(data=request.POST)
        serie.is_valid(raise_exception=True)
        serie.save()
        return self.list(request)


    # def post(self, request):
    #     serie = ModelSeriesSerializers(data=request.POST)
    #     serie.is_valid(raise_exception=True)
    #     serie.save()
    #     return self.get(request)
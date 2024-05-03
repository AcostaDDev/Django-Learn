from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from series.models import Series


class SerieApiView(APIView):

    def get(self, request):
        series = [serie.title for serie in Series.objects.all()]
        return Response(data=series, status=status.HTTP_200_OK)

    def post(self, request):
        Series.objects.create(title=request.POST['title'], description=request.POST['description'])
        return self.get(request)
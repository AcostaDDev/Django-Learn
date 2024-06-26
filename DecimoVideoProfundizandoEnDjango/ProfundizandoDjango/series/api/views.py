import logging

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import  ModelViewSet
from rest_framework import status

from .serializers import SerieSerializer, DetailSerieSerializer, ScoreSerializer, DetailEpisodeSerializer
from .permissions import IsMeOrReadOnly
from series.models import Serie, Episode, Score


class SeriesViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SerieSerializer
    queryset = Serie.objects.all()

    def __init__(self, **kwargs):
        self.logger = logging.getLogger(__name__)
        super().__init__(**kwargs)

    def get_serializer_class(self):
        # raise Exception(self.action)
        self.logger.error(self.action)
        if self.action == 'retrieve':
            return DetailSerieSerializer
        elif self.action == 'set_score':
            return ScoreSerializer
        else:
            return self.serializer_class

    @action(detail=True, methods=['PUT'], url_path='set-score', permission_classes=[IsAdminUser])   # --> Se importa al router automaticamente
    def set_score(self, request, pk: int):
        data = {
            'serie': pk,
            'user':  request.user.pk,
            'score': int(request.POST['score'])
        }

        serializer = self.get_serializer_class()(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)

class EpisodesViewSet(ModelViewSet):
    permission_classes = [IsMeOrReadOnly]

    serializer_class = DetailEpisodeSerializer
    queryset = Episode.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailEpisodeSerializer
        elif self.action == 'set_score':
            return ScoreSerializer
        else:
            return self.serializer_class

    @action(detail=True, methods=['PUT'], url_path='set-score',
            permission_classes=[IsAdminUser])  # --> Se importa al router automaticamente
    def set_score(self, request, pk: int):
        episode = Episode.objects.get(pk=pk)
        episode_serie = Episode.objects.filter(serie=episode.serie).first()
        serie = episode_serie.serie_id
        data = {
            'serie': serie,
            'user': request.user.pk,
            'episode': pk,
            'score': int(request.POST['score'])
        }

        serializer = self.get_serializer_class()(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)
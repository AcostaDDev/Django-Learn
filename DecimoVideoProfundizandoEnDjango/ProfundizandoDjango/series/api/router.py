from rest_framework.routers import DefaultRouter

from series.api.views import SeriesViewSet, EpisodesViewSet

router = DefaultRouter()

router.register(prefix='series', basename='series', viewset=SeriesViewSet)
router.register(prefix='episodes', basename='episodes', viewset=EpisodesViewSet)
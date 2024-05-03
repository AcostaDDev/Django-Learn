from rest_framework.routers import DefaultRouter

from .views import SerieApiView

router = DefaultRouter()
router.register(prefix='series', basename='series', viewset=SerieApiView)
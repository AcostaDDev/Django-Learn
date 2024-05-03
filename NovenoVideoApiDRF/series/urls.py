from django.urls import path

from .views import SerieView, EpisodeView
from .api.views import SerieApiView

app_name = "series"

urlpatterns = [
    path("", SerieView.as_view(), name="series"),
    path("episode/<int:pk>/", EpisodeView.as_view(), name="episodes"),
]
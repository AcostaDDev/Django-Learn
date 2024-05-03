from django.urls import path

from .views import SerieApiView

app_name = "api"

urlpatterns = [
    path("series/", SerieApiView.as_view()),
]
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import View

from .models import Series, Episode


class SerieView(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'series': list(Series.objects.all())
            }
            return render(request, 'series/series.html', context)
        else:
            return Http404


class EpisodeView(View):
    def get(self, request, pk: int):
        context = {
            'episodes': list(Episode.objects.filter(serie_id=pk))
        }

        return render(request, 'series/episodes.html', context)
from django.contrib import admin

from .models import Series, Episode


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(Episode)
class EpisodesAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'serie')
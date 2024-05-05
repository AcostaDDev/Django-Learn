from django.db.models import Avg
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField

from series.models import Serie, Episode, Score


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('id', 'title', 'description',)


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('id', 'name',)


class DetailEpisodeSerializer(serializers.ModelSerializer):
    score = SerializerMethodField()

    def get_score(self, instance):
        return Score.objects.filter(episode=instance.pk).aggregate(score=Avg('score')).get('score')
    class Meta:
        model = Episode
        fields = ('id', 'name', 'number', 'serie', 'score')


class DetailSerieSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(source='episode_set', many=True)
    score = SerializerMethodField()

    def get_score(self, instance):
        return Score.objects.filter(serie=instance.pk).aggregate(score=Avg('score')).get('score')

    class Meta:
        model = Serie
        fields = ('id', 'title', 'description', 'episodes', 'score')


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'score', 'user', 'serie', 'episode')

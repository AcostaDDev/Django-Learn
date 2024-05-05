from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField

from series.models import Serie, Episode


class SerieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Serie
        fields = ('id', 'title', 'description',)


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Episode
        fields = ('id', 'name',)


class DetailSerieSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(source='episode_set', many=True)
    # episodes = SerializerMethodField()
    # def get_episodes(self, instance):
    #     return list(instance.episode_set.all().values('id', 'name'))
    class Meta:
        model = Serie
        fields = ('id', 'title', 'description', 'episodes',)
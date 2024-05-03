from typing import Dict

from rest_framework import serializers

from series.models import Series


class ModelSeriesSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    def validate(self, serie: Dict[str, str]):
        if not serie.get('title'):
            raise serializers.ValidationError('title is mandatory')
        return serie

    class Meta:
        model = Series
        fields = '__all__'

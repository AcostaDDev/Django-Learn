from rest_framework import serializers


class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    amount = serializers.FloatField()

    class Meta:
        fields = ('id', 'amount')


class CreateAccountSerializer(serializers.Serializer):
    owners = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        fields = ('amount', 'owners')

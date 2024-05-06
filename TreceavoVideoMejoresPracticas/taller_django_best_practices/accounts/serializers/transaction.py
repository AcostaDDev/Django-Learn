from rest_framework import serializers

from accounts.models import Transaction


class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    type = serializers.CharField(max_length=50)
    account = serializers.IntegerField()
    amount = serializers.FloatField()

    class Meta:
        fields = ('id', 'type', 'account', 'amount')

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from accounts.models import Account
from accounts.models.accounts import AccountCustomer
from accounts.serializers import AccountSerializer, CreateAccountSerializer
from customers.models import Customer


class AccountViewset(ViewSet):
    def list(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = CreateAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

                        # Validamos que existan todos los owners
        if not all(Customer.objects.filter(pk=owner).exists() for owner in serializer.owners):
            raise ValidationError('One or more owners do not exist')

        account = Account.objects.create(amount=serializer.validated_data.get('amount'))
                        # Creamos la cuenta con el listado de owners
        for owner_id in serializer.validated_data.get('owners'):
            AccountCustomer.objects.create(account=account, owner_id=owner_id)

        account_serializer = AccountSerializer(account)
        return Response(data=account_serializer.data, status=status.HTTP_201_CREATED)

from django.db import models

from accounts.models.exceptions import AccountDoesNotHaveEnoughMoneyError
from customers.models import Customer


class Account(models.Model):
    amount = models.FloatField()

    def withdraw(self, amount: float):
        if self.amount < amount:
            raise AccountDoesNotHaveEnoughMoneyError()

        self.amount -= amount


class AccountCustomer(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='owners')
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='accounts')

    class Meta:
        unique_together = ('account', 'owner')

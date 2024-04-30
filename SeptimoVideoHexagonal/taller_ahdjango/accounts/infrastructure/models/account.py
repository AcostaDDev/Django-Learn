from django.db import models
from accounts.domain.account import Account

class AccountDjango(models.Model):
    owner = models.CharField(max_length=100)
    amount = models.FloatField()

    def to_domain(self) -> Account:
        return Account(owner=self.owner, amount=self.amount)
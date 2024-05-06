from unittest import TestCase

from accounts.models import Account
from accounts.models.exceptions import AccountDoesNotHaveEnoughMoneyError


class TestAccounts(TestCase):

    def test_withdraw_is_working_fine(self):
        account = Account(amount=10.0)
        account.withdraw(10.0)

        self.assertEqual(account.amount, 0)

    def test_withdraw_not_enough_money(self):
        account = Account(amount=10.0)

        with self.assertRaises(AccountDoesNotHaveEnoughMoneyError):
            account.withdraw(15.0)

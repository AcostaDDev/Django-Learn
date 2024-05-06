from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import Account


# Create your tests here.
class TestAccount(APITestCase):
    def test_list_account_is_working(self):
        Account.objects.create(amount=130.0)
        response = self.client.get('/accounts/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

from uuid import uuid4

from django.contrib.auth.models import User
from django.test import TestCase

from series.models import Serie, Episode


class TestSerie(TestCase):

    fixtures = ['series', 'users']

    def test_retrieve_serie(self):
        serie = Serie.objects.first()
        response = self.client.get(f'/api/series/{serie.pk}/')

        self.assertEqual(response.status_code, 200)

        response_json = response.json()
        self.assertIsInstance(response_json, dict)
        self.assertIsInstance(response_json.get('id'), int)
        self.assertIsInstance(response_json.get('title'), str)
        self.assertIsInstance(response_json.get('description'), str)
        self.assertIsInstance(response_json.get('episodes'), list)
        self.assertEqual(len(response_json.get('episodes')), serie.episode_set.all().count())

    def test_create_serie(self):
        user = User.objects.first()
        self.client.force_login(user)
        serie_dict = {
            'title': f'mock serie {uuid4()}',
            'description': 'mock description',
        }
        response = self.client.post(f'/api/series/', serie_dict)
        response_json = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response_json.get('id'), int)
        self.assertIsInstance(response_json.get('title'), str)
        self.assertIsInstance(response_json.get('description'), str)


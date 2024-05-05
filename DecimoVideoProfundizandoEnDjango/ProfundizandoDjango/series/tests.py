from uuid import uuid4

from django.contrib.auth.models import User
from django.test import TestCase

from series.models import Serie, Episode


class TestSerie(TestCase):

    def _generate_user(self) -> User:
        return User.objects.create_user(username=f'fake username {uuid4()}', password='supersafe', email=f'fake email {uuid4()}')

    def _generate_serie(self):
        serie = Serie.objects.create(title=f'mock serie {uuid4()}', description='mock description}')

        for i in range(1,6):
            Episode.objects.create(
                number=i,
                name=f'mock episode {uuid4()}',
                serie=serie
            )
        return serie
    def test_retireve_serie(self):
        serie = self._generate_serie()
        response = self.client.get(f'/api/series/{serie.pk}/')

        self.assertEqual(response.status_code, 200)

        response_json = response.json()
        self.assertIsInstance(response_json, dict)
        self.assertIsInstance(response_json.get('id'), int)
        self.assertIsInstance(response_json.get('title'), str)
        self.assertIsInstance(response_json.get('description'), str)
        self.assertIsInstance(response_json.get('episodes'), list)
        self.assertEqual(len(response_json.get('episodes')), 5)

    def test_create_serie(self):
        user = self._generate_user()
        self.client.force_login(user)
        serie_dict = {
            'title': f'mock serie {uuid4()}',
            'description': 'mock description',
        }
        response = self.client.post(f'/api/series/', serie_dict)
        response_json = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response_json, dict)
        self.assertIsInstance(response_json.get('id'), int)
        self.assertIsInstance(response_json.get('title'), str)
        self.assertIsInstance(response_json.get('description'), str)


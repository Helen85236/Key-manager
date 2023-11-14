from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from safe_secret.services import sha256_hash


class SecretTestCase(APITestCase):
    def setUp(self) -> None:
        self.code_phrase_hash = sha256_hash('code_phrase')
        self.data = {
            "lifetime": 1,
            "secret_text": "Текст который должен быть зашифрован",
        }
        self.url_to_create = reverse('safe_secret:secret_create')
        self.created_object = self.client.post(self.url_to_create, data=self.data)

    def test_post(self):
        url = reverse('safe_secret:secret_create')
        data = {
            "lifetime": 1,
            "secret_text": "Текст который должен быть зашифрован",
            "code_phrase": "code_phrase"
        }
        response = self.client.post(url, data=data)
        expected_data = {
            'link': 'http://127.0.0.1:8000/secret/3c3c0afd40f2b619624123375d6578910a0a039e0eec403d354b3dd9576ca17f/'
        }

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_data)
        self.assertIn('link', response.data)

    def test_get(self):
        response_to_get = self.client.get(self.created_object.data['link'])
        self.assertEqual(response_to_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_to_get.data['secret_text'], self.data['secret_text'])

    def test_delete(self):
        url = self.created_object.data['link'] + 'delete/'
        response_to_delete = self.client.delete(url)
        self.assertEqual(response_to_delete.status_code, status.HTTP_204_NO_CONTENT)

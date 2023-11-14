from rest_framework.test import APITestCase
from safe_secret.serializers import SecretSerializer, SecretRetrieveSerializer


class SecretSerializerTest(APITestCase):
    def test_secret_serializer(self):
        data = {
            'code_phrase': 'your_code',
            'lifetime': 60,
            'secret_text': 'your_secret_text',
            'link': 'your_link'
        }

        serializer = SecretSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['code_phrase'], 'your_code')

    def test_secret_retrieve_serializer(self):
        data = {
            'secret_text': 'your_secret_text'
        }

        serializer = SecretRetrieveSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['secret_text'], 'your_secret_text')

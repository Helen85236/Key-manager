from rest_framework.test import APITestCase
from safe_secret.services import sha256_hash, make_link


class ServicesTestcase(APITestCase):
    def test_hash(self):
        text = 'text'
        hashed_text = sha256_hash(text)
        expected_value = '982d9e3eb996f559e633f4d194def3761d909f5a3b647d1a851fead67c32c9d1'
        self.assertEqual(hashed_text, expected_value)

    def test_make_link(self):
        text = 'text'
        link = make_link(text)
        expected_value = 'http://127.0.0.1:8000/secret/text/'
        self.assertEqual(link, expected_value)

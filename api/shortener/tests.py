import random

from rest_framework import status
from rest_framework.test import APITestCase


class ShortenerTestCase(APITestCase):
    def do_create_shortener(self, client, num):
        res = client.post(
            '/api/short/',
            data={'ledger': num}
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        return res.data

    def do_get_shortener_data(self, client, code):
        res = client.get(f'/api/short/{code}/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        return res.data

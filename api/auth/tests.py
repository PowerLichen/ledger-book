import random
import string

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase


class AuthTestCase(APITestCase):
    letter_lst = string.ascii_letters + string.digits

    def do_register(self):
        email_id = ''.join(random.choices(self.letter_lst, k=5))

        email = email_id + '@payheremail.net'
        password = ''.join(random.choices(self.letter_lst, k=8))
        res = self.client.post(
            '/api/auth/register/',
            data={
                'email': email,
                'password': password
            }
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['email'], email)
        return (email, password)

    def do_login(self, email, password):
        res = self.client.post(
            '/api/auth/login/',
            data={
                'email': email,
                'password': password
            }
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        return res.data

    def do_register_and_login(self):
        email, password = self.do_register()
        login_data = self.do_login(email, password)

        token = login_data['access']
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        return client

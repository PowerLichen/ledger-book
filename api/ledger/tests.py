import random

from rest_framework import status
from rest_framework.test import APITestCase


class LedgerTestCase(APITestCase):
    desc_lst = ['식사', '도서구입비', '선물구입비', '카페이용', '병원 이용', '영화관 비용']

    def do_create_ledger_item(self, client):
        amount = random.randint(1, 100) * 1000
        desc = random.choice(self.desc_lst)
        res = client.post(
            '/api/ledger/',
            data={
                'amount': amount,
                'description': desc
            }
        )

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['amount'], amount)
        self.assertEqual(res.data['description'], desc)
        return res.data

    def do_create_multiple_item(self, client, num):
        ret = list()
        for _ in range(num):
            data = self.do_create_ledger_item(client)
            ret.append(data)

        return ret

    def do_get_ledger_list(self, client):
        res = client.get('/api/ledger/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        return res.data

    def do_get_ledger_item(self, client, num):
        res = client.get(f'/api/ledger/{num}/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        return res.data

    def do_update_ledger_item(self, client, num, amount=None, desc=None):
        data = {}
        if amount is not None:
            data['amount'] = amount
        if desc is not None:
            data['description'] = desc

        res = client.patch(
            f'/api/ledger/{num}/',
            data=data
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        return res.data

    def do_delete_ledger_item(self, client, num):
        res = client.delete(f'/api/ledger/{num}/')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def do_duplicate_ledger_item(self, client, num):
        res = client.post(f'/api/ledger/{num}/dup/')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        return res.data

import random
import string

from freezegun import freeze_time
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from api.auth.tests import AuthTestCase
from api.ledger.tests import LedgerTestCase
from api.shortener.tests import ShortenerTestCase


class LedgerViewSetTestCase(AuthTestCase,
                            LedgerTestCase,
                            ShortenerTestCase):
    def test_01_write_and_change(self):
        """
        시나리오:
        1. 회원가입, 로그인
        2. 지출내역 6개 작성, 조회
        3. 지출내역 금액 수정, 조회
        4. 지출내역 메모 수정, 조회
        5. 지출내역 금액과 메모 수정, 조회
        """
        client = self.do_register_and_login()

        # 지출내역 6개 작성, 조회
        self.do_create_multiple_item(client, 6)

        item_lst = self.do_get_ledger_list(client)
        self.assertEqual(len(item_lst), 6)

        # 지출내역 금액 수정, 조회
        modified_amount = 100000
        target_id = item_lst[1]['id']
        self.do_update_ledger_item(client, target_id, amount=modified_amount)

        item = self.do_get_ledger_item(client, target_id)
        self.assertEqual(item['amount'], modified_amount)

        # 지출내역 메모 수정, 조회
        modified_desc = "식사 후 카페이용"
        target_id = item_lst[3]['id']
        self.do_update_ledger_item(client, target_id, desc=modified_desc)

        item = self.do_get_ledger_item(client, target_id)
        self.assertEqual(item['description'], modified_desc)

        # 지출내역 금액과 메모 수정, 조회
        modified_amount = 8760
        modified_desc = "버스비 결재"
        target_id = item_lst[5]['id']
        self.do_update_ledger_item(
            client, target_id, amount=modified_amount, desc=modified_desc)

        item = self.do_get_ledger_item(client, target_id)
        self.assertEqual(item['amount'], modified_amount)
        self.assertEqual(item['description'], modified_desc)

    def test_02_write_and_delete(self):
        """
        시나리오:
        1. 회원가입, 로그인
        2. 지출내역 4개 작성, 리스트 조회
        3. 지출내역 1개 삭제, 리스트 조회
        """
        client = self.do_register_and_login()

        # 지출내역 4개 작성, 조회
        self.do_create_multiple_item(client, 4)

        item_lst = self.do_get_ledger_list(client)
        self.assertEqual(len(item_lst), 4)

        # 지출내역 1개 삭제, 조회
        target_id = item_lst[2]['id']
        self.do_delete_ledger_item(client, target_id)

        item_lst = self.do_get_ledger_list(client)
        self.assertEqual(len(item_lst), 3)

    def test_03_write_and_duplicate(self):
        """
        시나리오
        1. 회원가입, 로그인
        2. 지출내역 1개 작성
        3. 지출내역 1개 복제
        4. 생성된 지출내역 비교
        """
        client = self.do_register_and_login()

        # 지출내역 1개 작성
        data = self.do_create_ledger_item(client)

        # 지출내역 1개 복제
        self.do_duplicate_ledger_item(client, data['id'])

        # 지출내역 비교
        raw_data, dup_data = self.do_get_ledger_list(client)
        self.assertEqual(raw_data['amount'], dup_data['amount'])
        self.assertEqual(raw_data['description'], dup_data['description'])

    def test_04_create_short_url(self):
        """
        시나리오
        1. 2023년 1월 1일 12:00
            1. 사용자 A 회원가입, 로그인
            2. 지출내역 1개 생성
            3. 지출내역 단축 URL 생성
        2. 2023년 1월 1일 12:00
            1. 사용자 B 회원가입, 로그인
            2. 사용자 A가 생성한 단축 URL 확인
        3. 2023년 1월 2일 13:00
            1. 사용자 C 회원가입, 로그인
            1. 단축 URL 확인 실패
        """
        with freeze_time("2023-01-01 12:00:00"):
            client = self.do_register_and_login()
            item = self.do_create_ledger_item(client)

            target_id = item['id']
            data = self.do_create_shortener(client, target_id)

            short_url_code = data['code']

        with freeze_time("2023-01-01 12:00:00"):
            client = self.do_register_and_login()
            self.do_get_shortener_data(client, short_url_code)

        with freeze_time("2023-01-02 13:00:00"):
            client = self.do_register_and_login()
            res = client.get(f'/api/short/{short_url_code}/')
            self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

class Test(APITestCase):
    def test_csv_upload(self):
        with open ('./test_files/test.csv', 'rb') as f:
            response = self.client.post('/csvs/', data={'csv': f})
        self.assertTrue(200 <= response.status_code < 300)

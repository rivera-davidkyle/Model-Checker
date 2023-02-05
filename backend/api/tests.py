from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

class Test(APITestCase):
    def test_csv_upload(self):
        with open ('test.csv', 'rb') as f:
            response = self.client.post('/csvs/', data={'csv': f})
            print(f.read())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

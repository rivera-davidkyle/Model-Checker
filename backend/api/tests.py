from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
import csv, random, io, time

csv_num = 100

def create_csv(rows, columns):
    file = io.StringIO()
    writer = csv.writer(file)
    for i in range(rows):
        row = [random.randint(0, 100) for j in range(columns)]
        writer.writerow(row)
    file.seek(0)
    return file

# Create your tests here.
class Test(APITestCase):
    def test_csv_upload_func(self):
        f = create_csv(1000,20)
        response = self.client.post('/csvs/', data={'csv': f})
        self.assertTrue(200 <= response.status_code < 300)
    def test_csv_upload_load(self):
        total_duration = 0
        for i in range(csv_num):
            f = create_csv(1000,20)
            start_time = time.time()
            response = self.client.post('/csvs/', data={'csv': f})
            end_time = time.time()
            total_duration+=end_time - start_time
        rps = csv_num/total_duration
        self.assertTrue(200<rps)

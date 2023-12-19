from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import FizzBuzzRequest

class FizzBuzzViewTests(APITestCase):
    def test_fizzbuzz_valid_request(self):
        # Valid FizzBuzz request
        url = reverse('fizzbuzz')
        response = self.client.get(url, {'int1': '3', 'int2': '5', 'limit': '15', 'str1': 'fizz', 'str2': 'buzz'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("fizzbuzz", response.data[-1])  # Check last element for 'fizzbuzz'

    def test_fizzbuzz_invalid_request(self):
        # Invalid parameters
        url = reverse('fizzbuzz')
        response = self.client.get(url, {'int1': 'test', 'int2': '5', 'limit': '15', 'str1': 'fizz', 'str2': 'buzz'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class FizzBuzzStatisticsViewTests(APITestCase):
    def test_statistics_no_requests(self):
        # When no requests have been made
        url = reverse('fizzbuzz_stats')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("error", response.data)

    def test_statistics_with_requests(self):
        # Make a FizzBuzz request
        fizzbuzz_url = reverse('fizzbuzz')
        self.client.get(fizzbuzz_url, {'int1': '3', 'int2': '5', 'limit': '15', 'str1': 'fizz', 'str2': 'buzz'})

        # Check statistics
        stats_url = reverse('fizzbuzz_stats')
        response = self.client.get(stats_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["hits"], 1)
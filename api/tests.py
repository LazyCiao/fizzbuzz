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
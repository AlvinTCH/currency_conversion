from conversion.models import CURRENCY_RATE

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

class CurrencyTestCase(APITestCase):
    def setUp(self):
      CURRENCY_RATE.objects.create(currency="SGD", rate="0")
      CURRENCY_RATE.objects.create(currency="USD", rate="1.0")

    # when currency is queried, it should return all the data in the backend
    def test_get_all_rates(self):
      url = reverse('currency_rate_list')
      response = self.client.get(url, format='json')
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(len(response.data), 2)

    # check if filters for the endpoint works (i.e filter for SGD only)
    # it should return only the data for SGD
    def test_get_currency_filtered(self):
      url = reverse('currency_rate_list')
      response = self.client.get(url + '?filters=currency~SGD', format='json')
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(len(response.data), 1)
      self.assertEqual(response.data[0]['currency'], 'SGD')

    # check if order_by for the endpoint works (i.e order by currency in descending order)
    # it should return only the data with "USD" being the first
    def test_get_currency_ordered_by(self):
      url = reverse('currency_rate_list')
      response = self.client.get(url + '?order_by=-currency', format='json')
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(len(response.data), 2)
      self.assertEqual(response.data[0]['currency'], 'USD')

    # check if sync_currencies endpoint works
    def test_get_currency_ordered_by(self):
      # call the endpoint to initialize the sync
      post_url = reverse('sync_currencies')
      post_response = self.client.post(post_url, format='json')
      self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)


      get_url = reverse('currency_rate_list')
      get_response = self.client.get(get_url, format='json')
      # check if the data is written to the db. if it is, it will be greater than
      # the 2 data that was initially created
      self.assertGreater(len(get_response.data), 2)
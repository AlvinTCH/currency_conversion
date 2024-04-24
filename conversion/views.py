from rest_framework.generics import (
  ListAPIView,
  CreateAPIView
)
from rest_framework.response import Response
from rest_framework import status

from conversion.models import CURRENCY_RATE
from conversion.serializers import CurrencyRateSerializer

from conversion.helpers.FilterAndOrdering import FilterAndOrder
from conversion.helpers.YahooCurrency import GetCurrenciesFromYahoo

'''
Get list of currency rates
inside the database
'''
class CurrencyRateList(ListAPIView):
    serializer_class = CurrencyRateSerializer

    permitted_filters = ['currency', 'rate__gte', 'rate__lte']
    permitted_order_by = [
      'currency', 'rate'
    ]

    def get_queryset(self):
      FilterAndOrderClass = FilterAndOrder(
        self.permitted_filters,
        self.permitted_order_by
      )
      filters, order_by = FilterAndOrderClass.ParamsParser(self.request.query_params)

      return CURRENCY_RATE.objects.filter(
        **filters
      ).order_by(
         *order_by
      )

'''
Sync Currencies from Yahoo
'''
class SyncCurrencies(CreateAPIView):
    serializer_class = CurrencyRateSerializer

    def get_queryset(self):
      return CURRENCY_RATE.objects.all()
    
    def create(self, request, *args, **kwargs):
      # get data from yahoo
      currencies = GetCurrenciesFromYahoo().get_currencies()
      serializer = self.get_serializer(
        data=currencies, many=True,
      )

      # check for valid data
      if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
      # write data to db
      serializer.save()
      return Response({
         "success": True
      }, status=status.HTTP_201_CREATED)
from django.urls import include, path

from conversion.views import (
  CurrencyRateList,
  SyncCurrencies
)

urlpatterns = [
    path(
      r'currency/',
      CurrencyRateList.as_view(),
      name='currency_rate_list'
    ),
    path(
      r'sync_currencies/',
      SyncCurrencies.as_view(),
      name='sync_currencies'
    )
]
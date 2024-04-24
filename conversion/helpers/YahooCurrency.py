import yfinance as yf
import re

from typing import List, NamedTuple

class CurrencyData(NamedTuple):
  currency: str
  rate: float


# get currencies from Yahoo Finance
class GetCurrenciesFromYahoo:

  def __init__(self):
    self.ticker_list = [
      'EURUSD=X',
      'JPY=X',
      'GBPUSD=X',
      'AUDUSD=X',
      'NZDUSD=X',
      'CNY=X',
      'HKD=X',
      'SGD=X',
      'INR=X',
      'MXN=X',
      'PHP=X',
      'IDR=X',
      'THB=X',
      'MYR=X',
      'ZAR=X',
      'RUB=X',
    ]

  # download currencies from list of tickers indicated in self.ticker_list
  def get_currencies(self) -> List[CurrencyData]:
    data = yf.download(
      tickers=self.ticker_list,
      period='1d',
      interval='1d'
    )
    
    parsed_data = []
    for x in data['Adj Close']:
        parsed_data.append({
          "currency": re.sub('(USD)?=X$', '', x),
          "rate": list(data['Adj Close'][x])[0]
        })
    return parsed_data
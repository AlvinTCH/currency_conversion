from typing import List

import re

class FilterAndOrder:

  def __init__(self, permitted_filters: List[str], permitted_order_by: List[str]):
    self.permitted_filters = permitted_filters
    self.permitted_order_by = permitted_order_by

  '''
  parse the value under the query params "filters"
  into a valid dictionary to be used to filter for results

  filters: str - the value under the query params "filters"
  permitted_filters: List[str] - the list of permitted filters to limit what can be sent to the queryset
  '''
  def FilterParser(self, filters: str) -> dict:
    filtersDict = {}

    # if filter is not sent in, return empty dict
    if filters == '':
      return filtersDict

    # split as there can be multiple filters
    filtersList = filters.split(',')
    for filter in filtersList:
      # split the key and value, which the separator is standardized to be using "~"
      key, value = filter.split('~')

      if key in self.permitted_filters:
        filtersDict[key] = value
    return filtersDict

  # 
  '''
  parse the value under the query params "order_by"
  into a valid order_by list for ordering

  order_by: str - the value under the query params "order_by"
  permitted_order_by: List[str] - the list of permitted order_by to limit what can be sent to the queryset
  '''
  def OrderByParser(self, order_by: str) -> List[str]:
    order_by_list = order_by.split(',')
    order_by_list = [x for x in order_by_list if re.sub(r'^-', '', x) in self.permitted_order_by]
    return order_by_list
  

  def ParamsParser(self, queryParams: dict) -> dict:
    return (
      # if query params includes "filters", parse it into valid filters to be passed
      # to the queryset for filtering
      self.FilterParser(queryParams.get('filters', '')),
      
      # if query params includes "order_by", parse it into valid order_by to be passed
      # to the queryset for ordering
      self.OrderByParser(queryParams.get('order_by', ''))
    )
from django.contrib import admin

from conversion.models import CURRENCY_RATE
from simple_history.admin import SimpleHistoryAdmin

@admin.register(CURRENCY_RATE)
class CurrencyRateAdmin(SimpleHistoryAdmin):
    list_display = ('currency', 'rate')
    search_fields = ('currency',)
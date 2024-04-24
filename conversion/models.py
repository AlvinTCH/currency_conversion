from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class CURRENCY_RATE(models.Model):
    currency = models.CharField(
      max_length=4,
      unique=True,
      null=False,
      blank=False,
    )
    rate = models.FloatField(
      null=False,
      blank=False
    )
    last_updated = models.DateTimeField(
      auto_now=True
    )
    history = HistoricalRecords()

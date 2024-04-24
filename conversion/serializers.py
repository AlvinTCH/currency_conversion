
from rest_framework import serializers

from conversion.models import CURRENCY_RATE


class CurrencyRateSerializer(serializers.HyperlinkedModelSerializer):
    currency = serializers.CharField()

    class Meta:
        model = CURRENCY_RATE
        fields = ['currency', 'rate']

    def create(self, validated_data):
        print(validated_data)
        return CURRENCY_RATE.objects.update_or_create(
          currency=validated_data['currency'],
          defaults=validated_data
        )
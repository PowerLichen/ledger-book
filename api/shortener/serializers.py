from rest_framework import serializers

from api.ledger.serializers import LedgerBaseSerializer
from model.shortenermodel.models import Shortener


class ShortenerBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ['ledger', 'code', 'expired_dt']


class ShortenerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ['ledger', 'code']


class ShortenerGetLedgerSerializer(serializers.ModelSerializer):
    ledger = LedgerBaseSerializer()

    class Meta:
        model = Shortener
        fields = ['ledger', 'code']
        lookup_field = 'code'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        return res['ledger']

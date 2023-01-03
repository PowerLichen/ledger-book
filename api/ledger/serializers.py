from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from model.ledgermodel.models import Ledger


class LedgerBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ['amount', 'description', 'create_date']
        
    
    def save(self, **kwargs):
        user = self.context['request'].user
        return super().save(user=user, **kwargs)
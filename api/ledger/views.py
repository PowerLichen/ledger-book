from rest_framework.viewsets import ModelViewSet

from api.ledger.serializers import LedgerBaseSerializer
from model.ledgermodel.models import Ledger


class LedgerViewSet(ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = LedgerBaseSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Ledger.objects.all().filter(user=user)
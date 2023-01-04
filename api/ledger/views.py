from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from api.ledger.serializers import (LedgerBaseSerializer,
                                    LedgerDupSerializer)
from model.ledgermodel.models import Ledger


class LedgerViewSet(ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = LedgerBaseSerializer

    def get_queryset(self):
        user = self.request.user
        return Ledger.objects.all().filter(user=user)

    def get_serializer_class(self):
        if self.action == 'dup_create':
            return LedgerDupSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=['post'], url_path='dup')
    def dup_create(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        for attr, value in serializer.data.items():
            request.data[attr] = value

        return super().create(request, *args, **kwargs)

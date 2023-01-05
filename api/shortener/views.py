from django.utils import timezone
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.shortener.serializers import (ShortenerBaseSerializer,
                                       ShortenerCreateSerializer,
                                       ShortenerGetLedgerSerializer)
from model.shortenermodel.models import Shortener


class ShortenerViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       GenericViewSet):
    queryset = Shortener.objects.all()
    lookup_field = 'code'

    def get_queryset(self):
        return Shortener.objects.filter(expired_dt__gte=timezone.now())

    def get_serializer_class(self):
        if self.action == 'create':
            return ShortenerCreateSerializer
        if self.action == 'retrieve':
            return ShortenerGetLedgerSerializer

        return ShortenerBaseSerializer

from django.urls import include
from django.urls import path
from rest_framework import routers

from api.ledger import views


router = routers.DefaultRouter()
router.register(r'', views.LedgerViewSet, basename='ledger')

urlpatterns = [
    path('', include(router.urls)),
]

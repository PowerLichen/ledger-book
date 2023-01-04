from django.urls import include
from django.urls import path
from rest_framework import routers

from api.shortener.views import ShortenerViewSet


router = routers.DefaultRouter()
router.register(r'', ShortenerViewSet, basename='shortener')

urlpatterns = [
    path('', include(router.urls)),
]

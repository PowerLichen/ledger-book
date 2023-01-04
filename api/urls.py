from django.urls import include
from django.urls import path

urlpatterns = [
    path('auth/', include('api.auth.urls')),
    path('ledger/', include('api.ledger.urls')),
    path('short/', include('api.shortener.urls'))
]

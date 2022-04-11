from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', CartAPIView.as_view()),
    path('delivery-cost/', DeliveryCostViewSet.as_view({'get': 'list'})),
]
from django.urls import path

from apps.orders import views


urlpatterns = [
    path('checkout/', views.checkout),  
    path('orders/', views.OrderListAPIView.as_view()),
]
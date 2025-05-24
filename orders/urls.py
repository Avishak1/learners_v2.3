from django.urls import path
from . import views

urlpatterns = [
    path('place-order/<int:vendor_id>/', views.place_order, name='place_order'),
    path('order-success/', views.order_success, name='order_success'),
    
]

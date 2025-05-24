from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendor_list, name='vendor_list'),
    path('menu/', views.vendor_menu, name='vendor_menu'),
    path('add-menu-item/', views.add_menu_item, name='add_menu_item'),
]

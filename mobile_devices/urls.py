from django.urls import path
from . import views

urlpatterns = [
    path('device_list/', views.DeviceListView.as_view(), name='device_list'),
    path('device_detail/<int:id>/', views.DeviceDetailView.as_view(), name='device_detail'),
    path('device_create/', views.DeviceCreateView.as_view(), name='device_create'),
    path('smartphone_list/', views.SmartphoneListView.as_view(), name='smartphone_list'),
    path('tablet_list/', views.TabletListView.as_view(), name='tablet_list'),
    path('smartwatch_list/', views.SmartwatchListView.as_view(), name='smartwatch_list'),
]
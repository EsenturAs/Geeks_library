from django.urls import path
from . import views

urlpatterns = [
    path('make_an_order/', views.OrderView.as_view(), name='make_an_order'),
    path('order_list/', views.OrderListView.as_view(), name='order_list'),
    path('order_list/<int:id>/delete/', views.DeleteOrderView.as_view(), name='delete_order'),
    path('order_list/<int:id>/update/', views.UpdateOrderView.as_view(), name='update_order'),
]
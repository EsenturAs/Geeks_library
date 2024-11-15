from django.urls import path
from . import views

urlpatterns = [
    path('make_an_order/', views.make_an_order_view, name='make_an_order'),
    path('order_list/', views.order_list_view, name='order_list'),
    path('order_list/<int:id>/delete/', views.delete_order_view, name='delete_order'),
    path('order_list/<int:id>/update/', views.update_order_view, name='update_order'),
]
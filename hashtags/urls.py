from django.urls import path
from . import views

urlpatterns = [
    path('all_products_list/', views.all_products_list_view, name='all_products_list'),
    path('for_elder', views.for_elder_view, name='for_elder'),
    path('for_young/', views.for_young_view, name='for_young'),
    path('for_kids/', views.for_kids_view, name='for_kids'),
]
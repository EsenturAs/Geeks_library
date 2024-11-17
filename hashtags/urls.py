from django.urls import path
from . import views

urlpatterns = [
    path('all_products_list/', views.ProductListView.as_view(), name='all_products_list'),
    path('for_elder', views.ForElderView.as_view(), name='for_elder'),
    path('for_young/', views.ForYoungView.as_view(), name='for_young'),
    path('for_kids/', views.ForKidsView.as_view(), name='for_kids'),
]
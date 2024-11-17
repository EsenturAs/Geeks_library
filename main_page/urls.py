from django.urls import path
from main_page import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='book_details'),
    path('search/', views.SearchView.as_view(), name='search'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("ranobelib_list/", views.RanobelibListView.as_view(), name="ranobelib_list"),
    path(
        "ranobelib_parser/", views.RanobelibFormView.as_view(), name="ranobelib_parser"
    ),
]

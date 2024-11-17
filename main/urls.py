from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main_page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_me/', views.AboutMeView.as_view(), name='about_me'),
    path('about_my_pets/', views.AboutMyPetsView.as_view(), name='about_my_pets'),
    path('system_time/', views.SystemTimeView.as_view(), name='system_time'),
    path('', include("main_page.urls")),
    path('', include("hashtags.urls")),
    path('', include("basket.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

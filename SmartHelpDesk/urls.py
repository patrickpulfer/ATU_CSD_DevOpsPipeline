from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('portal.urls')),
    path('search/', include('portal.urls')),
    path('ticket/', include('portal.urls')),
    path('dashboard/', include('portal.urls')),
]

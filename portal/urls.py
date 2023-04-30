from django.urls.resolvers import URLPattern
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.issue_search, name='issue_search'),
]

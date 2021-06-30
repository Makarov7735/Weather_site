from django.urls import path, include
from .views import Weather_api

urlpatterns = [
    path('', Weather_api.as_view())
]

from django.urls import path, include
from .views import Weather_by_city


urlpatterns = [
    path('', Weather_by_city.as_view(), name='default_p'),
]

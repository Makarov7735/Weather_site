from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from .services.weather_getter import *


class Weather_by_city(View):

    # available http methods
    http_method_names = ['get', ]

    # if http method = GET
    def get(self, request, *args, **kwargs):

        if 'city' in request.GET.keys() and request.GET['city'] != '':

            try:
                context = get_weather_context(
                    settings.WEATHER_API,
                    settings.URL,
                    request.GET['city'],
                    )
                get_forcast(
                    settings.WEATHER_API,
                    settings.URL_F,
                    request.GET['city'],
                    context
                    )
                get_forcast_for_5_days(
                    settings.WEATHER_API,
                    settings.URL_F_5_DAYS,
                    request.GET['city'],
                    context
                    )
                return render(request, 'main/get_weather.html', context)
            except ConnectionError and KeyError:
                city = request.GET['city']
                context = {
                    'city': city,
                    'error': f'Unknown city "{city}"'
                }

                return render(request, 'main/get_weather.html', context)

        else:

            return render(request, 'main/default.html')

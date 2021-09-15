from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from .services.weather_getter import *
from .services.cookie_setter import *


class Weather_by_city(View):

    # available http methods
    http_method_names = ['get', ]

    # if http method = GET
    def get(self, request):
        if 'city' in request.GET.keys() and request.GET['city'] != '':
            context = get_weather_context(request)
            response = render(request, 'main/forecast.html', context)
            if 'error' not in context.keys():
                set_cookies(request, response, context)

            return response

        else:
            context = {'citys': {},}
            for i in request.COOKIES:
                context['citys'][i] = request.COOKIES[i]

            response = render(request, 'main/home.html', context)
            check_cookies_count(request, response)

            return response

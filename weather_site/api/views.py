from django.shortcuts import render
from django.views.generic import View
from main.services import weather_getter
from django.http import JsonResponse
from django.conf import settings


class Weather_api(View):

    http_method_name = ['get', ]

    def get(self, request, *args, **kwargs):

        if 'city' in request.GET.keys():

            return JsonResponse(weather_getter.get_weather_context(
                settings.WEATHER_API,
                settings.URL,
                request.GET['city'],
                )
            )

        else:
            return JsonResponse({'error': f"Unknown GET key '{request.GET}'"})

    def http_method_not_allowed(self, request, *args, **kwargs):

        return JsonResponse({
            'error': 'You cant use method GET to receive api'
            })

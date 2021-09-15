from django.shortcuts import render
from django.views.generic import View
from main.services import weather_getter
from django.http import JsonResponse
from django.conf import settings


class Weather_api(View):

    http_method_name = ['get', ]

    def get(self, request, *args, **kwargs):

        if 'city' in request.GET.keys():

            return JsonResponse(weather_getter.get_weather(
                settings.WEATHER_API,
                settings.URL,
                request.GET['city'],
                )
            )

        elif 'deletecookie' in request.GET.keys():
            if request.GET['deletecookie'] in request.COOKIES.values():
                response = JsonResponse({'successfully': True})
                for key in request.COOKIES.keys():
                    if request.COOKIES[key] == request.GET['deletecookie']:
                        cookie = key
                response.delete_cookie(cookie)

                return response
            else:
                return JsonResponse({'error': f"Unknown GET key '{request.GET}'"})

        else:
            return JsonResponse({'error': f"Unknown GET key '{request.GET}'"})

    def http_method_not_allowed(self, request, *args, **kwargs):

        return JsonResponse({
            'error': 'You cant use method GET to receive api'
            })

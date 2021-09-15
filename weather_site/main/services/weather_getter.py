from .weather import Weather_getter
from django.conf import settings


def get_weather(WEATHER_API, url, city):

    wg = Weather_getter(WEATHER_API, url)

    try:
        weather_dict = wg.get_weather(city)

        temp = int(weather_dict['main']['temp'])
        feels_like = int(weather_dict['main']['feels_like'])

        icon_n = weather_dict['weather'][0]['icon']
        icon = f'http://openweathermap.org/img/wn/{icon_n}@4x.png'

        context = {
            'city': weather_dict['name'],
            'description': weather_dict['weather'][0]['description'].capitalize(),
            'temp': temp,
            'feels_like': feels_like,
            'icon': icon,
            'humidity': weather_dict['main']['humidity']
        }

    except KeyError:
        error = f'Unknown city "{city}"'
        context = {
            'error': error,
            'city': city,
        }

    return context


def get_forcast(WEATHER_API, url, city, context):
    wg = Weather_getter(WEATHER_API, url)

    weather_dict = wg.get_weather(city)

    j = 1
    for i in weather_dict['list']:
        temp = int(i['main']['temp'])
        icon_n = i['weather'][0]['icon']
        icon = f'http://openweathermap.org/img/wn/{icon_n}@4x.png'
        context[f'temp{j}'] = temp
        context[f'icon{j}'] = icon
        context[f'time{j}'] = i['dt_txt'][11:13]
        j += 1

    return context


def get_forcast_for_5_days(WEATHER_API, url, city, context):
    wg = Weather_getter(WEATHER_API, url)

    weather_dict = wg.get_weather(city)

    context['five_day_forecast'] = {}

    j = 1
    for i in weather_dict['list']:
        if i['dt_txt'][11:13] == '15':
            temp = int(i['main']['temp'])
            icon_n = i['weather'][0]['icon']
            icon = f'http://openweathermap.org/img/wn/{icon_n}@4x.png'
            context['five_day_forecast'][f'temp{j}'] = temp
            context['five_day_forecast'][f'icon{j}'] = icon
            context['five_day_forecast'][f'time{j}'] = i['dt_txt'][8:10]

            j += 1

    return context


def get_weather_context(request):
    try:
        context = get_weather(
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
    
    except ConnectionError and KeyError:
        city = request.GET['city']
        context = {
            'city': city,
            'error': f'Unknown city "{city}"'
        }

    return context
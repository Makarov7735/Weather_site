from .weather import Weather_getter


def get_weather_context(WEATHER_API, url, city):

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

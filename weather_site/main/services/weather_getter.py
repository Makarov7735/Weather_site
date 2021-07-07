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


def get_forcast(WEATHER_API, url, city, context):
    wg = Weather_getter(WEATHER_API, url)

    weather_dict = wg.get_weather(city)

    j = 1
    for i in weather_dict['list']:
        key = f'{j}'
        temp = int(i['main']['temp'])
        icon_n = i['weather'][0]['icon']
        icon = f'http://openweathermap.org/img/wn/{icon_n}@4x.png'
        context[f'temp{j}'] = temp
        context[f'icon{j}'] = icon
        context[f'time{j}'] = i['dt_txt'][11:13]
        j += 1

    return context

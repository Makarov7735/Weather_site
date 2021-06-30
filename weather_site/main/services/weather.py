import requests


class Weather_getter():

    def __init__(self, API, url):
        self.API = API
        self.url = url
        self.headers = {
            'Accept': '*/*',
            'User-Agent': '''
            Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)
            AppleWebKit/537.36 (KHTML, like Gecko)
            Chrome/89.0.4389.90 Mobile
            Safari/537.36'''
        }

    def get_weather(self, city):
        correct_url = self.url.format(city, self.API)
        response = requests.get(correct_url, self.headers)

        return response.json()

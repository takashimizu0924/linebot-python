import requests
import pprint
class Weather:
    weather : str
    lat : str
    lon : str
    base_URL : str
    api_key : str

    def __init__(self):
        self.base_URL = "https://api.openweathermap.org/data/2.5/weather?"
        # self.base_URL2 = "https://pro.openweathermap.org/data/2.5/forecast?"
        self.api_key = "f062eb60ee2ba02399bdce2ecea9a15c"
        # self.api_key2 ="105e9fb674d65edf874c519259246340"
        self.lat = "33.60639"
        self.lon = "130.41806"
        return
    
    def setWeather(self):
        res = requests.get(self.base_URL + "lat=" + self.lat + "&lon=" + self.lon + "&appid=" + self.api_key + "&lang=ja" + "&units=metric").json()
        # print(self.base_URL + "lat=" + self.lat + "&lon=" + self.lon + "&appid=" + self.api_key)
        # res2 = requests.get(self.base_URL2 + "id=1863967" + "&appid=" + self.api_key2 ).json()
        pprint.pprint(res)
        # pprint.pprint(res2)
        return

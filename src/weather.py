import requests
import json

area_code = {
    '福岡県':'400000'
}
base_URL = "https://www.jma.go.jp/bosai/forecast/data/forecast/"

def get_weather_info():
    res = requests.get(base_URL + area_code['福岡県']+ ".json").json()
    for re in res:
        time_series = re['timeSeries']
        for time in time_series:
            print(time)
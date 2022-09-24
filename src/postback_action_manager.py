"""
ポストバックアクション用

"""
from weather import get_weather_info
from weather_class import Weather

# 天気予報アクション
def weather_action():
    # get_weather_info()
    w = Weather()
    w.setWeather()

# 夜ご飯候補アクション
def dinner_action():
    return


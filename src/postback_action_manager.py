"""
ポストバックアクション用

"""
from weather import get_weather_info
from weather_class import Weather
from insta_crawler import insta
from instagram import Instagram
import pprint

# 天気予報アクション
def weather_action():
    # get_weather_info()
    # w = Weather()
    # w.setWeather()
    insta = Instagram()
    res = insta.GetHashTagMain('豚肉レシピ')
    print(res)
    
    # insta.GetUserMediaStatus('minnano_yorugohan')
# 夜ご飯候補アクション
def dinner_action():
    return


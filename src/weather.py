import requests
import json

area_code = {
    '福岡県':'400000'
}
base_URL = "https://www.jma.go.jp/bosai/forecast/data/forecast/"

def get_weather_info():
    target_lists = []
    weather = {}
    res = requests.get(base_URL + area_code['福岡県']+ ".json").json()
    for re in res:
        time_series = re['timeSeries']
        for time in time_series:
            for area in time["areas"]:
        #         local_name = time["areas"][i]["area"]["name"]
        #         for j in range(len(time_series[0]["timeDefines"])):
        #             if 'weaters' not in time["areas"][i]:
        #                 weather = ''
        #             else :
        #                 weather = time["areas"][i]["weathers"][j]
        #             if 'wind' not in time["areas"][i]:
        #                 wind = ''
        #             else:
        #                 wind = time["areas"][i]["winds"][j]
        #             target_list = []
        #             target_list.append(local_name)
        #             target_list.append(weather)
        #             target_list.append(wind)

        #             target_lists.append(target_list)
                
                """
                area.get('weathers') : 天気予報
                area.get('winds') : 風速
                area.get('waves') : 波
                area.get('pops') length 5 : 現在から6時間毎の降水確率　合計３０時間　['10', '10', '10', '0', '0']
                area.get('pops') length 7 : 現在から明後日からの６日後まで日ごとの降水確率　['', '20', '30', '20', '20', '30', '30']
                area.get('temps') : 明日の最低気温、最高気温 ['19', '26']
                area.get('tempsMin') : 現在より明後日から６日間の最低気温　['', '20', '21', '22', '21', '22', '23']
                area.get('tempsMax') : 現在より明後日から６日間の最高気温　['', '28', '28', '27', '29', '30', '29']
                """
                target_list = []
                # weather = {}
                if area.get('weathers') != None:
                    # target_list.append(area.get('weathers'))
                    weather["tennki"] = area.get('weathers')
                if area.get('winds') != None:
                    # target_list.append(area.get('winds'))
                    weather["winds"] = area.get('winds')
                if area.get('pops') != None:
                    # print(len(area.get('pops')))
                    weather["pops"] = area.get('pops')
                    # print(area.get('pops'))
                target_list.append(weather)
                target_lists.append(target_list)
    print(target_lists)
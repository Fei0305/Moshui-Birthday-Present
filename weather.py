#! /usr/bin/env python

import requests


def get_weather(city: str):
    """ 获取天气信息
    :param city: 城市
    :return city: 城市,
            weather: 天气,
            temp: 温度,
            wind_power: 风力
    """

    app_id = 'k9gevspmqclku7yk'  # 你的APP_ID
    app_secret = 'TzE4dGY3Mm5hNityNkJ4bzB2bGRZUT09'  # 你的APP_SECRET
    api = "https://www.mxnzp.com/api/weather/current/{}?app_id={}&app_secret={}".format(
        city,
        app_id,
        app_secret
    )
    weather_data = requests.get(api).json()['data']
    temp = weather_data['temp']
    weather = weather_data['weather']
    # wind_power = weather_data['windPower']

    return city, weather, temp


if __name__ == '__main__':
    weather = get_weather('汉中市')
    print(weather)
#! /usr/bin/env python

import datetime
import requests


def get_alldate():
    """ 获取万年历
    :return: 万年历字符串
    """

    str_today = datetime.datetime.today().strftime("%Y%m%d")  # 获取格式化日期如20220305
    app_id = 'k9gevspmqclku7yk'  # 你的APP_ID
    app_secret = 'TzE4dGY3Mm5hNityNkJ4bzB2bGRZUT09'  # 你的APP_SECRET
    api = "https://www.mxnzp.com/api/holiday/single/{}?ignoreHoliday=false&app_id={}&app_secret={}".format(
        str_today,
        app_id,
        app_secret
    )

    res_dict = requests.get(api).json()['data']

    today_date = res_dict['date']  # 日期
    year_tips = res_dict['yearTips']  # 年
    chinese_zodiac = res_dict['chineseZodiac']  # 生肖
    lunar_calendar = res_dict['lunarCalendar']  # 农历

    alldate = '{}                                      {}{}年{}'.format(
        today_date,
        year_tips,
        chinese_zodiac,
        lunar_calendar
    )

    return alldate

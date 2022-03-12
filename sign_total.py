import requests
import datetime


def get_wtb():
    """ 获取未填报人员
    :return: 整形
    """

    today = datetime.datetime.now().strftime('%Y-%m-%d')
    url = 'http://api.xg.bjwlxy.cn/v1/yqsb/jkrb/tutor/getwtblist?bjdm=2020951102&querydate=' + today

    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Mi 10 Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 yiban_android/5.0.8'}
    r = requests.get(url, headers).json()
    wtb_list = r["data"]

    return len(wtb_list)


if __name__ == '__main__':

    s = get_wtb()
    print(s)

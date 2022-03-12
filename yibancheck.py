import requests


def yiban_check(xh: str):
    """ 查询易班打卡情况
    :param xh: 学号
    :return: 字符x或√
    """

    url = "http://api.xg.bjwlxy.cn/v1/yqsb/jkrb/getpclist?xh=" + xh
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Mi 10 Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 yiban_android/5.0.8'}
    r = requests.get(url, headers)

    if r.text == '{"code":400,"message":"今日填报已完成","data":{}}':
        stat_str = '√'
    else:
        stat_str = 'x'

    return stat_str


if __name__ == '__main__':
    stat_str = yiban_check('201995014048')
    print(stat_str)

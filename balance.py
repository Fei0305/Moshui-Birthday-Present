import requests
from lxml import etree
import datetime


def get_data(cookie: str) -> str:
    """ 爬取一卡通数据
    :param cookie: 网站保存的cookies
    :return: 商户名称, 交易额, 余额
    """

    dateend = datetime.datetime.now()
    datestart = dateend + datetime.timedelta(days=-3)
    url = "http://yktcx.bjwlxy.cn/Handler/DBTrjn.ashx"
    headers = {
        'Host': 'yktcx.bjwlxy.cn',
        'Connection': 'keep-alive',
        'Referer': 'http://yktcx.bjwlxy.cn/User/User_HisTrjn.aspx?action=Search&searchtype=1&accounttype=AccountNo&accountno=54624&cardno=1357924680&studentno=&idno=&trancode=&datestart=2022-01-01&dateend=2022-01-31&page=1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
        'Cookie': cookie
    }
    data = {
        'action': 'Search',
        'managetype': 'User',
        'searchtype': '1',
        'accounttype': 'AccountNo',
        'accountno': '54624',
        'cardno': '1357924680',
        'studentno': "",
        'idno': "",
        'trancode': "",
        'datestart': '{}'.format(datestart.strftime('%Y-%m-%d')),
        'dateend': '{}'.format(dateend.strftime('%Y-%m-%d')),
        'page': '1'
    }
    r = requests.post(url, headers=headers, data=data)
    html = etree.HTML(r.text)
    business_name = html.xpath('//tr[2]/td/text()')[4].replace(' ', '')  # 商户名称
    trade_volume = html.xpath('//tr[2]/td/text()')[5].replace(' ', '').replace('-', '')  # 交易额
    balance = html.xpath('//tr[2]/td/text()')[6].replace(' ', '')  # 余额
    if business_name == '':
        text = "一卡通余额:{}元\n在银行充值{}元".format(trade_volume, balance)
    else:
        text = "一卡通余额:{}元\n上次消费{}元在<{}>".format(balance, trade_volume, business_name)

    return text


def get_cookie(username: str, userpassword: str, checkcode: str) -> str:
    """ 获取cookies并写入cookie.txt
    :param username: 学号
    :param userpassword: 学号密码，默认身份证后6位
    :param checkcode: 网址验证码
    :return: cookies值
    """

    url = 'http://yktcx.bjwlxy.cn/Handler/UserLogin.ashx'
    # username = '201995014048'
    # userpassword = '053952'
    post_data = {
        'action': 'Login',
        'managetype': 'Front',
        'acounttype': 'StudentNo',
        'username': username,
        'userpassword': userpassword,
        'checkcode': checkcode
    }
    headers = {
        'Host': 'yktcx.bjwlxy.cn',
        'Origin': 'http://yktcx.bjwlxy.cn',
        'Referer': 'http://yktcx.bjwlxy.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
        'Cookie': 'ASP.NET_SessionId=qaeslpjfa2ox2c4sx1oyhwus; ChenyisiCheckCode=CheckCode=' + checkcode
    }
    session = requests.session()
    res = session.post(url, data=post_data, headers=headers)
    cookies = requests.utils.dict_from_cookiejar(res.cookies)
    cookie = headers['Cookie'] + '; ChenyisiUserConfigInfo=' + cookies['ChenyisiUserConfigInfo']
    with open('/home/pi/moshui/cookie.txt', 'w') as f:
        f.write(cookie)

    return cookie


def get_checkcode() -> str:
    """ 获取验证码
    :return: 验证码
    """

    headers = {
        'Host': 'yktcx.bjwlxy.cn',
        'Referer': 'http://yktcx.bjwlxy.cn/Default.aspx',
        'Proxy-Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
    }
    url = 'http://yktcx.bjwlxy.cn/CheckCode.aspx'
    res = requests.get(url, headers=headers)
    # print(res.headers['Set-Cookie'][-12:-8])
    checkcode = res.headers['Set-Cookie'][-12:-8]

    return checkcode


def get_card_data(school_number: str, password: str) -> str:
    """ 获取一卡通数据
    :param school_number: 学号
    :param password: 账号密码，一般为身份证后六位
    :return: 余额交易额等字符串
    """

    try:
        with open('/home/pi/moshui/cookie.txt', 'r') as f:
            cookie = f.read()
            card_data = get_data(cookie)
    except:
        checkcode = get_checkcode()
        cookie = get_cookie(school_number, password, checkcode)
        card_data = get_data(cookie)

    print("获取一卡通数据成功")
    return card_data


if __name__ == '__main__':
    card_data = get_card_data('201995014048', '053952')
    print(card_data)

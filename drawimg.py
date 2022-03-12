#! /usr/bin/env python

from PIL import Image, ImageDraw, ImageFont
import timetable
import alldate
import datetime
from weather import get_weather
from cet4 import cet4_word
from balance import get_card_data
import cv2
from sign_total import get_wtb
from yibancheck import yiban_check


def edit_img(img_path):
    """ 处理图片解决文字红边
    :param img_path: 图片路径
    :return: None
    """

    img = cv2.imread(img_path)

    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    for x in range(400):
        for y in range(300):
            if g[y, x] > 130:
                r[y, x] = 255
                g[y, x] = 255
                b[y, x] = 255
            elif r[y, x] < 180:
                r[y, x] = 0
                g[y, x] = 0
                b[y, x] = 0

    img[:, :, 0] = b
    img[:, :, 1] = g
    img[:, :, 2] = r

    cv2.imwrite('/home/pi/moshui/show.png', img)


def font(size):
    ttf_path = "/home/pi/moshui/font.ttf"
    return ImageFont.truetype(ttf_path, size)


def img_paste(weather: str, raw_img: Image, xy: tuple):
    """ 叠加图片
    :param raw_img: 原始图片(实例化)
    :param object_img_path: 目标图像路径
    :param xy: 在背景图的坐标
    :return: None
    """
    sun_list = {'少云', '有风', '平静', '浮尘'}
    if '晴' in weather or weather in sun_list:
        object_img_path = '/home/pi/moshui/weather/sun.png'
        if datetime.datetime.now().hour > 19:
            object_img_path = '/home/pi/moshui/weather/moon.png'
    elif '风' in weather or weather == '阴':
        object_img_path = '/home/pi/moshui/weather/yin.png'
    elif '雨' in weather:
        object_img_path = '/home/pi/moshui/weather/rain.png'
    elif weather == '多云':
        object_img_path = '/home/pi/moshui/weather/duoyun.png'
        if datetime.datetime.now().hour > 19:
            object_img_path = '/home/pi/moshui/weather/moon.png'
    else:
        object_img_path = '/home/pi/moshui/weather/yin.png'
    
    object_im = Image.open(object_img_path)
    raw_img.paste(object_im, xy)



def draw_img():
    """ 画图
    :return: 墨水屏图片
    """

    bg_img_path = '/home/pi/moshui/bg.png'
    bg_img = Image.open(bg_img_path)
    # bg_img = Image.new('RGB', (400, 300), (255, 255, 255))

    draw = ImageDraw.Draw(bg_img)  # 实例化画板

    # 日历
    draw.text((43, 19), datetime.datetime.today().strftime("%a"), 'white', font(16))
    draw.text((28, 49), datetime.datetime.today().strftime("%m/%d"), 'black', font(21))

    # 四级单词
    word, word_mean, sample = cet4_word()
    draw.text((120, 19), word, 'red', font(22))
    draw.text((120, 45), word_mean, 'black', font(13))
    if len(sample) > 33:
        draw.text((120, 65), sample[:38]+'...', 'black', font(12))
    else:
        draw.text((120, 64), sample, 'black', font(14))
    draw.text((313, 26), '今日新词', 'black', font(11))

    # 课程表
    draw.text((153, 109), "第{}周".format(timetable.which_week(2022, 3, 6)), 'black', font(17))
    draw.text((30, 109), timetable.get_today_table()[0], 'black', font(17))
    draw.text((30, 136), timetable.get_today_table()[1], 'black', font(13))
    draw.text((30, 160), timetable.get_today_table()[2], 'black', font(13))
    draw.text((30, 184), timetable.get_today_table()[3], 'black', font(13))
    draw.text((30, 208), timetable.get_today_table()[4], 'black', font(13))
    
    # 天气
    city, weather, temp = get_weather('宝鸡')
    if len(temp) == 2:
        temp = '0' + temp
    if len(weather) == 1:
        weather = weather + '天'
    img_paste(weather, bg_img, (236, 185))
    draw.text((242, 224), weather, 'black', font(13))
    draw.text((241, 239), temp, 'black', font(13))
    draw.text((240, 259), city, 'white', font(16))

    # 在一起天数
    draw.text((327, 242), str(timetable.together_days(2020, 11, 6)), 'white', font(15))

    # 一卡通余额
    # draw.text((30, 248), '一卡通余额:18.95元\n上次消费10元在<老校区风味12>', 'black', font(12))
    try:
        draw.text((30, 248), get_card_data('202095154059', '137847'), 'black', font(12))
    except:
        draw.text((30, 248), '出错啦！\n快去找你的宝修BUG！', 'black', font(12))

    # 易班签到
    now_time = datetime.datetime.now()
    # now_time = datetime.datetime(2022, 3, 12, 19)
    if now_time.hour <= 11:
        img1 = Image.open('/home/pi/moshui/sun.png')
        bg_img.paste(img1, (312, 110))
    elif now_time.hour >= 19:
        img1 = Image.open('/home/pi/moshui/night.png')
        bg_img.paste(img1, (312, 110))
    else:
        wtb_number = get_wtb()
        # wtb_number = 18
        draw.text((315, 110), "通信2班", 'black', font(14))
        draw.rectangle((314, 126, 365, 133), 'black')
        draw.rectangle((315, 127, 364, 132), 'white')
        draw.rectangle((315, 127, round(315+(42-wtb_number)/42*49), 132), 'black')
        draw.text((321, 132), "{}/42".format(42-wtb_number), 'black', font(13))
        draw.text((321, 151), "林 [    ]", 'black', font(12))
        draw.text((321, 164), "费 [    ]", 'black', font(12))
        draw.text((343, 151), "{}".format(yiban_check('202095154059')), 'black', font(12))
        draw.text((343, 164), "{}".format(yiban_check('201995014048')), 'black', font(12))
    draw.text((313, 183), "TOR: {}".format(now_time.strftime('%H:%M')), 'black', font(10))
        

    # 保存
    bg_img.save("/home/pi/moshui/show.png")
    edit_img("/home/pi/moshui/show.png")


if __name__ == '__main__':
    draw_img()

#! /usr/bin/env python


'''利用selenium上传图片到8266终端'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def upload(
    url='http://192.168.xx.xx/',
    img_path='/home/pi/moshui/show.png',
    mode=4
) -> None:

    '''
    url -> 8266终端ip
    img_path -> 图片路径
    mode -> 算法模式选择
    '''

    upimg_xpath = '//*[@id="_0"]'  # 加载图片Xpath
    in42b_xpath = '//*[@id="RB"]/input[15]'  # 4.2b按钮Xpath
    if mode == 1:
        algorithm_xpath = '//*[@id="BT"]/div[2]'  # 黑白色阶算法按钮Xpath
    elif mode == 2:
        algorithm_xpath = '//*[@id="BT"]/div[3]'  # 彩色色阶算法按钮Xpath
    elif mode == 3:
        algorithm_xpath = '//*[@id="BT"]/div[4]'  # 黑白抖动算法按钮Xpath
    elif mode == 4:
        algorithm_xpath = '//*[@id="BT"]/div[5]'  # 彩色抖动算法按钮Xpath
    else:
        print('参数错误，默认选择彩色抖动算法')
    upload_xpath = '//*[@id="BT"]/div[6]'  # 上传图片XPath

    ch_options = webdriver.ChromeOptions()
    ch_options.add_argument("--headless")
    ch_options.add_argument('--no-sandbox')
    ch_options.add_argument('--disable-gpu')
    ch_options.add_argument('--disable-dev-shm-usage')

    # 实例化并且在启动浏览器时加入配置
    dr = webdriver.Chrome(options=ch_options)
    dr.get(url=url)  # 打开网页
    time.sleep(2)
    dr.find_element(By.XPATH, upimg_xpath).send_keys(img_path)  # 上传图片
    time.sleep(1)
    dr.find_element(By.XPATH, in42b_xpath).click()  # 选择墨水屏型号4.2b
    dr.find_element(By.XPATH, algorithm_xpath).click()  # 选择算法模式
    time.sleep(1)
    dr.find_element(By.XPATH, upload_xpath).click()  # 开始上传
    time.sleep(10)
    dr.quit()  # 关闭窗口

    print("Upload Finished")


# upload(img_path='/home/pi/moshui/show.png', mode=2)

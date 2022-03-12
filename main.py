#! /usr/bin/env python

import socket
import time
from upload import upload
from drawimg import draw_img
import os


def listener(port: int):
    """ 开始  监听8266
    :param port: 端口
    :return: None
    """

    try:
        MaxBytes = 1024
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '0.0.0.0'
        server.bind((host, port))         # 绑定端口
        server.listen(1)                  # 监听
        print('Listening...')
        client, addr = server.accept()    # 等待客户端连接
        print('Connected', addr)
        while True:
            data = client.recv(MaxBytes)
            if not data:
                break
            print(time.strftime("%Y-%m-%d %H:%M:%S -> ", time.localtime()), data.decode())
            client.send(data)

            '''此处添加自定义内容'''
            time.sleep(2)
            print("Upload Start...")
            if os.path.exists("/home/pi/moshui/frist_show.png") == True:
                upload(img_path="/home/pi/moshui/frist_show.png", mode=4)
                time.sleep(2)
                os.remove("/home/pi/moshui/frist_show.png")
            else:
                draw_img()      # 绘画
                upload(mode=2)  # 上传
            print(" ")
        # server.shutdown(2)
        # server.close()

    except BaseException as e:
        print("Error：")
        print(repr(e))
        time.sleep(2)

    finally:
        server.close()


while 1:
    listener(8888)

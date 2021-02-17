#!/usr/bin/python
# -*- coding: UTF-8 -*-

import telegram
import socket
import socks

def networkinit():
    port = input("初始化网络，本地代理端口(默认7891):")
    if (port == 0 or port == "") :
        port = 7891
    port = int(port)
    print("OK, setting to", port)
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", port)
    socket.socket = socks.socksocket

def gettokenfrom(input_A):
    if input_A == "keydown":
        TOKEN = input("tgBot TOKEN：")
        return TOKEN

def main ():
    TOKEN = gettokenfrom("keydown")
    bot = telegram.Bot(token=TOKEN)
    print(bot.get_me())


def printhello():
    hello='''你好，欢迎下载我的代码并运行
本代码所有功能仅基于本人对于下载转发以及telegram bot的拙见
项目基于telegrambot框架
创建者：github.com/Matt-wzy'''
    print(hello)

if __name__ == "__main__":
    # execute only if run as a script
    printhello()
    networkinit()
    main()

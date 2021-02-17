#!/usr/bin/python
# -*- coding: UTF-8 -*-

import telegram
import socket
import socks

def networkinit():
    port = int(input("端口:"))
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", port)
    socket.socket = socks.socksocket

def gettokenfrom(input_A):
    if input_A == "keydown":
        TOKEN = input("TOKEN：")
        return TOKEN

def main ():
    TOKEN = gettokenfrom("keydown")
    bot = telegram.Bot(token=TOKEN)
    print(bot.get_me())

if __name__ == "__main__":
    # execute only if run as a script
    networkinit()
    main()

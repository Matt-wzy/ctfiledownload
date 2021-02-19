#!/usr/bin/python
# -*- coding: UTF-8 -*-

import telegram
import socket
import socks
import logging
import message
import password
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext
)

global updater
global dispatcher

# Control the version (WTF?)
botversion = 1

def networkinit():
    # port = input("初始化网络，本地代理端口(默认####):")
    # if (port == 0 or port == "") :
    #     port = ####
    # port = int(port)
    port = password.get_port()
    print("OK, setting to", port)
    socks.set_default_proxy(socks.SOCKS5, password.get_proxy_ip(), port)
    socket.socket = socks.socksocket

def gettokenfrom(input_A):
    if input_A == "keydown":
        TOKEN = input("tgBot TOKEN：")
        return TOKEN
    if input_A == "file":
       TOKEN = password.get_password(botversion)
       return TOKEN


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def logtomessage():
    # Enable logging
    logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )
    logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.




def main ():
    TOKEN = gettokenfrom("file")
    bot = telegram.Bot(token=TOKEN)
    print("调试输出，检查机器人是否正常：")
    a = bot.get_me()
    print(a)
    
    updater = Updater(token=TOKEN, use_context=True)
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", message.start))
    dispatcher.add_handler(CommandHandler("help", message.help_command))
    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message.echo))
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


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
    logtomessage()
    main()
    

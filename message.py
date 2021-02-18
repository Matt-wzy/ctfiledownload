#!/usr/bin/python
# -*- coding: UTF-8 -*-

import telegram
import socket
import socks


def test():
    pass


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

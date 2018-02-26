
from config import *

import telebot

from recolector import *


bot = telebot.TeleBot(token)


@bot.message_handler(commands=[command])
def command_start(user):
    value = takeValue()
    bot.send_message(user.chat.id, round(value, decimals))


bot.polling()

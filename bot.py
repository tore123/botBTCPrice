
from config import *

import telebot

import recolector


btc = recolector.getCoinDesk()

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=[command]) 
def command_start(user):
    value = btc.getCurrentPrice() 
    bot.send_message(user.chat.id, round(value,decimals))

bot.polling()
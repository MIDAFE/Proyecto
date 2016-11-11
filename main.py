import ConfigParser
import commands
import json
import telebot
from telebot import types
import time
import unicodedate

from apscheduler.scheduler import Scheduler
from collections import OrderedDict

from telegram.ext import Updater, CommandHandler, MessageHandler, 
Filters

credentials = ConfigParser.ConfigParser()
credentialsfile = "credentials.config"
credentials.read(credentialsfile)

def functionTranslate(bot, update):
    bot.sendMessage(update.message.chat_id, text=message)

commandsbot = {
		'anuncio': 'Enviar anuncio para el bot'
}

@bot.message_handlerd(commands=["anuncio"])

def command_announcement(m):
	msg = bot.reply_to(m, "Bienvenido, Que desea traducir?")
	bot.registrer_netx_step_handler(msg, process_message)

def process_message(m):
	try:
		chat_id = m.chat.id
		callsing = m.text
	except Exeption as e:
		bot.reply_to(m, 'No se detecto ninguna palabra')

	
if __name__ == '__main__':

    credential = credentials.get("telegram", "token")
    updater = Updater(credential)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("Go", functionTranslate))

updater.start_polling()

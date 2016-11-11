import ConfigParser
import commands
import json
import telebot
from telebot import types
import time
import unicodedate

from apscheduler.scheduler import Scheduler
from collections import OrderedDict


commandsbot = {
		'anuncio': 'Enviar anuncio para reproducir en el repetidor'
}

@bot.message_handlerd(commands=["anuncio"])

def command_announcement(m):
	msg = bot.reply_to(m, "Bienvenido")
	bot.registrer_netx_step_handler(msg, process_message)

def process_message(m):
	try:
		chat_id = m.chat.id
		callsing = m.text
		user_User(callsing)
		user_dict[chat_id] = user
		msg = bot.reply_to(m, 'Que palabra quieres traducir?')
		bot.registrer_next_step_handler(msg, process_message_repeater)
	except Exeption as e:
		bot.reply_to(m, 'No se detecto ninguna palabra')

def process_message_recurrence(m):
	try:
		chat_id = m.chat.id
		recurrence = m.text
		user = user_dict[chat_id]
		user.recurrence = recurrence
		recurrence = int(user.recurrence)
		global callsing
		global announcement
		global sched
		global schedinstance
	try:
		sched.unschedule_job(schedinstance)
	except:
		pass
	callsing = user.callsign
	anno

import telebot

import keyboards

from secret import API_TOKEN
from lists import greetings

bot = telebot.TeleBot(API_TOKEN)
	
@bot.message_handler(commands=["start"])
def start_message(message):
	bot.send_message(message.chat.id, text="Бот запущен!", reply_markup=keyboards.start_message())

@bot.message_handler(commands=["hello"])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет! Я бот.")

@bot.message_handler(func=lambda message: any(greeting in message.text.lower() for greeting in greetings))
def say_hello(message):
	bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=keyboards.hru_keyboard())


@bot.callback_query_handler(fun=lambda callback: True)
def handle_callback(callback):
	bot.send_message(

	if callback.data == "good"
	bot.send_message(
		callback.message.chat.id,
		text="Круто"
	)

	if callback.data == "good"
	bot.send_message(
		callback.message.chat.id,
		text="Круто"
	)
bot.infinity_polling()


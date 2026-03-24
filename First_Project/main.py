import telebot
from telebot import types

from lists import greetings

bot = telebot.TeleBot("8319729969:AAG0c2EhuAVyI0WPFH3aD5Iop9PF_iXEofk")

def star_keyboard():
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

	keyboard.add(
		telebot.types.KeyboardButton(text="✌Привет")
	)

return keyboard

@bot.message_handler(commands=["start"])
def start_message(message):
	bot.send_message(
		message.chat.id,
		text="Бот запущен!", 
		reply_markup=start_keyboard()
	)
	

	bot.send_message(
		message.chat.id, 
		text="Бот запущен!", 
		reply_markup=keyboard
	)

@bot.message_handler(commands=["hello"])	
def send_welcome(message):
	bot.send_message(
		message.chat.id, 
		text="Привет"
	)

@bot.message_handler(funс=lambda message: any(greetings in message.text.lower() for greetings in greetings))
def say_hello(message):
	bot.send_message(
		message.chat.id, 
		text="Привет! Как дела?"
	)

@bot.message_handler()
def echo_all(message):
	bot.send_message(
		message.chat.id, 
		text="я не понял что ты сказал"
	)

bot.infinity_polling()

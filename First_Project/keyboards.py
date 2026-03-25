import telebot
from telebot import types

def start_message():
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

	keyboard.add(
		types.KeyboardButton(text="👋 Привет")
	)
	return keyboard

def hru_keyboard():
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(
		types.InlineKeyboardButton(
            text="Плохо",
			callback_data="bed"
        ),
		types.InlineKeyboardButton(
            text="Хорошо",
            callback_data="good"
        )
    )
	return keyboard
import telebot

from secrets import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

def gameboard():
    keyboard = telebot.types.InlineKeyboardMarkup()

    for i in range(3):
        one_row = []
        for j in range(3):
            one_row.append(
                telebot.types.InlineKeyboardButton(
                    text=" ",
                    callback_data="Click"
                )
            )
        keyboard.add(*one_row)
    return keyboard

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        text="Привет! Я бот для игры в крестики-нолики. "\
        "\nЧтобы начать игру, отправь команду /play"
    )

@bot.message_handler(commands=['play'])
def start_game(message):
    bot.send_message(
        message.chat.id,
        text="Игра началась! Ты играешь за крестики-нолики" \
        "\n\nЧтобы начать игру, отправь команду /start",
        reply_markup=gameboard()
    )

bot.infinity_polling()
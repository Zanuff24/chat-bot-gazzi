import telebot

from telebot import types

bot = telebot.TeleBot('5737567559:AAGeSHNwFO0OINui86J3tqig2zaBDwq7GiE')

@bot.message_handler(commands=['start'])
def f_start(message):
    bot.send_message(message.chat.id,
                     f'Привет,{message.from_user.first_name}.\nЗдесь вы узнаете информацию о догазификации в Республике Адыгея',
                     reply_markup='html')
    main(message)
def main(message):
    keyboard_markup = types.InlineKeyboardMarkup()
    key_hi = types.InlineKeyboardButton(text='Привет, я чат-бот Газзи', callback_data='hi')
    key_start = types.InlineKeyboardButton(text='Начать', callback_data='main_start')
    key_tsur = types.InlineKeyboardButton(text='ЦУР в эфире', callbak_data='tsur')
    keyboard_markup.add(key_hi, key_start, key_tsur)
    bot.send_message(message.chat.id, reply_markup=keyboard_markup)






bot.polling(none_stop=True)
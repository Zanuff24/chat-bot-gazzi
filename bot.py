import telebot

from telebot import types

bot = telebot.TeleBot('5737567559:AAGeSHNwFO0OINui86J3tqig2zaBDwq7GiE')


@bot.message_handler(commands=['start'])
def f_start(message):
    bot.send_message(message.chat.id,
                     f'Привет,{message.from_user.first_name}.\nЗдесь вы узнаете информацию о догазификации в Республике Адыгея',
                     parse_mode='html')
    main_create(message)


def main_keyboard():
    keyboard_markup = types.InlineKeyboardMarkup()
    key_hi = types.InlineKeyboardButton(text='Привет, я чат-бот Газзи', callback_data='hi')
    key_start = types.InlineKeyboardButton(text='Начать', callback_data='main_start')
    key_tsur = types.InlineKeyboardButton(text='ЦУР в эфире', callback_data='tsur')
    keyboard_markup.row(key_hi)
    keyboard_markup.row(key_start)
    keyboard_markup.row(key_tsur)
    return keyboard_markup

def main_create(message):
    keyboard_markup = main_keyboard()
    bot.send_message(message.chat.id,'Вы в главном меню', parse_mode='html', reply_markup=keyboard_markup)

def main_edit(message):
    keyboard_markup = main_keyboard()
    bot.edit_message_text('Вы в главном меню',message.chat.id, message.message_id, parse_mode='html', reply_markup=keyboard_markup)


@bot.callback_query_handler(func=lambda call:True)
def answer(call):
    if call.data == 'hi':
        keyboard_back = types.InlineKeyboardMarkup()
        key_back = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
        keyboard_back.add(key_back)
        '''bot.send_message(call.message.chat.id,
                         '',
                         parse_mode='html',
                         reply_markup=keyboard_back)'''
        bot.edit_message_text('Привет. Меня зовут <b>Газзи</b>. Я чат-Бот, который поможет Вам узнать информацию о бесплатной газификации населения.',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_back,
                              parse_mode='html')
    if call.data == 'main_menu':
        main_edit(call.message)

bot.polling(none_stop=True)
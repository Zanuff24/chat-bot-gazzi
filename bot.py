import telebot

from telebot import types

bot = telebot.TeleBot('5737567559:AAGeSHNwFO0OINui86J3tqig2zaBDwq7GiE')


@bot.message_handler(commands=['start'])   #приветствие
def f_start(message):
    bot.send_message(message.chat.id,
                     f'Привет,{message.from_user.first_name}.\nЗдесь вы узнаете информацию о догазификации в Республике Адыгея',
                     parse_mode='html')
    main_create(message)


def main_keyboard(): #функция создания клавиатуры для главного меню
    keyboard_markup = types.InlineKeyboardMarkup()
    key_hi = types.InlineKeyboardButton(text='Привет, я чат-бот Газзи', callback_data='hi')
    key_start = types.InlineKeyboardButton(text='Начать', callback_data='main_start')
    key_tsur = types.InlineKeyboardButton(text='ЦУР в эфире', callback_data='tsur')
    keyboard_markup.row(key_hi)
    keyboard_markup.row(key_start)
    keyboard_markup.row(key_tsur)
    return keyboard_markup

def main_start_keyboard(): #функция создания клавиатуры для меню НАЧАТЬ
    keyboard_markup = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(text='За чей счет проведут газ к участку', callback_data='b1')
    key_2 = types.InlineKeyboardButton(text='Условия подключения', callback_data='b2')
    key_3 = types.InlineKeyboardButton(text='Кто будет проводить бесплатный газ', callback_data='b3')
    key_4 = types.InlineKeyboardButton(text='Кто может подключать газ в 2021 году', callback_data='b4')
    key_5 = types.InlineKeyboardButton(text='Этапы подключения газа', callback_data='b5')
    key_6 = types.InlineKeyboardButton(text='Возможные причины отклонения заявки', callback_data='b6')
    key_7 = types.InlineKeyboardButton(text='Как подать заявку, я чат-бот Газзи', callback_data='b7')
    key_8 = types.InlineKeyboardButton(text='Часто задаваемые вопросы', callback_data='b8')
    key_back = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
    keyboard_markup.row(key_1)
    keyboard_markup.row(key_2)
    keyboard_markup.row(key_3)
    keyboard_markup.row(key_4)
    keyboard_markup.row(key_5)
    keyboard_markup.row(key_6)
    keyboard_markup.row(key_7)
    keyboard_markup.row(key_8)
    keyboard_markup.row(key_back)
    return keyboard_markup


def main_create(message): #создание главного меню
    keyboard_markup = main_keyboard()
    bot.send_message(message.chat.id,'Вы в главном меню', parse_mode='html', reply_markup=keyboard_markup)

def main_edit(message): #редактирование предыдущего сообщения в главное меню
    keyboard_markup = main_keyboard()
    bot.edit_message_text('Вы в главном меню',message.chat.id, message.message_id, parse_mode='html', reply_markup=keyboard_markup)


@bot.callback_query_handler(func=lambda call:True)
def answer(call):
    if call.data == 'hi': #кнопка о чат боте
        keyboard_back = types.InlineKeyboardMarkup()
        key_back = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
        keyboard_back.add(key_back)
        bot.edit_message_text('Привет. Меня зовут <b>Газзи</b>. Я чат-Бот, который поможет Вам узнать информацию о бесплатной газификации населения.',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_back,
                              parse_mode='html')
    elif call.data == 'main_menu': #кнопка главное меню
        main_edit(call.message)
    elif call.data == 'tsur':
        keyboard_back = types.InlineKeyboardMarkup()
        key_back = types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu')
        keyboard_back.add(key_back)
        bot.edit_message_text('Подписывайтесь на наш телеграмканал',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_back,
                              parse_mode='html')
    elif call.data == 'main_start': # вход кнопку начать
        keyboard_start = main_start_keyboard()
        bot.edit_message_text('Выбирете интересующий вас пункт',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_start,
                              parse_mode='html')


bot.polling(none_stop=True)
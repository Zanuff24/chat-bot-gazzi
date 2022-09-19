import csv

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
    key_7 = types.InlineKeyboardButton(text='Как подать заявку', callback_data='b7')
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


def create_keyboard_back(): #создание клавиатуры из кнопки НАЗАД
    keyboard_back = types.InlineKeyboardMarkup()
    key_back = types.InlineKeyboardButton(text='Назад', callback_data='main_menu')
    keyboard_back.add(key_back)
    return keyboard_back

def main_create(message): #создание главного меню
    keyboard_markup = main_keyboard()
    bot.send_message(message.chat.id,'Вы в главном меню', parse_mode='html', reply_markup=keyboard_markup)

def main_edit(message): #редактирование предыдущего сообщения в главное меню
    keyboard_markup = main_keyboard()
    bot.edit_message_text('Вы в главном меню',message.chat.id, message.message_id, parse_mode='html', reply_markup=keyboard_markup)


@bot.callback_query_handler(func=lambda call:True)
def answer(call):


    if call.data == 'hi': #кнопка о чат боте
        keyboard_back = create_keyboard_back()
        bot.edit_message_text('Привет. Меня зовут <b>Газзи</b>. Я чат-Бот, который поможет Вам узнать информацию о бесплатной газификации населения.',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_back,
                              parse_mode='html')
    elif call.data == 'main_menu': #кнопка главное меню
        main_edit(call.message)
    elif call.data == 'tsur':
        keyboard_back = create_keyboard_back()
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


    elif call.data == 'b1':
        keyboard_start = main_start_keyboard()
        bot.edit_message_text('От газовой трубы, которая проложена в населенном пункте, до границы домовладения газ будут обязаны подвести за счет средств государства.\nА уже непосредственно на территории своего земельного участка подключение к дому гражданин будет оплачивать сам',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_start,
                              parse_mode='html')
    elif call.data == 'b2':
        keyboard_start = main_start_keyboard()
        bot.edit_message_text('1.Участок должен находиться от газопровода на расстоянии не более чем 200 метров.\n2. Площадь частного жилого дома не должна превышать 300 кв.метров\n3. Мощность газового оборудования в доме не должна превышать 7 кубометров в час',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_start,
                              parse_mode='html')
    elif call.data == 'b3':
        keyboard_start = main_start_keyboard()
        bot.edit_message_text('АО "Газпром газораспределение Майкоп"\n8 800 200 66 04\nhttp://adyggaz.ru/dogazifikacziya/',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_start,
                              parse_mode='html')
    elif call.data == 'b4':
        keyboard_start = main_start_keyboard()
        bot.edit_message_text('Заявителем на подключение газа могут выступать физические и юридические лица, владеющие объектом на праве собственности.\nВозможны несколько вариантов:\n1. Если у дома только один собственник, он подает заявление по собственному решению;\n2. При наличии нескольких совершеннолетних собственников, каждый из них должен дать свое согласие на газификацию (за детей-собственников согласие дают родители, опекуны или попечители);\n3. Cобственники могут поручить все формальности представителю, однако для этого нужно оформить доверенность через нотариат.',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_start,
                              parse_mode='html')
    elif call.data == 'b5':
        keyboard_start = main_start_keyboard()
        bot.edit_message_text('Какие этапы у подключения к газу?\n1. Подача заявки\n2. Определение технической возможности подключения\n3. Заключение договора\n4. Подготовка домовладения (приобретение и монтаж оборудования)\n5. Технологическое присоединение',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_start,
                              parse_mode='html')
    elif call.data == 'b6':
        keyboard_start = main_start_keyboard()
        bot.edit_message_text('1. Если вы живете в доме, но не являетесь ни собственником, ни арендатором, ваша заявка будет отклонена.\n2. Если дом еще не построен, и отсутствует  наличие прав на земельный участок, заявка будет отклонена.',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_start,
                              parse_mode='html')
    elif call.data == 'b7':
        keyboard_start = main_start_keyboard()
        bot.edit_message_text('Необходимо подготовить пакет документов и отправить заявку. На данный момент это делается через газораспределительную организацию (ГРО). На рассмотрение заявки у нее есть 15 рабочих дней. \nВ дальнейшем все будет организовано по принципу «единого окна» через заключение комплексных договоров.\nПодача заявок также будет реализована через МФЦ или портал «Госуслуги». \nМфц (контакты)  8(8772)52-64-64\nГде подать заявку?\nЕдиный центр предоставления услуг по адресу: г. Майкоп, ул. Апшеронская, 4;\nфилиалы \"Газпром газораспределение Майкоп\" в муниципальных образованиях;\nмногофункциональные центры «Мои документы»; \nна сайте \"Газпром газораспределение Майкоп\" adyggaz.ru;\nна портале догазификации https://connectgas.ru.',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_start,
                              parse_mode='html')
    elif call.data == 'b8':
        keyboard_start = main_start_keyboard()
        bot.edit_message_text('В: Я сам провел газ. Вернут ли мне деньги?\nО: нет\n\nЧто такое догазификация?\nДогазификация — подведение газа до границ негазифицированных домовладений в газифицированных населенных пунктах без привлечения средств потребителей. Согласно Поручению Правительства Российской Федерации, она должна быть обеспечена до 2023 года в газифицированных населенных пунктах для домовладений, расположенных вблизи от внутрипоселковых газопроводов, при наличии соответствующей заявки.\n\nКакие критерии для соответствия догазификации?\n\nВ случае, если ваш индивидуальный жилой дом и земельный участок зарегистрированы в установленном порядке, и дом расположен в населенном пункте, который уже газифицирован, Вы попадете в программу ускоренной социальной газификации (догазификации).\nКакие работы при догазификации делаются бесплатно, за какие нужно платить?\n\nБезвозмездно проводится подведение газа до границ земельного участка, все работы внутри домовладения (монтаж сетей, приобретение и монтаж газового оборудования) проводятся за счет собственника.\n\nЯ подал заявку - когда мне проведут газ?\n\nВ договоре будут указаны предельные сроки осуществления подключения, в зависимости от протяженности газопровода, который требуется построить газораспределительной организации до границы Вашего земельного участка. Срок подключения также учитывает время, требующееся для выполнения мероприятий в границах Вашего земельного участка, а именно: прокладку сети газопотребления, внутреннего газопровода по дому, монтаж газоиспользующего оборудования.\nМогут ли мне отказать после того, как я подал заявку?\nМогут, если Вы представите не полный комплект документов или данные будут заполнены некорректно.\nТакже, если параметры подключения Вашего индивидуального жилого дома не будут соответствовать критериям, а именно дом не зарегистрирован или расположен в негазифицированном населенном пункте.',
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=keyboard_start,
                              parse_mode='html')

bot.polling(none_stop=True)
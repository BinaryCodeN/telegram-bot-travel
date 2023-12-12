# Бот будет незаменимым помощником для подбора увлекательного маршрута
# В планах:
# При выводе топ 10 показывать только список городов и, если человека какой-то из этих городов заинтересует, в ссылке
# под этим городом вывести текст

import telebot
import random
from telebot import types
from cities import variants, top10
from API import bot_tg_API, yandex_api_key
from Aviasales import first_step
import requests

bot: telebot.TeleBot = telebot.TeleBot(bot_tg_API)

for_button_dict = {}


# Для разработчика вывод инфы
@bot.message_handler(commands=['inf'])
def main(message):
    bot.send_message(message.chat.id, message)


# Приветствие при команде START
@bot.message_handler(commands=['start'])
def start(message: types.Message):
    if message.from_user.last_name is not None and message.from_user.first_name is not None:
        bot.send_message(message.chat.id,
                         f"Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}! \nЧтобы"
                         f"продолжить подбор города, нажмите '→' или выберите команду /choose из списка 'Меню'",
                         reply_markup=next_button())
    elif message.from_user.last_name is None and message.from_user.first_name is not None:
        bot.send_message(message.chat.id,
                         f"Здравствуй, {message.from_user.first_name}! \nЧтобы продолжить подбор города, "
                         f"нажмите '→' или выберите команду /choose из списка 'Меню'",
                         reply_markup=next_button())


def next_button() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup(row_width=1)
    next_start_choose = types.InlineKeyboardButton('→', callback_data='next_start_choose')
    markup.add(next_start_choose)
    return markup


# # --------------------------------------------------------------------------------------------------------------------
def start_choose(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    rand_route = types.InlineKeyboardButton('Случайный маршрут', callback_data='rand_route')
    top10m = types.InlineKeyboardButton('Топ 10 маршрутов', callback_data='top10m')
    next1 = types.InlineKeyboardButton('Продолжить подбор маршрута', callback_data='next1')
    markup.add(rand_route, top10m, next1)
    # Текст, выводимый над кнопками
    bot.send_message(message.chat.id, "Всем пользователям данного бота - добро пожаловать!🙂\n"
                                      "Он будет для вас незаменимым путеводителем в любой точке России. "
                                      "Попробуйте и убедитесь сами!", reply_markup=markup)


# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

# Действия при нажатиии кнопки "CHOOSE"
@bot.message_handler(commands=['choose'])
def button(message):  # действия для связки с "ПРОДОЛЖИТЬ ПОДБОР МАРШРУТА"
    start_choose(message)


# Распределение действий на каждую команду с конопк в choose
@bot.callback_query_handler(func=lambda call: True)
def callback(call: types.CallbackQuery):
    print(call.data)
    if call.data == 'rand_route':  # рандомное определение города для поездки
        markup = types.InlineKeyboardMarkup(row_width=1)
        next1 = types.InlineKeyboardButton('→', callback_data='next1')
        markup.add(next1)
        bot.send_message(call.message.chat.id, random.choice(variants))
        bot.send_message(call.message.chat.id, "Для дальнейшего составления маршрута, нажмите '→'", reply_markup=markup)

    elif call.data == 'top10m':  # топ 10 городов
        markup = types.InlineKeyboardMarkup(row_width=1)
        next1 = types.InlineKeyboardButton('→', callback_data='next1')
        markup.add(next1)
        bot.send_message(call.message.chat.id, top10)
        bot.send_message(call.message.chat.id, "Для дальнейшего составления маршрута, нажмите '→'", reply_markup=markup)

    elif call.data == 'next_start_choose':  # функция для связки
        for_button_dict[call.message.chat.id] = {}
        start_choose(call.message)

    elif call.data == 'next1':
        markup = types.InlineKeyboardMarkup()
        k1 = types.InlineKeyboardButton(text='Субтропический:\nиюль:+22, январь:+6', callback_data='Субтропический')
        k2 = types.InlineKeyboardButton('Муссонный:\nиюль:+16, январь:-16', callback_data='Мусонный')
        k3 = types.InlineKeyboardButton('Резко-континентальный:\nиюль:+18, январь:-40',
                                        callback_data='Резко-континентальный')
        k4 = types.InlineKeyboardButton('Континентальный:\nиюль:+18, январь:-20', callback_data='Континентальный')
        k5 = types.InlineKeyboardButton('Умеренно-континентальный:\nиюль:+18, январь:-10',
                                        callback_data='Умеренно-континентальный')
        k6 = types.InlineKeyboardButton('Субарктический:\nиюль:+12, январь:-32', callback_data='Субарктический')
        k7 = types.InlineKeyboardButton('Арктический:\nиюль:+6, январь:-28', callback_data='Арктический')
        #next2 = types.InlineKeyboardButton('→', callback_data='климат')
        back1 = types.InlineKeyboardButton('←', callback_data='back1')
        markup.add(k1)
        markup.add(k2)
        markup.add(k3)
        markup.add(k4)
        markup.add(k5)
        markup.add(k6)
        markup.add(k7)
        markup.add(back1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Укажите подходящий температурный диапазон', reply_markup=markup)
    elif call.data == 'back1':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text, reply_markup=button(message=call.message))
        start_choose(call.message)

        # bot.send_message(call.message.chat.id, text='Мусонный', reply_markup=time_buttons(['+6', '+7', '+8']))
        # bot.send_message(call.message.chat.id, text='Резко-континентальный', reply_markup=time_buttons(['+2', '+4', '+3']))

    # надо чтоб новообразовавшаяся кнопка переходила прямиком в
    elif call.data == 'Субтропический':
        # bot.send_message(call.message.chat.id, text='Субтропический', reply_markup=time_buttons(['+1', '+2', '+3']))
        inline_markup1 = types.InlineKeyboardMarkup()
        item_alone = types.InlineKeyboardButton(text=call.data, callback_data='next2')
        back = types.InlineKeyboardButton(text='←', callback_data='next1')
        inline_markup1.add(back, item_alone)
        bot.edit_message_text(text='Выберите подходящий часовой пояс:', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=time_buttons(['0', '+1']))
        for_button_dict[call.message.chat.id]['климат'] = 'Субтропический'
        # bot.message_handler()

    elif call.data == 'Мусонный':
        inline_markup1 = types.InlineKeyboardMarkup()
        item_alone = types.InlineKeyboardButton(text=call.data, callback_data='next2')
        back = types.InlineKeyboardButton(text='←', callback_data='next1')
        inline_markup1.add(back, item_alone)
        bot.edit_message_text(text='Выберите подходящий часовой пояс:', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=time_buttons(['+7', '+8', '+9']))
        for_button_dict[call.message.chat.id]['климат'] = 'Мусонный'

    elif call.data == 'Резко-континентальный':
        inline_markup1 = types.InlineKeyboardMarkup()
        item_alone = types.InlineKeyboardButton(text=call.data, callback_data='next2')
        back = types.InlineKeyboardButton(text='←', callback_data='next1')
        inline_markup1.add(back, item_alone)
        bot.edit_message_text(text='Выберите подходящий часовой пояс:', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=time_buttons(['+2', '+3', '+4', '+5']))
        for_button_dict[call.message.chat.id]['климат'] = 'Резко-континентальный'

    elif call.data == 'Континентальный':
        inline_markup1 = types.InlineKeyboardMarkup()
        item_alone = types.InlineKeyboardButton(text=call.data, callback_data='next2')
        back = types.InlineKeyboardButton(text='←', callback_data='next1')
        inline_markup1.add(back, item_alone)
        bot.edit_message_text(text='Выберите подходящий часовой пояс:', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=time_buttons(['+2', '+3', '+4']))
        for_button_dict[call.message.chat.id]['климат'] = 'Континентальный'

    elif call.data == 'Умеренно-континентальный':
        inline_markup1 = types.InlineKeyboardMarkup()
        item_alone = types.InlineKeyboardButton(text=call.data, callback_data='next2')
        back = types.InlineKeyboardButton(text='←', callback_data='next1')
        inline_markup1.add(back, item_alone)
        bot.edit_message_text(text='Выберите подходящий часовой пояс:', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=time_buttons(['-1', '0', '+1', '+2']))
        for_button_dict[call.message.chat.id]['климат'] = 'Умеренно-континентальный'

    elif call.data == 'Субарктический':
        inline_markup1 = types.InlineKeyboardMarkup()
        item_alone = types.InlineKeyboardButton(text=call.data, callback_data='next2')
        back = types.InlineKeyboardButton(text='←', callback_data='next1')
        inline_markup1.add(back, item_alone)
        bot.edit_message_text(text='Выберите подходящий часовой пояс: ', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=time_buttons(['0', '+2', '+8', '+9']))
        for_button_dict[call.message.chat.id]['климат'] = 'Субарктический'

    elif call.data == 'Арктический':
        inline_markup1 = types.InlineKeyboardMarkup()
        item_alone = types.InlineKeyboardButton(text=call.data, callback_data='next2')
        back = types.InlineKeyboardButton(text='←', callback_data='next1')
        inline_markup1.add(back, item_alone)
        bot.edit_message_text(text= 'Выберите подходящий часовой пояс:', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=time_buttons(['+7', '+8', '+9']))
        for_button_dict[call.message.chat.id]['климат'] = 'Арктический'
        print(for_button_dict)

    # Часовой пояс
    elif call.data == 'next2':  # 'inline_markup':
        markup = types.InlineKeyboardMarkup(row_width=3)
        t1 = types.InlineKeyboardButton('-1 от МСК', callback_data='-1')
        t2 = types.InlineKeyboardButton('0 от МСК', callback_data='0')
        t3 = types.InlineKeyboardButton('+1 к МСК', callback_data='+1')
        t4 = types.InlineKeyboardButton('+2 к МСК', callback_data='+2')
        t5 = types.InlineKeyboardButton('+3 к МСК', callback_data='+3')
        t6 = types.InlineKeyboardButton('+4 к МСК', callback_data='+4')
        t7 = types.InlineKeyboardButton('+5 к МСК', callback_data='+5')
        t8 = types.InlineKeyboardButton('+6 к МСК', callback_data='+6')
        t9 = types.InlineKeyboardButton('+7 к МСК', callback_data='+7')
        t10 = types.InlineKeyboardButton('+8 к МСК', callback_data='+8')
        t11 = types.InlineKeyboardButton('+9 к МСК', callback_data='+9')
        next3 = types.InlineKeyboardButton('→', callback_data='next3')
        back = types.InlineKeyboardButton('←', callback_data='next1')
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, next3, back)
        bot.edit_message_text(chat_id=call.message.chat.id, text='Выберите подходящий часовой пояс:',
                              message_id=call.message.message_id, reply_markup=markup)
        # bot.edit_message_text(call.message.chat.id, call.message.id, reply_markup=None)

    elif call.data == '-1':
        # inline_markup1 = types.InlineKeyboardMarkup()
        # item_alone = types.InlineKeyboardButton(text=call.data, callback_data='next3')
        # back = types.InlineKeyboardButton(text='←', callback_data='next2')
        # inline_markup1.add(back, item_alone)
        # bot.edit_message_text(text=call.message.text, message_id=call.message.message_id, chat_id=call.message.chat.id,
        #                       reply_markup=inline_markup1)

        # bot.edit_message_text(text=call.message.text, message_id=call.message.message_id, chat_id=call.message.chat.id,
        #                       reply_markup=for_time(call))
        bot.edit_message_text(text='Далее вы можете продолжить построение маршрута или'
                                   '\nвернуться к выбору климата', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=for_time(call))
        for_button_dict[call.message.chat.id]['время'] = '-1'
        print(for_button_dict)

    elif call.data == '0':
        bot.edit_message_text(text='Далее вы можете продолжить построение маршрута или'
                                   '\nвернуться к выбору климата', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=for_time(call))
        for_button_dict[call.message.chat.id]['время'] = '0'

    elif call.data == '+1':
        bot.edit_message_text(text='Далее вы можете продолжить построение маршрута или'
                                   '\nвернуться к выбору климата', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=for_time(call))
        for_button_dict[call.message.chat.id]['время'] = '+1'

    elif call.data == '+2':
        bot.edit_message_text(text='Далее вы можете продолжить построение маршрута или'
                                   '\nвернуться к выбору климата', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=for_time(call))
        for_button_dict[call.message.chat.id]['время'] = '+2'
        print(for_button_dict)

    elif call.data == '+3':
        bot.edit_message_text(text='Далее вы можете продолжить построение маршрута или'
                                   '\nвернуться к выбору климата', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=for_time(call))
        for_button_dict[call.message.chat.id]['время'] = '+3'

    elif call.data == '+4':
        bot.edit_message_text(text='Далее вы можете продолжить построение маршрута или'
                                   '\nвернуться к выбору климата', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=for_time(call))
        for_button_dict[call.message.chat.id]['время'] = '+4'

    elif call.data == '+5':
        bot.edit_message_text(text='Далее вы можете продолжить построение маршрута или'
                                   '\nвернуться к выбору климата', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=for_time(call))
        for_button_dict[call.message.chat.id]['время'] = '+5'

    elif call.data == '+6':
        bot.edit_message_text(text='Далее вы можете продолжить построение маршрута или'
                                   '\nвернуться к выбору климата', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=for_time(call))
        for_button_dict[call.message.chat.id]['время'] = '+6'

    elif call.data == '+7':
        bot.edit_message_text(text='Далее вы можете продолжить построение маршрута или'
                                   '\nвернуться к выбору климата', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=for_time(call))
        for_button_dict[call.message.chat.id]['время'] = '+7'

    elif call.data == '+8':
        bot.edit_message_text(text='Далее вы можете продолжить построение маршрута или'
                                   '\nвернуться к выбору климата', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=for_time(call))
        for_button_dict[call.message.chat.id]['время'] = '+8'

    elif call.data == '+9':
        bot.edit_message_text(text='Далее вы можете продолжить построение маршрута или'
                                   '\nвернуться к выбору климата', message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=for_time(call))
        for_button_dict[call.message.chat.id]['время'] = '+9'

    # elif call.data == '-1':
    #     inline_markup = types.InlineKeyboardMarkup()
    #     item_alone = types.InlineKeyboardButton(text=call.data, callback_data=call.data)
    #     inline_markup.add(item_alone)
    #     bot.edit_message_text(text=call.message.text, message_id=call.message.message_id, chat_id=call.message.chat.id,
    #                           reply_markup=inline_markup)

    # elif call.data == 'next3':
    #     markup = types.InlineKeyboardMarkup(row_width=2)
    #     c1 = types.InlineKeyboardButton('до 3000р.', callback_data='с1')
    #     c2 = types.InlineKeyboardButton('от 3000р. до 5000р.', callback_data='с2')
    #     c3 = types.InlineKeyboardButton('от 5000р. до 7000р.', callback_data='с3')
    #     c4 = types.InlineKeyboardButton('от 7000 до 10000р.', callback_data='с4')
    #     c5 = types.InlineKeyboardButton('от 10000 до 13000р.', callback_data='с5')
    #     c6 = types.InlineKeyboardButton('от 13000 до 16000р.', callback_data='с6')
    #     c7 = types.InlineKeyboardButton('от 16000 до 19000р.', callback_data='с7')
    #     c8 = types.InlineKeyboardButton('от 19000 до 24000р.', callback_data='с8')
    #     next4 = types.InlineKeyboardButton('→', callback_data='next4')
    #     markup.add(c1, c2, c3, c4, c5, c6, c7, c8, next4)
    #
    #     bot.send_message(call.message.chat.id, 'Последним этапом подбора маршрута будет расчет бюджета:', reply_markup=markup)

    # elif call.data == 'c1':
    #     bot.edit_message_text(text=call.message.text, message_id=call.message.message_id, chat_id=call.message.chat.id)

    elif call.data == 'next3':
        p(call.message)

    elif call.data == 'next4':  # После определения с местом полёта, для поиска дешевого авиабилета введите пункт отправления:
        # генерация городов/маршрутов отправления по заданным пользователем критериям
        first_step(call.message, bot)


def time_buttons(mas: list) -> types.InlineKeyboardMarkup:
    inline_markup: types.InlineKeyboardMarkup = types.InlineKeyboardMarkup()
    for x in mas:
        item = types.InlineKeyboardButton(text=x, callback_data=x)
        inline_markup.add(item)
    return inline_markup


from functools import lru_cache


@lru_cache(maxsize=1)
def buttons() -> types.InlineKeyboardMarkup:
    item = types.InlineKeyboardButton(text='a', callback_data='+1')
    markup = types.InlineKeyboardMarkup()
    markup.add(item)
    return markup


# @bot.message_handler(commands=['t'])
# def time(call):
#     time = ['-1', '0', '+1', '+2', '+3', '+4', '+5', '+6', '+7', '+8', '9']
#     for x in range(len(time)):
#         if call.data == 'Субтропический':
#             markup = types.InlineKeyboardMarkup()
#             choose_time = types.InlineKeyboardButton(text = '0', callback_data= '0')
#             markup.add(choose_time)
#         if call.data == 'Мусонный':
#             markup = types.InlineKeyboardMarkup()
#             choose_time = types.InlineKeyboardButton(text='+8', callback_data='+8')
#             markup.add(choose_time)
#     bot.send_message(call.chat.id, 'fgbf')


def for_time(call):
    inline_markup1 = types.InlineKeyboardMarkup()
    item_alone = types.InlineKeyboardButton(text='→', callback_data='next3')
    back = types.InlineKeyboardButton(text='←', callback_data='next1')
    inline_markup1.add(back, item_alone)
    return inline_markup1


# @bot.message_handler(commands=['p'])
def p(message: types.Message):
    towns_sub0 = ['Сочи', 'Туапсе', 'Анапа', 'Геленджик', 'Ялта', 'Новороссийск', 'Севастополь', 'Магас']
    towns_sub1 = ['Самара', 'Ижевск', 'Ульяновск', 'Нижнекамск']
    towns_mus9 = ['Благовещенск', 'Тында', 'Архара']
    towns_mus7 = ['Владивосток', 'Хабаровск', 'Николаевск', 'Находка', 'Уссурийск']
    towns_mus8 = ['Южно-Сахалинск', 'Комсомольск-на-Амуре', 'Амурск', 'Нижнетамбовское']
    towns_rezk2 = ['Новосибирск', 'Красноярск', 'Кемерово', 'Томск']
    towns_rezk3 = ['Барнаул', 'Горно-Алтайск', 'Новокузнецк']
    towns_rezk4 = ['Кызыл', 'Абакан', ' Красноярск', 'Ачинск']
    towns_rezk5 = ['Усть-Илимск', 'Иркутск', 'Улан-Удэ', 'Чита', 'Бодайбо']
    towns_kont2 = ['Екатеринбург', 'Сургут', 'Челябинск', 'Тюмень', 'Тобольск']
    towns_kont3 = ['Омск', 'Томск', 'Новосибирск', 'Барнаул']
    towns_kont4 = ['Норильск', 'Кемерово', 'Красноярск', 'Норильск', 'Ванавара']
    towns_ymkont0 = ['Калининград', 'Москва Шереметьево/Домодедово/Жуковский/Внуково', 'Вологда', 'Тверь', 'Брянск', 'Орел', 'Курск', 'Санкт-Петербург', 'Псков',
                     'Смоленск', 'Калуга', 'Воронеж', 'Липецк', 'Казань']
    # 'Красноярск', 'Иркутск', 'Чита', 'Братск'
    towns_ymkont1 = ['Самара', 'Волгоград', 'Саратов', 'Ульяновск']
    towns_ymkont2 = ['Пермь', 'Уфа', 'Оренбург', 'Сыктывкар', 'Печора']
    towns_subar0 = ['Мурманск', 'Архангельск', 'Сыктывкар', 'Петрозаводск', 'Нарьян-Мар']
    towns_subar2 = ['Салехард', 'Надым', 'Ноябрьск', 'Муравленко', 'Новый Уренгой']
    # towns_subar4 = []
    # towns_subar6 = []
    towns_subar8 = ['Певек', 'Хатанга', 'Среднеколымск']
    towns_subar9 = ['Мурманск', 'Салехард', 'Анадырь', 'Норильск', 'Кировск', 'Якутск', 'Томск', 'Ханты-Мансийск',
                    'Чита']
    # towns_arct6 = ['Омск', 'Красноярск']
    towns_arct7 = ['Норильск', 'Дудинка', 'Новый Уренгой', 'Тазовский', 'Надым']
    towns_arct8 = ['Певек', 'Анадырь', 'Билибино', 'Магадан', 'Якутск']
    towns_arct9 = ['Мурманск', 'Норильск', 'Салехард', 'Анадырь', 'Певек']
    dict_cities = {'Субтропический': {'0': towns_sub0, '+1': towns_sub1},
                   'Мусонный': {'+9': towns_mus9, '+7': towns_mus7, '8': towns_mus8},
                   'Резко-континентальный': {'+2': towns_rezk2, '+3': towns_rezk3, '+4': towns_rezk4,
                                             '+5': towns_rezk5},
                   'Континентальный': {'+2': towns_kont2, '+3': towns_kont3, '+4': towns_kont4},
                   'Умеренно-континентальный': {'-1': towns_ymkont0, '0': towns_ymkont0, '+1': towns_ymkont1,
                                                '+2': towns_ymkont2},
                   'Субарктический': {'0': towns_subar0, '+2': towns_subar2, '+8': towns_subar8, '+9': towns_subar9},
                   'Арктический': {'+7': towns_arct7, '+8': towns_arct8, '+9': towns_arct9}}
    # ['+4', '+6', '+7', '+8', '+9']
    # dict_cities = {'Субтропический': {'-1': townssub, '0': townssub0, '+1': townssub1, '+2': townssub2}, 'Мусонный': {'+6': townsmus6, '+7': townsmus7, '+8': townsmus8}, 'Резко-континентальный': {'+2': , '+3': ,'+4': }}

    climate = for_button_dict[message.chat.id]['климат']
    time = for_button_dict[message.chat.id]['время']
    cities = 'Ваши города прибытия:'
    used_cities = []
    while len(used_cities) != 3:
        r = random.randint(0, len(dict_cities[climate][time]) - 1)
        if dict_cities[climate][time][r] in used_cities:
            pass
        else:
            used_cities.append(dict_cities[climate][time][r])
            cities += ('\n' + str(len(used_cities)) + '. ' + dict_cities[climate][time][r])
    item = types.InlineKeyboardButton(text='→', callback_data='next4')
    item2 = types.InlineKeyboardButton(text='←', callback_data='next1')
    inline_markup = types.InlineKeyboardMarkup().add(item2, item)
    # bot.send_message(chat_id=message.chat.id, text = cities, reply_markup=inline_markup)
    bot.edit_message_text(text=cities, message_id=message.message_id, chat_id=message.chat.id,
                          reply_markup=inline_markup)


@bot.message_handler(content_types=['location'])
def handle_location(message: telebot.types.Message):
    # Получаем координаты из сообщения
    latitude = message.location.latitude
    longitude = message.location.longitude
    user_location = f"{longitude}, {latitude}"
    print(user_location)
    bot.send_message(message.chat.id, "Теперь отправьте место, до которого построить маршрут: ",
                     reply_markup=types.ReplyKeyboardRemove())

    bot.register_next_step_handler(message, handle_text, latitude, longitude)


def handle_text(message: telebot.types.Message, latitude, longitude):
    # Получаем адрес от пользователя
    destination = message.text
    print(destination)

    # Получаем координаты выбранной точки с помощью Геокодера Яндекс API
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={yandex_api_key}&format=json&geocode={destination}&"
    response = requests.get(url)
    data = response.json()
    print(data)
    coordinates = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    print(coordinates)
    dest_longitude, dest_latitude = map(float, coordinates.split())
    print(map(float, coordinates.split()))
    # maps = f"https://yandex.ru/maps/?ll={latitude}%2C{longitude}&mode=routes&rtext={dest_latitude}%2C{dest_longitude}~{latitude}%2C{longitude}&rtt=pd&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1MzAwMDExNxIc0JHQtdC70LDRgNGD0YHRjCwg0JzRltC90YHQuiIKDQ5y3EEVZpxXQg%2C%2C~ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1MzAwMDA5MxIr0KDQvtGB0YHQuNGPLCDQodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQsyIKDR2F8kEVUcFvQg%2C%2C&z=6.3"
    # response = requests.get(maps)
    # data = response.json()
    # print(data)
    # Отправляем сообщение с координатами точки и ссылкой на карту
    bot.send_message(message.chat.id, f"Координаты места: \nШирота {dest_latitude}, Долгота {dest_longitude}")
    # bot.send_message(message.chat.id,
    #                  f"Ссылка на карту: \nhttps://yandex.com/maps/?ll={dest_longitude},{dest_latitude}&z=12")
    bot.send_message(message.chat.id, f'Ссылка на карту: '
                                      f'\nhttps://yandex.ru/maps/?ll={latitude}%2C{longitude}&mode=routes&routes%5BactiveComparisonMode%5D=auto&routes%5BignoreTravelModes%5D=bicycle%2Cscooter&rtext={dest_latitude}%2C{dest_longitude}~{latitude}%2C{longitude}&rtt=comparison&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1MzE1MjgwNBIr0KDQvtGB0YHQuNGPLCDQodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQsyIKDRSE8kEVNMFvQg%2C%2C~ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1MzE2NjU2NhI70KDQvtGB0YHQuNGPLCDQmtGA0LDRgdC90L7QtNCw0YDRgdC60LjQuSDQutGA0LDQuSwg0KHQvtGH0LgiCg1z5B5CFYdXLkI%2C&source=serp_navig&z=5')
                     #f'Ссылка на карту: \nhttps://yandex.ru/maps/?ll={latitude}%2C{longitude}&mode=routes&rtext={dest_latitude}%2C{dest_longitude}~{latitude}%2C{longitude}&rtt=pd&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1MzAwMDExNxIc0JHQtdC70LDRgNGD0YHRjCwg0JzRltC90YHQuiIKDQ5y3EEVZpxXQg%2C%2C~ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1MzAwMDA5MxIr0KDQvtGB0YHQuNGPLCDQodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQsyIKDR2F8kEVUcFvQg%2C%2C&z=6.3')

    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("📝Оставьте отзыв", url='https://t.me/nensi_m')
    markup.add(button1)
    bot.send_message(message.chat.id, 'На этом подбор маршрута подошел к концу. '
                                      '\nСпасибо всем, кто выбрал данного бота для путешествия✨'.format(message.from_user),
                     reply_markup=markup)
    # Теперь можно использовать найденные координаты для построения маршрута или других действий


# def for_times(call):
#     inline_markup1 = types.InlineKeyboardMarkup()
#     item_alone = types.InlineKeyboardButton(text=call.data, callback_data='next4')
#     back = types.InlineKeyboardButton(text='←', callback_data='next2')
#     inline_markup1.add(back, item_alone)
#     bot.edit_message_text(text=call.message.text, message_id=call.message.message_id, chat_id=call.message.chat.id,
#                           reply_markup=inline_markup1)
#     return  inline_markup1


# Разработать систему релевантности: (8**11 вариантов) составления вариаций выбора города -> нужно добавить 214 358 881
# городов (может быть меньше, в зависимости он универсальности города)

# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
    # bot.polling(none_stop=True)

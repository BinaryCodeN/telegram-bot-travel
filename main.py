# Бот будет незаменимым помошником для подбора увлекательного маршрута
# В планах:
'''При выводе топ 10 показывать только список городов и ,если человека какой-то из этих городов заинтересует, в ссылке под этим городом вывести текст'''
import telebot
import random
from telebot import types
from cities import variants, top10
from API import bot_tg_API
# from API import aviasales

bot: telebot.TeleBot = telebot.TeleBot(bot_tg_API)


# Для разработчика вывод инфы
@bot.message_handler(commands=['inf'])
def main(message):
    bot.send_message(message.chat.id, message)


# Приветствие при команде START
@bot.message_handler(commands=['start'])
def start(message: types.Message):
    if message.from_user.last_name is not None and message.from_user.first_name is not None:
        bot.send_message(message.chat.id,
                         f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}! \nЧтобы '
                         f'продолжить нажмите "→" или выберите команду из списка "Меню"',
                         reply_markup=next_button())
    elif message.from_user.last_name is None and message.from_user.first_name is not None:
        bot.send_message(message.chat.id,
                         f'Здравствуй, {message.from_user.first_name}! \nЧтобы продолжить нажмите "→" или выберите '
                         f'команду из списка "Меню"',
                         reply_markup=next_button())


def next_button() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup(row_width=1)
    next = types.InlineKeyboardButton('→', callback_data='next_start_choose')
    markup.add(next)
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
def button(message): #действия для связки с ПРОДОЛЖИТЬ ПОДБОР МАРШРУТА
    start_choose(message)

# Распределение действий на каждую команду с конопк в choose
@bot.callback_query_handler(func=lambda call: True)
def callback(call: types.CallbackQuery):
    if call.data == 'rand_route':  # рандомное определение города для поездки
        markup = types.InlineKeyboardMarkup(row_width=1)
        next = types.InlineKeyboardButton('→', callback_data='next1')
        markup.add(next)
        bot.send_message(call.message.chat.id, random.choice(variants))
        bot.send_message(call.message.chat.id, "Для дальнейшего составления маршрута, нажмите '→'", reply_markup=markup)

    elif call.data == 'top10m':  # топ 10 городов
        markup = types.InlineKeyboardMarkup(row_width=1)
        next = types.InlineKeyboardButton('→', callback_data='next1')
        markup.add(next)
        bot.send_message(call.message.chat.id, top10)
        bot.send_message(call.message.chat.id,"Для дальнейшего составления маршрута, нажмите '→'", reply_markup=markup)

    elif call.data == 'next_start_choose': #функция для связки
        start_choose(call.message)

    elif call.data == 'next1':
        markup = types.InlineKeyboardMarkup(row_width=1)
        k1 = types.InlineKeyboardButton(text='Субтропический:\nиюль:+22, январь:+6', callback_data='k1')
        k2 = types.InlineKeyboardButton('Муссонный:\nиюль:+16, январь:-16', callback_data='k2')
        k3 = types.InlineKeyboardButton('Резко-континентальный:\nиюль:+18, январь:-40', callback_data='k3')
        k4 = types.InlineKeyboardButton('Континентальный:\nиюль:+18, январь:-20', callback_data='k4')
        k5 = types.InlineKeyboardButton('Умеренно-континентальный:\nиюль:+18, январь:-10', callback_data='k5')
        k6 = types.InlineKeyboardButton('Субарктический:\nиюль:+12, январь:-32', callback_data='k6')
        k7 = types.InlineKeyboardButton('Арктический:\nиюль:+6, январь:-28', callback_data='k7')
        next2 = types.InlineKeyboardButton('→', callback_data='next2')
        markup.add(k1, k2, k3, k4, k5, k6, k7, next2)
        bot.send_message(call.message.chat.id, 'Укажите подходящий температурный диапазон', reply_markup=markup)

    #надо чтоб новообразовавшаяся кнопка переходила прямиком в
    elif call.data == 'k1':
        inline_markup = types.InlineKeyboardMarkup()
        item_alone = types.InlineKeyboardButton(text=call.data, callback_data=call.data)
        inline_markup.add(item_alone)
        bot.edit_message_text(text=call.message.text, message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=inline_markup)
        bot.send_message(call.message.text, 'fvdv', reply_markup=inline_markup)

    # Часовой пояс
    elif call.data == 'next2': #'inline_markup':
        markup = types.InlineKeyboardMarkup(row_width=3)
        t1 = types.InlineKeyboardButton('-1 от МСК', callback_data='t1')
        t2 = types.InlineKeyboardButton('0 от МСК', callback_data='t2')
        t3 = types.InlineKeyboardButton('+1 к МСК', callback_data='t3')
        t4 = types.InlineKeyboardButton('+2 к МСК', callback_data='t4')
        t5 = types.InlineKeyboardButton('+3 к МСК', callback_data='t5')
        t6 = types.InlineKeyboardButton('+4 к МСК', callback_data='t6')
        t7 = types.InlineKeyboardButton('+5 к МСК', callback_data='t7')
        t8 = types.InlineKeyboardButton('+6 к МСК', callback_data='t8')
        t9 = types.InlineKeyboardButton('+7 к МСК', callback_data='t9')
        t10 = types.InlineKeyboardButton('+8 к МСК', callback_data='t10')
        t11 = types.InlineKeyboardButton('+9 к МСК', callback_data='t11')
        next3 = types.InlineKeyboardButton('→', callback_data='next3')
        markup.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, next3)
        bot.send_message(call.message.chat.id, 'Выберите подходящий часовой пояс:', reply_markup=markup)
        # bot.edit_message_text(call.message.chat.id, call.message.id, reply_markup=None)

    elif call.data == 't1':
        inline_markup = types.InlineKeyboardMarkup()
        item_alone = types.InlineKeyboardButton(text=call.data, callback_data=call.data)
        inline_markup.add(item_alone)
        bot.edit_message_text(text=call.message.text, message_id=call.message.message_id, chat_id=call.message.chat.id,
                              reply_markup=inline_markup)


    elif call.data == 'next3':
        markup = types.InlineKeyboardMarkup(row_width=2)
        c1 = types.InlineKeyboardButton('до 3000р.', callback_data='с1')
        c2 = types.InlineKeyboardButton('от 3000р. до 5000р.', callback_data='с2')
        c3 = types.InlineKeyboardButton('от 5000р. до 7000р.', callback_data='с3')
        c4 = types.InlineKeyboardButton('от 7000 до 10000р.', callback_data='с4')
        c5 = types.InlineKeyboardButton('от 10000 до 13000р.', callback_data='с5')
        c6 = types.InlineKeyboardButton('от 13000 до 16000р.', callback_data='с6')
        c7 = types.InlineKeyboardButton('от 16000 до 19000р.', callback_data='с7')
        c8 = types.InlineKeyboardButton('от 19000 до 24000р.', callback_data='с8')
        next4 = types.InlineKeyboardButton('→', callback_data='next4')
        markup.add(c1, c2, c3, c4, c5, c6, c7, c8, next4)

        bot.send_message(call.message.chat.id, 'Последним этапом подбора маршрута будет расчет бюджета:',
                         reply_markup=markup)

    elif call.data == 'c1':
        bot.edit_message_text(text=call.message.text, message_id=call.message.message_id, chat_id=call.message.chat.id)

    elif call.data == 'next4':
        #генерация городов/маршрутов отправления по заданным пользователем критериям
        bot.send_message(call.message.chat.id, 'После определения с местом полёта, для поиска дешевого авиабилета \n'
                                               'введите пункт отправления: ')




#Разработать систему релевантности: (8**11 вариантов) составления вариаций выбора города -> нужно добавить 214 358 881
# гродов (может быть меньше, в зависимости он универсальности города)

# def next_button2():
#     markup = types.InlineKeyboardMarkup()
#     next = types.InlineKeyboardButton('>', callback_data='next')
#     markup.add(next)
#     return markup


# Если пользователь нажал Next, нужно задать наводящие вопросы, по типу: какой климат, зона страны, бюджет
# Действия для кнопки Next
def on_click_Next(call):
    if call.data == 'next1':
        markup = types.InlineKeyboardMarkup(row_width=1)
        # markup = types.InlineKeyboardMarkup(row_width=1)
        climate = types.InlineKeyboardButton('Подходящий климат', callback_data='climate')
        zone = types.InlineKeyboardButton('Территориальная зона России', callback_data='zone')
        budget = types.InlineKeyboardButton('Бюджет', callback_data='budget')
        markup.add(climate, zone, budget)
        bot.send_message(call.data.call.id, 'Выберите действие: ', reply_markup=markup)


# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)

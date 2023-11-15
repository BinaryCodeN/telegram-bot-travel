# Бот будет незаменимым помошником для подбора увлекательного маршрута
# В планах:
'''При выводе топ 10 показывать только список городов и ,если человека какой-то из этих городов заинтересует, в ссылке под этим городом вывести текст'''
import telebot
import random
from telebot import types
from cities import variants, top10
from API import bot_tg_API

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
                         f'продолжить нажмите ">" или выберите команду из списка "Меню"',
                         reply_markup=next_button())
    elif message.from_user.last_name is None and message.from_user.first_name is not None:
        bot.send_message(message.chat.id,
                         f'Здравствуй, {message.from_user.first_name}! \nЧтобы продолжить нажмите ">" или выберите '
                         f'команду из списка "Меню"',
                         reply_markup=next_button())

def next_button() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup(row_width=1)
    next = types.InlineKeyboardButton('>', callback_data='next')
    markup.add(next)
    return markup

#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# @bot.callback_query_handler(func=lambda call: True)
# def next_choose(call: types.CallbackQuery):
#     if call.data == next_button():  # переход к choose
#         markup = types.InlineKeyboardMarkup(row_width=1)
#         next = types.InlineKeyboardButton(next_button(), commands='choose')
#         markup.add(next)
#         bot.send_message(call.message.chat.id, 'Next', reply_markup=markup)

# @bot.message_handler(commands=['next'])
# def button(message):
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     rand_route = types.InlineKeyboardButton('Случайный маршрут', callback_data='rand_route')
#     top10m = types.InlineKeyboardButton('Топ 10 маршрутов', callback_data='top10m')
#     next1 = types.InlineKeyboardButton('Продолжить подбор маршрута', callback_data='next1')
#     markup.add(rand_route, top10m, next1)
#     # Текст, выводимый над кнопками
#     bot.send_message(message.chat.id, "Всем пользователям данного бота - добро пожаловать!🙂\n"
#                                       "Он будет для вас незаменимым путеводителем в любой точке России. "
#                                       "Попробуйте и убедитесь сами!", reply_markup=markup)
# def next_start(message: types.CallbackQuery):
#     if message.data == next_button():  #если срабатывает нажатие next_button

# # --------------------------------------------------------------------------------------------------------------------

# Действия при нажатиии кнопки "CHOOSE"
@bot.message_handler(commands=['choose'])
def button(message):
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

# Распределение действий на каждую команду с конопк в choose
@bot.callback_query_handler(func=lambda call: True)
def callback(call: types.CallbackQuery):
    if call.data == 'rand_route':  # рандомное определение города для поездки
        markup = types.InlineKeyboardMarkup(row_width=1)
        next = types.InlineKeyboardButton('Next', callback_data='next1')
        markup.add(next)
        bot.send_message(call.message.chat.id, random.choice(variants), reply_markup=markup)

    if call.data == 'top10m':  # топ 10 городов
        markup = types.InlineKeyboardMarkup(row_width=1)
        next = types.InlineKeyboardButton('Next', callback_data='next1')
        markup.add(next)
        bot.send_message(call.message.chat.id, top10, reply_markup=markup)

    # if call.data == 'next1':  # продолжить подбор
    #             markup = types.InlineKeyboardMarkup(row_width=1)
    #             climate = types.InlineKeyboardButton('Укажите подходящий климат', callback_data='climate')
    #             zone = types.InlineKeyboardButton('Территориальная зона России', callback_data='zone')
    #             budget = types.InlineKeyboardButton('Бюджет', callback_data='budget')
    #             markup.add(climate, zone, budget)
    #             bot.send_message(call.message.chat.id, 'Укажите значимые для Вас критерии', reply_markup=markup)
    ####↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
    if call.data == 'next1':
        markup = types.InlineKeyboardMarkup(row_width=1)
        t1 = types.InlineKeyboardButton('Субтропический:\nиюль:+22, январь:+6', callback_data='t1')
        t2 = types.InlineKeyboardButton('Муссонный:\nиюль:+16, январь:-16', callback_data='t2')
        t3 = types.InlineKeyboardButton('Резко-континентальный:\nиюль:+18, январь:-40', callback_data='t3')
        t4 = types.InlineKeyboardButton('Континентальный:\nиюль:+18, январь:-20', callback_data='t4')
        t5 = types.InlineKeyboardButton('Умеренно-континентальный:\nиюль:+18, январь:-10', callback_data='t5')
        t6 = types.InlineKeyboardButton('Субарктический:\nиюль:+12, январь:-32', callback_data='t6')
        t7 = types.InlineKeyboardButton('Арктический:\nиюль:+6, январь:-28', callback_data='t7')
        next = types.InlineKeyboardButton('>', callback_data='next')
        markup.add(t1, t2, t3, t4, t5, t6, t7, next)
        bot.send_message(call.message.chat.id, 'Укажите подходящий температурный диапазон', reply_markup=markup)
        #bot.send_message(call.message.chat.id, 'fvdv', reply_markup=next_button2())

def next_button2():
    markup = types.InlineKeyboardMarkup()
    next = types.InlineKeyboardButton('>', callback_data='next')
    markup.add(next)
    return markup


    # if call.data == 't1' or 't2'or't3'or't4'or't5'or't6':
    #     bot.send_message()



    

        ################# ЗАДАНИЕ: Разделить next1 на отдельные разделы, по типу УКАЖИТЕ ПОДХОДЯЩИЙ КЛИМАТ и выводятся варианты выбора,
        # затем после того, как пользователь выбирает выводится новое окно с заглавием ТЕРРИТОРИАЛЬНАЯ ЗОНА....

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


#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑



if __name__ == '__main__':

    while True:
        try:

            bot.polling(none_stop=True)
        except any as e:
            print(e)

# Запуск бота
bot.polling(none_stop=True, interval=0)

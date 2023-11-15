# '''import telebot
# import random
# from telebot import types
# from random import choice
#
# bot = telebot.TeleBot('6465619279:AAG2y1bq4RFzPtIz3WAp4Rh4LrorOIxbYCE')
#
# '''@bot.message_handler(commands = ['start'])
# def start(message):
#     #bot.send_message(message.chat.id, message)
#     #bot.send_message(message.chat.id, message.chat.id)
#     bot.send_message(message.chat.id, "Всем пользователям данного бота - добро пожаловать!\n"
#                                       "Он будет для вас незаменимым путеводителем в любой точке России. Попробуйте и убедитесь сами!")'''
#
'''@bot.message_handler(commands = ['start'])
def start(message):
    #bot.send_message(message.chat.id, message)
    #bot.send_message(message.chat.id, message.chat.id)
    bot.send_message(message.chat.id, "Всем пользователям данного бота - добро пожаловать!\n"
                                      "Он будет для вас незаменимым путеводителем в любой точке России. Попробуйте и убедитесь сами!")'''
#
#
#
# # приветствие при команде START
# @bot.message_handler(commands=['start'])
# def start(message):
#     if message.from_user.last_name is not None and message.from_user.first_name is not None:
#         bot.send_message(message.chat.id,
#                          f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}! \n Выберите, пожалуйста, команду из списка "Меню"')
#     elif message.from_user.last_name is None and message.from_user.first_name is not None:
#         bot.send_message(message.chat.id,
#                          f'Здравствуй, {message.from_user.first_name}! \n Выберите, пожалуйста, команду из списка "Меню"')
#     else:
#         pass
#
# # для разработчика вывод инфы
# @bot.message_handler(commands=['inf'])
# def main(message):
#     bot.send_message(message.chat.id, message)
# ########### Команды для каждой кнопки
# # @bot.message_handler(commands = ['first'])
# # def button(message):
#
#
# #
# @bot.message_handler(commands=['choose'])
# def button(message):
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     item = types.InlineKeyboardButton('Рандомный маршрут', callback_data='b1')
#     item2 = types.InlineKeyboardButton('Топ 10 маршрутов', callback_data='b2')
#     item3 = types.InlineKeyboardButton('Продолжить подбор маршрута', callback_data='b3')
#     markup.add(item, item2, item3)
#
#     bot.send_message(message.chat.id, "Всем пользователям данного бота - добро пожаловать!\n"
#                                       "Он будет для вас незаменимым путеводителем в любой точке России. Попробуйте и убедитесь сами!",
#                      reply_markup=markup)
#
#
#
# '''variants = ['Сочи, Санкт-Петербург, Тыва, Шахты']
#
# @bot.message_handler(content_types=['text', 'photo'])
# def messagelist(message):
#   if message.text == 'Нажми на кнопку, и я отправлю тебе название':
#     bot.send_message(message.chat.id, random.choice(fruit))
#   else:
#     bot.send_message(message.chat.id, 'ниче не понял')'''
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     # if call.message:
#     if call.data == 'b1':
#         bot.send_message(call.message.chat.id, 'Случайный маршрут: ')
#     elif call.data == 'b2':
#         bot.send_message(call.message.chat.id, '1.	Москва (можно найти абсолютно всё; глобализированное место)\n'
#                                                '2.	Великий Новгород (история; набожное, глубоко православное место)\n'
#                                                '3.	Кавказские минеральные воды (оздоровление; популярны лечебные процедуры)\n'
#                                                '4.	Санкт-Петербург (культура; множество исторически значимых мест)\n'
#                                                '5.	Екатеринбург (урбанистика; прогрессирующий город с развитой инфраструктурой)\n'
#                                                '6.	Казань (история; монголо-татарское иго, фантастической красоты здания)\n'
#                                                '7.	Владивосток (промысел; амурский залив)\n'
#                                                '8.	Новосибирск (глобализация; )\n'
#                                                '9.	Калининград (российская европа; западный форт России)\n'
#                                                '10.	Сочи (активный отдых; популярны горный туризм и купание в море)\n'
#                                                'Чтобы продолжить подбор, нажмите "Next"И этот список можно еще продолжать, но здесь приведен список самых часто посещаемых и увлекающих городов России')
#
#
#
#
# if __name__ == '__main__':
#     fruit = ['Сочи, Санкт-Петербург, Тыва, Шахты']
#
#     while True:
#         try:
#             bot.polling(none_stop=True)
#         except any as e:
#             print(e)
#
# '''
# import telebot
# import random
#
# from telebot import types
# from random import choice
#
# #Токен телеграм-бота
# bot = telebot.TeleBot('6465619279:AAG2y1bq4RFzPtIz3WAp4Rh4LrorOIxbYCE')
#
# #Приветственное сообщение при команде '/start'
# @bot.message_handler(commands=['start'])
# def zdarova(message):
#     bot.send_message(message.chat.id, 'Privet', reply_markup=markup )
#
# #Клавиатура
# markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# item1 = types.KeyboardButton('Нажми на кнопку, и я отправлю тебе название фрукта')
#
# markup.add(item1)
#
# fruit = ['яблоко', 'банан', 'груша', 'персик']
#
#
# @bot.message_handler(content_types=['text', 'photo'])
# def messagelist(message):
#   if message.text == 'Нажми на кнопку, и я отправлю тебе название фрукта':
#     bot.send_message(message.chat.id, random.choice(fruit))
#   else:
#     bot.send_message(message.chat.id, 'ниче не понял')
#
# #Запуск бота
# bot.polling(none_stop=True, interval=0)
# '''
import telebot
# import random
# from telebot import types
# from random import choice

bot = telebot.TeleBot('6465619279:AAG2y1bq4RFzPtIz3WAp4Rh4LrorOIxbYCE')

'''@bot.message_handler(commands = ['start'])
def start(message):
    #bot.send_message(message.chat.id, message)
    #bot.send_message(message.chat.id, message.chat.id)
    bot.send_message(message.chat.id, "Всем пользователям данного бота - добро пожаловать!\n"
                                      "Он будет для вас незаменимым путеводителем в любой точке России. Попробуйте и убедитесь сами!")'''


# приветствие при команде START
@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name is not None and message.from_user.first_name is not None:
        bot.send_message(message.chat.id,
                         f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}! \n Выберите, пожалуйста, команду из списка "Меню"')
    elif message.from_user.last_name is None and message.from_user.first_name is not None:
        bot.send_message(message.chat.id,
                         f'Здравствуй, {message.from_user.first_name}! \n Выберите, пожалуйста, команду из списка "Меню"')
    else:
        bot.send_message(message.chat.id, text="Здарова, залупа")

# для разработчика вывод инфы
# @bot.message_handler(commands=['inf'])
# def main(message):
#     bot.send_message(message.chat.id, message)
# ########### Команды для каждой кнопки
# # @bot.message_handler(commands = ['first'])
# # def button(message):


'''@bot.message_handler(commands=['choose'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('Рандомный маршрут', callback_data='b1')
    item2 = types.InlineKeyboardButton('Топ 10 маршрутов', callback_data='b2')
    item3 = types.InlineKeyboardButton('Продолжить подбор маршрута', callback_data='b3')
    markup.add(item, item2, item3)

    bot.send_message(message.chat.id, "Всем пользователям данного бота - добро пожаловать!\n"
                                      "Он будет для вас незаменимым путеводителем в любой точке России. Попробуйте и убедитесь сами!",
                     reply_markup=markup)'''


variants = ['Сочи, Санкт-Петербург, Тыва, Шахты']

# @bot.message_handler(content_types=['text', 'photo'])
# def messagelist(message):
#   if message.text == 'Нажми на кнопку, и я отправлю тебе название':
#     bot.send_message(message.chat.id, random.choice(fruit))
#   else:
#     bot.send_message(message.chat.id, 'ниче не понял')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    # with open('cities.py', 'r', encoding="utf-8") as variants:
    #     variants = variants.readlines()
    # random_number: int = randint(0, len(variants) - 1)
    # random_number: int = random.choice(variants)
    # bot.send_message(call.message.chat.id, variants[random_number])
    # bot.send_message(call.message.chat.id, ('Чтобы продолжить подбор, нажмите "Next"'))
    # markup.row(item4)

    # bot.send_message(call.chat.id, 'Next', reply_markup=markup)
    # if a==True:
    #     types.InlineKeyboardButton("Next", call.data == 'b4')

'''годно'''
    # @bot.message_handler(commands=['Next'])
    # def button(message):
    #     markup = types.InlineKeyboardMarkup(row_width=1)
    #     # markup = types.InlineKeyboardMarkup(row_width=1)
    #     climate = types.InlineKeyboardButton('Укажите подходящий климат', callback_data='b5')
    #     zone = types.InlineKeyboardButton('Территориальная зона России', callback_data='b6')
    #     budget = types.InlineKeyboardButton('Бюджет', callback_data='b7')
    #     markup.add(climate, zone, budget)
    #     bot.send_message(message.chat.id,'Выберите действие',reply_markup=markup)

    # if next.callback_data == 'b4':
    #     markup2 = types.InlineKeyboardMarkup(row_width=1)
    #     climate = types.InlineKeyboardButton('Укажите подходящий климат', callback_data='b5')
    #     zone = types.InlineKeyboardButton('Территориальная зона России', callback_data='b6')
    #     budget = types.InlineKeyboardButton('Бюджет', callback_data='b7')
    #     markup2.add(climate, zone, budget)


    if call.data == 'b1':
        bot.send_message(call.message.chat.id, 'Случайный маршрут: ')
    elif call.data == 'b2':
        bot.send_message(call.message.chat.id, '1.	Москва (можно найти абсолютно всё; глобализированное место)\n'
                                               '2.	Великий Новгород (история; набожное, глубоко православное место)\n'
                                               '3.	Кавказские минеральные воды (оздоровление; популярны лечебные процедуры)\n'
                                               '4.	Санкт-Петербург (культура; множество исторически значимых мест)\n'
                                               '5.	Екатеринбург (урбанистика; прогрессирующий город с развитой инфраструктурой)\n'
                                               '6.	Казань (история; монголо-татарское иго, фантастической красоты здания)\n'
                                               '7.	Владивосток (промысел; амурский залив)\n'
                                               '8.	Новосибирск (глобализация; )\n'
                                               '9.	Калининград (российская европа; западный форт России)\n'
                                               '10.	Сочи (активный отдых; популярны горный туризм и купание в море)\n'
                                               'Чтобы продолжить подбор, нажмите "Next"И этот список можно еще продолжать, но здесь приведен список самых часто посещаемых и увлекающих городов России')


if __name__ == '__main__':
    fruit = ['Сочи, Санкт-Петербург, Тыва, Шахты']

    while True:
        try:
            bot.polling(none_stop=True)
        except any as e:
            print(e)

'''
import telebot
import random

from telebot import types
from random import choice

#Токен телеграм-бота
bot = telebot.TeleBot('6465619279:AAG2y1bq4RFzPtIz3WAp4Rh4LrorOIxbYCE')

#Приветственное сообщение при команде '/start'
@bot.message_handler(commands=['start'])
def zdarova(message):
    bot.send_message(message.chat.id, 'Privet', reply_markup=markup )

#Клавиатура
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('Нажми на кнопку, и я отправлю тебе название фрукта')

markup.add(item1)

fruit = ['яблоко', 'банан', 'груша', 'персик']


@bot.message_handler(content_types=['text', 'photo'])
def messagelist(message):
  if message.text == 'Нажми на кнопку, и я отправлю тебе название фрукта':
    bot.send_message(message.chat.id, random.choice(fruit))
  else:
    bot.send_message(message.chat.id, 'ниче не понял')

#Запуск бота
bot.polling(none_stop=True, interval=0)
'''

import telebot
# import random
#from telebot import types
# from random import choice

bot = telebot.TeleBot('6465619279:AAG2y1bq4RFzPtIz3WAp4Rh4LrorOIxbYCE')

'''@bot.message_handler(commands = ['start'])
def start(message):
    #bot.send_message(message.chat.id, message)
    #bot.send_message(message.chat.id, message.chat.id)
    bot.send_message(message.chat.id, "Всем пользователям данного бота - добро пожаловать!\n"
                                      "Он будет для вас незаменимым путеводителем в любой точке России. Попробуйте и убедитесь сами!")'''


# приветствие при команде START
@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name is not None and message.from_user.first_name is not None:
        bot.send_message(message.chat.id,
                         f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}! \n Выберите, пожалуйста, команду из списка "Меню"')
    elif message.from_user.last_name is None and message.from_user.first_name is not None:
        bot.send_message(message.chat.id,
                         f'Здравствуй, {message.from_user.first_name}! \n Выберите, пожалуйста, команду из списка "Меню"')
    else:
        bot.send_message(message.chat.id, text="Здарова, залупа")

# для разработчика вывод инфы
# @bot.message_handler(commands=['inf'])
# def main(message):
#     bot.send_message(message.chat.id, message)
# ########### Команды для каждой кнопки
# # @bot.message_handler(commands = ['first'])
# # def button(message):


'''@bot.message_handler(commands=['choose'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('Рандомный маршрут', callback_data='b1')
    item2 = types.InlineKeyboardButton('Топ 10 маршрутов', callback_data='b2')
    item3 = types.InlineKeyboardButton('Продолжить подбор маршрута', callback_data='b3')
    markup.add(item, item2, item3)

    bot.send_message(message.chat.id, "Всем пользователям данного бота - добро пожаловать!\n"
                                      "Он будет для вас незаменимым путеводителем в любой точке России. Попробуйте и убедитесь сами!",
                     reply_markup=markup)'''


variants = ['Сочи, Санкт-Петербург, Тыва, Шахты']

# @bot.message_handler(content_types=['text', 'photo'])
# def messagelist(message):
#   if message.text == 'Нажми на кнопку, и я отправлю тебе название':
#     bot.send_message(message.chat.id, random.choice(fruit))
#   else:
#     bot.send_message(message.chat.id, 'ниче не понял')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    # if call.message:
    if call.data == 'b1':
        bot.send_message(call.message.chat.id, 'Случайный маршрут: ')
    elif call.data == 'b2':
        bot.send_message(call.message.chat.id, '1.	Москва (можно найти абсолютно всё; глобализированное место)\n'
                                               '2.	Великий Новгород (история; набожное, глубоко православное место)\n'
                                               '3.	Кавказские минеральные воды (оздоровление; популярны лечебные процедуры)\n'
                                               '4.	Санкт-Петербург (культура; множество исторически значимых мест)\n'
                                               '5.	Екатеринбург (урбанистика; прогрессирующий город с развитой инфраструктурой)\n'
                                               '6.	Казань (история; монголо-татарское иго, фантастической красоты здания)\n'
                                               '7.	Владивосток (промысел; амурский залив)\n'
                                               '8.	Новосибирск (глобализация; )\n'
                                               '9.	Калининград (российская европа; западный форт России)\n'
                                               '10.	Сочи (активный отдых; популярны горный туризм и купание в море)\n'
                                               'Чтобы продолжить подбор, нажмите "Next"И этот список можно еще продолжать, но здесь приведен список самых часто посещаемых и увлекающих городов России')


if __name__ == '__main__':
    fruit = ['Сочи, Санкт-Петербург, Тыва, Шахты']

    while True:
        try:
            bot.polling(none_stop=True)
        except any as e:
            print(e)


'''
import telebot
import random

from telebot import types
from random import choice

#Токен телеграм-бота
bot = telebot.TeleBot('6465619279:AAG2y1bq4RFzPtIz3WAp4Rh4LrorOIxbYCE')

#Приветственное сообщение при команде '/start'
@bot.message_handler(commands=['start'])
def zdarova(message):
    bot.send_message(message.chat.id, 'Privet', reply_markup=markup )

#Клавиатура
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('Нажми на кнопку, и я отправлю тебе название фрукта')

markup.add(item1)

fruit = ['яблоко', 'банан', 'груша', 'персик']


@bot.message_handler(content_types=['text', 'photo'])
def messagelist(message):
  if message.text == 'Нажми на кнопку, и я отправлю тебе название фрукта':
    bot.send_message(message.chat.id, random.choice(fruit))
  else:
    bot.send_message(message.chat.id, 'ниче не понял')

#Запуск бота
bot.polling(none_stop=True, interval=0)
'''

# Если пользователь нажал Next, нужно задать наводящие вопросы, по типу: какой климат, зона страны, бюджет
# Действия для кнопки Next
def on_click_Next(call):
    if call.data == 'next':
        markup = types.InlineKeyboardMarkup(row_width=1)
        # markup = types.InlineKeyboardMarkup(row_width=1)
        climate = types.InlineKeyboardButton('Подходящий климат', callback_data='climate')
        zone = types.InlineKeyboardButton('Территориальная зона России', callback_data='zone')
        budget = types.InlineKeyboardButton('Бюджет', callback_data='budget')
        markup.add(climate, zone, budget)
        bot.send_message(call.data.call.id, 'Выберите действие: ', reply_markup=markup)


#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
#-----------------------------------------------------------------------------------------------------------------------


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


#----------------------------------------------------------------------------------------------------------------------

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

#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# Если пользователь нажал Next, нужно задать наводящие вопросы, по типу: какой климат, зона страны, бюджет
# Действия для кнопки Next
def on_click_Next(call):
    if call.data == 'next':
        markup = types.InlineKeyboardMarkup(row_width=1)
        # markup = types.InlineKeyboardMarkup(row_width=1)
        climate = types.InlineKeyboardButton('Укажите подходящий климат', callback_data='climate')
        zone = types.InlineKeyboardButton('Территориальная зона России', callback_data='zone')
        budget = types.InlineKeyboardButton('Бюджет', callback_data='budget')
        markup.add(climate, zone, budget)
        bot.send_message(call.data.call.id, 'Выберите действие: ', reply_markup=markup)

#def climate(message):

# ----------------------------------------------------------------------------------------------------------------------

# Распределение действий на каждую команду с конопк в choose
@bot.callback_query_handler(func=lambda call: True)
def callback(call: types.CallbackQuery):
    if call.data == 'rand_route':  # рандомное определение города для поездки
        bot.send_message(call.message.chat.id, random.choice(variants))

    if call.data == 'top10m':  # топ 10 городов
        bot.send_message(call.message.chat.id, (top10))
        markup = types.InlineKeyboardMarkup(row_width=1)
        next = types.InlineKeyboardButton('Next', callback_data='next1')
        markup.add(next)
        bot.send_message(call.message.chat.id, 'Чтобы продолжить подбор, нажмите "Next"',
                         reply_markup=markup)

    if call.data == 'next1':  # продолжить подбор
        markup = types.InlineKeyboardMarkup(row_width=1)
        climate = types.InlineKeyboardButton('Укажите подходящий климат', callback_data='climate')
        if climate == True:
            zone = types.InlineKeyboardButton('Территориальная зона России', callback_data='zone')
            if zone == True:
                budget = types.InlineKeyboardButton('Бюджет', callback_data='budget')
                markup.add(climate, zone, budget)
        bot.send_message(call.message.chat.id, 'Жопа', reply_markup=markup)






if __name__ == '__main__':

    while True:
        try:

            bot.polling(none_stop=True)
        except any as e:
            print(e)



# Запуск бота
bot.polling(none_stop=True, interval=0)

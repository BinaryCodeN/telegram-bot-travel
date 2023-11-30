import telebot

'''# Подлкючаем библиотеку requests
import requests
# Подключаем нужные для бота модули из библиотеки telegram.ext
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, filters
from API import bot_tg_API
from API import aviasales

avia: telebot.TeleBot = telebot.TeleBot(aviasales)
bot: telebot.TeleBot = telebot.TeleBot(bot_tg_API)


# функция для получения адреса по координатам.
def get_address_from_coords(choose):
    PARAMS = {
        "apikey": avia,
        "format": "json",
        "lang": "ru_RU",
        "kind": "house",
        "reis": choose
    }

    try:
        r = requests.get(url="https://api.travelpayouts.com/aviasales/v3/prices_for_dates", params=PARAMS)
        json_data = r.json()
        ticket_str = json_data['success']['data']['origin']['destination']['']
        return ticket_str
    except Exception as e:
        return "Не могу определить билет по этому направлению.\n\nОтправь мне билет (город отправления, город прибытия):"


def start(numlock1, numlock2):
    print(type(numlock1))
    numlock1.message.reply_text('Отправьте начальный и конечный пункты')


def choose_ticket(numlock1, numlock2: CallbackContext):
    usertext = numlock1.message.text.split(' ')[1]
    response = requests.get(
        f'https://api.travelpayouts.com/v1/prices/cheap?origin=MOW&destination={location}&token={avia}')



def main() -> None:
    updater = Updater(bot, update_queue=True)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('search', search))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    # запускаем функцию def main
'''
import json

import requests
from telegram.ext import Updater, CommandHandler, ConversationHandler, filters
import telebot
from telegram import Update
from API import bot_tg_API
from API import aviasales

bot: telebot.TeleBot = telebot.TeleBot(bot_tg_API)

# def choose_ticket(from_where, where_to, avia, otprav, vosvr):
#     location = update.message.text.split(' ')
#     response = requests.get(f'https://api.travelpayouts.com/v1/prices/cheap?origin={from_where}&destination={where_to}&token={avia}&departure_at={otprav}')
#     response2 = requests.get(f'https://api.travelpayouts.com/v1/prices/cheap?return_at={vosvr}&token={avia}')
# if response.status_code == 200:
# tickets = response.json()['data'] + response2.json()['data']
# print(tickets)

# choose_ticket(from_where="AER", where_to="OVB", avia=aviasales, otprav=2023-11, vosvr=2023-12)



# Создание словаря для того, чтобы пользователь, введя нужные города, мог в авиасейлз узнать стоимость билета
dictionary: dict[int, list[str]] = {}


@bot.message_handler(commands=['start'])
def first_step(message: telebot.types.Message) -> None:
    dictionary[message.chat.id] = []
    bot.send_message(chat_id=message.chat.id, text="Введите город отправления:")
    bot.register_next_step_handler(message, second_step)


def second_step(message: telebot.types.Message) -> None:
    dictionary[message.chat.id].append(message.text)
    bot.send_message(message.chat.id, "Введите город прибытия: ")
    bot.register_next_step_handler(message, third_step)


def third_step(message: telebot.types.Message) -> None:
    dictionary[message.chat.id].append(message.text)
    bot.send_message(message.chat.id, f"Введите дату отправления в формате ГГГГ-ММ-ДД")
    bot.register_next_step_handler(message, fourth_step)


def fourth_step(message: telebot.types.Message) -> None:
    dictionary[message.chat.id].append(message.text)
    bot.send_message(chat_id=message.chat.id, text="Если вы планируете возвратный биллет, то напишите дату "
                                                   "возвращения в формате ГГГГ-ММ-ДД.\n<i><b>Если вам не интересен обратный билет, напишите слово 'Нет' без ковычек, инче ничего не будет работать</b></i>",
                     parse_mode='HTML')
    bot.register_next_step_handler(message, fifth_step)


def fifth_step(message: telebot.types.Message) -> None:
    if message.text == 'Нет' or message.text == 'нет':
        bot.send_message(message.chat.id,
                         f"Вы ввели {dictionary[message.chat.id][0]} - {dictionary[message.chat.id][1]} {dictionary[message.chat.id][2]} (Пидора ответ)\nВыолняется поиск авиабилета...")
        try:
            from_where = air[dictionary[message.chat.id][0]]
            where_to = air[dictionary[message.chat.id][1]]
            departure = dictionary[message.chat.id][2]
            rez: str = choose_ticket(from_where=from_where, where_to=where_to, departure_at=departure)
            bot.send_message(message.chat.id, f"Ваш билет найден:\n\n{rez}")

        except Exception as e:
            print(e)
            bot.send_message(message.chat.id, 'Вы ввели неверный город или дату, попробуйте ещё раз')

    else:
        dictionary[message.chat.id].append(message.text)
        bot.send_message(message.chat.id,
                         f"Вы ввели {dictionary[message.chat.id][0]} - {dictionary[message.chat.id][1]} {dictionary[message.chat.id][2]}, возвращение {dictionary[message.chat.id][3]}\nВыолняется поиск авиабилета...")
        try:
            from_where = air[dictionary[message.chat.id][0]]
            where_to = air[dictionary[message.chat.id][1]]
            departure = dictionary[message.chat.id][2]
            return_at = dictionary[message.chat.id][3]
            rez: str = choose_ticket(from_where=from_where, where_to=where_to, departure_at=departure, return_at=return_at)
            bot.send_message(message.chat.id, f"Ваш билет найден:\n\n{rez}")
        except Exception as e:
            print(e)
            bot.send_message(message.chat.id, "Вы ввели неверный город или дату")


def choose_ticket(from_where: str, where_to: str, departure_at: str, return_at: None | str = None) -> str:
    print(from_where, where_to, departure_at, return_at)
    if return_at is None:
        response = requests.get(f'https://api.travelpayouts.com/v1/prices/cheap?origin={from_where}&destination={where_to}'
                                f'&token={aviasales}&departure_at={departure_at}')
    else:
        response = requests.get(f'https://api.travelpayouts.com/v1/prices/cheap?origin={from_where}&destination={where_to}'
                                f'&token={aviasales}&departure_at={departure_at}&return_at={return_at}')
    if response.status_code == 200:
        tickets = response.json()['data'][where_to]
        ass_index: str
        for x in tickets:
            ass_index = x
            pass
        tickets = response.json()['data'][where_to][ass_index]
        if return_at is None:
            tickets = f"Цена: {tickets['price']}\nДата отпраления: {tickets['departure_at']}\nДата отправления обратно: {tickets['return_at']}"
        else:
            tickets = f"Цена: {tickets['price']}\nДата отпраления: {tickets['departure_at']}"
        return tickets


air: dict[str, str] = {"Абакан": "ABA", "Алдан": "ADH", "Амдерма": "AMV", "Анадырь": "DYR", "Анапа": "AAQ",
                       "Апатиты": "KVK",
                       "Астрахань": "ASF", "Ачинск": "ACS	", "Барнаул": "BAX", "Белорецк": "BCX",
                       "Благовещенск": "BQS",
                       "Бор": "TGP", "Бугульма": "UUA", "Великие Луки": "VLU", "Великий Устюг": "VUS",
                       "Владивосток": "VVO",
                       "Владикавказ	": "OGZ", "Воркута": "VKT", "Воронеж": "VOZ", "Геленджик": "GDZ",
                       "Грозный": "GRV",
                       "Екатеринбург": "SVX", "Енисейск": "EIE", "Иваново": "IWA", "Ижевск": "IJK", "Иркутск": "IKT",
                       "Казань": "KZN",
                       "Калининград": "KGD", "Кемерово": "KEJ", "Когалым": "KGP", "Кострома": "KMW", "Котлас": "KSZ",
                       "Краснодар": "KRR", "Красноярск": "KJA", "Курган": "KRO", "Курильск": "BVV", "Курск": "URS",
                       "Кызыл": "KYZ",
                       "Липецк": "LPK", "Магадан": "GDX", "Магдагачи": "GDG", "Махачкала": "MCX", "Мирный": "MJZ",
                       "Жуковский": "ZIA",
                       "Внуково": "VKO", "Шереметьево": "SVO",
                       "Быково": "BKA", "Мурманск": "MMK", "Нарьян-Мар": "NNM", "Нерюнгри": "CNN",
                       "Нижневартовск": "NJC",
                       "Нижнекамск": "NBC", "Нижний-Новгород": "GOJ", "Новокузнецк": "NOZ", "Новый Уренгой": "NUX",
                       "Ноглики": "NGL", "Новосибирск": "OVB",
                       "Норильск": "NSK", "Ноябрьск": "NOJ", "Омск": "OMS", "Орёл": "OEL", "Оренбург": "REN",
                       "Орск": "OSW", "Оха": "OHH",
                       "Пермь": "PEE", "Петрозаводск": "PES", "Печора": "PEX", "Провидения": "PVS", "Псков": "PKV",
                       "Радужный": "RAT",
                       "Рыбинск": "RYB", "Рязань": "RZN", "Самара": "KUF", "Саранск": "SKX", "Саратов": "RTW",
                       "Смоленск": "LNX", "Советская Гавань": "GVN","Сочи": "AER", "Соловецкие острова": "CSH", "Ставрополь": "STW",
                       "Сыктывкар	": "SCW", "Санкт-Петербург":"LED",
                       "Тикси": "IKS", "Тобольск": "TOX", "Томск": "TOF", "Тында": "TYD", "Тюмень": "TJM",
                       "Удачный": "PYJ",
                       "Улан-Удэ": "UUD", "Ульяновск": "ULY", "Усть-Кут": "UKX", "Уфа": "UFA", "Ухта": "UCT",
                       "Хабаровск": "KHV",
                       "Ханты-Мансийск": "HMA", "Цимлянск": "VLK", "Чебоксары": "CSY", "Челябинск": "CEK",
                       "Череповец": "CEE",
                       "Черский": "CYX", "Чита": "HTA", "Чокурдах": "CKH", "Щёлково": "CKL", "Элиста": "ESL",
                       "Южно-Курильск": "DEE",
                       "Якутск": "YKS", "Ярославль": "IAR"}





@bot.callback_query_handler(func=lambda call: True)
def handler(call: telebot.types.CallbackQuery) -> None:
    if call.data == 'change_city':
        choose_ticket(from_where=dictionary[call.message.chat.id][0], where_to=dictionary[call.message.chat.id][1],
                      aviasales=aviasales, departure_at='2023-12-11', return_at='2023-12-15')


# @bot.callback_query_handler(func=lambda call: True)
# def ticket(call):
#     air = {"Абакан": "ABA", "Алдан": "ADH", "Амдерма": "AMV", "Анадырь": "DYR", "Анапа": "AAQ", "Апатиты": "KVK",
#          "Астрахань": "ASF", "Ачинск": "ACS	", "Барнаул": "BAX", "Белорецк": "BCX", "Благовещенск": "BQS",
#          "Бор": "TGP", "Бугульма": "UUA", "Великие Луки": "VLU", "Великий Устюг": "VUS", "Владивосток": "VVO",
#          "Владикавказ	": "OGZ", "Воркута": "VKT", "Воронеж": "VOZ", "Геленджик": "GDZ", "Грозный": "GRV",
#          "Екатеринбург": "SVX", "Енисейск": "EIE", "Иваново": "IWA", "Ижевск": "IJK", "Иркутск": "IKT", "Казань": "KZN",
#          "Калининград": "KGD", "Кемерово": "KEJ", "Когалым": "KGP", "Кострома": "KMW", "Котлас": "KSZ",
#          "Краснодар": "KRR", "Красноярск": "KJA", "Курган": "KRO", "Курильск": "BVV", "Курск": "URS", "Кызыл": "KYZ",
#          "Липецк": "LPK", "Магадан": "GDX", "Магдагачи": "GDG", "Махачкала": "MCX", "Мирный": "MJZ", "Москва": "BKA",
#          "Москва": "VKO", "Мурманск": "MMK", "Нарьян-Мар": "NNM", "Нерюнгри": "CNN", "Нижневартовск": "NJC",
#          "Нижнекамск": "NBC", "НижнийНовгород": "GOJ", "Новокузнецк": "NOZ", "Новый Уренгой": "NUX", "Ноглики": "NGL",
#          "Норильск": "NSK", "Ноябрьск": "NOJ", "Омск": "OMS", "Орёл": "OEL", "Оренбург": "REN", "Орск": "OSW", "Оха": "OHH",
#          "Пермь": "PEE", "Петрозаводск": "PES", "Печора": "PEX", "Провидения": "PVS", "Псков": "PKV", "Радужный": "RAT",
#          "Рыбинск": "RYB", "Рязань": "RZN", "Рязань": "RZN", "Самара": "KUF", "Саранск": "SKX", "Саратов": "RTW",
#          "Смоленск": "LNX", "Советская Гавань": "GVN", "Соловецкие острова": "CSH", "Ставрополь": "STW", "Сыктывкар	": "SCW",
#          "Тикси": "IKS", "Тобольск": "TOX", "Томск": "TOF", "Тында": "TYD", "Тюмень": "TJM", "Удачный": "PYJ",
#          "Улан-Удэ": "UUD", "Ульяновск": "ULY", "Усть-Кут": "UKX", "Уфа": "UFA", "Ухта": "UCT", "Хабаровск": "KHV",
#          "Ханты-Мансийск": "HMA", "Цимлянск": "VLK", "Чебоксары": "CSY", "Челябинск": "CEK", "Череповец": "CEE",
#          "Черский": "CYX", "Чита": "HTA", "Чокурдах": "CKH", "Щёлково": "CKL", "Элиста": "ESL", "Южно-Курильск": "DEE",
#          "Якутск": "YKS", "Ярославль": "IAR"}
#     for key, value in air.items():
#         choose_ticket(from_where=key, where_to=key, avia=aviasales, otprav=2023-11, vosvr=2023-12)

bot.polling(none_stop=True)

# def main():

# updater = Updater(bot, use_context=True)
# dispatcher = updater.dispatcher
# dispatcher.add_handler(CommandHandler('start', start))
# dispatcher.add_handler(CommandHandler('search', choose_ticket, pass_args=True))

# updater.start_polling()
# updater.idle()

# if __name__ == '__main__':
#     main()

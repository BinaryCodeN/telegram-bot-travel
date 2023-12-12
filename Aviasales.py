import requests
import telebot
from API import aviasales
from telebot import types

# Создание словаря для того, чтобы пользователь, введя нужные города, мог в авиасейлз узнать стоимость билета
dictionary: dict[int, list[str]] = {}


def first_step(message: telebot.types.Message, bot: telebot.TeleBot) -> None:
    dictionary[message.chat.id] = []
    bot.send_message(message.chat.id, 'После определения с местом полёта, \n'
                                      'для поиска дешевого авиабилета \n'
                                      'введите <b>свой</b> город отправления: ', parse_mode='HTML')
    bot.register_next_step_handler(message, second_step, bot)


def second_step(message: telebot.types.Message, bot: telebot.TeleBot) -> None:
    dictionary[message.chat.id].append(message.text)
    bot.send_message(message.chat.id, "Введите введите любой из трёх вариантов город прибытия: ")
    bot.register_next_step_handler(message, third_step, bot)


def third_step(message: telebot.types.Message, bot: telebot.TeleBot) -> None:
    dictionary[message.chat.id].append(message.text)
    bot.send_message(message.chat.id, f"Введите дату отправления в формате ГГГГ-ММ-ДД")
    bot.register_next_step_handler(message, fourth_step, bot)


def fourth_step(message: telebot.types.Message, bot: telebot.TeleBot) -> None:
    dictionary[message.chat.id].append(message.text)
    bot.send_message(chat_id=message.chat.id, text="Если вы планируете возвратный биллет, то напишите дату "
                                                   "возвращения в формате ГГГГ-ММ-ДД."
                                                   "\n\n<i><b>Если вам не интересен обратный билет, напишите слово 'Нет' без кавычек</b></i>",
                     parse_mode='HTML')
    bot.register_next_step_handler(message, fifth_step, bot)


def fifth_step(message: telebot.types.Message, bot: telebot.TeleBot) -> None:
    print('запуск fifth_step')
    if message.text == 'Нет' or message.text == 'нет':
        bot.send_message(message.chat.id,
                         f"Вы ввели {dictionary[message.chat.id][0]} - {dictionary[message.chat.id][1]} {dictionary[message.chat.id][2]} "
                         f"\nВыполняется поиск авиабилета...")

        try:
            from_where = air[dictionary[message.chat.id][0]]
            where_to = air[dictionary[message.chat.id][1]]
            departure = dictionary[message.chat.id][2]
            rez: str = choose_ticket(from_where=from_where, where_to=where_to, departure_at=departure)

            markup = types.ReplyKeyboardMarkup()
            button_geo = types.KeyboardButton(text='Геолокация', request_location=True)
            markup.add(button_geo)

            bot.send_message(message.chat.id, f"Ваш билет найден:\n\n{rez}", reply_markup=markup)

        except Exception as e:
            print(e)
            bot.send_message(message.chat.id, 'Вы ввели неверный город или дату, попробуйте ещё раз')



    else:
        dictionary[message.chat.id].append(message.text)
        bot.send_message(message.chat.id,
                         f"Вы ввели {dictionary[message.chat.id][0]} - {dictionary[message.chat.id][1]} {dictionary[message.chat.id][2]}, "
                         f"возвращение {dictionary[message.chat.id][3]}\nВыполняется поиск авиабилета...")
        try:
            from_where = air[dictionary[message.chat.id][0]]
            where_to = air[dictionary[message.chat.id][1]]
            departure = dictionary[message.chat.id][2]
            return_at = dictionary[message.chat.id][3]
            rez: str = choose_ticket(from_where=from_where, where_to=where_to, departure_at=departure,
                                     return_at=return_at)
            bot.send_message(message.chat.id, f"Ваш билет найден:\n\n{rez}")

            markup = types.ReplyKeyboardMarkup()
            button_geo = types.KeyboardButton(text='Геолокация', request_location=True)
            markup.add(button_geo)

            bot.send_message(chat_id=message.chat.id,
                             text="Далее вы можете посмотреть маршрут на карте до выбранного пункта\n"
                                  "Для этого отправьте свою геолокацию, чтобы построить маршрут от выбранной точки: ",
                             reply_markup=markup)

        except Exception as e:
            print(e)
            bot.send_message(message.chat.id, "Вы ввели неверный город или дату, попробуйте с другой датой")
            markup = types.InlineKeyboardMarkup()
            inline = types.InlineKeyboardButton('←', callback_data='back1')
            markup.add(inline)
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='Назад',
                                  reply_markup=markup)


'''def six_step(message: telebot.types.Message, bot: telebot.TeleBot):
    dictionary[message.chat.id].append(message.text)
    print(dictionary[message.chat.id].append(message.text))
    bot.send_message(chat_id=message.chat.id, text='Далее вы можете посмотреть маршрут на карте до выбранного пункта')
    print(six_step(message, bot))'''


# Работа непосредственно с API


def choose_ticket(from_where: str, where_to: str, departure_at: str, return_at: None | str = None) -> str:
    print(from_where, where_to, departure_at, return_at)

    if return_at is None:
        response = requests.get(
            f'https://api.travelpayouts.com/v1/prices/cheap?origin={from_where}&destination={where_to}'
            f'&token={aviasales}&departure_at={departure_at}')
    else:
        response = requests.get(
            f'https://api.travelpayouts.com/v1/prices/cheap?origin={from_where}&destination={where_to}'
            f'&token={aviasales}&departure_at={departure_at}&return_at={return_at}')

    if response.status_code == 200:
        tickets = response.json()['data'][where_to]
        ass_index: str
        for x in tickets:  # для того, чтобы не учитывался индекс
            ass_index = x
            pass
        tickets = response.json()['data'][where_to][ass_index]
        if return_at is None:
            tickets = f"Цена: {tickets['price']}₽\nДата отправления:\n{tickets['departure_at'][:10] + ' ' + tickets['departure_at'][11:19]} \nЧасовой пояс: {tickets['departure_at'][19:]} \nАвиакампания: {avia[tickets['airline']]}"

        else:
            tickets = f"Цена: {tickets['price']}₽\nДата отправления:\n{tickets['departure_at'][:10] + ' ' + tickets['departure_at'][11:19]} \nЧасовой пояс: {tickets['departure_at'][19:]} \nАвиакампания: {avia[tickets['airline']]} \n\nДата отправления обратно: \n{tickets['return_at'][:10] + ' ' + tickets['return_at'][11:19]} \nЧасовой пояс: {tickets['return_at'][19:]} \nАвиакампания: {avia[tickets['airline']]}"

        return tickets


def six_step(message: telebot.types.Message, bot: telebot.TeleBot) -> None:
    print('запуск six_step')
    # dictionary[message.chat.id].append(message.text)
    bot.send_message(chat_id=message.chat.id, text="Далее вы можете посмотреть маршрут на карте до выбранного пункта")


air: dict[str, str] = {'Абакан': 'ABA', 'Алдан': 'ADH', 'Амдерма': 'AMV', 'Анадырь': 'DYR', 'Анапа': 'AAQ',
                       'Апатиты': 'KVK', 'Архангельск': 'ARH', 'Астрахань': 'ASF', 'Ачинск': 'ACS', 'Барнаул': 'BAX',
                       'Белгород': 'EGO', 'Белорецк': 'BCX', 'Благовещенск': 'BQS', 'Бор': 'TGP', 'Братск': 'BTK',
                       'Брянск': 'BZK', 'Бугульма': 'UUA', 'Великие Луки': 'VLU', 'Великий Устюг': 'VUS',
                       'Владивосток': 'VVO', 'Владикавказ': 'OGZ', 'Волгоград': 'VOG', 'Вологда': 'VGD',
                       'Воркута': 'VKT', 'Воронеж': 'VOZ', 'Геленджик': 'GDZ', 'Грозный': 'GRV', 'Диксон': 'DKS',
                       'Екатеринбург': 'SVX', 'Енисейск': 'EIE', 'Иваново': 'IWA', 'Игарка': 'IAA', 'Ижевск': 'IJK',
                       'Инта': 'INA', 'Иркутск': 'IKT', 'Йошкар-Ола': 'JOK', 'Казань': 'KZN', 'Калининград': 'KGD',
                       'Кемерово': 'KEJ', 'Киров': 'KVX', 'Когалым': 'KGP', 'Комсомольск-на-Амуре': 'KXK',
                       'Кострома': 'KMW', 'Котлас': 'KSZ', 'Краснодар': 'KRR', 'Красноярск': 'KJA', 'Курган': 'KRO',
                       'Курильск': 'BVV', 'Курск': 'URS', 'Кызыл': 'KYZ', 'Лешуконское': 'LDG', 'Липецк': 'LPK',
                       'Магадан': 'GDX', 'Магдагачи': 'GDG', 'Магнитогорск': 'MQF', 'Махачкала': 'MCX',
                       'Минеральные Воды': 'MRV', 'Мирный': 'MJZ', 'Москва Быково': 'BKA', 'Москва Внуково': 'VKO',
                       'Москва Домодедово': 'DME',
                       'Москва Шереметьево': 'SVO', 'Жуковский': 'ZIA', 'Мурманск': 'MMK', 'Надым': 'NYM',
                       'Нальчик': 'NAL', 'Нарьян-Мар': 'NNM',
                       'Нерюнгри': 'CNN', 'Нижневартовск': 'NJC', 'Нижнекамск': 'NBC', 'Нижний Новгород': 'GOJ',
                       'Новокузнецк': 'NOZ', 'Новосибирск': 'OVB', 'Новый Уренгой': 'NUX', 'Ноглики': 'NGL',
                       'Норильск': 'NSK', 'Ноябрьск': 'NOJ', 'Октябрьский': 'OKT', 'Омск': 'OMS', 'Орёл': 'OEL',
                       'Оренбург': 'REN', 'Орск': 'OSW', 'Оха': 'OHH', 'Охотск': 'OHO', 'Певек': 'PWE', 'Пенза': 'PEZ',
                       'Пермь': 'PEE', 'Петрозаводск': 'PES', 'Петропавловск-Камчатский': 'PKC', 'Печора': 'PEX',
                       'Провидения': 'PVS', 'Псков': 'PKV', 'Радужный': 'RAT', 'Ростов-на-Дону': 'ROV',
                       'Рыбинск': 'RYB', 'Рязань': 'RZN', 'Салехард': 'SLY', 'Самара': 'KUF',
                       'Санкт-Петербург': 'LED', 'Саранск': 'SKX', 'Саратов': 'RTW', 'Смоленск': 'LNX',
                       'Советская Гавань': 'GVN', 'Соловецкие острова': 'CSH', 'Сочи': 'AER', 'Ставрополь': 'STW',
                       'Сургут': 'SGC', 'Сыктывкар': 'SCW', 'Тамбов': 'TBW', 'Тикси': 'IKS', 'Тобольск': 'TOX',
                       'Томск': 'TOF', 'Тында': 'TYD', 'Тюмень': 'TJM', 'Удачный': 'PYJ', 'Улан-Удэ': 'UUD',
                       'Ульяновск': 'ULY', 'Усть-Кут': 'UKX', 'Усинск': 'USK', 'Уфа': 'UFA', 'Ухта': 'UCT',
                       'Хабаровск': 'KHV', 'Ханты-Мансийск': 'HMA', 'Хатанга': 'HTG', 'Цимлянск': 'VLK',
                       'Чебоксары': 'CSY', 'Челябинск': 'CEK', 'Череповец': 'CEE', 'Черский': 'CYX', 'Чита': 'HTA',
                       'Чокурдах': 'CKH', 'Шахтерск': 'EKS', 'Щёлково': 'CKL', 'Элиста': 'ESL', 'Южно-Курильск': 'DEE',
                       'Южно-Сахалинск': 'UUS', 'Якутск': 'YKS', 'Ярославль': 'IAR'}

avia = {'KC': 'Air Astana', 'BT': 'AirBaltic', 'ZM': 'Air Manas', '9U': 'Air Moldova', 'YK': 'Avia Traffic Company',
        'X9': 'Avion Express', 'R6': 'DOT LT', '5F': 'FlyOne', 'IQ': 'Qazaq Air',
        'S7': 'S7 Airlines', 'DV': 'SCAT', 'S9': 'Silk Road Cargo Business', 'Y3': 'SKY KG Airlines',
        'S5': 'Small Planet Airlines', '6Y': 'SmartLynx Airlines', 'S3': 'Sunkar Air', 'ZR': 'Авиакон Цитотранс',
        'V2': 'Авиализинг', '4B': 'Авиастар-ТУ', 'HZ': 'Аврора', 'J2': 'АЗАЛ', 'А4': 'Азимут', 'ZF': 'АЗУР эйр',
        'F7': 'Ай Флай', '6R': 'АЛРОСА', '2G': 'Ангара', 'RM': 'Армения', 'V8': 'АТРАН', 'SU': 'Аэрофлот',
        'Z9': 'БЕК ЭЙР', 'B2': 'Белавиа', 'VI': 'Волга-Днепр', '4G': 'Газпром авиа', '6Z': 'Евро-Азия-Эйр',
        'RF': 'Ерофей', 'I8': 'Ижавиа', 'EO': 'Икар', 'IO': 'ИрАэро', 'KZ': 'Казавиаспас', 'KO': 'Комиавиатранс',
        'PS': 'МАУ', '5N': 'Смартавиа', 'Y7': 'НордСтар', 'O7': 'Оренбуржье', 'DP': 'Победа',
        'PI': 'Полярные авиалинии', 'WZ': 'Ред Вингс', 'FV': 'Россия', 'RL': 'РОЯЛ ФЛАЙТ', '7R': 'РусЛайн',
        'N4': 'Северный Ветер', 'D2': 'Северсталь', 'U3': 'Скай Гейтс Эйрлайнс', 'SZ': 'Сомон Эйр', '7J': 'Таджик Эйр',
        'TQ': 'Тандем Аэро', 'H7': 'Тарон Авиа', 'T5': 'Туркменистан', 'HY': 'Узбекские авиалинии',
        'U6': 'Уральские авиалинии', 'AY': 'ФиннЭйр', 'ZP': 'Шелковый путь (Silk Way Airlines)', 'RU': 'ЭйрБриджКарго',
        'RT': 'ЮВТ Аэро', 'UT': 'ЮТэйр', 'R3': 'Якутия', 'YС': 'Ямал АТК'}

# #@bot.callback_query_handler(func=lambda call: True)
# def handler(call: telebot.types.CallbackQuery) -> None:
#     if call.data == 'change_city':
#         choose_ticket(from_where=dictionary[call.message.chat.id][0], where_to=dictionary[call.message.chat.id][1],
#                       aviasales=aviasales, departure_at='2023-12-11', return_at='2023-12-15')

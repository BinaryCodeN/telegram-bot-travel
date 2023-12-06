import telebot
import requests

# Токен вашего бота
token = '6465619279:AAG2y1bq4RFzPtIz3WAp4Rh4LrorOIxbYCE'
# Токен API Яндекс Геокодер
yandex_api_key = 'a98d6dc4-8048-4942-a5d9-e0f82054afd3'

# Инициализация бота
bot = telebot.TeleBot(token)


#@bot.message_handler(commands=['start'])
def send_welcome(message):

    bot.reply_to(message, "Далее вы можете посмотреть маршрут на карте до выбранного пункта\n"
                          "Для этого отправьте свою геолокацию, чтобы построить маршрут от выбранной точки: ")
    bot.register_next_step_handler(message, handle_location, bot)


#@bot.message_handler(content_types=['location'])
def handle_location(message):
    # Получаем координаты из сообщения
    latitude = message.location.latitude
    longitude = message.location.longitude
    user_location = f"{longitude}, {latitude}"
    print(user_location)
    bot.send_message(message.chat.id, "Теперь отправьте место, до которого построить маршрут: ")
    bot.register_next_step_handler(message, handle_text, bot)


#@bot.message_handler(content_types=['text'])
def handle_text(message):
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

    # Отправляем сообщение с координатами точки и ссылкой на карту
    bot.send_message(message.chat.id, f"Координаты места: \nШирота {dest_latitude}, Долгота {dest_longitude}")
    bot.send_message(message.chat.id, f"Ссылка на карту: \nhttps://yandex.com/maps/?ll={dest_longitude}, {dest_latitude}&z=12")

    # Теперь можно использовать найденные координаты для построения маршрута или других действий



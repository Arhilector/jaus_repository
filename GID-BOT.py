import telebot
from telebot import types
import sqlite3
import datetime
import random
from datetime import datetime, timedelta


def init_db():
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            category TEXT,
            date TEXT,
            location TEXT,
            price TEXT,
            contact_info TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def populate_db_with_sample_events():
    sample_events = [
        ("Рок-концерт", "Наслаждайтесь живой рок-музыкой", "Концерты", "2024-05-05", "Стадион", "500", "info@rockconcert.com"),
        ("Джазовый вечер", "Вечер гладкого джаза", "Концерты", "2024-05-15", "Джаз-клуб", "300", "contact@jazznight.com"),
        ("Фестиваль поп-музыки", "Выступления топовых поп-артистов", "Концерты", "2024-05-25", "Арена", "750", "tickets@popfestival.com"),
        ("Вечер классической музыки", "Живое выступление оркестра", "Концерты", "2024-06-05", "Концертный зал", "600", "boxoffice@classicalmusic.com"),
        ("Инди-рок", "Живые выступления инди-групп", "Концерты", "2024-06-15", "На открытом воздухе", "350", "info@indierock.com"),
        ("Выставка искусств", "Экспозиция современного искусства", "Выставки", "2024-06-25", "Городская галерея", "200", "info@artexhibition.com"),
        ("Экспо фотографии", "Фотографии мирового класса", "Выставки", "2024-07-01", "Музей фотографии", "150", "contact@photoexpo.com"),
        ("Ярмарка скульптур", "Скульптуры со всего мира", "Выставки", "2024-07-10", "Искусственный центр", "180", "tickets@sculpturefair.com"),
        ("Выставка исторических артефактов", "Древние артефакты на выставке", "Выставки", "2024-07-20", "Исторический музей", "250", "info@historicalartifacts.com"),
        ("Выставка картин", "Новые и старые картины", "Выставки", "2024-07-30", "Художественная студия", "210", "contact@paintingexhibition.com"),
        ("Фестиваль еды", "Попробуйте блюда со всего мира", "Фестивали", "2024-05-10", "Городской парк", "Бесплатно", "info@foodfestival.com"),
        ("Пивной фестиваль", "Местные и международные сорта пива", "Фестивали", "2024-05-20", "Центр города", "100", "tickets@beerfestival.com"),
        ("Кинофестиваль", "Международные кинопоказы", "Фестивали", "2024-06-10", "Кинокомплекс", "350", "contact@filmfestival.com"),
        ("Музыкальный фестиваль", "Различные музыкальные жанры", "Фестивали", "2024-06-20", "Большое поле", "400", "info@musicfestival.com"),
        ("Культурный фестиваль", "Празднование разнообразных культур", "Фестивали", "2024-06-30", "Культурный центр", "220", "tickets@culturalfestival.com"),
        ("Кулинарный класс", "Научитесь готовить новые блюда", "Мастер-классы", "2024-05-12", "Кулинарная школа", "250", "register@cookingclass.com"),
        ("Художественная мастерская", "Создайте свое собственное искусство", "Мастер-классы", "2024-06-02", "Художественная мастерская", "300", "signup@artworkshop.com"),
        ("Танцевальная мастерская", "Научитесь современным танцам", "Мастер-классы", "2024-06-18", "Танцевальная студия", "150", "info@danceworkshop.com"),
        ("Фотографическая мастерская", "Улучшите свои навыки фотографии", "Мастер-классы", "2024-07-05", "Фотостудия", "200", "contact@photoworkshop.com"),
        ("Йога класс", "Утренние занятия йогой", "Мастер-классы", "2024-07-15", "Центр йоги", "100", "register@yogaclass.com")
    ]
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.executemany('''
        INSERT INTO events (title, description, category, date, location, price, contact_info)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', sample_events)
    conn.commit()
    conn.close()
populate_db_with_sample_events()

API_TOKEN = '7133472661:AAFUlIbFBsEpcjlvqtKyJY-GdpfTCjdYCVk'
bot = telebot.TeleBot(API_TOKEN)

def get_events_by_category(category):
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute("SELECT * FROM events WHERE category=?", (category,))
    events = c.fetchall()
    conn.close()
    return events

def add_event_to_db(event_data):
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO events (title, description, category, date, location, price, contact_info)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', event_data)
    conn.commit()
    conn.close()

def request_event_title(message):
    msg = bot.send_message(message.chat.id, 'Введите название события:')
    bot.register_next_step_handler(msg, request_event_description)

def request_event_description(message):
    data = {'title': message.text}
    msg = bot.send_message(message.chat.id, 'Введите описание события:')
    bot.register_next_step_handler(msg, request_event_category, data)

def request_event_category(message, data):
    data['description'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите категорию события (Концерты, Выставки, Фестивали, Мастер-классы):')
    bot.register_next_step_handler(msg, request_event_date, data)

def request_event_date(message, data):
    data['category'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите дату события (формат YYYY-MM-DD):')
    bot.register_next_step_handler(msg, request_event_location, data)

def request_event_location(message, data):
    data['date'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите место проведения события:')
    bot.register_next_step_handler(msg, request_event_price, data)

def request_event_price(message, data):
    data['location'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите цену билета:')
    bot.register_next_step_handler(msg, request_event_contact_info, data)

def request_event_contact_info(message, data):
    data['price'] = message.text
    msg = bot.send_message(message.chat.id, 'Введите контактную информацию:')
    bot.register_next_step_handler(msg, process_event_addition, data)

def process_event_addition(message, data):
    data['contact_info'] = message.text
    try:
        add_event_to_db(tuple(data.values()))
        bot.send_message(message.chat.id, "Событие успешно добавлено!")
    except Exception as e:
        bot.send_message(message.chat.id, 'Ошибка при добавлении события: ' + str(e))

@bot.message_handler(func=lambda message: message.text == 'Добавить событие')
def handle_add_event(message):
    request_event_title(message)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Устанавливаем resize_keyboard=True для удобства отображения
    # Размещаем кнопки по строкам
    markup.row('Концерты', 'Выставки')
    markup.row('Фестивали', 'Мастер-классы')
    markup.row('Добавить событие')
    bot.send_message(message.chat.id, "Выберите категорию события или добавьте новое:", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['Концерты', 'Выставки', 'Фестивали', 'Мастер-классы'])
def handle_category(message):
    events = get_events_by_category(message.text)
    for event in events:
        bot.send_message(message.chat.id, f"{event[1]} - {event[4]} - {event[5]}")

@bot.message_handler(func=lambda message: message.text == 'Добавить событие')
def handle_add_event(message):
    request_event_info(message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извините, я не понял ваш запрос.")

bot.polling()
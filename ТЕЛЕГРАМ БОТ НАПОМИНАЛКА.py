import telebot
import datetime
import time
import threading
import random
from gtts import gTTS
import os


bot = telebot.TeleBot('7068949693:AAGfm3WjgISQ-GnOCmNZLbII7XKAvdnbWIc')

morning_remember = "09:00"
afternoon_remember = "12:00"
evening_remember = "20:55"

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, " привет, я чат бот который будет напоминать тебе делать зарядку")
    sozdat_potok = threading.Thread(target=send_reminds, args=(message.chat.id,))
    sozdat_potok.start()
@bot.message_handler(commands=['fact'])
def fact_message(message):

    list = ['**Улучшает кровообращение**: Утренняя физическая зарядка способствует ускорению кровотока и насыщению органов и тканей кислородом. Это не только улучшает работоспособность и концентрацию внимания в течение дня, но и положительно сказывается на общем состоянии здоровья, в том числе на состоянии сердечно-сосудистой системы',"**Способствует выработке эндорфинов**: Упражнения во время зарядки стимулируют выработку эндорфинов, известных как гормоны счастья. Эндорфины помогают снизить уровень стресса и тревожности, также они могут облегчить болевые ощущения. Благодаря этому утренняя физическая активность помогает улучшить настроение и повысить мотивацию на весь день","**Улучшает метаболизм**: Регулярная утренняя зарядка способствует ускорению обмена веществ, что, в свою очередь, помогает контролировать вес. Повышенная метаболическая активность после утренних упражнений означает, что организм будет сжигать больше калорий не только во время самой зарядки, но и в течение дня, что способствует поддержанию здорового веса и предотвращению набора лишних килограммов"]
    random_fact = random.choice(list)
    bot.reply_to(message, f'Расскажу тебе несколько фактов о зарядке {random_fact}' )


def send_audio_message(chat_id, text):
    tts = gTTS(text=text, lang='ru')
    file_name = 'audio_message.ogg'
    tts.save(file_name)
    with open(file_name, 'rb') as audio:
        bot.send_voice(chat_id, audio)
    os.remove(file_name)  # Удаление файла после отправки

def send_reminds(chat_id):
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == morning_remember:
            send_audio_message(chat_id, "Утренняя зарядка")
            time.sleep(61)
        elif now == afternoon_remember:
            send_audio_message(chat_id, "Дневная зарядка")
            time.sleep(61)
        elif now == evening_remember:
            send_audio_message(chat_id, "Вечерняя зарядка")
            time.sleep(61)
        time.sleep(1)


bot.polling(none_stop=True) #чтобы бот включеным постоянноо


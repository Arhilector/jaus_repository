import requests
from bs4 import BeautifulSoup
from googletrans import Translator


def get_english_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        english_word = soup.find('div', id="random_word").text.strip()
        word_definition = soup.find('div', id="random_word_definition").text.strip()

        return {
            'english_word': english_word,
            'word_definition': word_definition
        }
    except:
        print(f'Произошла ошибка')


def word_game():
    translator = Translator()
    print("Добро пожаловать в игру 'Слова'")

    while True:
        word_dict = get_english_words()
        word = word_dict.get('english_word')
        word_definition = word_dict.get('word_definition')

        # Переводим описание слова на русский
        translated_definition = translator.translate(word_definition, src='en', dest='ru').text
        print(f'Значение слова: {translated_definition}')

        user_input = input("Что это за слово? ")


        # Переводим ответ пользователя на английский
        translated_user_input = translator.translate(user_input, src='ru', dest='en').text

        if translated_user_input.lower() == word.lower(): # lower() - приводит к нижнему регистру
            print('Верно!')
        else:
            print(f"Неверно. Было загадано слово: {word}")

        play_again = input("Хотите сыграть еще раз? (y/n): ")
        if play_again.lower() != 'y':
            print("Спасибо за игру!")
            break  # Выход из цикла


word_game()
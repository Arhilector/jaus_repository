# main.py
import requests

def get_random_cat():
    try:
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        if response.status_code == 200:
            data = response.json()
            return data[0]['url']  # Возвращаем только URL изображения
        return None
    except Exception:
        return None
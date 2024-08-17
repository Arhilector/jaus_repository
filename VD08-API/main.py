import requests
from flask import Flask, render_template, request
from urllib.parse import quote

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = get_news()
    error = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather = get_weather(city)
            if weather is None:
                error = "Город не найден."

    return render_template("index.html", weather=weather, news=news, error=error)


def get_weather(city):
    api_key = "ab67e558f089a2e9111e8046a4bdc4b0"
    city_encoded = quote(city)  # Кодирование названия города
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_news():
    api_key = "99c4a16d935941f5ae87121d730094f0"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        return []


if __name__ == '__main__':
    app.run(debug=True)

import pytest
from main import get_weather


def test_get_weather_success(mocker):
    mock_get = mocker.patch('main.requests.get')

    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 200


    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    } # вместо запроса к API мок-ответ

    api_key = 'ab67e558f089a2e9111e8046a4bdc4b0'
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }

def test_get_weather_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    api_key = 'ab67e558f089a2e9111e8046a4bdc4b0'
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data is None
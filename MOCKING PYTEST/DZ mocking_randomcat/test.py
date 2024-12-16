
import pytest
from main import get_random_cat


def test_get_random_cat_success(mocker):
    # Создаем мок для успешного ответа с реальными данными
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{
        "id": "b40",
        "url": "https://cdn2.thecatapi.com/images/b40.jpg",
        "width": 900,
        "height": 1200
    }]

    # Подменяем реальный запрос на мок
    mock_get = mocker.patch('main.requests.get', return_value=mock_response)

    result = get_random_cat()

    # Проверяем, что функция вернула правильный URL
    assert result == 'https://cdn2.thecatapi.com/images/b40.jpg'
    # Проверяем, что запрос был сделан по правильному URL
    mock_get.assert_called_once_with('https://api.thecatapi.com/v1/images/search')


def test_get_random_cat_error(mocker):
    # Создаем мок для неуспешного ответа
    mock_response = mocker.Mock()
    mock_response.status_code = 404

    # Подменяем реальный запрос на мок
    mocker.patch('main.requests.get', return_value=mock_response)

    result = get_random_cat()

    # Проверяем, что функция вернула None при ошибке
    assert result is None


def test_get_random_cat_exception(mocker):
    # Подменяем requests.get, чтобы он вызывал исключение
    mocker.patch('main.requests.get', side_effect=Exception('Connection error'))

    result = get_random_cat()

    # Проверяем, что функция вернула None при исключении
    assert result is None
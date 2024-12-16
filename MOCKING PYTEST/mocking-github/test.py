import pytest
from main import get_github_user

def test_get_github_user(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'blabla',
        "id": 435435345,
        "name": "Arhilector"
    } # эту хуйню

    user_data = get_github_user('blabla') # передаем имя юзера

    assert user_data == {
        'login': 'blabla',
        "id": 435435345,
        "name": "Arhilector"
    } # сравниваем с этой хуйней

def test_get_github_user_with_error(mocker):
   mock_get = mocker.patch('main.requests.get')
   mock_get.return_value.status_code = 500

   user_data = get_github_user('cat')
   assert user_data == None


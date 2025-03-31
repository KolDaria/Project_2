from typing import Any
from unittest.mock import Mock, patch

from src.interaction_API import HeadHunterAPI


@patch('requests.get')
def test_connect(mock_get: Any, capsys: Any) -> Any:
    api = HeadHunterAPI()
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'items': [{'id': 1}, {'id': 2}]}

    mock_get.return_value = mock_response
    api.connect()

    captured = capsys.readouterr()
    assert "Подключение успешно" in captured.out
    mock_get.assert_called_once_with('https://api.hh.ru/vacancies')


@patch('requests.get')
def test_connect_invalid_status_code(mock_get: Any, capsys: Any) -> Any:
    api = HeadHunterAPI()
    mock_response = Mock()
    mock_response.status_code = 400
    mock_response.json.return_value = {'items': [{'id': 1}, {'id': 2}]}

    mock_get.return_value = mock_response
    api.connect()

    captured = capsys.readouterr()
    assert "Запрос не был успешным." in captured.out
    mock_get.assert_called_once_with('https://api.hh.ru/vacancies')


@patch('requests.get')
def test_load_vacancies(mock_get: Any) -> Any:
    api = HeadHunterAPI()
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'items': [{'id': 117652180, "name": "Аналитик данных"}]}

    mock_get.return_value = mock_response
    api.load_vacancies("Аналитик данных")

    assert len(api.get_vacancies()) == 20
    assert api.get_vacancies()[0]['name'] == 'Аналитик данных'


@patch('requests.get')
def test_load_vacancies_invalid_status_code(mock_get: Any, capsys: Any) -> Any:
    api = HeadHunterAPI()
    mock_response = Mock()
    mock_response.status_code = 404

    mock_get.return_value = mock_response
    api.load_vacancies("hjjk")

    captured = capsys.readouterr()
    assert "Ошибка при загрузке вакансий." in captured.out

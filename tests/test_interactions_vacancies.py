from typing import Any

from src.interactions_vacancies import Vacancy


def test_create_vacancy_objects_valid() -> Any:
    raw_vacancies = [{
        "name": "Python-разработчик",
        "alternate_url": "https://hh.ru/vacancy/118783415",
        "salary": {'from': 50000, 'to': 70000},
        'snippet': {'requirement': 'Python', 'responsibility': 'Develop software'}
        },
        {
        "name": "Backend-разработчик",
        "alternate_url": "https://hh.ru/vacancy/118830536",
        "salary": {'from': 30000},
        'snippet': {'requirement': 'Test', 'responsibility': 'Test software'}
        }]
    vacancies_list = Vacancy.create_vacancy_objects(raw_vacancies)
    assert len(vacancies_list) == 2
    assert vacancies_list[0].name == 'Python-разработчик'
    assert vacancies_list[0].salary == 60000.0
    assert vacancies_list[1].name == 'Backend-разработчик'
    assert vacancies_list[1].salary == 30000.0


def test_create_vacancy_objects_invalid_salary() -> Any:
    raw_vacancies = [
        {
            'name': 'Invalid Salary',
            'salary': {'from': 'abc', 'to': 70000},
            'alternate_url': 'http://example.com',
            'snippet': {'requirement': 'Something', 'responsibility': 'Do something'}
        },
        {
            'name': 'Invalid Salary',
            'salary': {'from': None, 'to': None},
            'alternate_url': 'http://example.com',
            'snippet': {'requirement': 'Something', 'responsibility': 'Do something'}
        },
    ]

    vacancies = Vacancy.create_vacancy_objects(raw_vacancies)

    assert len(vacancies) == 2
    assert vacancies[0].salary == 0.0
    assert vacancies[1].salary == 0.0


def test_create_vacancy_objects_exception(capsys: Any) -> Any:
    raw_vacancies = [
        {
            'name': 'Invalid Salary',
            'salary': {'from': 'abc', 'to': '70000'},
            'alternate_url': 'http://example.com',
            'snippet': {'requirement': 'Something', 'responsibility': 'Do something'}
        }
    ]

    Vacancy.create_vacancy_objects(raw_vacancies)
    captured = capsys.readouterr()
    assert "Ошибка при обработке зарплаты для вакансии" in captured.out


def test_create_vacancy_objects_without_salary() -> Any:
    raw_vacancies = [
        {
            'name': 'No Salary',
            'alternate_url': 'http://example.com/vacancy4',
            'snippet': {'requirement': 'Any', 'responsibility': 'Work on something'}
        }
    ]

    vacancies = Vacancy.create_vacancy_objects(raw_vacancies)

    assert vacancies[0].salary == 0.0

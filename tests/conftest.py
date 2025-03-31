from typing import Any

import pytest

from src.interactions_files import JsonFile
from src.interactions_vacancies import Vacancy


@pytest.fixture
def temp_json_file(tmpdir: Any) -> Any:
    """
    Фикстура для создания временного JSON-файла и его очистки после теста.
    """
    filename = tmpdir.join("test_data.json")
    return str(filename)


@pytest.fixture
def json_file_instance(temp_json_file: Any) -> Any:
    """
    Фикстура для создания экземпляра класса JsonFile с временным файлом.
    """
    return JsonFile(filename=temp_json_file)


@pytest.fixture
def sample_data() -> dict:
    """
    Фикстура для предоставления образца данных для тестов.
    """
    return {"name": "Test Vacancy", "salary": 100000, "description": "Test description"}


@pytest.fixture
def sample_vacancies() -> list:
    """
    Фикстура для примера полученных вакансий.
    """
    return [
        Vacancy("Python Developer", "url1", "150000", "Описание с Python"),
        Vacancy("Data Scientist", "url2", "200000", "Описание с анализом данных"),
        Vacancy("Junior Developer", "url3", "80000", "Описание для начинающих"),
        Vacancy("Senior Python Developer", "url4", "250000", "Описание с опытом Python"),
        Vacancy("Project Manager", "url5", "180000", "Управление проектами"),
    ]

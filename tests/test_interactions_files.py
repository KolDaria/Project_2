import json
from typing import Any

from src.interactions_files import FileDesigner, JsonFile


class MockVacancy:
    """
    Мок класс для имитации объекта вакансии
    """

    def __init__(self, name: str, salary: int | float, description: str) -> None:
        self.name = name
        self.salary = salary
        self.description = description

    def to_dict(self) -> dict:
        return {"name": self.name, "salary": self.salary, "description": self.description}


def test_jsonfile_is_subclass_of_filedesigner() -> Any:
    assert issubclass(JsonFile, FileDesigner)


def test_get_data_empty_file(json_file_instance: Any) -> Any:
    assert json_file_instance.get_data() == []


def test_get_data_existing_data(json_file_instance: Any, temp_json_file: str) -> Any:
    data = [{"name": "Vacancy1", "salary": 50000}, {"name": "Vacancy2", "salary": 60000}]
    with open(temp_json_file, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    assert json_file_instance.get_data() == data


def test_add_data(json_file_instance: Any, sample_data: dict, temp_json_file: str) -> Any:
    mock_vacancy = MockVacancy(**sample_data)
    json_file_instance.add_data(mock_vacancy)
    with open(temp_json_file, "r", encoding='utf-8') as f:
        file_content = json.load(f)
    assert len(file_content) == 1
    assert file_content[0] == sample_data


def test_add_data_duplicate(json_file_instance: Any, sample_data: dict, temp_json_file: str) -> Any:

    mock_vacancy = MockVacancy(**sample_data)

    json_file_instance.add_data(mock_vacancy)

    json_file_instance.add_data(mock_vacancy)

    with open(temp_json_file, "r", encoding='utf-8') as f:
        file_content = json.load(f)

    assert len(file_content) == 1, "Duplicate data was added"
    assert file_content[0] == sample_data


def test_del_data(json_file_instance: Any, sample_data: dict, temp_json_file: str) -> Any:
    mock_vacancy = MockVacancy(**sample_data)
    json_file_instance.add_data(mock_vacancy)
    json_file_instance.add_data(MockVacancy("Another Vacancy", 70000, "Another Description"))

    json_file_instance.del_data(mock_vacancy)

    with open(temp_json_file, "r", encoding='utf-8') as f:
        file_content = json.load(f)
    assert len(file_content) == 1
    assert file_content[0]["name"] == "Another Vacancy"


def test_del_data_not_found(json_file_instance: Any, temp_json_file: str) -> Any:
    initial_data = [{"name": "Initial Vacancy", "salary": 60000, "description": "Initial Description"}]
    with open(temp_json_file, "w", encoding='utf-8') as f:
        json.dump(initial_data, f, indent=4, ensure_ascii=False)

    vacancy_to_delete = MockVacancy("Nonexistent Vacancy", 50000, "Description")
    json_file_instance.del_data(vacancy_to_delete)

    with open(temp_json_file, "r", encoding='utf-8') as f:
        file_content = json.load(f)
    assert file_content == initial_data

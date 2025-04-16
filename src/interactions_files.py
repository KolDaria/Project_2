import json
from abc import ABC, abstractmethod
from typing import Any

from config import PATH_JSON_FILE

path_json = PATH_JSON_FILE


class FileDesigner(ABC):
    """
    Абстрактный класс для работы с файлами
    """
    @abstractmethod
    def get_data(self) -> None:
        pass

    @abstractmethod
    def add_data(self, data: Any) -> None:
        pass

    @abstractmethod
    def del_data(self, data: Any) -> None:
        pass


class JsonFile(FileDesigner):
    """
    Класс для загрузки данных в json файл
    """

    def __init__(self, filename: str = path_json) -> None:
        """
        Метод инициализации класса
        """
        self.__filename = filename

    def get_data(self) -> Any:
        """
        Метод получения данных из файла
        """
        try:
            with open(self.__filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_data(self, data: Any) -> Any:
        """
        Метод добавления данных в файл
        """
        vacancies = self.get_data()

        if not any(v['name'] == data.name for v in vacancies):
            vacancies.append(data.to_dict())
        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

    def del_data(self, data: Any) -> Any:
        """
        Метод удаления данных из файла
        """
        vacancies = self.get_data()
        vacancies = [v for v in vacancies if v['name'] != data.name]

        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

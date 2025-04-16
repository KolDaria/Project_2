from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    """
    Абстрактный родительский класс
    """
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def load_vacancies(self, keyword: str) -> None:
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """
    __url: str
    __headers: dict
    __params: dict
    __vacancies: list

    def __init__(self) -> None:
        """
        Метод инициализации класса
        """
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100, 'area': 113}
        self.__vacancies = []

    def connect(self) -> None:
        """
        Метод для проверки подключения к API.
        """
        self.__private_execute_connect()

    def __private_execute_connect(self) -> None:
        """
        Приватный метод подключения к API HH
        """
        response = requests.get(self.__url)
        if response.status_code == 200:
            print("Подключение успешно")
        else:
            print(f"Запрос не был успешным. Возможная причина: {response.reason}")

    def load_vacancies(self, keyword: str) -> None:
        """
        Метод для загрузки вакансий по ключевому слову.
        """
        self.__params['text'] = keyword
        self.connect()
        while self.__params.get('page') < 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code != 200:
                print("Ошибка при загрузке вакансий.")
                break
            vacancies_keyword = response.json().get('items', [])
            self.__vacancies.extend(vacancies_keyword)
            self.__params['page'] += 1

    def get_vacancies(self) -> list[dict]:
        """
        Метод для получения загруженных вакансий.
        """
        return self.__vacancies

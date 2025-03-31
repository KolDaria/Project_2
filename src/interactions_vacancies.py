from src.interaction_API import HeadHunterAPI


class Vacancy(HeadHunterAPI):
    """
    Класс для работы с вакансиями.
    """
    __slots__ = ["name", "vacancies_urls", "salary", "description"]

    def __init__(self, name: str, vacancies_urls: str, salary: str, description: str) -> None:
        """
        Метод инициализации атрибутов класса
        """
        super().__init__()
        self.name = name
        self.vacancies_urls = vacancies_urls
        self.salary = self.__validate_salary(salary)
        self.description = description

    def __lt__(self, other: 'Vacancy') -> bool:
        """
        Метод сравнения вакансий между собой по зарплате
        """
        return self.salary < other.salary

    def __gt__(self, other: 'Vacancy') -> bool:
        """
        Метод сравнения вакансий между собой по зарплате
        """
        return self.salary > other.salary

    def __eq__(self, other: 'Vacancy') -> bool:
        """
        Метод сравнения вакансий между собой по зарплате
        """
        return self.salary == other.salary

    def __str__(self) -> str:
        """
        Метод вывода информации о вакансиях
        """
        return (f"Вакансия: {self.name}, Зарплата: {self.salary}, URL: {self.vacancies_urls}, "
                f"Описание: {self.description}")

    def __validate_salary(self, salary: str) -> float:
        """
        Метод валидации данных по зарплате и извлечение средней зарплаты
        """
        if salary is None:
            return 0.0
        return float(salary)

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'vacancies_urls': self.vacancies_urls,
            'salary': self.salary,
            'description': self.description
        }

    @classmethod
    def create_vacancy_objects(cls, raw_vacancies: list[dict]) -> list['Vacancy']:
        """
        Преобразование вакансий (из JSON) в список вакансий
        """
        vacancies = []
        for item in raw_vacancies:
            name = item['name']
            salary_info = item.get('salary')
            salary = 0.0
            if salary_info:
                salary_from = salary_info.get('from')
                salary_to = salary_info.get('to')
                if salary_from is not None and salary_to is not None:
                    try:
                        salary = (float(salary_from) + float(salary_to)) / 2
                    except (TypeError, ValueError):
                        print(
                            f"Ошибка при обработке зарплаты для вакансии {name}.  salary_from: {salary_from}, "
                            f"salary_to: {salary_to}")
                        salary = 0.0
                elif salary_from is not None:
                    try:
                        salary = float(salary_from)
                    except (TypeError, ValueError):
                        print(f"Ошибка при обработке зарплаты для вакансии {name}.  salary_from: {salary_from}")
                        salary = 0.0
                elif salary_to is not None:
                    try:
                        salary = float(salary_to)
                    except (TypeError, ValueError):
                        print(f"Ошибка при обработке зарплаты для вакансии {name}.  salary_to: {salary_to}")
                        salary = 0.0
            url = item['alternate_url']
            description = (item['snippet']['requirement'] or '') + ' ' + (item['snippet']['responsibility'] or '')
            vacancies.append(cls(name, url, str(salary), description))
        return vacancies

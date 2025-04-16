from typing import Any

from src.interaction_API import HeadHunterAPI
from src.interactions_files import JsonFile
from src.interactions_vacancies import Vacancy


def filter_vacancies(vacancies_list: list, filter_words: list[str]) -> list:
    """
    Фильтрация вакансий по ключевому слову
    """
    filtered_vacancies = []
    for vacancy in vacancies_list:
        if any(word.lower() in vacancy.description.lower() for word in filter_words):
            filtered_vacancies.append(vacancy)
    return filtered_vacancies


def get_vacancies_by_salary(vacancies_list: list, salary_range: str) -> list:
    """
    Фильтрация вакансий по заданному диапазону зарплат
    """
    try:
        min_salary, max_salary = map(int, salary_range.replace(" ", "").split('-'))
    except ValueError:
        print("Неверный формат диапазона зарплат. Возвращаются все вакансии.")
        return vacancies_list

    ranged_vacancies = []
    for vacancy in vacancies_list:
        if min_salary <= vacancy.salary <= max_salary:
            ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(vacancies_list: list) -> list:
    """
    Сортировка вакансий по заработной плате в порядке убывания.
    """
    return sorted(vacancies_list, reverse=True)


def get_top_vacancies(vacancies_list: list, top_n: int) -> list:
    """
    Возвращает топ N-ых вакансий
    """
    return vacancies_list[:top_n]


def save_vacancies(saving_input: str, top_vacancies: list) -> Any:
    """
    Сохраняет вакансии в файл json
    """
    for vac in top_vacancies:
        if saving_input.lower() == "да":
            json_file = JsonFile()
            json_file.add_data(vac)
    return "Вакансии успешно добавлены"


def user_interaction() -> None:
    """
    Взаимодействует с пользователем
    """
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат, пример ввода 100000 - 150000: ")

    hh_api = HeadHunterAPI()
    hh_api.load_vacancies(search_query)
    raw_vacancies = hh_api.get_vacancies()

    vacancies_list = Vacancy.create_vacancy_objects(raw_vacancies)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    for vacancy in top_vacancies:
        print(vacancy)

    saving_input = input(f"Сохранить {top_n} вакансий в файл: ")
    save_vacancies(saving_input, top_vacancies)

from typing import Any

from src.utils import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, sort_vacancies


def test_filter_vacancies_keyword_found(sample_vacancies: list) -> Any:
    filter_words = ["Python"]
    filtered_vacancies = filter_vacancies(sample_vacancies, filter_words)
    assert len(filtered_vacancies) == 2
    assert "Python Developer" in [v.name for v in filtered_vacancies]
    assert "Senior Python Developer" in [v.name for v in filtered_vacancies]


def test_filter_vacancies_keyword_not_found(sample_vacancies: list) -> Any:
    filter_words = ["Java"]
    filtered_vacancies = filter_vacancies(sample_vacancies, filter_words)
    assert len(filtered_vacancies) == 0


def test_get_vacancies_by_salary_valid_range(sample_vacancies: list) -> Any:
    salary_range = "100000 - 200000"
    ranged_vacancies = get_vacancies_by_salary(sample_vacancies, salary_range)
    assert len(ranged_vacancies) == 3
    salaries = [v.salary for v in ranged_vacancies]
    assert all(100000 <= s <= 200000 for s in salaries)


def test_get_vacancies_by_salary_empty_range(sample_vacancies: list, capsys: Any) -> Any:
    salary_range = ""
    ranged_vacancies = get_vacancies_by_salary(sample_vacancies, salary_range)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Неверный формат диапазона зарплат. Возвращаются все вакансии."
    assert ranged_vacancies == sample_vacancies


def test_sort_vacancies(sample_vacancies: list) -> Any:
    sorted_vacancies = sort_vacancies(sample_vacancies)
    salaries = [v.salary for v in sorted_vacancies]
    assert salaries == [250000, 200000, 180000, 150000, 80000]


def test_get_top_vacancies(sample_vacancies: list) -> Any:
    top_n = 3
    top_vacancies = get_top_vacancies(sample_vacancies, top_n)
    assert len(top_vacancies) == 3
    assert [v.name for v in top_vacancies] == [
        "Python Developer",
        "Data Scientist",
        "Junior Developer",
    ]


def test_get_top_vacancies_zero(sample_vacancies: list) -> Any:
    top_n = 0
    top_vacancies = get_top_vacancies(sample_vacancies, top_n)
    assert len(top_vacancies) == 0
    assert top_vacancies == []

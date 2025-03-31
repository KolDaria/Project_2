# Проект 2.

## **Установка:**

Версия python для данного проекта `^3.13`

1. Установите Poetry:
```
https://install.python-poetry.org | python -
```
2. Клонируйте репозиторий:
```
git clone https://github.com/KolDaria/Project_2
```
3. Установите зависимости:
```
poetry add requests
```

## **Использование:**

### *Проект содержит:*

#### Папку `src` в которой реализованны следующие функции:

1. `__init__`: инициализация объекта.
2. `Parser`: создан абстрактный (родительский) класс для класса API.
3. `HeadHunterAPI`: класс для работы с API.
4. `Vacancy`: класс для работы с полученными вакансиями.
5. `FileDesigner`: создан абстрактный (родительский) класс для класса загрузки вакансий в json файл.
6. `JsonFile`: класс для загрузки данных в json файл.
7. `filter_vacancies`: вспомогательная функция фильтрации вакансий по ключевому слову.
8. `get_vacancies_by_salary`: вспомогательная функция фильтрации вакансий по заданному диапазону зарплат.
9. `sort_vacancies`: вспомогательная функция сортировки вакансий по заработной плате в порядке убывания.
10. `get_top_vacancies`: вспомогательная функция возвращающая топ N-ых вакансий.
11. `save_vacancies`: вспомогательная функция сохраняющая вакансии в файл json.
12. `user_interaction`: функция для взаимодействия с пользователем. 

#### Папку `tests` в которой реализованно следующее:

1. `__init__`: инициализация объекта.
2. `test_utils.py`: модуль для тестирования функций `filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, save_vacancies, user_interaction`.
3. `test_interaction_API.py`: модуль для тестирования класса `HeadHunterAPI`.
4. `test_interactions_files.py`: модуль для тестирования класса `JsonFile`.
5. `test_interactions_vacancies.py`: модуль для тестирования класса `Vacancy`.

#### Папку `data` которая содержит:

1. `data.json`: файл содержащий сохраненные вакансии.

#### В корне проекта:

1. `main.py`: функция связывающая функциональности между собой.

##### Примеры использования функций `filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies`:

```python

# Пример для функции filter_vacancies
filter_words = ["Python"]  # входной аргумент
"Python Developer"
"Senior Python Developer"  # выход функции
# Пример для функции get_vacancies_by_salary
salary_range = "100000 - 200000"  # входной аргумент
"100000"  # выход функции
# Пример для функции sort_vacancies
vac1 = Vacancy("Python Developer", "url1", 150000, "Описание с Python"),
vac2 = Vacancy("Data Scientist", "url2", 200000, "Описание с анализом данных")  # входной аргумент
[200000, 150000]  # выход функции
# Пример для функции get_top_vacancies
top_n = 3  # входной аргумент
[
    "Python Developer",
    "Data Scientist",
    "Junior Developer",
    ]                  # выход функции

```

## Тестирование функций:

```
---------- coverage: platform win32, python 3.13.0-final-0 -----------
Name                                   Stmts   Miss  Cover
----------------------------------------------------------
config.py                                  4      0   100%
src\__init__.py                            0      0   100%
src\interaction_API.py                    39      2    95%
src\interactions_files.py                 35      3    91%
src\interactions_vacancies.py             55     13    76%
src\utils.py                              48     21    56%
tests\__init__.py                          0      0   100%
tests\conftest.py                         17      0   100%
tests\test_interaction_API.py             44      0   100%
tests\test_interactions_files.py          52      0   100%
tests\test_interactions_vacancies.py      25      0   100%
tests\test_utils.py                       38      0   100%
----------------------------------------------------------
TOTAL                                    357     39    89%

```

## Документация:

Дополнительную информацию о структуре проекта и API можно найти в [документации](docs/README.md).

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).
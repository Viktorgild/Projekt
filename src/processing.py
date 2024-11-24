import logging
from venv import logger


logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("..\\logs\\processing.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


list_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция возвращает список словарей по ключу."""
    result = []
    for item in list_dict:
        if item["state"] == state:
            result.append(item)
    logging.info("Фильтрация списка словарей.")
    return result
filtered_list = filter_by_state(list_dict)
print("Отфильтрованный список:")
for item in filtered_list:
    print("- ", item["id"], ":", item["state"])

def sort_by_date(list_dict: list, order: str = "DESC") -> list:
    """Функция сортирует список словарей по дате."""
    result = sorted(list_dict, key=lambda x: x["date"], reverse=(order == "DESC"))
    logging.info("Сортировка списка словарей по дате.")
    return result
filtered_list = filter_by_state(list_dict)
sorted_list = sort_by_date(filtered_list)
print("Отсортированный список:")
for item in sorted_list:
    print("- ", item["id"], ":", item["state"], ", дата:", item["date"])

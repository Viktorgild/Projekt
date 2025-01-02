import logging
from venv import logger

logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("..\\logs\\processing.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция возвращает список словарей по ключу."""
    result = []
    for item in list_dict:
        if "state" in item:
            if item["state"] == state:
                result.append(item)
    logging.info("Фильтрация списка словарей.")
    return result


def sort_by_date(list_dict: list, order: bool = False) -> list:
    """Функция сортирует список словарей по дате."""
    result = sorted(list_dict, key=lambda x: x["date"], reverse=order)
    logging.info("Сортировка списка словарей по дате.")
    return result

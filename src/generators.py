import logging
from typing import Dict, Iterator
from venv import logger

logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("..\\logs\\generators.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def filter_by_currency(transactions: list, currency: str) -> Iterator:
    """Функция, которая принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочерёдно выдаёт транзакции, где валюта
    операции соответствует заданной (например, USD).
    """
    # logger.info("Starting filter_by_currency function")
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except KeyError:
            if transaction["currency_code"] == currency:
                yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[Dict]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    logger.info("Starting transaction_descriptions function")
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    """Генератор, который выдаёт номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    logger.info("Starting card_number_generator function with start: {}, end: {}".format(start, end))
    for i in range(start, end + 1):
        card_num = str(i).zfill(16)
        yield card_num[:4] + " " + card_num[4:8] + " " + card_num[8:12] + " " + card_num[12:16]

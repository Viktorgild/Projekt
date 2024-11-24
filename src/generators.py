import logging
from venv import logger

logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("..\\logs\\generators.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


transactions = [
    {
        "description": "Покупка в магазине",
        "operationAmount": {
            "currency": {
                "code": "USD"
            },
            "value": 100
        }
    },
    {
        "description": "Перевод другу",
        "operationAmount": {
            "currency": {
                "code": "EUR"
            },
            "value": 50
        }
    }
]


def filter_by_currency(transactions, currency):
    """Функция, которая принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочерёдно выдаёт транзакции, где валюта операции соответствует заданной (например, USD).
    """
    logger.info("Starting filter_by_currency function")
    filtered_transactions = []
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            filtered_transactions.append(transaction)
    return filtered_transactions
filtered_transactions = filter_by_currency(transactions, "USD")
for transaction in filtered_transactions:
    print("- ", transaction["description"])


def transaction_descriptions(transactions):
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    logger.info("Starting transaction_descriptions function")
    for transaction in transactions:
        yield transaction["description"]


transaction_descriptions_generator = transaction_descriptions(transactions)
for description in transaction_descriptions_generator:
    print("- ", description)


def card_number_generator(start, end):
    """Генератор, который выдаёт номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    logger.info("Starting card_number_generator function with start: {}, end: {}".format(start, end))
    for i in range(start, end + 1):
        card_num = str(i).zfill(16)
        yield card_num[:4] + " " + card_num[4:8] + " " + card_num[8:12] + " " + card_num[12:16]

card_numbers = card_number_generator(1000, 2000)
print("Номера карт:")
for card_num in card_numbers:
    print("- ", card_num)
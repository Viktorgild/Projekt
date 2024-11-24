import json
from typing import Any
import os
import logging
from venv import logger

logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("..\\logs\\utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_financial_transactions_data(file_path: str) -> Any:
    """
    Функция для получения данных о финансовых операциях из файла в формате JSON.

    Args:
        file_path: путь к файлу с данными о финансовых операциях.

    Returns:
        Данные о финансовых операциях в виде списка или пустой список, если данные не удалось загрузить.
    """
    _list = []
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            transactions = json.load(file)
            if transactions == 0 or type(transactions) != list:
                return _list
            else:
                logger.info("Данные о транзакциях успешно загружены.")
                return transactions
        except json.JSONDecodeError:
            print("invalid JSON data")
            logger.error("Обнаружены неверные данные JSON.")
            return _list


if __name__ == "__main__":
    path_to_file = os.path.join(os.path.dirname(__file__), "data", "operations.json")
    transactions_data = get_financial_transactions_data(r"C:\Users\35347\PycharmProjects\Projekt\data\operations.json")
    print(transactions_data)

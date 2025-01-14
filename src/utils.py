import json
from typing import Any


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
            if not isinstance(transactions, list):
                return _list
            else:
                return transactions
        except json.JSONDecodeError:
            print("invalid JSON data")
            return _list


#

import re
from collections import Counter


def filter_bank_operations(bank_operations: list[dict], search_string: str) -> list[dict]:
    # Создаем пустой список для хранения отфильтрованных словарей
    filtered_bank_operations = []

    # Проходимся по каждому словарю в списке bank_operations
    for operation in bank_operations:
        # Используем регулярное выражение для проверки наличия строки search_string в описании операции
        if re.search(search_string, operation["description"]):
            # Если строка найдена, добавляем словарь в отфильтрованный список
            filtered_bank_operations.append(operation)

    return filtered_bank_operations


def count_bank_operations_by_category(bank_operations, categories):
    # Инициализируем счетчик для подсчета количества операций в каждой категории
    counter = Counter()

    # Проходимся по каждой операции в списке bank_operations
    for operation in bank_operations:
        # Извлекаем категорию операции из поля description
        category = operation["description"].split()[0]
        if category in categories:
            # Добавляем операцию в соответствующую категорию в счетчике
            counter[category] += 1

    # Преобразуем счетчик в словарь
    result_dictionary = {category: count for category, count in counter.items()}

    # Возвращаем словарь с количеством операций в каждой категории
    return result_dictionary

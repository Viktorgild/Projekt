import collections
import re


def filter_transactions_by_description(bank_operations, search_string):
    # Создаём пустой список для хранения отфильтрованных операций
    filtered_operations = []

    # Проходимся по каждому словарю в списке bank_operations
    for operation in bank_operations:
        # Проверяем наличие ключа 'description' в операции
        if "status" in operation and re.search(search_string, operation["status"].lower()):
            # Если строка найдена и ключ присутствует, добавляем словарь с операцией в filtered_operations
            filtered_operations.append(operation)

    # Возвращаем список отфильтрованных операций
    return filtered_operations


def count_operations_by_category(filtered_operations, categories):
    # Создаём словарь Counter для хранения количества операций в каждой категории
    count_by_category = collections.Counter()

    # Проходимся по каждой операции в отфильтрованном списке
    for operation in filtered_operations:
        # Получаем категорию операции из поля description
        category = operation.get("description", None)  # используем get для обработки отсутствующего ключа

        # Увеличиваем количество операций в данной категории
        count_by_category[category] += 1

    # Возвращаем словарь с количеством операций в каждой категории
    return count_by_category


def sort_operations_by_date(operations):
    sorted_operations = sorted(operations, key=lambda x: x["date"])
    return sorted_operations


def sort_operations_by_currency(operations):
    sorted_operations = {}
    for op in operations:
        currency = op["currency"]
        if currency not in sorted_operations:
            sorted_operations[currency] = [op]
        else:
            sorted_operations[currency].append(op)
    return list(sorted_operations.values())


def print_sorted_operations(operations):
    print("Всего банковских операций в выборке:")
    total_count = len(operations)
    print(total_count)
    for i, op in enumerate(operations):
        print(f"{i+1}. {op['description']}")
        print("Счет:", op["account"])
        print("Сумма:", op["amount"])
        print("Дата:", op["date"])
        print()

from collections.abc import Callable
from functools import wraps
from typing import Any

import pytest


def log(filename: str | None = None) -> Callable:
    def my_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok \n")
                else:
                    print(f"{func.__name__} ok \n")
            except Exception as e:
                error_message = f" {func.__name__} error: {e} : ({args}, {kwargs})"
                if filename:
                    with open(filename, "a") as file:
                        file.write(error_message + ". input: " + str(args) + "," + str(kwargs) + "\n")
                else:
                    print(error_message + ". input: " + str(args) + "," + str(kwargs))
            return result

        return wrapper

    return my_decorator


# @log(filename="mylog.txt")
# def my_func(x: int, y: int) -> int:
#     return x + y
#
#
# result = my_func(14, 22)  # Сохраняем результат в переменную
# print("Результат работы функции:", result)  # Выводим результат на экран

@log()
def my_function(a, b):
    return a / b

# Вызов функции с аргументами, которые вызывают ошибку
result = my_function(1, 0)

# my_function error: тип ошибки. Inputs: (1, 2), {}


# def test_log():
#     with pytest.raises(Exception, match='Enter Number'):
#         my_function
#
#
# def test_may_log(capsys):
#     @log(filename=None)
#     def my_function(x, y):
#         return x + y
#     my_function(1, 2)
#     captured = capsys.readuterr()
#     assert captured.out ==

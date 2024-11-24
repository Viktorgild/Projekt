from collections.abc import Callable
from functools import wraps


def log(filename: str | None = None) -> Callable:
    """
    Декоратор для логирования результатов выполнения функции.

    Параметры:
        filename (str | None): имя файла, в который будут записываться результаты выполнения функций. Если filename не указан или равен None, результаты выводятся на экран.

    Возвращает:
        Callable: декорированную функцию.
    """

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


@log()
def my_function(a, b):
    return a / b


result = my_function(1, 8)

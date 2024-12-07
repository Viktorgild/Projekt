import logging
from venv import logger

from src.masks import get_mask_account, get_mask_card_number

logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("..\\logs\\widget.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_date(input_date: str) -> str:
    """Функция принимает на вход дату и время и выдает дату в порядке ДД.ММ.ГГГГ"""
    logger.info("Функция отработала успешно")
    return input_date.split("T")[0].replace("-", ".")


input_date = "2023-07-14T15:30:00"
result_date = get_date(input_date)
print("Дата в нужном формате:", result_date)


def mask_account_card(user_card: str) -> str | None:
    """Принимать один аргумент — строку, содержащую тип и номер карты или счета.
    Возвращать строку с замаскированным номером.
    """
    if "Счет" in user_card:
        get_acc_numb = f"{user_card[:4]} {get_mask_account(user_card[5:])}"
        logger.info("Номер счета")
        return get_acc_numb
    else:
        get_card_num = f"{user_card[:-16]} {get_mask_card_number(user_card[-16:])}"
        logger.info("Номер карты")
        return get_card_num


user_card = "Счет: 1234567890123456"
result_card_or_acc = mask_account_card(user_card)
print("Замаскированный номер:", result_card_or_acc)

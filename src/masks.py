import logging
from venv import logger

logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("..\\logs\\masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    logger.info("Маскируем карту клиента")
    return card_number[:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[-4:]


def get_mask_account(account_number: str) -> str | None:
    """Функция принимает на вход номер счета и возвращает его маску"""
    logger.info("Маскируем счет клиента")
    return "**" + str(account_number)[-4:]

def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    card_number = str(card_number)
    return card_number[:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[-4:]


def get_mask_account(account_number: str) -> str | None:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return "**" + str(account_number)[-4:]

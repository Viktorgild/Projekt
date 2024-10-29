from src.masks import get_mask_account, get_mask_card_number


def get_date(input_date: str) -> str:
    """Функция принимает на вход дату и время и выдает дату в порядке ДД.ММ.ГГГГ"""
    return input_date.split("T")[0].replace("-", ".")


def mask_account_card(user_card: str) -> str | None:
    """Принимать один аргумент — строку, содержащую тип и номер карты или счета.
    Возвращать строку с замаскированным номером.
    """
    if "Счет" in user_card:
        get_acc_numb = f"{user_card[:4]} {get_mask_account(user_card[5:])}"
        return get_acc_numb
    else:
        get_card_num = f"{user_card[:-16]} {get_mask_card_number(user_card[-16:])}"
        return get_card_num

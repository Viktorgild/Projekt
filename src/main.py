#from src.widget import get_date, mask_account_card
from src.processing import list_dict, filter_by_state

#print(get_date(str("2024-03-11T02:26:18.671407")))
#print(mask_account_card(str("Maestro 1596837868705199")))
#print(mask_account_card(str("Счет 64686473678894779589")))
#print(mask_account_card(str("MasterCard 7158300734726758")))
#print(mask_account_card(str("Счет 35383033474447895560")))
#print(mask_account_card(str("Visa Classic 6831982476737658")))
#print(mask_account_card(str("Visa Platinum 8990922113665229")))
#print(mask_account_card(str("Visa Gold 5999414228426353")))
#print(mask_account_card(str("Счет 73654108430135874305")))


print(filter_by_state(list_dict, 'CANCELED'))
from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, list_dict, sort_by_date

#print(get_date(str("2024-03-11T02:26:18.671407")))
#print(mask_account_card(str("Maestro 1596837868705199")))
# print(mask_account_card(str("Счет 64686473678894779589")))
# print(mask_account_card(str("MasterCard 7158300734726758")))
# print(mask_account_card(str("Счет 35383033474447895560")))
# print(mask_account_card(str("Visa Classic 6831982476737658")))
# print(mask_account_card(str("Visa Platinum 8990922113665229")))
# print(mask_account_card(str("Visa Gold 5999414228426353")))
# print(mask_account_card(str("Счет 73654108430135874305")))

#print(
 #   sort_by_date(
 #       [
 #           {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
 #           {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
 #           {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
 #           {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
 #       ]
 #   )
#)
print(filter_by_state(list_dict, "CANCELED"))

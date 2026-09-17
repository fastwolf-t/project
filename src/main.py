import masks
import widget
import processing
import utils

# print(masks.get_mask_card_number("9923923271549754"))
# print(masks.get_mask_account("73654108430135874305"))

client_bank_operations = [
    {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

# тест функции mask_account_card в 2 случаях
utils.print_result("mask_account_card()", widget.mask_account_card("Visa Platinum 7000792289606361"))
utils.print_result("mask_account_card()", widget.mask_account_card("Счет 73654108430135874305"))
utils.print_result("get_date()", widget.get_date("2024-03-11T02:26:18.671407"))

# тест функции filter_by_state в 2 случаях
utils.print_result("filter_by_state()", processing.filter_by_state(client_bank_operations))
utils.print_result("filter_by_state()", processing.filter_by_state(client_bank_operations, "CANCELED"))

# тест функции sort_by_date в 2 случаях
print("sort_by_date()", processing.sort_by_date(client_bank_operations))
print("sort_by_date()", processing.sort_by_date(client_bank_operations, False))

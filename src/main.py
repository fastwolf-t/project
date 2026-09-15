# import masks
import processing

# print(masks.get_mask_card_number("9923923271549754"))
# print(masks.get_mask_account("73654108430135874305"))

data_to_test = [
    {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

# тест функции filter_by_state в 2 случаях
print(f"""processing.filter_by_state(data_to_test):
         {processing.filter_by_state(data_to_test)}\n""")
print(f"""processing.filter_by_state(data_to_test, "CANCELED"):  
         {processing.filter_by_state(data_to_test, "CANCELED")}\n""")

# тест функции sort_by_date в 2 случаях
print(f"""processing.sort_by_date(data_to_test):
         {processing.sort_by_date(data_to_test)}\n""")
print(f"""processing.sort_by_date(data_to_test, False):
         {processing.sort_by_date(data_to_test, False)}\n""")

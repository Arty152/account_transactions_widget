import re
from utils import get_last_5_operations


def display_last_5_operations():
    """Функция показа 5 последних операций"""
    last_operations = get_last_5_operations()
    for operation in last_operations:
        operation_date = operation['date'][:10]
        date = operation_date[-2:] + '.' + operation_date[5:7] + '.' + operation_date[:4]
        operation_description = operation['description']

        if 'from' in operation:
            operation_from = operation['from'].split()[-1]
            prop_name_card = operation['from'].split()[0]

            if len(operation_from) == 16:
                secure_number_from = operation_from[:6] + len(operation_from[6:-4]) * '*' + operation_from[-4:]
                secure_number_split_from = re.sub(r'.{4}', r'\g<0> ', secure_number_from)
            else:
                secure_number_split_from = len(operation_from[-6:-4]) * '*' + operation_from[-4:]

        else:
            prop_name_card = 'Открытие'
            secure_number_split_from = 'нового счета'

        operation_to = operation['to'].split()[-1]
        prop_name_check = operation['to'].split()[0]

        if len(operation_to) == 16:
            secure_number_to = operation_to[:6] + len(operation_to[6:-4]) * '*' + operation_to[-4:]
            secure_number_split_to = re.sub(r'.{4}', r'\g<0> ', secure_number_to)
        else:
            secure_number_split_to = len(operation_to[-6:-4]) * '*' + operation_to[-4:]

        operation_amount = operation['operationAmount']['amount']
        operation_currency = operation['operationAmount']['currency']['name']

        print(f"{date} {operation_description}")
        print(f"{prop_name_card} {secure_number_split_from} -> {prop_name_check} {secure_number_split_to}")
        print(f"{operation_amount} {operation_currency}\n")


display_last_5_operations()

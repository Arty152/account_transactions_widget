import re
from utils import get_last_5_operations


def display_last_5_operations():
    """Функция показа 5 последних операций"""
    last_operations = get_last_5_operations()
    for operation in last_operations:
        operation_date = operation['date'][:10]
        date = operation_date[-2:] + '.' + operation_date[5:7] + '.' + operation_date[:4]
        description = operation['description']
        number_to = operation['to'].split()[-1]
        name_check_to = operation['to'].split()[0]
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        from_list = []
        if 'from' in operation:
            from_list.append(operation['from'])
            number_from = operation['from'].split()[-1]
            for item in from_list:
                if len(item.split()) == 3:
                    card_name = item.split()[:2]
                    card_name = ' '.join(card_name)
                else:
                    card_name = operation['from'].split()[0]

            if len(number_from) == 16:
                secure_number_from = number_from[:6] + len(number_from[6:-4]) * '*' + number_from[-4:]
                secure_number_split_from = re.sub(r'.{4}', r'\g<0> ', secure_number_from)
            else:
                secure_number_split_from = len(number_from[-6:-4]) * '*' + number_from[-4:]

        else:
            card_name = 'Открытие'
            secure_number_split_from = 'нового счета'

        if len(number_to) == 16:
            secure_number_to = number_to[:6] + len(number_to[6:-4]) * '*' + number_to[-4:]
            secure_number_split_to = re.sub(r'.{4}', r'\g<0> ', secure_number_to)
        else:
            secure_number_split_to = len(number_to[-6:-4]) * '*' + number_to[-4:]

        print(f"{date} {description}")
        print(f"{card_name} {secure_number_split_from} -> {name_check_to} {secure_number_split_to}")
        print(f"{amount} {currency}\n")

display_last_5_operations()

import json
import re


def get_file_data(file_name):
    """Функция получения данных из файла"""
    with open(file_name, encoding='utf-8') as f:
        return json.load(f)


def get_executed_operations(file_data):
    """Функция получения выполненных операций"""
    operations_executed = []
    for element in file_data:
        if element:
            if element['state'] == 'EXECUTED':
                operations_executed.append(element)
    return operations_executed


def get_last_5_operations(operations):
    """Функция получения 5 последних операций отсортированных по дате"""
    operations_sorted_by_date = sorted(operations, key=lambda key: key['date'])
    return operations_sorted_by_date[-5:][::-1]


def format_date(date):
    """Функция возвращает дату операции в формате 'DD.MM.YYYY'"""
    operation_date = date[:10]
    formatted_date = operation_date[-2:] + '.' + operation_date[5:7] + '.' + operation_date[:4]
    return formatted_date


def format_number(number):
    """Функция возвращает номер счёта или карты в защищённом формате"""
    if len(number) == 16:
        secure_number = number[:6] + len(number[6:-4]) * '*' + number[-4:]
        secure_number_split = re.sub(r'.{4}', r'\g<0> ', secure_number)
    else:
        secure_number_split = len(number[-6:-4]) * '*' + number[-4:]
    return secure_number_split


def display_operation(operation):
    operation_date = format_date(operation['date'])
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
        secure_number_split_from = format_number(number_from)
    else:
        card_name = 'Открытие'
        secure_number_split_from = 'нового счета'
    secure_number_split_to = format_number(number_to)
    print(f"{operation_date} {description}")
    print(f"{card_name} {secure_number_split_from} -> {name_check_to} {secure_number_split_to}")
    print(f"{amount} {currency}\n")


def display_last_5_operations(data):
    """Функция показа 5 последних операций"""
    for operation in data:
        display_operation(operation)

import json

SOURCE_DATA_OPERATIONS = 'operations.json'


def get_file_data(filename):
    """Функция получения данных из файла"""
    with open(filename, encoding='utf-8') as f:
        return json.load(f)


def get_executed_operations():
    """Функция получения выполненных операций"""
    file_data = get_file_data(SOURCE_DATA_OPERATIONS)
    operations_executed = []
    for element in file_data:
        if element:
            if element['state'] == 'EXECUTED':
                operations_executed.append(element)
    return operations_executed


def get_last_5_operations():
    """Функция получения 5 последних операций отсортированных по дате"""
    executed_operations = get_executed_operations()
    operations_sorted_by_date = sorted(executed_operations, key=lambda key: key['date'])
    return operations_sorted_by_date[-5:][::-1]
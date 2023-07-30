from account_transactions_widget.src.utils import \
    get_file_data, \
    get_executed_operations, \
    get_last_5_operations, \
    format_date, \
    format_number, \
    display_operation, \
    display_last_5_operations

file_data = get_file_data('operations.json')
executed_operations = get_executed_operations(file_data)
last_5_operations = get_last_5_operations(executed_operations)

display_last_5_operations(last_5_operations)
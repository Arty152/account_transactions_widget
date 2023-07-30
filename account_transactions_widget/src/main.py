from account_transactions_widget.src import utils

file_data = utils.get_file_data('operations.json')
executed_operations = utils.get_executed_operations(file_data)
last_5_operations = utils.get_last_5_operations(executed_operations)
utils.display_last_5_operations(last_5_operations)

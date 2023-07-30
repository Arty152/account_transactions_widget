from account_transactions_widget.src import utils
from account_transactions_widget.src.utils import get_last_5_operations, get_executed_operations, display_operation


def test_get_executed_operations():
    file_data = [{'state': 'EXECUTED'},
                 {'state': 'CANCELED'},
                 {'state': 'EXECUTED'},
                 {'state': 'CANCELED'}]

    result = get_executed_operations(file_data)

    assert result[0]['state'] == 'EXECUTED'
    assert result[1]['state'] == 'EXECUTED'


def test_get_last_5_operations():
    operations_dates = [{'date': '2019-09-07T07:20:13.889610'},
                        {'date': '2019-03-29T10:57:20.635567'},
                        {'date': '2019-07-18T12:27:13.355343'},
                        {'date': '2019-07-03T18:35:29.512364'},
                        {'date': '2018-03-23T10:45:06.972075'},
                        {'date': '2018-12-20T16:43:26.929246'}]

    result = get_last_5_operations(operations_dates)

    assert len(result) == 5
    assert result[0]['date'] == '2019-09-07T07:20:13.889610'
    assert result[-1]['date'] == '2018-12-20T16:43:26.929246'


def test_format_date():
    assert utils.format_date('2021-03-19T10:30:00+03:00') == '19.03.2021'
    assert utils.format_date('2022-12-31T23:59:59+03:00') == '31.12.2022'
    assert utils.format_date('2023-10-01T00:00:00+03:00') == '01.10.2023'


def test_format_number():
    assert utils.format_number('7158300734726758') == '7158 30** **** 6758 '
    assert utils.format_number('9876543210987654') == '9876 54** **** 7654 '
    assert utils.format_number('35383033474447895560') == '**5560'
    assert utils.format_number('12383033234447890249') == '**0249'


def test_display_operation(capsys):
    operations = [{"id": 41428829,
                   "state": "EXECUTED",
                   "date": "2019-07-03T18:35:29.512364",
                   "operationAmount": {
                       "amount": "8221.37",
                       "currency": {"name": "USD",
                                    "code": "USD"}},
                   "description": "Перевод организации",
                   "from": "MasterCard 7158300734726758",
                   "to": "Счет 35383033474447895560"},
                  {"id": 895315941,
                   "state": "EXECUTED",
                   "date": "2018-08-19T04:27:37.904916",
                   "operationAmount": {
                       "amount": "56883.54",
                       "currency": {"name": "USD",
                                    "code": "USD"}},
                   "description": "Перевод с карты на карту",
                   "from": "Visa Classic 6831982476737658",
                   "to": "Visa Platinum 8990922113665229"}]
    display_operation(operations[0])
    captured = capsys.readouterr()
    assert captured.out == ('03.07.2019 Перевод организации\n'
                            'MasterCard 7158 30** **** 6758  -> Счет **5560\n'
                            '8221.37 USD\n'
                            '\n')
    display_operation(operations[1])
    captured = capsys.readouterr()
    assert captured.out == ('19.08.2018 Перевод с карты на карту\n'
                            'Visa Classic 6831 98** **** 7658  -> Visa 8990 92** **** 5229 \n'
                            '56883.54 USD\n'
                            '\n')

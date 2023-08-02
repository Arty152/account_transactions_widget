import pytest
from account_transactions_widget.src import utils


def test_get_executed_operations(operations_fixture):
    assert utils.get_executed_operations(operations_fixture)[0]['state'] == 'EXECUTED'
    assert utils.get_executed_operations(operations_fixture)[-1]['state'] == 'EXECUTED'


def test_get_last_5_operations(operations_fixture):
    operations = utils.get_last_5_operations(operations_fixture)
    assert len(operations) == 5
    assert operations[0]['date'] == '2019-08-16T04:23:41.621065'
    assert operations[-1]['date'] == '2018-09-12T21:27:25.241689'


def test_format_date():
    assert utils.format_date('2018-10-14T08:21:33.419441') == '14.10.2018'
    assert utils.format_date('2019-08-16T04:23:41.621065') == '16.08.2019'


def test_format_number():
    assert utils.format_number('7158300734726758') == '7158 30** **** 6758 '
    assert utils.format_number('9876543210987654') == '9876 54** **** 7654 '
    assert utils.format_number('35383033474447895560') == '**5560'
    assert utils.format_number('12383033234447890249') == '**0249'


def test_display_operation(capsys, operations_fixture):
    operations = operations_fixture
    utils.display_operation(operations[0])
    captured = capsys.readouterr()
    assert captured.out == ('03.07.2019 Перевод организации\n'
                            'MasterCard 7158 30** **** 6758  -> Счет **5560\n'
                            '8221.37 USD\n'
                            '\n')
    utils.display_operation(operations[1])
    captured = capsys.readouterr()
    assert captured.out == ('19.08.2018 Перевод с карты на карту\n'
                            'Visa Classic 6831 98** **** 7658  -> Visa 8990 92** **** 5229 \n'
                            '56883.54 USD\n'
                            '\n')
    utils.display_operation(operations[2])
    captured = capsys.readouterr()
    assert captured.out == ('11.07.2018 Открытие вклада\n'
                            'Открытие нового счета -> Счет **6215\n'
                            '79931.03 руб.\n'
                            '\n')


if __name__ == "__main__":
    pytest.main()

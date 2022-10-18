def number_input(num):
    a = 'number 1' if not num else 'number 2'
    return input(f'Enter {a} number: ')


def operator_input():
    return input('Enter operation: ')


def type_input():
    print('Rational or Complex numbers.')
    user_type = input(
        'Eneter 1 for Rational or 2 - for Complex : ')
    return 1 if user_type == '1' else 2 if user_type == '2' else 0

import complex_numbers
import rational_numbers
import inputs
import logger


def operation(a=0, b=0, t=0):
    t = inputs.type_input()
    if t == 0:
        print('Try again, please.\n')
        return operation()
    tp = 'Rational' if t == 1 else 'Complex'
    print(f'Working with {tp} numbers.')
    a = inputs.number_input(0)
    b = inputs.number_input(1)
    return a, b, t


def result(a, b, t):
    o = inputs.operator_input()
    result = rational_numbers.rattional_operation(a, b, o) if t == 1 \
        else complex_numbers.complex_operation(a, b, o)
    if not result:
        print('Error operation, try again. (+,-,*,/)\n ')
        return result(a, b, t)
    print(f'({a} {o} {b}) = {result}')
    return (f'({a} {o} {b}) = {result}')


def calculate():
    a, b, t = operation()
    logger.write_log(result(a, b, t))

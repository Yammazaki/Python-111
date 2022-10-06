
a = int(input('Введите число: '))
print(f'Число в 10-ой системе: {a}')
b = ''
while a > 0:
    b = str(a%2) + b
    a = a // 2
print(f'Число в 2-ой системе: {b}')

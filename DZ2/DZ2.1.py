def factorial(z):
    if z == 0:
          return 1
    f=1
    for x in range(1,z+1): 
        f*=x
    return f

n = int(input('Введите число: '))
print(f'Список факториалов от 0 до {n} = ', end = '')
for i in range(0, n+1):
    if i == n: 
        print(f'{factorial(i)}')
    else:
        print(f'{factorial(i)}', end = ', ')
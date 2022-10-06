from random import uniform
n = int(input('Введите размер списка: '))

def succession(n):
    list1 = []
    for i in range(n):
      f = uniform(0, 10)
      list1.append(round(f, 2))
    return (list1)
   
list = succession(n)
print(f'Созданный список {list}')

min = list[0]
max = 0
for i in range(len(list)): 
    if max < list[i]%1:
        max = list[i]%1
    if min > list[i]%1:
        min = list[i]%1
dif = (max - int(max)) - (min - int(min))

print(f'Максимальная дробная часть {round(max,2)}')
print(f'Минимальная дробная часть {round(min,2)}')
print(f'(MAX - MIN) = {round(abs(dif),2)}')
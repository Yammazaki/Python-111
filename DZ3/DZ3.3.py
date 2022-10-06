import random
n = int(input('Введите количество элементов списка: '))

def succession(n):
    a = []
    for i in range(0,n):
      a.append(random.randint(0, 10))
    return (a)
   
list = succession(n)
print(f'Начальный список {list}')
list2=[]
for i in range(len(list)):
  while i < len(list)/2 and n > len(list)/2:
     n = n - 1
     a = list[i] * list[n]
     list2.append(a)
     i += 1
print(f'Результат обработки {list2}')
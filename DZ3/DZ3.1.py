import random
n = int(input('Введите количество элементов списка: '))

def succession(n):
    a = []
    for i in range(0,n):
      sum = 0
      a.append(random.randint(0, 100))
    return (a)
   
list = succession(n)
print(list)
def sum_nechet(list):
  sum=0
  for i in range(0,len(list)):
    if i % 2 != 0:
        sum += list[i]
  return(sum)
S = sum_nechet(list)
print(f'Сумма элементов с нечетными индексами: {S}')
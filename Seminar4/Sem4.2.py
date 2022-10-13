import random
n = int(input('Введите количество элементов списка: ')) 
def succession(n):
    a = [] 
    for i in range(1, n+1):
      a.append(random.randint(-n, n))
    return(a)
   
list = succession(n)
print(f'Созданный список {list}')

min_zn = list[0]
max_zn = 0
for i in range(len(list)): 
    if max_zn < list[i]:
        max_zn = list[i]
    if min_zn > list[i]:
        min_zn = list[i]
print(f'Максимальное значение {round(max_zn,2)}')
print(f'Минимальное значение {round(min_zn,2)}')

k = input("Введите список чисел: ").split()
print(k)
min_num = int(k[0])
max_num = int(k[0])
for i in range(len(k)):
    if int(k[i]) > max_num:
        max_num = int(k[i])
    if int(k[i]) < min_num:
        min_num = int(k[i])
print(min_num, max_num)

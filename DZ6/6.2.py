import random
import os
n = int(input('Введите старшую степень полинома: ')) 
def succession(n):
    a = [] 
    for i in range(0, n+1):
      a.append(random.randint(0, 101))
    return(a)

list = succession(n)
print(f'Случайные коеефициенты: {list}')
print('степень: n =', n) 
p = []
for i in range(0, len(list)):
    p.append(list[i]) 
    if i < len(list) - 1:
        p.append('x')
    if i < len(list)- 2:
        p.append(f'^{(len(list) - i - 1)}')
    if i < len(list) - 1:
        p.append(' + ')
p.append(' = 0')
print("".join(map(str, p)))
dir = r'file.txt'
with open(dir,'w') as f:
    f.write(f'Polinom :{"".join(map(str, p))}')
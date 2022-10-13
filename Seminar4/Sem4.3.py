k = input("Введите значения A, B, C: для проверки выражения Ax² + Bx + C = 0: ").split() 
# D = b2 − 4ac
A = int(k[0])
B = int(k[1])
C = int(k[2])
D = B**2 - 4 * A * C
print(D)
x1 = (-B + D**0.5) / 2 * A
x2 = (-B - D**0.5) / 2 * A
print(x1, x2)

import os

road = r'file.txt'
with open(road,'w') as f:
     f.write(f'x1 = {x1} x2 = {x2}')

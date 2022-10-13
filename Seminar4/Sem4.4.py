k = input("Введите значения A и B: ").split() 
A = int(k[0])
B = int(k[1])
n = A * B
if n%2 == 1:
    print(n)
while  B % A == 0 and n % B == 0 and n % 2 == 0:
    n = n//2
   
print(n*2)

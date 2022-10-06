n = int(input('Введите длину ряда: '))
f1=f2 = 1
a = [0,1,1] 
for i in range(3, n):
    f1, f2 = f2, f1 + f2
    a.append(f2)
f3=f4 = -1
b = [-1,-1] 
for i in range(3, n):
    f3, f4 = f4, f3 + f4
    b.insert(0,f4)
print(b+a)









 
 

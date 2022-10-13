n = int(input("Введите число: "))
i = 2 # первое простое число в последовательности простых чисел
list = []
number=n
while i <= n:
    if n % i == 0:
        list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {number} ==>: {list}")
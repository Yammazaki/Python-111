def input_numbers(x): 
    xyz = ['X', 'Y', 'Z']
    a = []
    for i in range(x):
        reality = False
        while not reality:
            try:
                number = float(input(f"Введите координату {xyz[i]}: "))
                a.append(number)
                reality = True
            except ValueError:
                print('некорректные данные')
    return a


def Length(a, b):  
    length = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2+(b[2] - a[2]) ** 2) ** (0.5)  
    return length


print('Введите координаты точки А')
pointA = input_numbers(3)
print('Введите координаты точки В')
pointB = input_numbers(3)

print(f"Длина отрезка: {round(Length(pointA, pointB),2)}")
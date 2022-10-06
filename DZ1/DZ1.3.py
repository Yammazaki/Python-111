x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))

leftSide = not (x or y or z)
rightSide = not x and not y and not z
result = leftSide == rightSide
if result == True:
     print('Утверждение истинно')
else:
     print('Утверждение ложно')
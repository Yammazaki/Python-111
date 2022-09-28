import math #Математические функции

x_A = float(input('Введите координату точки А по оси Х: '))
y_A = float(input('Введите координату точки А по оси Y: '))
x_B = float(input('Введите координату точки B по оси Х: '))
y_B = float(input('Введите координату точки B по оси Y: '))

def dlina (x1,y1,x2,y2):
  distance = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)
  print(f'расстояние между точками = {distance}')
  
dlina(x_A,y_A,x_B,y_B)
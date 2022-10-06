q = int(input('Введите номер четверти от 1 до 4 - '))

def koordinat (q):
 if q==1: 
     print('x>0 and y>0')
 elif q==2:
      print('x<0 and y>0')
 elif q==3:
      print('x<0 and y<0')
 elif q==4 : 
     print('x>0 and y<0')
 else: 
     print('Введите корректное значение')
koordinat(q)
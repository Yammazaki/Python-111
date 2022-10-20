import func
import view 

def directory():
     oper = int(input('1 - Добавить контакт \n2 - Удалить контакт \n3 - Найти котакт \n4 - Показать все контакты \n5 - Удаление по поиску \n6 - Выход \n Введите, что вы хотите сделать 1-6: '))
     while oper <= 6:
          if oper == 1:
               func.get_add()
          elif oper == 2:
               func.get_del()
          elif oper == 3:
               func.get_find()
          elif oper == 4:
               func.get_see()
          elif oper == 5:
               func.get_del_find()
          if oper == 6:
               print('Спасибо, что выбрали наш Продукт')
               break
          oper = int(input('1 - Добавить контакт \n2 - Удалить контакт \n3 - Найти котакт \n4 - Показать все контакты \n5 - Удаление по поиску \n6 - Выход \n Введите, что вы хотите сделать 1-6: '))
            

    
    
      
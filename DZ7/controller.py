import func
import view 
import log

def directory():
     oper = int(input('1 - Добавить контакт \n2 - Удалить контакт \n3 - Найти котакт \n4 - Показать все контакты \n5 - Удаление по поиску \n6 - Выход \n Введите, что вы хотите сделать 1-6: '))
     while oper <= 6:
          if oper == 1:
               func.get_add()
               log.input_write('Добавили контакт')
          elif oper == 2:
               func.get_del()
               log.input_write('Удалили контакт')
          elif oper == 3:
               func.get_find()
               log.input_write('Нашли контакт')
          elif oper == 4:
               func.get_see()
               log.input_write('Вывод тел.книги')
          elif oper == 5:
               func.get_del_find()
               log.input_write('Удалали поисковую информацию')
          if oper == 6:
               log.input_write('Выход')
               print('Спасибо, что выбрали наш Продукт')
               break
          oper = int(input('1 - Добавить контакт \n2 - Удалить контакт \n3 - Найти котакт \n4 - Показать все контакты \n5 - Удаление по поиску \n6 - Выход \n Введите, что вы хотите сделать 1-6: '))
            

    
    
      
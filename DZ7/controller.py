import func
import view 

def directory():
    oper = input('Выберите действие: ')

    if oper == '1':
         res = func.get_add()
    # elif oper == '2':
    #    res = func.get_del()
    elif oper == '3':
       res = func.get_find()
    elif oper == '4':
         res = func.get_see()
    return res
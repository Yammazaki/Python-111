import view
import csv

def get_add():
    list = ['Фамилию: ','Имя: ','номер телефона: ','коментарий']
    data = view.get_input(list)
    with open('people.csv', 'a', encoding = 'UTF-8') as file:
        file.writelines(
            f'{data[0]}, {data[1]}, {data[2]}, {data[3]} \n')

def get_see():
    with open('people.csv', 'r', encoding = 'UTF-8') as file:
        list = []
        list = ''.join(file.readlines())
        print(list)

def get_find():
   
# def get_find():
#    with open('people.csv', 'r', encoding = 'UTF-8') as file:
#         list = []
#         list = file.readlines()
#         print(list)
#         for i in range(len(list)):
#             list[i] = ''.join(list[i])
#             list[i] = list[i].replace(',','').split()
#             req = []
#             reg = list[i]
#             print(req)

#             # text = input('Введите слово для поика: ')
#             # for i in range(len(list[i])):
#             #     if text == (list[i])[i]:
#             #     print(list[i][i],i)
        
        

# def get_find():
#    with open('people.csv', 'r', encoding = 'UTF-8') as file:
#         list = []
#         list = ' '.join(' '.join(file.readlines()).split())
#         print(list)
#         list = list.replace(',','').split()
#         print(list)
#         text = input('Введите слово для поика: ')
#         for i in range(len(list)):
#             if text == list[i]:
#                 print(list[i],i)
        
        

     
           
           
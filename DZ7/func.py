import view
import csv

def get_add():
    list = ['Фамилию: ','Имя: ','номер телефона: ','коментарий']
    data = view.get_input(list)
    with open('people.csv', 'a', encoding = 'UTF-8') as file:
        file.writelines(
            f'{data[0]} {data[1]} {data[2]} {data[3]} \n')
    with open('people.txt', 'a', encoding = 'UTF-8') as file:
        file.writelines(
            f'{data[0]} {data[1]} {data[2]} {data[3]} \n')

def get_see():
    with open('people.csv', 'r', encoding = 'UTF-8') as file:
        list = []
        list = ''.join(file.readlines())
        print(list)

def get_find():
   with open('people.csv', 'r', encoding = 'UTF-8') as file:
        data = []
        data = file.readlines()
        text = input('Введите слово для поиска: \n')
        for i in range(len(data)):
            data[i] = ''.join(data[i])
            row = []
            row = data[i]
            if text in row:
                print(row)
    

                
            
        
        
        


                  

        
          

           
        
        

        
        

     
           
           
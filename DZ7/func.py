def get_input(lst):
    data = []
    for i in lst:
        print(f'\n Введите {i}')
        data.append(input())
    return data

def get_add():
    list = ['Фамилию:','Имя:','номер телефона:','коментарий:']
    data = get_input(list)
    with open('people.csv', 'a', encoding = 'UTF-8') as file:
        file.writelines(
            f'{data[0]},{data[1]},{data[2]},{data[3]}\n')
    
        
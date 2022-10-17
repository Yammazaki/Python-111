# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

lst = list(map(int, input('Введите числа через пробел:').split())) # функция map переводит каждый элемент в int, в данном случае  

print(f'Start list: {lst}')
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst] #Добавляем элементы в новый список из старого при условии, что их еще нет в новом списке
print(f'Result list: {new_lst}')

#функция MAP
# old_list = ['1', '2', '3', '4', '5', '6', '7']
# new_list = []
# for item in old_list:
#  new_list.append(int(item))
# print (new_list)
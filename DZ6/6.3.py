n = int(input('Введите число n для создание последовательности (1+1/n)^n: ')) 

def succession(n):
    new_lst = []
    [new_lst.append(i+1/i**i) for i in range(1,n+1)] 
    a = [] 
    return(new_lst)
 
print(f'Элементы последовательности : {succession(n)}')
print(f'Сумма элементов последовательности = {round(sum(succession(n)),2)}')
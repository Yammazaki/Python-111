n = int(input('Введите число n для создание последовательности (1+1/n)^n: ')) 

def succession(n):
    new_lst = []
    [new_lst.append(round (i+1/i**i,3)) for i in range(1,n+1)] 
    return(new_lst)
print(f'Элементы последовательности : {succession(n)}')
print(f'Сумма элементов последовательности = {round(sum(succession(n)),2)}')
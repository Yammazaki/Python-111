n = int(input('Введите число n для создание последовательности (1+1/n)^n: ')) 

def succession(n):
    a = [] 
    for i in range(1, n+1):
      a.append((1+1/i)**i)
    return(a)

   # return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(f'Элементы последовательности : {succession(n)}')
print(f'Сумма элементов последовательности = {round(sum(succession(n)),2)}')
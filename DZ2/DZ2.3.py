import random
n = int(input('Введите количество элементов списка: ')) 
def succession(n):
    a = [] 
    for i in range(1, n+1):
      a.append(random.randint(0, n*10 - 1))
    return(a)

list = succession(n)
print(f'Start list: {list}')

def list_mix(list):
  for i in range(0,len(list)):
    ind = random.randint(0, len(list)-1 )
    temp = list[ind]
    list[ind] = list[i]
    list[i]=temp
  return(list)

print(f'Mixed list: {list_mix(list)}')




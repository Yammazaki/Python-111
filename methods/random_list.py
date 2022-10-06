import random
def succession(n):
    a = [] 
    for i in range(1, n+1):
      a.append(random.randint(0, n - 1))
    return(a)
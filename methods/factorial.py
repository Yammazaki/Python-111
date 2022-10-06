def factorial(z):
    if z == 0:
          return 1
    f=1
    for x in range(1,z+1): 
        f*=x
    return f
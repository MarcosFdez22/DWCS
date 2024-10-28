def factorial(n):
    if n>=0:
        for i in range(1,n):
            n = n*i
        return n
    else:
        raise Exception("El numero es menor que 0")
    
    
try:
    print(factorial(5))
    print(factorial(0))
    print(factorial(10))
    print(factorial(-5))    
except Exception as e:
    print(e)
def powers(a, b):
    if type(a)==int and type(b)==int:
        result=1
        for _ in range(b):
            result*=a
        return result
    else:
        raise Exception("No int")
    
try:
    print(powers(3,4))
    print(powers(2.1,2))
except Exception as erro:
    print(erro)
    





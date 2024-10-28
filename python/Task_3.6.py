class Calculator:
    numberofObjects=0
    
    def __init__(self):
        pass    
      
    def __init__(self,num1=None,num2=None):
        if type(num1)==int and type(num2)==int:
            self.num1=num1
            self.num2=num2
            Calculator.numberofObjects+=1
        else:
            raise Exception("No int")
        
    
    def __str__(self):
       return f"The numbers are {self.num1} and {self.num2} and number of objects is {Calculator.numberofObjects}"

    
    def sum(self,num1,num2):
        return num1+num2 
    
    def getNumberofObjects(cls):
        return cls.numberofObjects
    
#PROGRAM

#Primero crea el objeto Calcular vacío. Luego asigna valores a los atributos. Finalmente muestra los valores de los atributos sin utilizar la función toString.


try:
    calculator1=Calculator()
    calculator1.num1=3
    calculator1.num2=2
    print("The numbers are " + calculator1.num1 + "and" + calculator1.num2)
except Exception as e:
    print(e)
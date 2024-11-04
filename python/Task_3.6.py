class Calculator:
    numberofObjects=0
    
    def __init__(self):
        pass    
      
    def __init__(self,num1=None,num2=None):
        if type(num1)==int and type(num2)==int or num1==None and num2==None:
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
#Creates the object firstCalcule empty. Then it assigns values to the attributes. Finally it shows the values of the attributes without using the toString function.

try:
    calculator1=Calculator()
    calculator1.num1=3
    calculator1.num2=2
    print("The numbers are " + str(calculator1.num1) + " and " + str(calculator1.num2))
except Exception as e:
    print(e)
    

#Creates the object secondCalcule assigning the values to the attributes at the moment of creation. Use the function toString to show the values of the attributes.  
try:
    secondCalculator=Calculator(5,7)
    print(secondCalculator) 
except Exception as e:
    print(e)
    
#Show the value returned by the "suma" function.    
try:
    print(secondCalculator.sum(5,7))
except Exception as e:  
    print(e)
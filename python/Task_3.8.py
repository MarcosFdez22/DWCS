class Alien:
    numberofAliens=0
    def __init__(self):
        pass
    
    def __init__(self,name):
        self.name=name
        Alien.numberofAliens+=1
        
    def getNumberOfAliens(al):
        return al.numberofAliens
    
    
#Write the code that creates several objects of Alien and shows the value returned by the numberOfAliens method.
a1 = Alien("Calamardo")
a2 = Alien("Et")
a3 = Alien("Eduardo")
print(a3.getNumberOfAliens())

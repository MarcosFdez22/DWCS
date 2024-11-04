class Person:
    def __init__(self):
        pass
    
    def __init__(self,id:int,name:str,age:int):
        self.id=id
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"The id of person is {self.id}, the name is {self.name} and is {self.age} years old"
    

class Student:
    def __init__(self):
        pass
    
    def __init__(self,id:int,Person:Person,degree:str):
        self.id=id
        self.Person=Person
        self.degree=degree
        
    def __str__(self):
        return f"The id is {self.id}, person: {self.Person}, degree {self.degree} \n"
    

class StudentGroup:
    def __init__(self):
        pass
    
    def __init__(self,id:int,groupName:str,students):
        self.id=id
        self.groupName=groupName
        self.students=students
    
    def __str__(self):
        cadea = f"Grupo: {self.id}-{self.groupName} \n"
        for estudante in self.students:
            cadea=cadea+str(estudante)
        return cadea
    
    








#Create three different students. Show the value of the attributes on the screen.

es1=Student(1,Person(1,"JERY",22),"a")

es2=Student(2,Person(2,"Alba",27),"b")

es3=Student(3,Person(3,"Anxo",55),"c")

print(es1)
print(es2)
print(es3)


#Create an student group that contains the previously created students and show on the screen all the information of the students in this group.

Grupo1 = StudentGroup(1,"Grupo Uno",[es1,es2,es3])

print(Grupo1)


#Remove a student from this group. Show the information of the group on the screen.
Grupo1.students.remove(es1)
print(Grupo1)


#Add a new student to this group. Show the information of the group on the screen.

##Grupo1.students.insert(0,es1)

Grupo1.students.extend([es1])
print(Grupo1)
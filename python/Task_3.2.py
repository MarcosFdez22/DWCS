def function(age, name=None, surname="Apelido"):
    if name==None:
        print(surname + " is " + str(age))
    else:
        print(name + " " +surname + " is " + str(age))
    
function(21, None ,"Fernández")

function(30,"Ana","Vázquez")

function(20)
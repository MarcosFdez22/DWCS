products = {0: 'potatoes', 1:'tomatoes', 3:'onions', 4:'garlic'}

#1. Write a function called ‘showDictionary’ that receives the dictionary as a parameter and prints its contents with a nice format.

def showDictionary(dictionary):
    print("Los productos que tenemos son:")
    for key in dictionary:
        print(str(key) + " " + dictionary[key])

showDictionary(products)

#2. Write a function called ‘findValue’ that receives as parameters the dictionary and a key and shows the value on the screen.

def findvalue(dictionary,key):
    
    if (key not in dictionary):
        print("No esta en el diccionario, el número máximo es " + str(len(dictionary)))
    else:
        print("Has seleccionado " + dictionary[key])
    
findvalue(products, 5)


#3. Escriba una función llamada 'mergeDictionaries' que reciba dos diccionarios, cree un tercer diccionario que tenga los valores de ambos y lo devuelva.
products = {0: 'potatoes', 1:'tomatoes', 3:'onions', 4:'garlic'}
items = {0:'pencil',1:'pen',2:'eraser'}

def mergeDictionariesSequential(*dictionaries):
    merged = {}
    counter = 0  
    for dictionary in dictionaries:
        for value in dictionary.values():
            merged[counter] = value
            counter += 1  
    return merged
print(mergeDictionariesSequential(products, items))


